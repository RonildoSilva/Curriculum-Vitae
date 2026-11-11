#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as imagens da identidade visual do README em assets/readme/.

    python3 scripts/gerar-identidade.py

- banner-{claro,escuro}.svg  nome, títulos e a trajetória desenhada como um
                             grafo de processo (o tema da pesquisa)
- numeros-{claro,escuro}.svg faixa com os totais, calculados do catálogo
- botoes/*.svg               botões de link (substituem badges externos)
- secoes/*.svg               títulos de seção numerados
- rodape-{claro,escuro}.svg  assinatura e data do catálogo

O README usa <picture> para servir a versão certa ao tema do GitHub. O
gerar-site.py chama este script, então os números acompanham o catálogo.
Paleta igual à do index.html.
"""
import json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(RAIZ, "data", "catalogo.json")
SAIDA = os.path.join(RAIZ, "assets", "readme")

TEMAS = {
    "claro": dict(bg="#fbfaf8", surface="#ffffff", line="#e6e2db", ink="#1c1a17",
                  ink2="#55504a", ink3="#8a837a", accent="#1c5d4a", soft="#e8f1ed"),
    "escuro": dict(bg="#14161a", surface="#1b1e23", line="#2b3038", ink="#eceae6",
                   ink2="#a9a49c", ink3="#7d7770", accent="#5fbfa1", soft="#16302a"),
}
SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif"
SANS = "Inter, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

# marcos da trajetória: (ano, rótulo)
MARCOS = [
    ("2009", "primeiro código"),
    ("2013", "Técnico · IFCE"),
    ("2019", "Best Paper · UFC"),
    ("2020", "Bacharel · UFC"),
    ("2023", "Artigo · SBBD"),
    ("2024", "Mestre · UFC"),
    ("2026", "Professor · CBS"),
]


def banner(c):
    W, H = 1280, 360
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'role="img" aria-label="Ronildo Oliveira da Silva — Mestre em Computação, engenheiro e cientista de dados">',
           f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}"/>',
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{c["line"]}"/>']

    # log de eventos ao fundo: grade de pontos, com um traço em destaque
    gx, gy, step = 900, 52, 26
    trace = {(0, 4), (1, 4), (2, 3), (3, 3), (4, 2), (5, 2), (6, 3), (7, 1), (8, 1), (9, 0), (10, 0), (11, 0)}
    for i in range(12):
        for j in range(6):
            x, y = gx + i * step, gy + j * step
            if (i, j) in trace:
                continue
            out.append(f'<circle cx="{x}" cy="{y}" r="2.2" fill="{c["line"]}"/>')
    pts = sorted(trace)
    path = " ".join(f'{"M" if k == 0 else "L"}{gx+i*step},{gy+j*step}' for k, (i, j) in enumerate(pts))
    out.append(f'<path d="{path}" fill="none" stroke="{c["accent"]}" stroke-width="2" '
               f'stroke-linejoin="round" stroke-linecap="round" opacity=".55"/>')
    for i, j in pts:
        out.append(f'<circle cx="{gx+i*step}" cy="{gy+j*step}" r="4" fill="{c["accent"]}"/>')

    # identificação
    out += [
        f'<rect x="64" y="58" width="6" height="22" rx="1.5" fill="{c["accent"]}"/>',
        f'<text x="82" y="75" font-family="{SANS}" font-size="14" font-weight="600" letter-spacing="2.4" '
        f'fill="{c["accent"]}">CURRÍCULO · PORTFÓLIO DOCUMENTADO</text>',
        f'<text x="62" y="146" font-family="{SERIF}" font-size="56" font-weight="700" fill="{c["ink"]}">'
        f'Ronildo Oliveira da Silva</text>',
        f'<text x="64" y="188" font-family="{SANS}" font-size="23" fill="{c["ink2"]}">'
        f'Mestre em Computação (UFC) · Engenheiro e cientista de dados</text>',
        f'<text x="64" y="222" font-family="{SANS}" font-size="23" fill="{c["ink2"]}">'
        f'Professor na UniCatólica · Instrutor certificado Huawei</text>',
    ]

    # trajetória como grafo de processo (directly-follows)
    x0, x1, ny = 96, 1184, 296
    xs = [x0 + k * (x1 - x0) / (len(MARCOS) - 1) for k in range(len(MARCOS))]
    out.append(f'<defs><marker id="seta" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" '
               f'orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{c["ink3"]}"/></marker></defs>')
    for k in range(len(xs) - 1):
        a, b = xs[k] + 13, xs[k + 1] - 15
        mid = (a + b) / 2
        out.append(f'<path d="M{a:.1f},{ny} Q{mid:.1f},{ny-16} {b:.1f},{ny}" fill="none" '
                   f'stroke="{c["ink3"]}" stroke-width="1.6" marker-end="url(#seta)"/>')
    for k, ((ano, rot), x) in enumerate(zip(MARCOS, xs)):
        ultimo = k == len(MARCOS) - 1
        if ultimo:
            out.append(f'<circle cx="{x:.1f}" cy="{ny}" r="17" fill="{c["soft"]}"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{ny}" r="9" fill="{c["accent"] if ultimo else c["surface"]}" '
                   f'stroke="{c["accent"]}" stroke-width="2.5"/>')
        out.append(f'<text x="{x:.1f}" y="{ny-26}" text-anchor="middle" font-family="{SANS}" font-size="17" '
                   f'font-weight="{600 if ultimo else 500}" fill="{c["ink"] if ultimo else c["ink2"]}">{rot}</text>')
        out.append(f'<text x="{x:.1f}" y="{ny+36}" text-anchor="middle" font-family="{SANS}" font-size="15" '
                   f'font-weight="600" letter-spacing="1" fill="{c["ink3"]}">{ano}</text>')
    out.append("</svg>")
    return "\n".join(out)


def numeros(c, dados):
    itens = dados["itens"]
    anos = [i["ano"] for i in itens if i.get("ano")]
    horas = sum(i.get("horas") or 0 for i in itens)
    cards = [
        (f'{len(itens)}', "documentos"),
        (f'{len({i["emissor"] for i in itens if i.get("emissor")})}', "instituições"),
        (f'{horas:,}'.replace(",", "."), "horas de formação"),
        (f'{min(anos)}–{max(anos)}', "período documentado"),
    ]
    W, H, gap = 1280, 124, 16
    cw = (W - gap * 3) / 4
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="{"; ".join(f"{v} {r}" for v, r in cards)}">']
    for k, (valor, rotulo) in enumerate(cards):
        x = k * (cw + gap)
        out += [
            f'<rect x="{x+0.5:.1f}" y="0.5" width="{cw-1:.1f}" height="{H-1}" rx="12" fill="{c["surface"]}" stroke="{c["line"]}"/>',
            f'<rect x="{x+24:.1f}" y="28" width="5" height="70" rx="2" fill="{c["accent"]}"/>',
            f'<text x="{x+44:.1f}" y="62" font-family="{SERIF}" font-size="44" font-weight="700" fill="{c["ink"]}">{valor}</text>',
            f'<text x="{x+44:.1f}" y="92" font-family="{SANS}" font-size="20" fill="{c["ink2"]}">{rotulo}</text>',
        ]
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------- botões
BOTOES = [  # (arquivo, rótulo, ícone, primário)
    ("portfolio", "Portfólio navegável", "grade", True),
    ("linkedin", "LinkedIn", "in", False),
    ("lattes", "Lattes", "doc", False),
    ("orcid", "ORCID", "id", False),
    ("zenodo", "Zenodo", "doi", False),
]


def icone(tipo, x, y, cor, fundo):
    if tipo == "grade":
        return "".join(f'<rect x="{x+dx}" y="{y+dy}" width="6" height="6" rx="1.2" fill="{cor}"/>'
                       for dx in (0, 8) for dy in (0, 8))
    if tipo == "doc":
        return (f'<path d="M{x+1},{y} h9 l4,4 v10 h-13 z" fill="none" stroke="{cor}" stroke-width="1.6" stroke-linejoin="round"/>'
                + "".join(f'<rect x="{x+4}" y="{y+yy}" width="7" height="1.6" rx=".8" fill="{cor}"/>' for yy in (6, 9.5)))
    if tipo == "id":
        return (f'<circle cx="{x+7}" cy="{y+7}" r="7.5" fill="{cor}"/>'
                f'<text x="{x+7}" y="{y+10.6}" text-anchor="middle" font-family="{SANS}" font-size="9.5" '
                f'font-weight="700" fill="{fundo}">iD</text>')
    rot = {"in": "in", "doi": "DOI"}[tipo]
    w = 15 if tipo == "in" else 26
    return (f'<rect x="{x}" y="{y}" width="{w}" height="15" rx="3" fill="{cor}"/>'
            f'<text x="{x+w/2}" y="{y+11.3}" text-anchor="middle" font-family="{SANS}" font-size="{10.5 if tipo == "in" else 8.5}" '
            f'font-weight="700" fill="{fundo}">{rot}</text>')


def botao(c, rotulo, tipo, primario):
    larg_icone = 26 if tipo == "doi" else 15
    W = round(20 + larg_icone + 9 + len(rotulo) * 8.6 + 20)
    H = 40
    fundo = c["accent"] if primario else c["surface"]
    tinta = c["bg"] if primario else c["accent"]
    texto = c["bg"] if primario else c["ink"]
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{rotulo}">',
        f'<rect x="0.75" y="0.75" width="{W-1.5}" height="{H-1.5}" rx="9" fill="{fundo}" stroke="{c["accent"] if primario else c["line"]}" stroke-width="1.5"/>',
        icone(tipo, 20, 12.5, tinta, fundo),
        f'<text x="{20+larg_icone+9}" y="25.5" font-family="{SANS}" font-size="15" font-weight="600" fill="{texto}">{rotulo}</text>',
        "</svg>"])


# --------------------------------------------------------- títulos de seção
SECOES = [  # (arquivo, título) — na ordem do README
    ("formacao", "Formação"),
    ("certificacoes", "Certificações"),
    ("producao-cientifica", "Produção científica"),
    ("docencia", "Docência"),
    ("pesquisa", "Pesquisa"),
    ("idiomas", "Idiomas"),
    ("formacao-continuada", "Formação continuada"),
    ("curriculo", "Currículo"),
]


def secao(c, n, titulo):
    W, H = 1280, 64
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{titulo}">',
           f'<text x="0" y="44" font-family="{SANS}" font-size="15" font-weight="700" letter-spacing="1.5" fill="{c["accent"]}">{n:02d}</text>',
           f'<rect x="32" y="22" width="2" height="28" rx="1" fill="{c["line"]}"/>',
           f'<text x="48" y="45" font-family="{SERIF}" font-size="32" font-weight="700" fill="{c["ink"]}">{titulo}</text>']
    # assinatura: o mesmo traço do banner, em miniatura, no canto direito
    pts = [(0, 3), (1, 3), (2, 2), (3, 2), (4, 1), (5, 0)]
    gx, gy, st = W - 6 - 5 * 14, 18, 8
    out.append(f'<polyline points="{" ".join(f"{gx+i*14},{gy+j*st}" for i, j in pts)}" fill="none" '
               f'stroke="{c["accent"]}" stroke-width="1.6" stroke-linejoin="round" opacity=".55"/>')
    out += [f'<circle cx="{gx+i*14}" cy="{gy+j*st}" r="2.8" fill="{c["accent"]}"/>' for i, j in pts]
    out.append("</svg>")
    return "\n".join(out)


# ------------------------------------------------------------------ rodapé
def rodape(c, dados):
    W, H = 1280, 72
    d = dados.get("gerado_em", "")
    data = "/".join(reversed(d.split("-"))) if d else ""
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Catálogo atualizado em {data}">',
           f'<rect x="0" y="8" width="{W}" height="1" fill="{c["line"]}"/>',
           f'<rect x="0" y="7" width="64" height="3" rx="1.5" fill="{c["accent"]}"/>',
           f'<text x="0" y="48" font-family="{SERIF}" font-size="20" font-weight="700" fill="{c["ink"]}">Ronildo Oliveira da Silva</text>',
           f'<text x="{W}" y="48" text-anchor="end" font-family="{SANS}" font-size="14" fill="{c["ink3"]}">'
           f'Catálogo atualizado em {data} · {dados["total"]} documentos com original anexado</text>',
           "</svg>"]
    return "\n".join(out)


def main():
    with open(CAT, encoding="utf-8") as f:
        dados = json.load(f)
    os.makedirs(SAIDA, exist_ok=True)
    for nome, c in TEMAS.items():
        arquivos = [("banner", banner(c)), ("numeros", numeros(c, dados)), ("rodape", rodape(c, dados))]
        arquivos += [(f"botoes/{a}", botao(c, r, i, p)) for a, r, i, p in BOTOES]
        arquivos += [(f"secoes/{a}", secao(c, n, t)) for n, (a, t) in enumerate(SECOES, 1)]
        for base, svg in arquivos:
            destino = os.path.join(SAIDA, f"{base}-{nome}.svg")
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8") as f:
                f.write(svg + "\n")
    print("identidade visual : assets/readme/ (banner, números, botões, seções e rodapé; temas claro e escuro)")


if __name__ == "__main__":
    main()
