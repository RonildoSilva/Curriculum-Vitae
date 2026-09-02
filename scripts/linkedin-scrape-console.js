/*
 * linkedin-scrape-console.js  (v4)
 * Exporta o SEU próprio perfil do LinkedIn (logado) para JSON e Markdown.
 *
 * Como usar:
 *   1. Abra https://www.linkedin.com/in/ronildooliveira/ logado.
 *   2. F12 → Console. Se o Chrome pedir, digite "allow pasting" e Enter.
 *   3. Cole este arquivo inteiro e pressione Enter. Leva uns 3 segundos.
 *   4. O navegador baixa linkedin-perfil-<data>.json e linkedin-perfil-<data>.md.
 *      Se o download for bloqueado: copy(window.liPerfilMd)  ou  copy(JSON.stringify(window.liPerfil, null, 2))
 *
 * Como funciona: quando a página principal do perfil é pedida por fetch (sem JavaScript), o LinkedIn
 * devolve uma versão renderizada no servidor com TODAS as seções expandidas (experiência completa,
 * 100 competências, certificados, prêmios, idiomas, cursos, voluntariado, contato). O script lê esse
 * texto e o organiza por seção. As páginas /details/ não vêm renderizadas, por isso não são usadas.
 *
 * Só funciona no seu próprio perfil, com você logado. Não use em perfis de terceiros.
 */

