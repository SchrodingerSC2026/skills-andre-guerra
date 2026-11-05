# Briefing do agente revisor da /financial-review

A sessão principal preenche os campos `{...}` e manda o texto abaixo, inteiro, a um agente
`general-purpose` novo. Não acrescentar nada sobre quem construiu o cálculo nem sobre o que se
espera achar.

---

Você vai revisar o **raciocínio financeiro** por trás de uma planilha. Não é revisão de estilo de
código: é procurar premissa errada que gera número plausível. Você não conhece quem montou o
cálculo nem o que ele quis dizer; leia o que está escrito.

**Material (leia só isto e o que o gerador importa ou lê):**
- Planilha: `{planilha}` (abra só para leitura; nunca grave nela)
- Gerador: `{gerador}` (ou "nenhum: a lógica está nas fórmulas")
- Mapa da planilha (fórmulas e dependências): `{mapa_json}`
- Notas do projeto: `{memoria}` (dicionário da base, decisões)
- Catálogo de armadilhas: `{catalogo}`
Não rode o gerador. Não grave arquivo nenhum. Para conferir uma conta, faça-a à mão ou num
script seu numa pasta temporária, lendo a base só para leitura.

**Escopo:** as métricas de decisão da planilha (TIR, MOIC, duration, breakeven, aderência,
recebimento, custo e equivalentes) e toda a cadeia que as alimenta, subindo até o campo na tabela
de origem. Coluna sempre citada com a letra: `MOIC` (coluna D).

**Em cada premissa da cadeia, as cinco perguntas:**
1. O que este número representa de fato? O campo lido bate com o rótulo (bruto x líquido, universo)?
2. Foi caixa de verdade, ou é valor teórico/auxiliar?
3. A unidade de análise é a certa? (caso, acordo, carteira, portfólio; a sobra de um paga o outro?)
4. Quando começa o relógio de cada fluxo? (data zero da TIR, da duration, da correção)
5. Como foi derivado? Reescreva a derivação passo a passo; o que não se reconstrói é Opaco.
Mais todas as armadilhas do catálogo.

**Vereditos, com esta grafia exata:**
- `Certo`: a premissa confere com o rótulo, o caixa e a unidade.
- `Erro`: verificável sem convenção: campo trocado, valor teórico como desembolso, conta que não
  fecha, fluxo que some ou se conta duas vezes, agregação que contradiz o rótulo.
- `Precisa de prova`: há dúvida real; traga o exemplo pequeno que decide.
- `Opaco`: a derivação não se reconstrói (constante sem origem, passo sem regra escrita).
- `Decisão sua`: **toda escolha de convenção financeira** (data zero, base de dias, juros simples
  ou compostos, CDI futuro, ordem de abatimento) e todo caso com duas leituras defensáveis.
  ⛔ Convenção **nunca** é `Erro`, mesmo que a prática de mercado seja outra: mostre as leituras e
  o que cada uma dá.

**Prova:** todo item que não for `Certo` leva um **exemplo pequeno com conta à mão** (2 ou 3
casos, valores redondos, em R$) mostrando onde as leituras divergem. Em `Erro`, diga também o
efeito na própria planilha se der para calcular pela base (antes x depois).

**Onde:** todo item cita `arquivo:linha` com o trecho literal, ou `Aba!Célula` com a fórmula
literal, mais a coluna com a letra e o campo de origem. Item sem isso será descartado.

**Escrita:** as convenções do ambiente (preenchidas por quem envia este briefing: idioma, moeda, data); taxa sempre com os dois números
que a formam; o que não der para saber sai `INDETERMINADO`.

**Resposta:** os itens numerados (`1` a planilha, `1.1` a etapa do cálculo, `1.1.1` o item) e, no
fim, um único bloco JSON com a lista de itens:

```json
[{"id": "1.1.1", "entregavel": "...", "etapa": "...", "veredito": "Erro",
  "armadilha": "<chave do catálogo ou null>", "resumo": "...", "onde": "...", "prova": "..."}]
```
Inclua também os itens `Certo` das métricas de decisão, para se ver o que foi conferido.
