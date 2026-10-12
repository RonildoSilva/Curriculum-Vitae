# Banco de perguntas e respostas · processos seletivos

Respostas para formulários de triagem e entrevistas, organizadas por tipo de vaga e montadas a
partir de `LINKEDIN.md` e da experiência real. Empresa, link, status e pretensão salarial ficam
em `perguntas-entrevista.privado.md`, que o git ignora.

Convenções:

- `[ ]` marca um dado que ainda não está no repositório. Preencha antes de enviar.
- Quando uma pergunta se repetir em outra vaga, copie a resposta e adapte. As perguntas que mais
  se repetem ficam reunidas no fim, em **Respostas reutilizáveis**.
- Respostas de formulário: até ~1.200 caracteres. Em entrevista, a mesma história contada em 2 minutos.

---

## Vaga: Analista de Dados Sênior

### 1. Qual o seu nível de proficiência em Python e SQL para manipulação e estruturação de pipelines de dados?

> **Python: avançado.** Uso Python em produção há cerca de 8 anos. Hoje, na WeCogno, mantenho o
> backend e a camada de dados de um SaaS de prevenção de churn (FastAPI, SQLAlchemy 2.0 async,
> Airflow), incluindo o loader de Parquet com upsert no PostgreSQL do pipeline Medallion (Bronze,
> Silver, Gold). Antes, construí pipelines com PySpark e AWS Glue no Big Data Ceará (SEPLAG-CE) e
> na New Rizon, e integração de dados com Delta Lake no Big Data Social. Uso pandas e PySpark para
> manipulação, pytest para testes (unitários e de integração com banco real) e ruff para padronização.
>
> **SQL: avançado.** Escrevo SQL analítico (CTEs, window functions, agregações para indicadores como
> MRR e evolução de contas críticas), modelo tabelas e versiono o schema com migrations (dbmate).
> Trabalhei com PostgreSQL (incluindo Row Level Security para isolamento multi-tenant e pgvector),
> Oracle, MySQL e MongoDB.

### 2. Descreva uma situação real em que você precisou investigar uma divergência ou inconsistência de dados em produção. Como foi o processo até encontrar a causa raiz?

Caso real: **Big Data Ceará (SEPLAG-CE, 2023 a 2025)**, cruzamento do CadÚnico com o Ceará Digital
para o programa Criança Feliz. Versão de formulário (~1.200 caracteres) e roteiro para entrevista.

**Versão de formulário:**

> No Big Data Ceará (SEPLAG-CE), cruzávamos o CadÚnico, da Secretaria de Proteção Social, com a base
> do Ceará Digital, da SEPLAG, para identificar as famílias do programa Criança Feliz. Percebi que o
> cruzamento não fechava. Investigando as bases, encontrei a causa: os dados de algumas secretarias
> chegavam anonimizados, e cada órgão usava chaves diferentes, o que tornava inviável a relação 1:1
> entre as pessoas. Propus usar o hash do CPF como chave comum entre as bases, o que permitiu o
> cruzamento sem expor o dado pessoal. Também particionei os dados por essa chave para acelerar a
> busca e a identificação de pessoas, e passei a tratar o data drift entre cargas comparando
> timestamps para detectar registros novos e alterados. O resultado foi um cruzamento consistente e
> mais seguro, 60% menos armazenamento e consultas 3 vezes mais rápidas.

**Roteiro para entrevista (STAR):**

- **Situação.** Programa Criança Feliz: era preciso identificar as famílias elegíveis cruzando o
  CadÚnico (Secretaria de Proteção Social) com o Ceará Digital (SEPLAG). Eram duas secretarias, duas
  bases, com chaves diferentes.
- **Como percebi.** Fui eu que notei que o resultado do cruzamento não fechava e fui atrás da causa.
- **Causa raiz.** Os dados de algumas secretarias chegavam anonimizados, e cada base tinha a sua
  própria chave. Sem um identificador comum, a relação 1:1 entre as pessoas ficava inviável.
- **Solução que propus.**
  - Hash do CPF como chave comum entre as secretarias: o cruzamento passou a funcionar sem que o CPF
    trafegasse em claro (mais seguro e alinhado à LGPD).
  - Particionamento pela chave hasheada, para buscar e identificar uma pessoa sem varrer a base toda.
  - Tratamento de data drift por comparação de timestamps entre cargas, identificando o que era novo
    ou tinha mudado em vez de reprocessar tudo.
- **Resultado.** Cruzamento consistente e mais seguro, **60% menos armazenamento** e **requisições
  3 vezes mais rápidas**.
- **O que eu levo disso.** Cruzamento entre órgãos falha nas chaves e nos contratos de dados, não no
  código do join. Por isso hoje começo qualquer integração definindo a chave, o formato e as
  validações de cada carga.

### 3. Quais ferramentas, orquestradores e arquiteturas de dados você já utilizou na prática em ambiente de produção?

