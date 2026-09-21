# Aderência à vaga · Jusbrasil, Engenheiro(a) Fullstack (Search e EVAL)

Análise honesta feita em 21 set 2026 a partir do repositório, do LinkedIn exportado, do Lattes,
dos PDFs em `portfolio/` e do histórico git dos repositórios da WeCogno em `~/GithubProjects/datarisk.io`.
Cada linha diz o que a vaga pede, o que você tem de fato, a evidência e como o CV tratou.

Vaga: `cvs/_raw/vaga_us.md`. CV gerado: `cv.md` (mesma pasta).

## Veredito

Aderência boa no perfil analítico, na fundamentação técnica, no uso de IA e nos diferenciais
acadêmicos. Aderência fraca no requisito "experiência sólida com React" e parcial em
"experimentação e análise de comportamento de usuário". Vale candidatar, com o gap de React
assumido de frente na carta ou na entrevista, não escondido.

| Requisito da vaga | Situação | Evidência | Como o CV trata |
|---|---|---|---|
| Experiência sólida com React | **Não atende** | 0 arquivos `.tsx`/`.jsx` de sua autoria em churn-ai, datarisk-churnai-platform e app-score-bet. Frontend real: AngularJS e JSP na iFactory (2016–18). Um curso de Angular 2 na Udemy. | Listado como "Básico", com a frase exata do que você fez (contratos de API para o app web) e do que não fez (componentes). |
| Perfil analítico, próximo de Data Science | **Atende** | Mestrado; artigo SBBD 2023 com partição temporal 60/20/20, MAE e baselines; best paper 2019; SHAP em produção na WeCogno; projetos SENASP/FUNCAP. | Resumo abre por aí. Seção de publicações detalha o método. |
| Resolução de problemas complexos, fundamentação técnica | **Atende** | 187 commits, 23 PRs, 328 testes em 6 meses; RLS multi-tenant; testes de arquitetura; pipeline Medallion; ADRs. | Bullets da WeCogno. |
| Experimentação, testes, otimização, análise de comportamento de usuário | **Parcial** | Experimentação científica offline, sim. A/B online, analytics de produto, funil de usuário: não há registro. Churn é modelagem de comportamento de cliente, adjacente mas não igual. | Marcado "Básico" em "Experimentos com usuários" com a fonte da base estatística. Não inventa A/B. |
| Uso intenso de ferramentas de IA (Claude Code, Cursor, agentes) | **Atende** | 22 projetos com histórico em `~/.claude/projects`; CLAUDE.md e `.claude/` em 8 repos da WeCogno; 27 canvases REASONS criados por você e revisados em PR; protótipo MCP; Gemini CLI instalado. Cursor: sem evidência, não citado. | Resumo e bullet próprio. Só cita ferramentas com uso comprovado. |
| Comunicação técnica e colaboração | **Atende** | Instrutor certificado Huawei; monitorias; PRs com rodadas de review documentadas; apresentação na CGE 2022; SBBD. | Docência e canvases aparecem; sem adjetivos. |
| Diferencial: Elasticsearch ou similar | **Não atende** | Sem Elasticsearch/OpenSearch/Solr em nenhum repo. Kibana na OSF foi observabilidade, não busca. Ceará Digital consta como "motor de busca para serviços públicos" no seu CV antigo, sem detalhe técnico documentado. Busca global e busca por documento na WeCogno usam `ILIKE` em PostgreSQL (o canvas EDP-121 descarta Elasticsearch explicitamente, e foi implementado por um colega). | "Busca: Básico", com a frase "sem Elasticsearch ou ranking como engine". Ceará Digital citado só como projeto. |
| Diferencial: mestrado ou doutorado | **Atende** | Diploma de mestrado (2024). Aprovado em seleção de doutorado UFC. | Formação. |
| Diferencial: publicações e pesquisa aplicada | **Atende** | 6 trabalhos, 1 em conferência nacional (SBBD), 1 best paper. 4 projetos de pesquisa financiados. | Publicações. |

## O que ficou de fora do CV, e por quê

- **Números do LINKEDIN.md** (236 commits, 22 PRs, 302 testes) foram recontados hoje excluindo merges e incluindo o terceiro repo: 187 commits, 23 PRs, 328 funções de teste. O CV usa os números recontados.
- **Docência atual** (há pastas `docencia-unicatolica`, `Estágio`, `LinguagensWEB` no histórico do Claude Code, em disco externo). Não consta em LinkedIn, Lattes nem no repositório. Se você leciona hoje, é relevante para "comunicação técnica" e para o requisito de React se a disciplina for de web. Confirmar antes de incluir.
- **Cursor**: não citado porque não há instalação nem histórico. A vaga cita como exemplo, não como exigência.
- **FCPC, New Rizon e ExACTa** ficaram curtos porque não há métricas nem detalhes verificáveis além do texto do LinkedIn. Se você tiver números (pipelines, volume, latência), vale acrescentar.
- **Localização**: o LinkedIn diz Pau dos Ferros (RN) e a WeCogno registra Florianópolis. O CV usa Pau dos Ferros e "remoto". Ajuste se preferir.

## Como jogar o gap de React na candidatura

Não prometa React sólido. A vaga diz textualmente que o perfil desejado é "mais próximo de Data
Science do que de engenharia full stack tradicional" e que busca não é pré-requisito. O argumento
honesto: você entrega a metade analítica e de backend hoje, tem histórico de aprender stack sob
demanda (Spring Boot, Django, FastAPI, pgvector em trocas de emprego sucessivas) e já convive com
o React do monorepo. Se quiser reduzir o gap antes da entrevista, um projeto pequeno em React que
consuma uma API sua e mostre um experimento (duas variantes de ranking, métrica, comparação)
cobre React, experimentação e busca de uma vez, e vira item de portfólio verificável.
