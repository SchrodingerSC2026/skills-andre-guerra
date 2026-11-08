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

1. **Leitura do documento 1, parágrafo a parágrafo.**
2. **Leitura do documento 2, parágrafo a parágrafo**, com página.

   Nas duas, leia como quem nunca viu o assunto, na ordem em que o leitor lê: a abertura, depois o resumo,
   depois cada parágrafo de cada seção. Uma tabela, uma fórmula, uma figura ou uma caixa de destaque
   contam como um parágrafo. **Escreva a entrada de um parágrafo ANTES de ler o seguinte**: não leia
   adiante para entender um termo, porque é exatamente isso que o leitor real não faz. Cada entrada tem:
   - **§n (página, primeiras palavras)**;
   - **O que entendi deste parágrafo**, em uma ou duas frases;
   - **O que entendo do documento até aqui**, em uma ou duas frases: o acumulado, refeito a cada parágrafo;
   - **Termos sem definição até aqui**: palavra usada como se o leitor já soubesse (nome interno, apelido,
     sigla, termo do jargão da equipe), com o trecho literal;
   - **Conclusões que tirei**: o que este parágrafo me levou a acreditar sobre o todo (o que a proposta
     oferta, o que o número mede, de onde vem o valor).

   Quando um parágrafo posterior **contradiz, corrige ou define de outro jeito** uma conclusão anterior,
   anote na entrada dele "desfaz a conclusão do §k". No fim de cada documento, o **Registro de leitura**:
   tabela com a conclusão errada, o § que a induziu (trecho literal), o § que a desfez (trecho literal) ou
   `nunca desfeita`, e quantos parágrafos o leitor passou acreditando nela. Conclusão `nunca desfeita` é
   a mais grave: o leitor sai do documento com ela.
3. **Desconexões entre os dois**: tabela com tema, o que diz cada um (trecho e página) e por que importa.
   Inclua sempre a **coerência do mecanismo**: quando o documento descreve um mecanismo central (a oferta que
   muda por período, por degrau ou por cenário) e outra parte diz aplicar a mesma conta em outro lugar (outro
   canal, outro prazo), confira na planilha que essa parte muda junto, período a período e no mesmo universo.
   Número que fica parado enquanto o mecanismo se move, ou que parte de outra base (o piso, o máximo), é
   `Universo` de gravidade alta. E toda comparação do texto ("mais alto", "mais barato") se mede também contra
   o que o leitor vai comparar (a oferta vizinha no mesmo período), não só contra a base que o texto escolheu.
4. **O que as planilhas mostram**: para cada número de decisão, arquivo, aba, coluna com letra e a conta
   que o reproduz. Reproduza SEMPRE com a definição que o documento declara (se o texto diz "renegociado =
   coluna X preenchida", use a coluna X); outra definição só como métrica adicional, com outro nome.
   Número que você não mediu, só estimou (proporção, regra de três), leva a palavra `estimativa`.
5. **Achados**: uma tabela com gravidade (alta = o leitor pode decidir errado; média = se perde ou
   desconfia; baixa = forma), tipo, onde, problema e sugestão. Os tipos:
   - `Número`: o número do texto não se reproduz, ou diverge entre documentos;
   - `Universo`: rótulo, denominador ou definição que conta outra história;
   - `Narrativa`: ordem, termo sem definição, conclusão que não decorre do número, contradição;
   - `Leitura`: conclusão errada que um parágrafo induz sobre o documento inteiro, tirada do Registro de
     leitura; o Onde leva o § que induz e o § que desfaz (ou `nunca desfeita`), os dois com trecho literal.
     Gravidade alta quando a conclusão errada mudaria a decisão do leitor ou nunca é desfeita;
   - `Método`: questiona premissa ou régua que as decisões já tomadas registram como escolha. Liste aqui,
     com a decisão citada, e não como defeito.
   Gravidade alta exige número medido, não `estimativa`.
6. **O que não consegui verificar.**

Os números já passaram por um auditor que confere se cada número do texto existe num conjunto válido;
o mais valioso é o que esse auditor não pega: universo, rótulo, ordem, conclusão sem sustentação, e a
conclusão errada que um parágrafo deixa no leitor até outro parágrafo desfazê-la.

Na resposta final: o caminho do .md, a contagem por tipo e gravidade, os 5 achados mais graves em uma
linha cada, as conclusões `nunca desfeita` do Registro de leitura, e o que você não verificou.
