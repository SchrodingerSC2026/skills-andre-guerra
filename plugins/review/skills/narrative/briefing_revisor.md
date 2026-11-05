# Briefing do revisor (preencher os campos <...> e enviar inteiro)

Você vai revisar, como LEITOR, os entregáveis abaixo. O leitor real (<quem lê: ex. o comitê que decide a compra>)
lê do resultado para a base: começa em <documento 1>, vai a <documento 2> e só então abre as planilhas.
Refaça esse caminho. NÃO altere nenhum arquivo; escreva só em <arquivo de saída .md, numa pasta temporária>.
Escreva nas convenções do ambiente: <idioma e regras de escrita, preenchidas por quem envia>.

Artefatos:
- Documento 1: <caminho>
- Documento 2: <caminho> (PDF: extrair texto com pymupdf; para ver gráfico, renderizar a página em PNG
  na pasta temporária e apagar no fim)
- Planilhas: <caminhos, com as abas principais>
- Decisões já tomadas (leia antes da etapa 3): <CLAUDE.md, MEMORIA.md, LEIA-ME.md do alvo>
- Python com pandas/openpyxl: <caminho>; escreva scripts .py na pasta temporária.

O arquivo de saída tem estas seções, escritas NESTA ORDEM, cada uma antes de abrir a fonte da seguinte:

1. **O que entendi do documento 1**: a recomendação, os números de decisão, a lógica em ordem, e cada
   dúvida de leitor com o trecho literal.
2. **O que entendi do documento 2**, com página.
3. **Desconexões entre os dois**: tabela com tema, o que diz cada um (trecho e página) e por que importa.
4. **O que as planilhas mostram**: para cada número de decisão, arquivo, aba, coluna com letra e a conta
   que o reproduz. Reproduza SEMPRE com a definição que o documento declara (se o texto diz "renegociado =
   coluna X preenchida", use a coluna X); outra definição só como métrica adicional, com outro nome.
   Número que você não mediu, só estimou (proporção, regra de três), leva a palavra `estimativa`.
5. **Achados**: uma tabela com gravidade (alta = o leitor pode decidir errado; média = se perde ou
   desconfia; baixa = forma), tipo, onde, problema e sugestão. Os tipos:
   - `Número`: o número do texto não se reproduz, ou diverge entre documentos;
   - `Universo`: rótulo, denominador ou definição que conta outra história;
   - `Narrativa`: ordem, termo sem definição, conclusão que não decorre do número, contradição;
   - `Método`: questiona premissa ou régua que as decisões já tomadas registram como escolha. Liste aqui,
     com a decisão citada, e não como defeito.
   Gravidade alta exige número medido, não `estimativa`.
6. **O que não consegui verificar.**

Os números já passaram por um auditor que confere se cada número do texto existe num conjunto válido;
o mais valioso é o que esse auditor não pega: universo, rótulo, ordem, conclusão sem sustentação.

Na resposta final: o caminho do .md, a contagem por tipo e gravidade, os 5 achados mais graves em uma
linha cada, e o que você não verificou.
