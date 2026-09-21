# Onde cada fato mora

| Fato | Fonte primária | Como extrair | Observações |
|---|---|---|---|
| Cargos, datas, empresas | `_raw/linkedin-perfil-atual.md` seção Experiência | leitura direta | Export do LinkedIn. Datas oficiais. Regenerar com `scripts/linkedin-scrape-console.js` se estiver velho (data no cabeçalho). |
| Bullets redigidos por cargo | `LINKEDIN.md` seção 6 | leitura direta | Já em formato verbo, entrega, número. Marcadores `[ ]` indicam número desconhecido: não invente. Números da WeCogno vieram de recontagem em git e envelhecem. |
| Contatos, URL, localização | `LINKEDIN.md` seção 2; `portfolio/09-curriculo/curriculo-ronildo-silva-msc-de-en.pdf` | `pdftotext -layout` | Telefone está no PDF (já público). Localização diverge entre fontes: perguntar ou usar "remoto". |
| Formação, diplomas | `CLAUDE.md` seção Formação; `portfolio/01-formacao-academica/` | leitura direta | Mestrado 2020–2023 (diploma jan 2024). Bacharelado 2014–2019 (diploma 2020). Técnico IFCE 2009–2013. Aprovado em seleção de doutorado UFC. |
| Publicações e método | `portfolio/04-producao-cientifica/*.pdf` | `pdftotext -layout ... \| grep -i -E "abstract\|dataset\|MAE\|teste"` | O artigo SBBD 2023 traz datasets (BPI 12, Helpdesk 17), partição 60/20/20 temporal e MAE. Use quando a vaga valoriza perfil analítico. |
| Certificações | `CLAUDE.md` seção Certificações; `LINKEDIN.md` seção 12 | leitura direta | HCIA-AI vale 3 anos (emitido fev 2024). |
| Docência e pesquisa | `CLAUDE.md`; `portfolio/05-docencia/`, `portfolio/06-projetos-pesquisa/` | leitura direta | Instrutor Huawei, monitorias, 4 projetos financiados. |
| Cursos | `data/catalogo.json`; `LINKEDIN.md` seção 18 | `python3 -c` ou `jq` | 148 cursos; cite só os 3 a 5 relevantes à vaga. |
| Idiomas | `CLAUDE.md`; `portfolio/02-idiomas/` | leitura direta | Inglês C2 (EF Level 16). |
| Skills declaradas no LinkedIn | `_raw/linkedin-perfil-atual.md` linha "Competências (100)" | `grep -i <tecnologia>` | Se a tecnologia não está nem aí, tratar como inexistente até prova em git. |
| Entregas na WeCogno | `~/GithubProjects/datarisk.io/{churn-ai,datarisk-churnai-platform,app-score-bet}` | `scripts/evidencias-git.sh` | Autor: `ronildo.silva@datarisk.io`. Canvases em `docs/spdd/canvases/`. |
| Uso de ferramentas de IA | `~/.claude/projects/` (um diretório por projeto), `CLAUDE.md` e `.claude/` nos repos, `~/.gemini`, `~/.cursor` | `ls`, `find -maxdepth 3 -name CLAUDE.md` | Em set 2026: Claude Code em 22 projetos, Gemini CLI presente, Cursor ausente. |
| Vagas | `cvs/_raw/` | leitura direta | Pasta ignorada pelo git (regra `_raw/` no `.gitignore`). Manter assim. |

## Currículos anteriores para comparar tom

- `portfolio/09-curriculo/curriculo-ronildo-silva-msc-de-en.pdf`: mais recente antes desta skill, foco em dados e backend. Tem "apaixonado" no resumo, evitar.
- `portfolio/09-curriculo/curriculo-lattes.pdf`: Lattes completo, útil para datas de bolsa e projetos.
- `cvs/*/cv.md`: currículos gerados por esta skill, um por vaga.

## Fatos conhecidos sem documento oficial (confirmar com o usuário antes de usar)

- Docência atual em instituição privada (aparece em `~/.claude/projects` como `docencia-unicatolica`, `LinguagensWEB`, `Estágio`). Não está no LinkedIn nem no Lattes.
- Detalhes técnicos de FCPC, New Rizon e ExACTa: só o texto curto do LinkedIn.
