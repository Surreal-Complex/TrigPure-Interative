# TrigPure Interative

Recurso educacional de trigonometria para ensino médio e mediação docente, de Jessica Camily Hildebrandt e Peterson Luiz do Nascimento da Silva. Tem sete abas, dez capítulos, laboratórios interativos, banco de 60 questões, listas, roteiro de investigação e dois jogos. O progresso de estudos é local e opcional.

- [Abrir o site público no GitHub Pages](https://surreal-complex.github.io/TrigPure-Interative/)
- [Abrir a edição privada de revisão](https://trigonometria-interativa.pastelkey1.chatgpt.site/)
- [Guia de edição do site e do código](documentos/GUIA-DE-EDICAO.md)
- [Pendências: o que falta, como confirmar e onde editar](documentos/AUDITORIA-DE-PENDENCIAS.md)
- [Guia de preenchimento](documentos/GUIA-DE-PREENCHIMENTO.md) e [roteiro de validação](documentos/GUIA-DE-VALIDACAO-FINAL.md)

## Montagem e validação

Use Python 3.9+, Pandoc e Node.js. Na raiz do projeto:

```sh
python3 scripts/build-private.py
node scripts/validar-site.mjs
```

Para publicar no GitHub Pages, a conta proprietária executa **Actions → Publicar no GitHub Pages → Run workflow** na branch `main`. A publicação utiliza a saída de `dist/`. Os documentos são editados em `documentos/*.md` e transformados em HTML durante a montagem. O guia de edição contém os caminhos dos módulos, controles, jogos e arquivos de estilo.

## Origem e licenças

Esta edição deriva de [Surreal-Complex/TrigTest](https://github.com/Surreal-Complex/TrigTest), commit `46c1ea40341bc13d013aa4d50fc8dd073e773a63`. A [cópia integral da versão de origem](documentos/historico-trigtest-46c1ea4.zip) inclui todos os arquivos e os guias históricos. A [edição anterior publicada](https://surreal-complex.github.io/TrigTest/) tem hospedagem independente.

A escolha das licenças originais do conteúdo e do código depende dos titulares. Consulte as [minutas e condições de licenciamento](documentos/LICENCIAMENTO.md) e os [créditos, fontes e uso de IA](documentos/CREDITOS-E-REFERENCIAS.md).
