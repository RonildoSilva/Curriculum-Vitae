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
- [Formação complementar: o que entra](#formação-complementar-o-que-entra)
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
- **Perguntas de todo formulário de produção:** "10 trabalhos mais relevantes" (reservar para
  artigos em periódico e anais completos; são 10 no total) e "educação e popularização de CeT"
  (sim para código e dados abertos, palestra ao público, material didático).
- **Trabalho aceito em congresso, anais ainda não publicados:** não usar *Artigos aceitos para
  publicação* (é para periódico). Registrar apresentação e participação já; o trabalho em anais
  entra quando os anais saírem.
- **DOI do volume não é DOI do artigo:** anais com DOI só no volume (comum no Even3,
  `10.29327/...`) não dão DOI ao trabalho. O campo DOI fica vazio e o DOI do volume vai em
  Informações adicionais; ISBN, título dos anais e páginas vêm da ficha catalográfica.
- **Qualis de evento:** o Lattes não tem campo de Qualis, mas banca e edital pontuam por
  estrato. Para conferir, use a lista oficial da área (Computação 2017–2020:
  `RelatorioQualisEventos2017-2020-Computacao.pdf`, CAPES) e case pelo **nome completo**,
  nunca só pela sigla. Estado conferido em 15/11/2026:
  - **SBBD** (Simpósio Brasileiro de Banco de Dados): **A4**.
  - **CBS da Uni-FACEF** (Congresso Brasileiro de Sistemas, com o Encontro de Pesquisadores):
    **sem Qualis**. Não está na lista, e os anais são interdisciplinares (CDD 050). Na lista,
    a sigla CBS é do *IEEE International Conference on Cyborg and Bionic Systems* (**B3**), e
    o CBSF (B4) é o *Congresso Brasileiro de Sistemas Fuzzy*: nenhum dos dois é o seu.
    Em barema, o trabalho conta como resumo expandido em anais de evento nacional com ISBN.
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
| Programa de computador sem registro | Repositório público, pacote Zenodo | home page, DOI, finalidade, plataforma, ambiente, disponibilidade (Irrestrita); obrigatórios: **linguagens**, **inventores** (incluindo você), **instituição financiadora** (sem fomento: a instituição onde foi feito) e **potencial de inovação** (código de pesquisa: o nível mais baixo, sem inflar) |
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

## Formação complementar: o que entra

O Lattes não é catálogo de certificados. Banca lê a seção procurando aderência à área do
edital; vinte cursos de 5 a 20 horas escondem os quatro que importam e sinalizam falta de
critério. Barema de docente costuma pontuar só "curso de atualização" a partir de 40 h e
"aperfeiçoamento" a partir de 180 h, e ignora o resto.

Um curso entra se passar nos três filtros:

1. **Carga horária ≥ 40 h**, lida no certificado (não no catálogo, que pode errar). Somar
   cursos para chegar lá só vale quando o certificado é de um programa que os agrupa
   (especialização Coursera, trilha com certificado próprio); aí entra o programa, uma vez,
   e não os cursos soltos.
2. **Aderência** às áreas de atuação e linhas de pesquisa do Lattes ou às disciplinas que
   leciona (computação, ciência de dados, IA, mineração de processos, engenharia de
   software, docência). Curso fora da área (massagem, música, ecologia) não entra, por
   longo que seja.
3. **Emissor verificável:** universidade, instituto federal, fornecedor que aplica exame
   ou plataforma com código de verificação. Comprovante que se declara "não é um
   certificado" entra só se informar carga horária e conclusão.

Exceções:

- **Programa sem carga horária no certificado** (Coursera, edX): some a estimativa que o
  emissor publica para cada curso (teto da faixa "N weeks of study, X–Y hours/week" anexa ao
  certificado, ou a página do curso) e registre em Informações adicionais que é estimativa do
  emissor. Curso sem estimativa conta zero; não arredonde para cima. Especialização contida
  em outro programa (mesmos cursos) é duplicata: fica o maior.
- **Certificação profissional com exame** (ex.: HCIA-AI, instrutor certificado) não é curso
  e não tem carga horária: não entra em Formação complementar, onde precisaria de uma carga
  inventada. Vai em **Dados gerais → Outras informações relevantes**, em texto corrido (nome
  oficial, emissor, ano), e pode ser citada no resumo.
- **Formação técnica de nível médio** já está em Formação acadêmica; cursos de informática
  básica anteriores à graduação saem.
- **Idioma** vai em Idiomas (proficiência). Curso de idioma só fica em Formação
  complementar se for institucional e ≥ 40 h; nota de prova (TOEFL) não é prêmio.

Fora da seção, mas no lugar certo: oficina ou minicurso que **ministrou** vai em Produção
técnica → Cursos de curta duração ministrados; participação em evento vai em Eventos;
certificado de participação (Maratona Xamarin) não é prêmio e sai de Prêmios e títulos.

Tamanho-alvo: 8 a 15 cursos, os mais recentes e aderentes primeiro. Para remover, o caminho
é o mesmo formulário (excluir o item); o Lattes não guarda histórico visível.

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
| Certificação profissional com exame (`portfolio/03-certificacoes/`) | Dados gerais → Outras informações relevantes; nunca Formação complementar sem carga horária, nem Prêmios e títulos |
| Curso livre (`portfolio/08-cursos/`) | Formação complementar, só o que passa nos três filtros de [o que entra](#formação-complementar-o-que-entra) |
| Best Paper, menção honrosa | Prêmios e títulos |
