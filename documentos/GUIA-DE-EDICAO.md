# Guia de edição do site e do código

## Começar uma revisão

Abra [Surreal-Complex/TrigPure-Interative](https://github.com/Surreal-Complex/TrigPure-Interative). Para uma correção curta, abra o arquivo na aba **Code**, escolha **Edit this file** e faça o commit em uma branch de revisão. Abra um pull request para comparar com `main` e ver a validação em **Actions**. Para mudanças em vários arquivos, clone o projeto e faça a revisão local:

```sh
git clone https://github.com/Surreal-Complex/TrigPure-Interative.git
cd TrigPure-Interative
git switch -c revisao-do-site
```

## Onde fazer cada alteração

| Quero alterar | Arquivo ou pasta | O que procurar |
| --- | --- | --- |
| Página inicial | `index.html` | Apresentação, cartões das abas e trajeto de aprendizagem. |
| Abas e atalhos internos | `estudar/index.html`, `explorar/index.html`, `praticar/index.html`, `jogar/index.html`, `professores/index.html`, `sobre/index.html` | Use o título da seção para encontrá-la. Mantenha os `id` se links existentes apontam para eles. |
| Identidade visual e ícone | `assets/rea.css`, `assets/logo-trigonometria.svg`, `assets/favicon-32.png`, `assets/apple-touch-icon.png`, `favicon.ico` | As cores compartilhadas ficam em `:root`; a marca do cabeçalho usa `.brand`. |
| Fórmulas e animação do topo | HTML de cada aba, `assets/rea.css`, `assets/rea.js` | Substitua as duas expressões `.hero-formula` no HTML. No CSS, ajuste os `@keyframes`. No JavaScript, procure `playFormulas`. |
| Teoria e trilha | `conteudos/*.html`, `conteudos/index.html`, `estudar/index.html`, `assets/progresso.js` | Atualize o capítulo, seu cartão e o índice. O progresso usa a ordem dos módulos. Preserve essa ordem ou atualize a chave e a compatibilidade dos dados em `assets/progresso.js`. |
| Laboratórios | `explorar/index.html`, `assets/rea.js`, `assets/laboratorios.js` | Preserve a correspondência entre os `id` dos controles no HTML e os usados no JavaScript. Confira graus e radianos, limites e valores conhecidos. |
| Questões e gabaritos | `assets/banco-questoes.js`, `praticar/index.html`, `assets/professores.js` | No banco, revise enunciado, alternativas, índice da correta e explicação. O mesmo banco abastece o treino e a folha docente. |
| Jogos | `jogar/index.html`, `palacio-trigonometrico.html`, `jogos/missao-quadrantes.html` | A aba descreve as regras. Os dois HTML dos jogos contêm os comportamentos e as questões correspondentes. |
| PDFs, listas e roteiro | `materiais/`, `estudar/index.html`, `praticar/index.html`, `professores/index.html` | Crie a subpasta adequada em `materiais/pdfs/`, coloque o arquivo e troque o respectivo aviso por um link relativo. |
| Autoria, licenças e citação | `sobre/index.html`, `documentos/`, `CITATION.cff` | Use o [guia de preenchimento](GUIA-DE-PREENCHIMENTO.md) e a [auditoria de pendências](AUDITORIA-DE-PENDENCIAS.md). |
| Novas páginas documentais | `documentos/index.html`, `documentos/*.md`, `scripts/build-private.py` | Registre o Markdown na lista `documents` do script e adicione o cartão correspondente ao portal. |
| Endereços, página 404 e mapa | `404.html`, `sitemap.xml` | Atualize os atalhos e o mapa ao alterar caminhos. A existência de um sitemap não torna a edição privada pesquisável. |

Ao acrescentar material de autoria própria ou de terceiros, indique no arquivo sua versão, autoria, fonte e licença aplicável. Registre as permissões no [inventário de fontes](REGISTRO-DE-FONTES-E-LICENCAS.md). Para testar uma nova lista em PDF, confira o link, o texto selecionável e a identificação da obra antes de publicar.

## Montar, testar e publicar

Com Python 3.9+, Pandoc e Node.js instalados, execute na raiz:

```sh
python3 scripts/build-private.py
node scripts/validar-site.mjs
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Abra no navegador `http://127.0.0.1:8000/`. Altere as fontes na raiz e regenere `dist/`. O arquivo `.github/workflows/validacao-site.yml` repete a montagem e as verificações no GitHub. O [guia de validação](GUIA-DE-VALIDACAO-FINAL.md) descreve os testes manuais.

Após aprovar o pull request, publique a mesma revisão de `main` no projeto privado de hospedagem. A plataforma recebe o diretório `dist/`, com o manifesto `.openai/hosting.json` que identifica o projeto. Integrar uma mudança no GitHub, isoladamente, não publica a revisão na hospedagem privada. Confira a versão servida, a aba Sobre e a central documental após publicar.

A edição anterior do TrigTest está disponível em [um ZIP integral](historico-trigtest-46c1ea4.zip). Para a edição vigente, use este guia, a auditoria atual e os arquivos da branch `main`.