> **Orquestração:** Apache Airflow (WeCogno; `[ ]` New Rizon).
>
> **Processamento:** Python (pandas), PySpark e AWS Glue para ETL em lote; Delta Lake na integração
> de dados sociais do Governo do Ceará.
>
> **Armazenamento e bancos:** Amazon S3, Amazon RDS, PostgreSQL 16 (com pgvector e Row Level
> Security), Oracle, MySQL, MongoDB, arquivos Parquet.
>
> **Arquiteturas:** Medallion (Bronze, Silver, Gold) com carga incremental via upsert; data lake em
> S3 com catálogo Glue; lakehouse com Delta Lake e PostgreSQL servindo a camada analítica; serviços
> REST (FastAPI, Spring Boot) expondo indicadores para painéis; RAG com embeddings em pgvector.
>
> **Engenharia e operação:** Docker, migrations versionadas (dbmate), CI com testes automatizados,
> observabilidade com Grafana, Kibana e AppDynamics (OSF Digital).
>
> **Contexto:** Big Data Ceará e Big Data Social (governo estadual), SINESP (segurança pública
> nacional), mercado financeiro (OSF Digital) e SaaS de saúde (WeCogno).
>
> Também me formei em GCP (BigQuery, Dataflow), com cursos e skill badges do Google Cloud, mas não
> usei a plataforma em produção.

Revise o último parágrafo. Databricks aparece nas suas competências do LinkedIn, mas sem projeto
associado: se você usou em produção, inclua acima. Se usou BigQuery em produção, mova para cima.

### 4. Qual é a sua pretensão salarial?

Resposta em `perguntas-entrevista.privado.md`.

---

## Vaga: Pesquisador em IA Generativa (RAG, GraphRAG, agentes e avaliação)

### 1. Qual foi o tema central da sua pesquisa no mestrado ou doutorado, e como ele se relaciona com as atividades e desafios previstos para esta vaga?

> No mestrado em Ciência da Computação pela UFC, pesquisei a predição do tempo restante para a
> conclusão de processos de negócio usando aprendizado profundo. Modelei logs de eventos
> corporativos como sequências e comparei arquiteturas de redes recorrentes com o estado da arte
> em dois datasets públicos (BPI Challenge 2012 e Helpdesk), com partição temporal e erro absoluto
> médio como métrica. O trabalho virou artigo completo no SBBD 2023. Minhas linhas de pesquisa
> incluíam também mineração de processos e web semântica.
>
> A relação com a vaga aparece em três pontos. Primeiro, conhecimento corporativo estruturado:
> mineração de processos trata o funcionamento de uma empresa como um grafo de atividades e
> relações, que é a mesma matéria-prima do GraphRAG em ambiente corporativo. Segundo, semântica:
> ontologias e grafos de conhecimento são a base de um MCP semântico, que expõe ao agente não só
> ferramentas, mas o significado dos dados. Terceiro, método de avaliação: a dissertação me treinou
> a comparar abordagens contra baselines, com protocolo reprodutível e sem vazamento entre treino e
> teste, que é o que a avaliação de respostas de agentes e de estratégias de busca exige.
> Hoje aplico isso na indústria, com RAG e LLM em produção num SaaS.

### 2. Possui conhecimento em LLMs, RAG, GraphRAG?

> Sim. Em LLMs e RAG tenho experiência prática em produção: construí o backend de um chat com RAG
> num SaaS de prevenção de churn. Em GraphRAG meu conhecimento é teórico, de estudo da literatura
> e das implementações de referência, sem projeto em produção. É um dos pontos que quero
> aprofundar.

### 3. Você possui conhecimento em LLMs, RAG e GraphRAG? Explique brevemente o que conhece sobre esses conceitos e como são utilizados em aplicações de inteligência artificial, recuperação de informações e geração de respostas contextualizadas. Caso tenha experiência acadêmica ou prática, cite um exemplo.

> **LLMs** são modelos de linguagem treinados em grandes volumes de texto que geram respostas a
> partir de um prompt. Sozinhos, respondem com o que aprenderam no treino, o que gera respostas
> desatualizadas ou inventadas sobre dados privados da empresa.
>
> **RAG** resolve isso buscando trechos relevantes de uma base própria e colocando-os no contexto do
> modelo. O pipeline típico: ingestão, divisão em trechos (chunking), embeddings, índice vetorial,
> recuperação dos k trechos mais próximos e geração condicionada a eles. A busca híbrida combina a
> similaridade vetorial com busca lexical (BM25), por exemplo com fusão de rankings (RRF) e
> reranking, porque termos exatos, siglas e códigos escapam dos embeddings.
>
> **GraphRAG** organiza o conhecimento como grafo: um LLM extrai entidades e relações dos
> documentos, o grafo é agrupado em comunidades e cada comunidade ganha um resumo. Isso permite
> responder perguntas globais ("quais os principais riscos citados no conjunto?") e perguntas com
> vários saltos entre entidades, onde o RAG vetorial puro falha.
>
> **Exemplo prático.** Na WeCogno construí o backend do chat com RAG de uma plataforma SaaS:
> ingestão de PDF e DOCX com chunking, embeddings com modelo local (sentence-transformers) em
> PostgreSQL com pgvector, busca por similaridade de cosseno restrita ao cliente (tenant) com Row
> Level Security, histórico de conversa, prompts de sistema por cliente com fallback e respostas em
> streaming. Também implementei um insight automático por conta, em que o LLM gera o texto apoiado
> nos dados da conta e nos principais fatores de risco explicados via SHAP.

