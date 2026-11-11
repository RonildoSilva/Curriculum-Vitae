---
name: lattes
description: Orienta o preenchimento do Currículo Lattes campo a campo e verifica e valida o Lattes contra as fontes deste repositório (catálogo, README, LINKEDIN.md, certificados em portfolio/, registros Zenodo). Use sempre que o usuário mencionar Lattes, CNPq, "atualizar o currículo" acadêmico, apontar um PDF em _raw/lattes/, pedir "o que colar em cada campo", ou quando surgir produção nova (artigo, certificado de apresentação, software/DOI, orientando, projeto, disciplina, emprego) que precise ir para o Lattes. Também use para auditar o Lattes antes de edital de pós, concurso ou bolsa ("meu Lattes está atualizado?", "falta alguma coisa?").
---

# Lattes: preencher, verificar e validar

O Lattes é o currículo que banca de concurso, seleção de pós e agência de fomento leem. Ele
pontua por seção (produção, orientação, projeto), então um fato cadastrado na seção errada
ou com natureza errada vale menos ou nada. O repositório já tem a evidência de quase tudo; a
skill transforma essa evidência em instruções de formulário e confere se o Lattes reflete o
que o repositório sabe.

Arquivos de trabalho ficam em `_raw/lattes/` (ignorado pelo git; o Lattes tem dados que o
repositório público não deve carregar):

- PDF exportado do Lattes (o mais recente é o que vale)
- `atualizacoes.md`: o guia de preenchimento que esta skill mantém

## Fluxo

### 1. Verificar: o que o Lattes não sabe

Peça ou localize o PDF mais recente (no Lattes: *Visualizar currículo → ícone de impressão →
Gerar PDF*). Rode, da raiz do repositório:

```bash
python3 -I .claude/skills/lattes/scripts/verificar-lattes.py [caminho.pdf]
```

O script devolve um relatório com OK / FALTA / AVISO cobrindo:

- data da última atualização (editais pedem até 3 meses) e caracteres corrompidos
- ORCID e nome em citações
- vínculos atuais, resumo citando vínculo encerrado, empregos do `LINKEDIN.md` ausentes
- produções do catálogo e do README ausentes, DOIs Zenodo não cadastrados
- seções esperadas (Orientações, Projetos com você como Coordenador, Eventos)

O script casa títulos pelas primeiras palavras e pode errar com quebra de linha. Antes de
afirmar que algo falta, confira no texto (`pdftotext -layout` + `grep -i`).

Depois complete à mão o que o script não cobre:

- **Fatos que só o usuário informou:** a memória do projeto e
  `.claude/skills/criar-cv/references/fontes.md` (disciplinas, orientandos, projetos).
- **Documentos novos em `_raw/`** ainda não catalogados.
- **Diferenças de nome:** curso de pós, cargo, nome do evento divergindo entre Lattes,
  README e LinkedIn. Aponte; não escolha um lado sem perguntar.

### 2. Preencher: o guia campo a campo

Para cada FALTA confirmada, escreva em `_raw/lattes/atualizacoes.md` a seção do formulário e
o valor de cada campo. Leia `references/campos.md` para saber em que seção cada fato entra e
quais campos importam, e `references/menus.md` para o nome exato de cada menu: o usuário procura
o texto na tela, então "Apresentações de trabalho" em vez de "Apresentação de trabalho e
palestra" o deixa perdido. Formato de cada item:

1. Caminho do menu em negrito, com os nomes de `menus.md`
   (`Produções → Produção Técnica → Programa de computador sem registro`)
2. Tabela `Campo | Colar`, com o valor pronto para copiar em crase
3. `[ ]` no lugar de cada valor que nenhuma fonte tem, dizendo onde achar
4. A nota de vinculação quando o item pertence a um projeto

Se o usuário trouxer capturas de tela do editor (`_raw/lattes/src/`), leia todas e use-as de
três formas:

- **Menus e formulários:** atualize `references/menus.md` (nomes de menu, abas e campos de cada
  formulário) quando algo divergir ou for novo. Ajuste o guia para listar só campos que o
  formulário realmente tem.
- **Progresso:** formulário preenchido na captura vira item marcado no checklist, com a nota
  "preenchido em DD/MM (captura HH-MM-SS)" e os valores conferidos. Ainda não é validação: ela
  só vem com o PDF novo.
- **Desvio:** formulário errado aberto (ex.: *Programa de Computador Registrado* para um pacote
  Zenodo, *Artigos aceitos para publicação* para trabalho de congresso) vira um aviso explícito
  no item correspondente do guia, dizendo onde é o certo e por quê. Não copie as capturas para a skill: elas
mostram a foto do perfil e a skill é versionada num repositório público.

Ordene por peso em avaliação: produção bibliográfica, orientações, projetos, produção
técnica, eventos, atuação, ajustes de texto. Termine com um checklist. Ao reescrever o
guia, preserve os itens que o usuário já marcou como feitos.

Textos longos (resumo, descrição de projeto) vão em bloco de código para copiar inteiro.
O resumo é em terceira pessoa, cita o vínculo atual primeiro e não diz "atua como" sobre
vínculo encerrado.

### 3. Validar: antes de dizer que está pronto

Quando o usuário trouxer um PDF novo depois de cadastrar, rode o script de novo e confira,
item a item do checklist:

- **Autoria:** ordem e nomes iguais aos do documento publicado; orientandos como coautores.
- **Natureza:** "Completo" só com artigo integral nos anais.
- **Registro falso:** o script avisa quando um programa de computador aparece em Patentes e
  registros com uma instituição que não é órgão de registro (ex.: zenodo.org). Isso declara
  propriedade intelectual que não existe; peça para excluir e refazer como "sem registro".
- **Formulário certo:** trabalho de congresso não entra em *Artigos aceitos para publicação*
  (é para periódico); software sem registro no INPI não entra em *Programa de Computador
  Registrado*.
- **Marcações de Dados gerais:** "10 mais relevantes" só para artigos em periódico e anais
  completos (o limite é 10); "popularização de CeT" sim para código e dados abertos, palestra
  ao público e material didático, não para artigo científico.
- **DOI no item certo:** DOI do Zenodo no software, não no artigo.
- **Coerência de datas:** produção no ano do evento; vínculo e atividades sem sobreposição
  impossível; orientação concluída só com ano de conclusão.
- **Duplicidade:** o mesmo artigo não pode aparecer duas vezes em produção bibliográfica.
  Anais + apresentação + participação é o padrão correto.
- **Sem dado sensível:** CPF, endereço residencial, telefone e salário nunca entram no guia.

Marque no checklist o que passou, com a data e a hora do PDF validado, e liste o que ainda
falta.

O PDF do Lattes **não** vai para o repositório: o README aponta para o link público
(lattes.cnpq.br), que é sempre a versão atual, e um PDF copiado fica velho na próxima edição.
O PDF fica só em `_raw/lattes/`, como insumo da verificação.

## Princípios

- **Evidência antes de campo.** Todo valor sugerido vem de um documento, do catálogo ou de
  algo que o usuário disse. Valor inventado no Lattes é declaração falsa a um órgão público.
- **Pergunte o que só o usuário sabe.** Natureza do trabalho, se o aluno é orientando de TCC
  ou de IC, financiamento, títulos de TCC. Uma pergunta curta vale mais que um palpite.
- **Repercuta para o resto do repositório.** Fato novo descoberto no Lattes (ex.: um artigo
  em periódico que não está no README) também vai para catálogo, README e `LINKEDIN.md`.
  Ofereça isso ao usuário em vez de fazer calado.