// ------------------------------------------------------------------ parser (puro, testável em node)
const liParse = (() => {
  const NOISE = new Set(['Ver mais', 'Ver menos', '…mais', 'Editar', 'Ver todos', 'Salvar', 'Cancelar', 'Descartar', 'Show more', 'Show less', '…more', 'See all', 'Show all', 'Compartilhar perfil', 'Share profile']);
  const isNoise = (l) => NOISE.has(l) || /^(Adicionar|Solicitar|Deslizar para item|Add |Request |Slide to item)/.test(l);
  const isDate = (l) => /^(?:[a-zçé]{3,4}\.? (?:de )?)?\d{4}$/i.test(l || '') || /^[A-Z][a-z]{2} \d{4}$/.test(l || '');
  const isEnd = (l) => isDate(l) || /^(O momento|Present|Atual)$/i.test(l || '');
  const isDuration = (l) => /^\d+ (anos?|meses|mês|yrs?|mos?)( \d+ (meses|mês|mos?))?$/i.test(l || '');
  const isLocation = (l) => !!l && l.length < 90 && !/^[•\-–]/.test(l) && /,/.test(l) && !/[.!?]$/.test(l) && /(Brasil|Brazil|Remoto|Remote|Híbrido|Hybrid|Presencial|On-site|[A-Z]{2}$)/.test(l);

  // cabeçalhos: [nome interno, texto, regra]  regra: 'add' = próxima linha começa com Adicionar/Solicitar; 'count' = linha anterior é número; 'first' = primeira ocorrência
  const HEADERS = [
    ['sobre', ['Sobre', 'About'], 'first'],
    ['destaque', ['Em destaque', 'Featured'], 'first'],
    ['atividades', ['Atividades', 'Activity'], 'first'],
    ['experiencia', ['Experiência', 'Experience'], 'add'],
    ['formacao', ['Formação acadêmica', 'Education'], 'add'],
    ['voluntariado', ['Experiência de voluntariado', 'Volunteer experience'], 'add'],
    ['competencias', ['Competências', 'Skills'], 'add'],
    ['recomendacoes', ['Recomendações', 'Recommendations'], 'add'],
    ['certificados', ['Certificados', 'Licenses & certifications', 'Certifications'], 'count'],
    ['publicacoes', ['Publicações', 'Publications'], 'count'],
    ['projetos', ['Projetos', 'Projects'], 'count'],
    ['idiomas', ['Idiomas', 'Languages'], 'count'],
    ['cursos', ['Cursos', 'Courses'], 'count'],
    ['reconhecimentos', ['Reconhecimentos', 'Honors & awards'], 'count'],
    ['organizacoes', ['Organizações', 'Organizations'], 'count'],
    ['patentes', ['Patentes', 'Patents'], 'count'],
    ['notas', ['Notas de provas', 'Test scores'], 'count'],
    ['contato', ['Contato', 'Contact'], 'first'],
    ['fim', ['Outros perfis semelhantes', 'Other similar profiles', 'People also viewed'], 'first'],
  ];

  function splitSections(lines) {
    const idx = {};
    const isHeaderAt = (i, textos, regra) => {
      if (!textos.includes(lines[i])) return false;
      if (regra === 'add') return /^(Adicionar|Solicitar|Add |Request )/.test(lines[i + 1] || '');
      if (regra === 'count') return /^\d+$/.test(lines[i - 1] || '');
      return true;
    };
    for (const [nome, textos, regra] of HEADERS) {
      let pos = -1;
      for (let i = 0; i < lines.length; i++) if (isHeaderAt(i, textos, regra)) { pos = i; break; }
      if (pos >= 0) idx[nome] = pos;
    }
    const ordered = Object.entries(idx).sort((a, b) => a[1] - b[1]);
    const sec = {};
    ordered.forEach(([nome, pos], k) => {
      const end = k + 1 < ordered.length ? ordered[k + 1][1] : lines.length;
      const corpo = lines.slice(pos + 1, end).filter((l) => !isNoise(l));
      while (corpo.length && /^\d+$/.test(corpo[corpo.length - 1])) corpo.pop();
      while (corpo.length && /^\d+$/.test(corpo[0])) corpo.shift();
      sec[nome] = corpo;
    });
    sec._cabecalho = lines.slice(0, ordered.length ? ordered[0][1] : 0).filter((l) => !isNoise(l));
    return sec;
  }

  function parseExperiencia(L) {
    const out = [];
    let grupo = null;
    const looksLikeTitle = (l) => !!l && l.length <= 90 && !/^[•\-–]/.test(l) && !/https?:\/\//.test(l) && !/[.!?:]$/.test(l);
    const startsEntry = (k) => (isDate(L[k + 1]) && L[k + 2] === '-') || (isDate(L[k + 2]) && L[k + 3] === '-' && !isDuration(L[k + 1]) && looksLikeTitle(L[k]) && looksLikeTitle(L[k + 1]));
    const startsGroup = (k) => isDuration(L[k + 1]) && !isDate(L[k]) && isDate(L[k + 3]) && L[k + 4] === '-';
    let k = 0;
    while (k < L.length) {
      if (startsGroup(k)) { grupo = L[k]; k += 2; continue; }
      if (!startsEntry(k)) { k++; continue; }
      const e = { cargo: L[k], empresa: '', inicio: '', fim: '', duracao: '', local: '', descricao: '' };
      if (isDate(L[k + 1])) { e.empresa = grupo || ''; k += 1; } else { e.empresa = L[k + 1]; grupo = null; k += 2; }
      e.inicio = L[k]; k += 2; // pula '-'
      if (isEnd(L[k])) { e.fim = L[k]; k++; }
      if (isDuration(L[k])) { e.duracao = L[k]; k++; }
      if (isLocation(L[k]) && !startsEntry(k) && !startsGroup(k)) { e.local = L[k]; k++; }
      const desc = [];
      while (k < L.length && !startsEntry(k) && !startsGroup(k)) { desc.push(L[k]); k++; }
      e.descricao = desc.join('\n').trim();
      out.push(e);
    }
    return out;
  }

  function parseFormacao(L) {
    const out = [];
    let k = 0;
    while (k < L.length) {
      let d = -1;
      for (let j = 1; j <= 3; j++) if (isDate(L[k + j]) && L[k + j + 1] === '-') { d = k + j; break; }
      if (d < 0) { k++; continue; }
      const head = L.slice(k, d);
      const e = { instituicao: head[0] || '', grau: head[1] || '', area: head[2] || '', inicio: L[d], fim: L[d + 2] || '', descricao: '' };
      k = d + 3;
      const desc = [];
      const next = (i) => [1, 2, 3].some((j) => isDate(L[i + j]) && L[i + j + 1] === '-') && !isDate(L[i]);
      while (k < L.length && !next(k)) { desc.push(L[k]); k++; }
      e.descricao = desc.join('\n').replace(/^Atividades e grupos:\n?/, 'Atividades e grupos: ').trim();
      out.push(e);
    }
    return out;
  }

  function parseVoluntariado(L) {
    const out = [];
    let k = 0;
    while (k < L.length) {
      let d = -1;
      for (let j = 1; j <= 3; j++) if (isDate(L[k + j]) && L[k + j + 1] === '-') { d = k + j; break; }
      if (d < 0) { k++; continue; }
      const head = L.slice(k, d);
      const e = { organizacao: head[0] || '', funcao: head[1] || '', causa: head[2] || '', inicio: L[d], fim: L[d + 2] || '', duracao: '', descricao: '' };
      k = d + 3;
      if (isDuration(L[k])) { e.duracao = L[k]; k++; }
      const desc = [];
      const next = (i) => [1, 2, 3].some((j) => isDate(L[i + j]) && L[i + j + 1] === '-') && !isDate(L[i]);
      while (k < L.length && !next(k)) { desc.push(L[k]); k++; }
      e.descricao = desc.join('\n').trim();
      out.push(e);
    }
    return out;
  }

  const parsePares = (L) => { const out = []; for (let k = 0; k + 1 < L.length; k += 2) out.push({ nome: L[k], emissor: L[k + 1] }); return out; };
  function parseReconhecimentos(L) {
    const out = [];
    let k = 0;
    while (k < L.length) {
      if (isDate(L[k + 2])) { out.push({ titulo: L[k], emissor: L[k + 1], data: L[k + 2] }); k += 3; }
      else if (isDate(L[k + 1])) { out.push({ titulo: L[k], emissor: '', data: L[k + 1] }); k += 2; }
      else { out.push({ titulo: L[k], emissor: '', data: '' }); k++; }
    }
    return out;
  }
  function parseContato(L) {
    const out = {};
    for (let k = 0; k + 1 < L.length; k++) {
      if (/^(E-mail|Email|Site|Website|LinkedIn|Telefone|Phone|Endereço|Address|Aniversário|Birthday|IM|Twitter)$/i.test(L[k])) { out[L[k]] = L[k + 1]; k++; }
    }
    return out;
  }
  function parseCabecalho(H) {
    const c = { nome: H[0] || '', titulo: H[1] || '', empresaAtual: '', local: '', conexoes: '', seguidores: '' };
    for (const l of H.slice(2)) {
      if (/conex|connections/i.test(l)) c.conexoes = l;
      else if (/seguidores|followers/i.test(l)) c.seguidores = l;
      else if (/,/.test(l) && !c.local) c.local = l;
      else if (!c.empresaAtual) c.empresaAtual = l;
    }
    return c;
  }
  function parseDestaque(L) {
    const stop = L.findIndex((l) => /^(Link|Adicionar|Add)$/.test(l) || /formato da URL|Colar ou digitar/.test(l));
    return (stop >= 0 ? L.slice(0, stop) : L).filter((l) => !/só estão disponíveis|Abrir no aplicativo|only available/.test(l));
  }
  function parseAtividades(L) {
    const meta = {};
    const rest = [];
    for (const l of L) { if (/seguidores|followers/i.test(l)) meta.seguidores = l; else rest.push(l); }
    return { ...meta, ultimaAtividade: rest.join('\n').slice(0, 2000) };
  }

  return function liParse(text) {
    const lines = [];
    for (const raw of text.split('\n')) { const l = raw.replace(/[ \t]+/g, ' ').trim(); if (l && lines[lines.length - 1] !== l) lines.push(l); }
    const S = splitSections(lines);
    const p = {
      cabecalho: parseCabecalho(S._cabecalho || []),
      sobre: (S.sobre || []).filter((l) => !/^(Credenciais de conteúdo|As informações de fonte|Saiba mais)/.test(l)).join('\n'),
      destaque: parseDestaque(S.destaque || []),
      atividades: parseAtividades(S.atividades || []),
      experiencia: parseExperiencia(S.experiencia || []),
      formacao: parseFormacao(S.formacao || []),
      voluntariado: parseVoluntariado(S.voluntariado || []),
      competencias: S.competencias || [],
      recomendacoes: (S.recomendacoes || []).filter((l) => !/^(Publicações|Patentes|Cursos|Projetos|Reconhecimentos e prêmios|Notas de provas|Idiomas|Organizações|Certificado|Conquistas|Publications|Patents|Courses|Projects|Honors & awards|Test scores|Languages|Organizations|Licenses & certifications)$/.test(l)),
      certificados: parsePares((S.certificados || []).filter((l) => !/^(Patentes|Cursos|Projetos|Reconhecimentos e prêmios|Notas de provas|Idiomas|Organizações|Certificado|Conquistas|Publicações)$/.test(l))),
      publicacoes: S.publicacoes || [],
      projetos: S.projetos || [],
      idiomas: S.idiomas || [],
      cursos: S.cursos || [],
      reconhecimentos: parseReconhecimentos(S.reconhecimentos || []),
      organizacoes: S.organizacoes || [],
      contato: parseContato(S.contato || []),
      _secoesEncontradas: Object.keys(S).filter((k) => k !== '_cabecalho'),
    };
    if (p.atividades.seguidores && !p.cabecalho.seguidores) p.cabecalho.seguidores = p.atividades.seguidores;
    return p;
  };
})();