### 4. Possui conhecimento em Agentes de IA, MCP, Avaliação de respostas, Grounding e segurança de IA?

> Sim. Tenho prática em grounding e segurança de RAG em produção (isolamento de dados por cliente,
> respostas apoiadas em dados estruturados) e em MCP com um protótipo de servidor com RAG. Em
> agentes e avaliação de IA generativa tenho base de estudo e de método científico, e estou
> aprofundando na pós-graduação em Engenharia de Software em IA Aplicada, em andamento.

### 5. Você possui conhecimento em Agentes de IA, MCP, avaliação de respostas, grounding e segurança de IA? Explique brevemente o que conhece sobre esses conceitos e como são utilizados no desenvolvimento, integração, avaliação e uso seguro de aplicações baseadas em inteligência artificial. Caso tenha experiência acadêmica ou prática, cite um exemplo.

> **Agentes de IA** são LLMs em laço: planejam, chamam ferramentas, observam o resultado e decidem o
> próximo passo, com memória e, nos pontos críticos, aprovação humana. **MCP** (Model Context
> Protocol) padroniza como o agente acessa ferramentas, recursos e prompts expostos por servidores,
> o que desacopla o agente das integrações e permite controlar permissões em um ponto só.
>
> **Grounding** é garantir que a resposta se apoie em fontes recuperadas e verificáveis: instruir
> o modelo a responder só com o contexto, citar o trecho de origem e se abster quando a evidência
> não basta. A **rastreabilidade** registra quais documentos, versões e chamadas de ferramenta
> produziram cada resposta. A **avaliação** separa recuperação (recall@k, MRR) de geração
> (fidelidade ao contexto, relevância, correção), com um conjunto de referência, LLM como juiz
> calibrado com anotação humana e testes de regressão a cada mudança de prompt ou modelo.
> **Segurança** cobre prompt injection (inclusive indireta, vinda de documentos), vazamento de
> dados entre usuários, dados pessoais (LGPD), ferramentas com privilégio mínimo e logs sem segredos.
>
> **Exemplos práticos.** Na WeCogno, garanti que o RAG só recupera documentos do próprio cliente,
> com Row Level Security no PostgreSQL e testes de integração contra banco real que verificam esse
> isolamento. Em outro produto SaaS, fiz a redação de segredos nos logs e o mascaramento de tokens.
> Estendi um protótipo de servidor MCP com RAG (FastAPI) com o domínio do produto, e uso agentes de
> código no dia a dia com especificação revisada antes da implementação. Para explicabilidade, a
> plataforma expõe os fatores de cada previsão via SHAP. Do mestrado trago o rigor de avaliação:
> baselines, partição sem vazamento e métricas definidas antes do experimento.

---

## Respostas reutilizáveis

Trechos curtos para perguntas que aparecem em quase toda vaga.

### Resumo profissional (pitch de 30 segundos)

> Sou engenheiro de software e dados, mestre em Ciência da Computação pela UFC. Há cerca de 8
> anos construo pipelines, APIs e camadas analíticas em Python, SQL, Spark, Airflow e AWS. Trabalhei
> em plataformas de dados de governo (Big Data Ceará, Big Data Social, SINESP), no mercado financeiro
> (OSF Digital) e, hoje, num SaaS de prevenção de churn em saúde na WeCogno, com RAG e LLM em
> produção. Também sou professor de ensino superior e instrutor certificado Huawei HCIA-AI.

### Disponibilidade e modelo de trabalho

> `[ ]` Remoto, híbrido ou presencial. Hoje moro em `[ ]`.

### Inglês

> Avançado (EF Level 16, CEFR C2). Leio documentação, escrevo e converso em reuniões técnicas em inglês.

### Formação

> Mestrado em Ciência da Computação pela UFC (2023), com artigo completo no SBBD 2023 sobre predição
> de tempo restante em processos de negócio usando aprendizado profundo. Bacharelado em Ciência da
> Computação pela UFC. Pós-graduação em Engenharia de Software em IA Aplicada em andamento
> (Anhanguera/UNIPDS, 2026 a 2027).

---

## Modelo para uma nova vaga

```markdown
## Vaga: <cargo>

### 1. <pergunta>

> <resposta>
```
