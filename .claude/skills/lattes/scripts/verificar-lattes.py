#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o PDF do Lattes contra as fontes do repositório e lista divergências.

Uso (da raiz do repositório):
    python3 -I .claude/skills/lattes/scripts/verificar-lattes.py [caminho-do-lattes.pdf]

Sem argumento, usa o PDF mais recente em _raw/lattes/.

Saída: relatório Markdown com OK / FALTA / AVISO por verificação. É um ponto de
partida: confirme cada FALTA no PDF antes de mandar o usuário cadastrar, porque a
quebra de linha do pdftotext pode esconder um título que existe.
"""
import datetime as dt, glob, json, os, re, subprocess, sys, unicodedata

RAIZ = os.getcwd()
HOJE = dt.date.today()
SECOES = ["Identificação", "Endereço", "Formação acadêmica/titulação", "Pós-doutorado",
          "Formação Complementar", "Atuação Profissional", "Projetos de pesquisa",
          "Projetos de extensão", "Projetos de desenvolvimento", "Revisor de periódico",
          "Áreas de atuação", "Idiomas", "Prêmios e títulos", "Produções", "Bancas",
          "Eventos", "Orientações", "Inovação", "Educação e Popularização de C & T"]


def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def achar_pdf():
    if len(sys.argv) > 1:
        return sys.argv[1]
    cand = sorted(glob.glob(os.path.join(RAIZ, "_raw", "lattes", "*.pdf")), key=os.path.getmtime)
    if not cand:
        sys.exit("nenhum PDF em _raw/lattes/: exporte o Lattes (Visualizar currículo → Gerar PDF) e salve lá")
    return cand[-1]


def texto_pdf(p):
    return subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, check=True).stdout


def secoes(txt):
    """Fatia o texto pelos títulos de seção, que no PDF ficam sozinhos na linha."""
    linhas = txt.splitlines()
    marcas = [(i, l.strip()) for i, l in enumerate(linhas) if l.strip() in SECOES]
    out = {"_resumo": "\n".join(linhas[:marcas[0][0]]) if marcas else ""}
    for k, (i, nome) in enumerate(marcas):
        fim = marcas[k + 1][0] if k + 1 < len(marcas) else len(linhas)
        out.setdefault(nome, "\n".join(linhas[i + 1:fim]))
    return out


def vinculos(atuacao):
    """[(instituição, sigla, [(início, fim)])] a partir da seção Atuação Profissional."""
    res, atual = [], None
    for l in atuacao.splitlines():
        m = re.match(r"^\s*(.+?), ([A-ZÀ-Ý0-9\-]{2,}), ([A-ZÀ-Ý][a-zà-ÿ]+)\.\s*$", l)
        if m:
            atual = [m.group(1).strip(), m.group(2), []]
            res.append(atual)
            continue
        p = re.match(r"^\s*((?:19|20)\d{2}) - ((?:19|20)\d{2}|Atual)\s*$", l)
        if p and atual:
            atual[2].append((p.group(1), p.group(2)))
    return res


def linkedin_experiencias():
    p = os.path.join(RAIZ, "LINKEDIN.md")
    if not os.path.exists(p):
        return []
    s = open(p, encoding="utf-8").read()
    exps = []
    for m in re.finditer(r"^### 6\.\d+ (.+?) · (.+)$\n(?:.*\n){0,3}?- Período: ([^\n·]+)", s, re.M):
        org = re.sub(r"\(.*?\)", "", m.group(1)).strip()
        siglas = re.findall(r"\(([^)]+)\)", m.group(1))
        exps.append((m.group(1), org, siglas, m.group(2).strip(), m.group(3).strip()))
    return exps


def producoes_repo():
    """Títulos de produção científica do catálogo e do README."""
    titulos = {}
    cat = os.path.join(RAIZ, "data", "catalogo.json")
    if os.path.exists(cat):
        for i in json.load(open(cat, encoding="utf-8"))["itens"]:
            if i["categoria"] != "04-producao-cientifica":
                continue
            t = i["titulo"].split(" — ")[0]
            if t.lower().startswith(("certificado", "apresentações de", "encontros universitários")):
                continue
            titulos[norm(t)] = (t, i.get("ano"))
    readme = os.path.join(RAIZ, "README.md")
    if os.path.exists(readme):
        s = open(readme, encoding="utf-8").read()
        # título da seção pode ser "## Produção científica" ou <h2> com imagem (alt="Produção científica")
        m = re.search(r'(^## Produção científica$|alt="Produção científica")', s, re.M)
        bloco = ""
        if m:
            resto = s[m.end():]
            fim = re.search(r"^(## |<h2>)", resto, re.M)
            bloco = resto[:fim.start()] if fim else resto
        for m in re.finditer(r"^- \**\[?([^\]*\n]+?)\]?(?:\([^)]*\))?\**\s+—", bloco, re.M):
            t = m.group(1).strip("* ")
            if not any(k.startswith(norm(t)) or norm(t).startswith(k) for k in titulos):
                titulos[norm(t)] = (t, None)
    return list(titulos.values())


def presente(titulo, alvo_norm, n=6):
    """Casa pelas n primeiras palavras significativas — tolera quebra de linha e caixa."""
    pal = [w for w in norm(titulo).split() if len(w) > 2][:n]
    if not pal:
        return False
    return re.search(r"\b" + r"\b.{0,40}?\b".join(map(re.escape, pal)) + r"\b", alvo_norm) is not None


def main():
    pdf = achar_pdf()
    txt = texto_pdf(pdf)
    sec = secoes(txt)
    tn = norm(txt)
    rel = [f"# Verificação do Lattes\n\nArquivo: `{os.path.relpath(pdf, RAIZ)}` · conferido em {HOJE:%d/%m/%Y}\n"]
    add = lambda nivel, msg: rel.append(f"- **{nivel}** {msg}")

    # 1. atualização
    rel.append("\n## Atualização e integridade\n")
    m = re.search(r"Última atualização do currículo em (\d{2})/(\d{2})/(\d{4})", txt)
    if m:
        d = dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        dias = (HOJE - d).days
        add("OK" if dias <= 90 else "AVISO", f"última atualização em {d:%d/%m/%Y} ({dias} dias)."
            + ("" if dias <= 90 else " Editais de pós e concursos costumam exigir Lattes atualizado nos últimos 3 meses."))
    else:
        add("AVISO", "data de atualização não encontrada; o PDF é mesmo o exportado do Lattes?")
    corromp = sorted({c for c in re.findall(r"\S*\w\?\w\S*", txt) if "://" not in c})
    for c in corromp:
        add("AVISO", f"caractere corrompido em `{c}` (provável travessão ou acento colado de outro sistema).")
    if not corromp:
        add("OK", "nenhum caractere corrompido do tipo `palavra?palavra`.")

    # 2. identificadores
    rel.append("\n## Identificação\n")
    add("OK" if "orcid" in tn else "FALTA", "ORCID em Identificação → Outros identificadores."
        if "orcid" not in tn else "ORCID informado.")
    m = re.search(r"Nome em citações\s+bibliográficas\s+(.+)", txt)
    if m:
        add("OK", f"nomes em citações: `{m.group(1).strip()}`. Use exatamente um deles como autor em toda produção.")

    # 3. vínculos x resumo x LinkedIn
    rel.append("\n## Atuação profissional\n")
    vs = vinculos(sec.get("Atuação Profissional", ""))
    ativos = [v for v in vs if any(f == "Atual" for _, f in v[2])]
    encerrados = [v for v in vs if v[2] and not any(f == "Atual" for _, f in v[2])]
    add("OK", "vínculos atuais no Lattes: " + (", ".join(f"{v[0]} ({v[1]})" for v in ativos) or "nenhum") + ".")
    resumo = norm(sec.get("_resumo", ""))
    for frase in re.findall(r"atua como [^.]*", resumo):
        for v in encerrados:
            if norm(v[1]) in frase.split() or norm(v[0]) in frase:
                add("AVISO", f"o resumo diz “{frase[:90]}…”, mas o vínculo com {v[1]} terminou em "
                    f"{max(f for _, f in v[2])}. Reescreva o resumo.")
    for v in ativos:
        if norm(v[1]) not in resumo.split() and norm(v[0]) not in resumo:
            add("AVISO", f"o resumo não menciona o vínculo atual com {v[0]} ({v[1]}).")
    for bruto, org, siglas, cargo, periodo in linkedin_experiencias():
        if org.lower().startswith("monitorias"):
            continue
        chaves = [norm(org)] + [norm(s) for s in siglas] + [norm(x) for x in re.split(r"[,/]", org) if len(norm(x)) > 2]
        ok = any(k and re.search(r"\b" + re.escape(k) + r"\b", tn) for k in chaves)
        if not ok:
            add("FALTA", f"vínculo do LinkedIn sem correspondente no Lattes: **{bruto}** · {cargo} · {periodo}.")

    # 4. produção
    rel.append("\n## Produção bibliográfica e técnica\n")
    prod = norm(sec.get("Produções", ""))
    for titulo, ano in producoes_repo():
        if presente(titulo, prod) or presente(titulo, tn):
            add("OK", f"{titulo}" + (f" ({ano})" if ano else ""))
        else:
            add("FALTA", f"{titulo}" + (f" ({ano})" if ano else "") + " — está no portfólio/README e não no Lattes.")
    # software cadastrado como registrado sem órgão de registro de verdade
    for m in re.finditer(r"Número do registro: ([^,]+),.{0,200}?Instituição de\s+registro: ([^.\n]+)", txt, re.S):
        inst = m.group(2).strip()
        if not re.search(r"INPI|Propriedade Industrial|Patent|Intellectual Property", inst, re.I):
            add("AVISO", f"programa de computador cadastrado como **registrado** (nº {m.group(1).strip()}, "
                f"instituição “{inst}”). Repositório aberto não é órgão de registro: exclua em Patentes e "
                "Registros e cadastre em Produção Técnica → Programa de computador sem registro.")
    for doi in sorted(set(re.findall(r"10\.5281/zenodo\.\d+", open(os.path.join(RAIZ, "README.md"), encoding="utf-8").read()))):
        add("OK" if doi in txt else "FALTA", f"software/dados `{doi}` (Produção Técnica → Programa de computador sem registro).")

    # 5. seções esperadas para quem é docente e pesquisador
    rel.append("\n## Seções\n")
    for s, motivo in [("Orientações", "docente com TCCs e iniciação científica"),
                      ("Projetos de pesquisa", "coordena projeto na instituição atual"),
                      ("Eventos", "apresentou trabalhos")]:
        add("OK" if s in sec else "FALTA", f"seção **{s}**" + ("" if s in sec else f" ausente ({motivo})."))
    if "Projetos de pesquisa" in sec and "coordenador" in norm(sec["Projetos de pesquisa"]):
        coord = re.findall(r"ronildo oliveira da silva coordenador", norm(sec["Projetos de pesquisa"]))
        add("OK" if coord else "AVISO", "projeto coordenado por você" if coord
            else "nenhum projeto com você como Coordenador.")

    print("\n".join(rel))


if __name__ == "__main__":
    main()
