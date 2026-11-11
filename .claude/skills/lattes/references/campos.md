# Mapa de campos do Lattes

Onde cada tipo de fato entra no formulário da Plataforma Lattes, os campos que importam e
as regras de validação de cada um. Caminho sempre a partir de **Atualizar currículo**; os nomes
exatos dos menus estão em `menus.md`.

## Sumário

- [Regras gerais](#regras-gerais)
- [Produção bibliográfica](#produção-bibliográfica)
- [Produção técnica](#produção-técnica)
- [Eventos](#eventos)
- [Orientações](#orientações)
- [Atuação profissional](#atuação-profissional)
- [Projetos](#projetos)
- [Dados gerais](#dados-gerais)
- [Qual seção para cada fato](#qual-seção-para-cada-fato)

## Regras gerais

- **Autoria:** ordem idêntica à do documento publicado. Para o Ronildo, nome em citações
  `SILVA, R. O.` (é o que o Lattes registra; manter um só padrão evita a produção aparecer
  como de outra pessoa nas buscas e no Currículo-Sucupira).
- **Coautor com Lattes:** buscar pelo nome para vincular o CV dele. Sem Lattes: incluir só
  nome completo e nome em citações (`SOBRENOME, I. I.`).
- **DOI:** só o DOI daquele item. O DOI de um pacote de código no Zenodo vai no software,
  nunca no artigo. Formato `10.xxxx/...`, sem `https://doi.org/`.
- **Datas:** o Lattes trabalha com ano (produção) ou mês/ano (vínculos, atividades). Use a
  data do documento, não a de cadastro.
- **Uma informação, um lugar:** o mesmo trabalho aparece em até três seções com papéis
  diferentes (anais, apresentação, participação no evento). Isso é esperado; o que não pode
  é cadastrar o mesmo artigo duas vezes em Produção bibliográfica.
- **Vínculo de produção a projeto:** depois de cadastrar o projeto, vincular cada produção a
  ele. É o que faz o projeto mostrar "Número de produções" e conta em relatórios de agência.
- **Campos `[ ]`:** quando o fato não está em nenhuma fonte, deixe `[ ]` no guia e diga ao
  usuário de onde tirar (ficha catalográfica dos anais, contrato, grade do curso).

## Produção bibliográfica

Caminho: **Produções → Produção bibliográfica**

| Tipo | Quando | Campos críticos |
| --- | --- | --- |
| Artigos completos publicados em periódicos | Revista com ISSN (ex.: JIDM) | ISSN, volume, fascículo, páginas, DOI |
| Trabalhos publicados em anais de eventos | Congresso, simpósio | **Natureza** (Completo / Resumo / Resumo expandido), nome do evento, classificação (Local/Regional/Nacional/Internacional), cidade e ano do evento, título dos anais, páginas, ISBN |
| Resumos expandidos em anais | Encontros Universitários e afins | entra como trabalho em anais com natureza Resumo expandido |
| Capítulos de livros | Livro com ISBN | ISBN, organizadores, editora |
| Texto em jornal ou revista (magazine) | Divulgação (não revisado por pares) | — |
| Apresentação de trabalho e palestra | Toda apresentação oral ou pôster, e palestras | natureza (Comunicação / Conferência / Congresso / Seminário / Simpósio / Outra), evento, instituição promotora, cidade |

**Validação:** natureza "Completo" exige artigo integral nos anais. Na dúvida, perguntar;
declarar resumo como completo é o erro que mais derruba ponto em barema.

## Produção técnica

Caminho: **Produções → Produção técnica**

| Tipo | Quando | Campos críticos |
| --- | --- | --- |
| Programa de computador sem registro | Repositório público, pacote Zenodo | home page, DOI, finalidade, plataforma, ambiente, disponibilidade (Irrestrita) |
| Cursos de curta duração ministrados | Oficinas, minicursos | carga horária, participação (Docente) |
| Relatório de pesquisa | Relatório técnico entregue a financiador | — |

## Eventos

Caminho: **Eventos → Participação em eventos, congressos, exposições, feiras e olimpíadas** (ou **Organização de eventos, ...**)

Campos: nome, tipo (Congresso, Encontro, Seminário, Simpósio, Oficina, Outra), forma de
participação (Participante, Ouvinte), tipo de participação (Apresentação oral, Pôster,
Ouvinte), título do trabalho, ano, cidade, instituição promotora. Carga horária vai em
Informações adicionais.

## Orientações

Caminho: **Orientações → Orientações e supervisões em andamento** (ou **concluídas**)

| Natureza | Quando |
| --- | --- |
| Trabalho de conclusão de curso de graduação | Orientação formal de TCC |
| Iniciação científica | Aluno em projeto de pesquisa, com ou sem bolsa |
| Monografia de especialização | Pós lato sensu |
| Dissertação / Tese | Mestrado / doutorado (orientador ou coorientador) |
| Orientação de outra natureza | Estágio supervisionado, monitoria, tutoria |

Campos: tipo de orientação (Orientador principal / Coorientador), título, ano de início,
nome do orientando, instituição, curso, bolsa e agência. Uma entrada **por aluno**. O
mesmo aluno pode ter TCC e IC em entradas separadas.

Ao concluir: mover para **concluídas**, informando ano de conclusão. Concluídas são as que
contam em concurso; em andamento mostram atividade.

## Atuação profissional

Caminho: **Atuação → Atuação profissional** → instituição

- **Vínculo institucional:** tipo (Celetista, Servidor público, Colaborador, Bolsista,
  Professor visitante, Outro), enquadramento funcional (cargo), carga horária semanal,
  mês/ano de início e fim, dedicação exclusiva (sim/não), outras informações.
- **Atividades** (dentro da instituição): Ensino (curso, disciplinas), Pesquisa e
  desenvolvimento (linha), Projetos de pesquisa, Direção e administração, Conselhos,
  Estágios, Serviços técnicos, Extensão.

**Validação:** o enquadramento é o cargo no contrato, não o título de mercado do LinkedIn
(ex.: "Analista de Desenvolvimento de Sistemas" na SEPLAG). Período deve bater com o
LinkedIn e com documentos; divergência maior que um mês, perguntar.

## Projetos

Caminho: **Projetos → Projetos de pesquisa** (ou desenvolvimento tecnológico, extensão, ensino). É menu
próprio na barra de cima; a instituição é escolhida dentro do formulário.

Campos: nome, ano início/fim, situação (Em andamento / Concluído / Desativado), natureza,
descrição, alunos envolvidos por nível, integrantes com papel (Coordenador / Integrante),
financiadores, número de produções.

## Dados gerais

- **Resumo** (Dados gerais → Texto inicial do Currículo Lattes): texto em terceira pessoa. Precisa citar o vínculo **atual** e não pode dizer
  "atua como" sobre vínculo encerrado. Atualizar a cada mudança de emprego.
- **Dados gerais → Identificação:** ORCID (`0009-0008-4629-117X`), Google Scholar,
  ResearcherID.
- **Formação acadêmica:** nome do curso como está no diploma ou contrato; em andamento com
  ano de início.
- **Áreas de atuação:** até 6. Subárea não deve repetir a área.

## Qual seção para cada fato

| Fato nas fontes do repositório | Seção no Lattes |
| --- | --- |
| Artigo em congresso (`portfolio/04-producao-cientifica/`) | Trabalhos publicados em anais de eventos + Apresentação de trabalho e palestra + Participação em eventos |
| Certificado de apresentação | Apresentação de trabalho (comprova; não cria produção nova) |
| Pacote Zenodo / repositório GitHub público | Software sem registro |
| Aluno coautor | Orientação (TCC ou IC) |
| Projeto que coordena | Projeto de pesquisa, com você como Coordenador |
| Disciplina que leciona | Atuação → Atuação profissional → vínculo → Ensino |
| Tema de pesquisa contínuo | Atuação → Linhas de pesquisa |
| Código ou dado aberto | Produção Técnica → Programa de computador sem registro, e marcar em Educação e Popularização de C&T |
| Software com registro no INPI | Patentes e Registros → Programa de Computador Registrado |
| Banca de TCC | Bancas → Participação em bancas de trabalhos de conclusão |
| Emprego novo (`LINKEDIN.md` seção 6) | Atuação profissional + resumo |
| Certificação (`portfolio/03-certificacoes/`) | Formação complementar (com carga horária) ou Prêmios e títulos |
| Curso livre (`portfolio/08-cursos/`) | Formação complementar, só os relevantes (o Lattes não é catálogo) |
| Best Paper, menção honrosa | Prêmios e títulos |