function liMarkdown(p, url) {
  const L = [];
  const h = (n, t) => L.push(`${'#'.repeat(n)} ${t}`, '');
  const block = (t) => { if (t) L.push('```', t, '```', ''); };
  const kv = (o, skip) => Object.entries(o).filter(([k, v]) => v && !skip.includes(k)).map(([k, v]) => `**${k}:** ${v}`).join(' · ');
  h(1, `Perfil LinkedIn · ${p.cabecalho.nome}`);
  L.push(`Exportado em ${new Date().toLocaleString('pt-BR')} de ${url}`, '');
  h(2, 'Cabeçalho');
  for (const [k, v] of Object.entries(p.cabecalho)) if (v) L.push(`- **${k}:** ${v}`);
  L.push('');
  h(2, 'Sobre'); block(p.sobre);
  h(2, `Em destaque (${p.destaque.length})`); for (const d of p.destaque) L.push(`- ${d}`); L.push('');
  h(2, `Experiência (${p.experiencia.length})`);
  for (const e of p.experiencia) { h(3, `${e.cargo} · ${e.empresa}`); L.push(kv(e, ['cargo', 'empresa', 'descricao']), ''); block(e.descricao); }
  h(2, `Formação acadêmica (${p.formacao.length})`);
  for (const e of p.formacao) { h(3, e.instituicao); L.push(kv(e, ['instituicao', 'descricao']), ''); block(e.descricao); }
  h(2, `Voluntariado (${p.voluntariado.length})`);
  for (const e of p.voluntariado) { L.push(`- **${e.funcao}** · ${e.organizacao} · ${e.inicio} a ${e.fim}${e.causa ? ' · ' + e.causa : ''}${e.descricao ? ' · ' + e.descricao : ''}`); }
  L.push('');
  h(2, `Competências (${p.competencias.length})`); L.push(p.competencias.join(' · '), '');
  h(2, `Certificados (${p.certificados.length})`);
  L.push('| Nome | Emissor |', '|---|---|'); for (const c of p.certificados) L.push(`| ${c.nome} | ${c.emissor} |`); L.push('');
  h(2, `Publicações (${p.publicacoes.length})`); for (const x of p.publicacoes) L.push(`- ${x}`); L.push('');
  h(2, `Projetos (${p.projetos.length})`); for (const x of p.projetos) L.push(`- ${x}`); L.push('');
  h(2, `Reconhecimentos (${p.reconhecimentos.length})`);
  L.push('| Título | Emissor | Data |', '|---|---|---|'); for (const r of p.reconhecimentos) L.push(`| ${r.titulo} | ${r.emissor} | ${r.data} |`); L.push('');
  h(2, `Idiomas (${p.idiomas.length})`); for (const x of p.idiomas) L.push(`- ${x}`); L.push('');
  h(2, `Cursos (${p.cursos.length})`); for (const x of p.cursos) L.push(`- ${x}`); L.push('');
  h(2, `Organizações (${p.organizacoes.length})`); for (const x of p.organizacoes) L.push(`- ${x}`); L.push('');
  h(2, `Recomendações (${p.recomendacoes.length})`); for (const x of p.recomendacoes) L.push(`- ${x}`); L.push('');
  h(2, 'Contato'); for (const [k, v] of Object.entries(p.contato)) L.push(`- **${k}:** ${v}`); L.push('');
  h(2, 'Diagnóstico'); block(`Seções encontradas: ${p._secoesEncontradas.join(', ')}`);
  return L.join('\n');
}

