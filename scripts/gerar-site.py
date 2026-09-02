#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Embute o catálogo e o mapa de logos dentro de index.html.

A página precisa funcionar também quando aberta por duplo clique (file://),
onde o navegador bloqueia fetch. Rode este script sempre que editar o catálogo
ou acrescentar uma logo:

    python3 scripts/gerar-site.py

Para adicionar a logo de uma instituição, salve um PNG de fundo transparente em
assets/logos/ com o nome do emissor em minúsculas e hifens — "EF English Live"
vira ef-english-live.png. O script encontra sozinho; emissor sem arquivo
continua exibindo o monograma colorido.
"""
import json, os, re, sys, unicodedata

RAIZ  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT   = os.path.join(RAIZ, "data", "catalogo.json")
LOGOS = os.path.join(RAIZ, "assets", "logos")
HTML  = os.path.join(RAIZ, "index.html")
INICIO, FIM = "<!-- catalogo:inicio -->", "<!-- catalogo:fim -->"
EXTS = (".png", ".svg", ".webp", ".jpg", ".jpeg")


def slug(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def mapear_logos(emissores):
    """Casa cada emissor com um arquivo em assets/logos/, pelo slug do nome."""
    if not os.path.isdir(LOGOS):
        return {}, []
    disponiveis = {}
    for f in sorted(os.listdir(LOGOS)):
        nome, ext = os.path.splitext(f)
        if ext.lower() in EXTS:
            disponiveis.setdefault(nome.lower(), f"assets/logos/{f}")

    achados, faltando = {}, []
    for e in sorted(emissores):
        arq = disponiveis.get(slug(e))
        if arq:
            achados[e] = arq
        else:
            faltando.append(e)
    return achados, faltando


def main():
    with open(CAT, encoding="utf-8") as f:
        dados = json.load(f)

    emissores = {i["emissor"] for i in dados["itens"] if i.get("emissor")}
    dados["logos"], faltando = mapear_logos(emissores)

    # compacto, e sem "<" cru para não fechar o <script> por acidente
    bruto = json.dumps(dados, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    bloco = f'{INICIO}<script id="catalogo" type="application/json">{bruto}</script>{FIM}'

    with open(HTML, encoding="utf-8") as f:
        html = f.read()
    if INICIO not in html or FIM not in html:
        sys.exit(f"marcadores {INICIO} … {FIM} não encontrados em index.html")

    novo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIM), lambda _: bloco, html, flags=re.S)
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(novo)

    print(f"catálogo embutido : {dados['total']} itens · index.html com {len(novo)/1024:.0f} KB")
    print(f"logos encontradas : {len(dados['logos'])} de {len(emissores)} emissores")
    if faltando:
        print(f"sem logo (usam monograma): {len(faltando)}")
        for e in faltando:
            print(f"    assets/logos/{slug(e)}.png   ← {e}")


main()
