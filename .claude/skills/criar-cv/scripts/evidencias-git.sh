#!/usr/bin/env bash
# Conta evidências de entrega em repositórios git, filtrando por autor.
# Para VERIFICAÇÃO interna (existe React? existe teste?), não para o CV:
# contagens de commits, PRs e testes são métricas de atividade e não entram no currículo.
# Uso: evidencias-git.sh [-a <padrao-autor>] <repo> [<repo>...]
# Padrão de autor default: "ronildo" (casa nome e e-mail, sem distinguir maiúsculas).
set -u
AUTHOR="ronildo"
if [ "${1:-}" = "-a" ]; then AUTHOR="$2"; shift 2; fi
[ $# -ge 1 ] || { echo "uso: $0 [-a autor] <repo> [<repo>...]" >&2; exit 1; }

for r in "$@"; do
  if [ ! -d "$r/.git" ]; then echo "== $r: não é repositório git, pulando"; continue; fi
  g() { git -C "$r" "$@"; }
  echo "== $r"
  echo "   período      : $(g log --author="$AUTHOR" -i --format='%ad' --date=short | sort | sed -n '1p;$p' | tr '\n' ' ')"
  echo "   commits (sem merge): $(g log --author="$AUTHOR" -i --no-merges --format='%h' | wc -l)"
  echo "   PRs mergeados por você: $(g log --author="$AUTHOR" -i --merges --format='%s' | grep -c 'Merge pull request')"
  echo "   funções de teste adicionadas (def test_): $(g log --author="$AUTHOR" -i -p --format='' -- '*.py' | grep -c '^+\s*\(async \)\?def test_')"
  echo "   arquivos de teste JS/TS adicionados: $(g log --author="$AUTHOR" -i --diff-filter=A --name-only --format='' | grep -E '\.(test|spec)\.(ts|tsx|js|jsx)$' | sort -u | wc -l)"
  echo "   canvases/ADRs criados: $(g log --author="$AUTHOR" -i --diff-filter=A --name-only --format='' | grep -i -E 'canvas|adr' | grep -E '\.md$' | sort -u | wc -l)"
  fe=$(g log --author="$AUTHOR" -i --name-only --format='' | grep -E '\.(tsx|jsx|vue|svelte)$' | sort -u | wc -l)
  echo "   arquivos de frontend tocados (tsx/jsx/vue/svelte): $fe"
  if [ "$fe" -gt 0 ]; then
    g log --author="$AUTHOR" -i --numstat --format='' -- '*.tsx' '*.jsx' '*.vue' '*.svelte' \
      | awk '{a+=$1;d+=$2} END{printf "     linhas frontend: +%d -%d\n", a, d}'
  fi
  echo "   linguagens por extensão (arquivos tocados):"
  g log --author="$AUTHOR" -i --name-only --format='' | grep -o '\.[a-zA-Z0-9]*$' | sort | uniq -c | sort -rn | head -8 | sed 's/^/     /'
  echo "   autores do repo (para conferir o filtro):"
  g shortlog -sne --all | head -5 | sed 's/^/     /'
done