if (typeof module !== 'undefined' && module.exports) module.exports = { liParse, liMarkdown };

// ------------------------------------------------------------------ execução no navegador
if (typeof window !== 'undefined' && typeof document !== 'undefined' && /linkedin\.com/.test(location.host)) {
  (async () => {
    const log = (...a) => console.log('%c[li-scrape]', 'color:#0a66c2;font-weight:bold', ...a);
    const SLUG = (location.pathname.match(/\/in\/([^/]+)/) || [])[1] || 'ronildooliveira';
    const URL_PERFIL = `https://www.linkedin.com/in/${SLUG}/`;
    const res = await fetch(URL_PERFIL, { credentials: 'include', headers: { accept: 'text/html' } });
    if (!res.ok) { log(`HTTP ${res.status} ao buscar o perfil`); return; }
    const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
    const main = doc.querySelector('main') || doc.body;
    const texto = main.innerText || main.textContent || '';
    const perfil = liParse(texto);
    perfil.exportadoEm = new Date().toISOString();
    perfil.url = URL_PERFIL;
    perfil._textoBruto = texto.split('\n').map((l) => l.trim()).filter(Boolean).join('\n');
    const md = liMarkdown(perfil, URL_PERFIL);
    window.liPerfil = perfil; window.liPerfilMd = md;
    const stamp = new Date().toISOString().slice(0, 10);
    const download = (name, content, type) => { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([content], { type })); a.download = name; document.body.appendChild(a); a.click(); a.remove(); };
    download(`linkedin-perfil-${stamp}.json`, JSON.stringify(perfil, null, 2), 'application/json');
    setTimeout(() => download(`linkedin-perfil-${stamp}.md`, md, 'text/markdown'), 600);
    log(`concluído: experiência ${perfil.experiencia.length} · formação ${perfil.formacao.length} · voluntariado ${perfil.voluntariado.length} · competências ${perfil.competencias.length} · certificados ${perfil.certificados.length} · idiomas ${perfil.idiomas.length} · cursos ${perfil.cursos.length} · reconhecimentos ${perfil.reconhecimentos.length}`);
    log('seções encontradas:', perfil._secoesEncontradas.join(', '));
    log('resultado em window.liPerfil e window.liPerfilMd');
  })();
}
