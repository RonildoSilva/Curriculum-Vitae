# Ronildo Oliveira da Silva

**Engenheiro de Software e Dados · Mestre em Computação (UFC)**
Backend, pipelines e IA aplicada (RAG, LLM) em produção · perfil analítico com base em pesquisa

Pau dos Ferros, RN · remoto · ronildo.comp@gmail.com · (88) 99639-7977
[linkedin.com/in/ronildooliveira](https://www.linkedin.com/in/ronildooliveira/) · [github.com/RonildoSilva](https://github.com/RonildoSilva) · [Portfólio verificável](https://ronildosilva.github.io/Curriculum-Vitae/) · [Lattes](http://lattes.cnpq.br/1445392245409691)

---

## Resumo

Engenheiro com 8 anos entre pesquisa aplicada em aprendizado de máquina e engenharia de software para dados. Formação analítica de mestrado: desenho de experimentos, partição temporal de dados, comparação contra baselines do estado da arte e publicação em conferência nacional (SBBD 2023). No dia a dia, construo APIs, pipelines e camadas de IA em Python sobre PostgreSQL, com testes automatizados e documentação de decisão (ADRs, canvases de especificação) revisada em pull request antes do código.

Uso Claude Code como parte central do fluxo de trabalho desde 2026, não como apoio pontual: especificação, implementação, testes e revisão passam por agentes, com regras por repositório e histórico em mais de 20 projetos.

Pontos de aderência à vaga: fundamentação técnica e analítica, experimentação com métricas, uso fluente de agentes de IA, comunicação técnica (docência e instrutor certificado). Ponto a desenvolver: React, onde tenho leitura e integração de API em monorepo, mas não entregas próprias de interface.

---

## Experiência

### WeCogno (antiga DataRisk) · Engenheiro de Software

**mar 2026 – atual · Florianópolis, SC (remoto)**

SaaS de prevenção de churn para operadoras de saúde. Monorepo com FastAPI, SQLAlchemy 2.0 async, PostgreSQL 16 com pgvector, Airflow e React.

- 187 commits e 23 pull requests mergeados em 3 repositórios em 6 meses, com 328 funções de teste escritas (unitários, integração com banco real e E2E).
- Backend do chat com RAG: ingestão de PDF e DOCX, chunking e embeddings em pgvector, histórico de conversas, prompts por tenant e streaming via SSE.
- 29 endpoints da API de risco: listagem e detalhe de contas com health score, explicabilidade dos drivers via SHAP, estatísticas de membros, MRR e MRA em risco, evolução de críticos.
- Busca e ordenação em API de listagem: busca por nome e documento, filtros por risco e tendência, ordenação dinâmica, sem N+1 (SQL e índices, sem engine de busca dedicada).
- Isolamento multi-tenant com Row Level Security em todas as tabelas e teste de arquitetura que trava a direção das dependências (DDD e hexagonal).
- Loader Parquet com upsert para o pipeline Medallion (Bronze, Silver, Gold) e migrations dbmate, incluindo o contrato de carga de MRR e MRA.
- Desenvolvimento orientado a especificação com Claude Code: 27 canvases REASONS (requisitos, entidades, abordagem, testes) revisados em PR antes do código; CLAUDE.md por repositório; protótipo de servidor MCP com RAG para expor a base de conhecimento a agentes.

### Fundação Cearense de Pesquisa e Cultura (FCPC) · Desenvolvedor Back-end

**nov 2025 – mar 2026 · Fortaleza, CE**

Plataforma segura de mensageria para a Agência Brasileira de Inteligência (ABIN), alternativa soberana a WhatsApp e Telegram para órgãos do SISBIN.

- Serviços backend em Django com autenticação e autorização centralizadas em Keycloak, foco em confidencialidade e autonomia operacional.

### New Rizon · Engenheiro de Dados

**mai 2025 – nov 2025 · Barueri, SP (remoto)**

- Pipelines de dados na AWS (Glue, S3) com Python e SQL, integração de múltiplas fontes e APIs, automação de fluxos.
- Agentes de IA com LLM para suporte jurídico.

### ExACTa PUC-Rio · Desenvolvedor de Software

**jan 2025 – abr 2025 · Rio de Janeiro, RJ**

- Desenvolvimento de software em laboratório de engenharia de software e IA da PUC-Rio.

### Secretaria do Planejamento e Gestão do Ceará (SEPLAG-CE) · Analista de Desenvolvimento de Sistemas

**mai 2023 – jan 2025 · Fortaleza, CE**

Plataformas estaduais de dados: Big Data Ceará, SUITE (processo eletrônico), Ceará Digital e Observai.

- Pipelines de Big Data e infraestrutura em nuvem (AWS Glue, S3, RDS) integrando bases de múltiplos órgãos.
- APIs e serviços de dados (Spring Boot, MongoDB, REST) que alimentam painéis de gestores.
- Ceará Digital: motor de busca de serviços públicos para o cidadão.

### ÍRIS, Laboratório de Inovação e Dados do Governo do Ceará · Cientista de P&D

**mar 2022 – mai 2023 · Fortaleza, CE**

- Big Data Social: integração de indicadores de auxílios sociais, educação, moradia, trabalho e renda em arquitetura Delta Lake e PostgreSQL, com serviços REST em Spring Boot. Programa Cientista Chefe. Apresentação na CGE em 2022.

### OSF Digital · Desenvolvedor Back-end

**nov 2020 – mar 2022 · remoto (empresa canadense)**

- APIs em Spring Boot sobre Oracle para clientes do setor financeiro.
- Observabilidade com Kibana, Grafana e AppDynamics; análise de métricas de performance.

### Universidade Federal do Ceará · Instrutor, projeto HCIA AI ATLAS Training CE

**out 2020 – mar 2021 · Crateús, CE**

- Aulas práticas de machine learning e deep learning (TensorFlow, MindSpore) para a certificação Huawei HCIA-AI, acordo UFC, ASTEF e Huawei. Certificado como Huawei Certified Academy Instructor.

### Insight Data Science Lab (UFC) · Bolsista de Pesquisa

**out 2019 – dez 2020 · Quixadá, CE**

- Projeto SINESP Big Data e IA para Segurança Pública (Ministério da Justiça): componentes de integração de dados dos estados, modelos de detecção de anomalias e predição, mineração de processos.

### FUNCAP / UFC · Bolsista de Inovação Tecnológica

**mar 2018 – set 2019 · Quixadá, CE**

- Visão computacional para identificação por impressões digitais (SSPDS-CE e PRF): avaliação comparativa de extratores e matchers de minúcias e proposta de melhoria sobre o NBIS. Dois trabalhos publicados, um com Best Paper.

### iFactory Solutions · Estagiário em Desenvolvimento

**ago 2016 – jan 2018 · Quixadá, CE**

- Frontend em AngularJS e JSP e automações em ServiceNow para a operação global da Hyatt Hotels.

Anteriores: monitor de Fundamentos de Programação, POO e Estrutura de Dados Avançada (UFC, 2014–2016); monitor de Programação Estruturada (IFCE, 2012).

---

## Formação

|                                          |                               |             |
| ---------------------------------------- | ----------------------------- | ----------- |
| **Mestrado em Ciência da Computação**    | Universidade Federal do Ceará | 2020 – 2023 |
| **Bacharelado em Ciência da Computação** | Universidade Federal do Ceará | 2014 – 2019 |
| **Técnico em Informática**               | IFCE                          | 2009 – 2013 |

Dissertação: predição de tempo restante em processos de negócio com redes recorrentes. Aprovado no POSCOMP 2019 e no processo seletivo de doutorado em Ciência da Computação da UFC.

## Publicações e pesquisa

- **Predição de Tempo Restante para Conclusão de Processos de Negócio Utilizando Aprendizado Profundo.** SBBD 2023, artigo completo. Arquiteturas recorrentes avaliadas em dois datasets públicos (BPI 12 e Helpdesk 17) com partição temporal treino/validação/teste e MAE, superando baselines do estado da arte.
- **Análise de Extratores e Matchers de Minúcias em Impressões Digitais.** Best Paper, Encontros Universitários UFC 2019.
- Proposta de Melhoria na Detecção de Minúcias pelo NBIS (2018); Reconhecimento de Textos Manuscritos com Aprendizado de Máquina (2017); dois relatos sobre docência (2015, 2016).
- TCC: análise de acurácia da Google Cloud Vision API em textos de imagens naturais.

## Competências

| Área                       | Nível  | Detalhe                                                                                                                                                       |
| -------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Análise e experimentação   | Sólido | Desenho experimental, partição de dados, métricas (MAE), comparação com baselines, explicabilidade (SHAP), estatística aplicada                               |
| Backend                    | Sólido | Python, FastAPI, SQLAlchemy, Django, Java, Spring Boot, REST, DDD e arquitetura hexagonal, testes automatizados                                               |
| Dados                      | Sólido | PostgreSQL, pgvector, SQL, Spark, Airflow, Delta Lake, AWS Glue e S3, GCP e BigQuery, Parquet, Medallion                                                      |
| IA aplicada                | Sólido | RAG, LLMs, embeddings, MCP, TensorFlow, scikit-learn, mineração de processos, visão computacional                                                             |
| Ferramentas de IA no fluxo | Sólido | Claude Code (diário, regras por repositório, especificação e revisão com agentes), Gemini CLI                                                                 |
| Busca                      | Básico | Busca textual em SQL, ordenação e filtros em API; Kibana para observabilidade. Sem Elasticsearch ou ranking como engine                                       |
| Experimentos com usuários  | Básico | Sem testes A/B online ou analytics de produto em produção; base estatística e experimental vem da pesquisa                                                    |
| Frontend                   | Básico | JavaScript, TypeScript (leitura), HTML e CSS, AngularJS (2016–18). React: convivência em monorepo e contratos de API para o app web, sem componentes próprios |

## Certificações

Huawei HCIA-AI V3 (2024) · Huawei Certified Academy Instructor (2021) · Huawei HCIA 5G (2020) · Google Cloud Arcade Facilitator (2025) · Scrum Foundation e DevOps Essentials (CertiProf, 2019) · Especializações Coursera: Data Engineering on Google Cloud, Algorithms (Stanford), Process Mining (TU Eindhoven).

## Idiomas

Português nativo · Inglês B2 (TOELF) · Espanhol intermediário.
