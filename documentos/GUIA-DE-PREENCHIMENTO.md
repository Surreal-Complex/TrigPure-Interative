# Guia de preenchimento e revisão

O marcador **@@@@** identifica uma pendência de verificação, decisão ou aprovação. Os campos de formulários em branco e os exemplos de referência são preenchidos quando usados. Consulte [Pendências](AUDITORIA-DE-PENDENCIAS.md) para saber onde confirmar cada item e quais arquivos precisam acompanhar a alteração.

## Como editar um campo

1. No [repositório do TrigPure Interative](https://github.com/Surreal-Complex/TrigPure-Interative), abra o arquivo indicado na auditoria e procure pelo nome do campo. Para localizar outros campos, busque pelo marcador **@@@@**.
2. Confira a evidência com a fonte indicada, anote a data e obtenha aprovação quando exigida. Para dados pré-preenchidos, confira também a evidência já registrada.
3. Em Markdown, substitua o marcador do campo pelo dado confirmado. Na aba Sobre, atualize o valor no elemento `<dd>` correspondente e retire o destaque somente daquele campo. Atualize os documentos relacionados e os resumos e selos de status de `documentos/index.html` apenas quando a revisão correspondente estiver aprovada.
4. Se mudar autoria, título, ano, versão ou endereço, atualize [Como citar](COMO-CITAR.md), `CITATION.cff` e a seção `#como-citar` em `sobre/index.html`. Adicione versão e data formal ao YAML somente depois de confirmá-las.
5. Faça o commit em uma branch, abra um pull request e siga o [guia de edição e publicação](GUIA-DE-EDICAO.md).

## Direitos, privacidade e aprovações

- **Titularidade e licenças.** Separe código e jogos de textos e PDFs. Depois de colher a anuência dos titulares, registre a licença aplicável. Só crie `LICENSE` após a escolha da licença do código. Para materiais de terceiros, registre versão, link, licença e crédito na [planilha de fontes](REGISTRO-DE-FONTES-E-LICENCAS.md).
- **Autorizações.** Use o [modelo em branco](MODELO-DE-AUTORIZACAO.md) quando aplicável. Guarde assinaturas, dados pessoais e comprovantes fora do site e da árvore versionada.
- **Privacidade.** Confira a configuração real da hospedagem, armazenamento local, cookies, rede, contato e fluxo de atendimento. Registre quem decide sobre tratamento de dados e, se aplicável, critérios para menores, retenção e transferências. Atualize [Privacidade](PRIVACIDADE.md) e [Termos](TERMOS-DE-USO.md).
- **Revisão final.** Use o [roteiro de validação humana](GUIA-DE-VALIDACAO-FINAL.md) para testar matemática, dispositivos, teclado, leitores de tela, jogos e gráficos. Registre os resultados e os responsáveis antes de aprovar as minutas ou declarar conformidade.
