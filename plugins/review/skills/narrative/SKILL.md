---
name: narrative
description: Revisa a coerência entre e-mail, PDF e planilhas como o leitor lê (do número final de volta à base) e aponta onde o texto não sustenta o número, onde dois documentos contam histórias diferentes e onde o leitor se perde. Use só quando o usuário pedir, digitando /review:narrative ou pedindo em palavras a revisão da narrativa; nunca por conta própria ao terminar uma entrega.
---

# /review:narrative

O leitor lê do resultado para a base: começa no e-mail, vai ao PDF e só então abre a planilha. A
revisão refaz esse caminho e aponta onde o texto não sustenta o número, onde dois documentos contam
histórias diferentes e onde o leitor se perde. Ela só aponta: quem corrige é o `/review:go`. Dentro do
`/review:all` e do `/review:go`, o agente da seção 2 sai em paralelo com os outros.

A skill não traz régua nem definição própria: o que é "certo" vem do que o documento declara e das
decisões registradas no ambiente.

**Autorização:** o pedido do usuário, digitado ou em palavras, já autoriza **um** agente revisor. Não
perguntar antes.

## 1. Fixar o alvo

1. Os artefatos: o e-mail (ou o primeiro documento que o leitor abre), o PDF e as planilhas de onde os
   números saem. Citação ambígua ("o pdf do lote"): listar candidatos com data e perguntar. Sem e-mail
   nem PDF, esta revisão não tem o que ler: dizer isso e parar.
2. As decisões já tomadas que valem para o alvo: as notas do projeto que existirem (`CLAUDE.md`,
   `MEMORIA.md`, `LEIA-ME` da pasta). O revisor recebe esses caminhos para separar defeito de decisão.

## 2. O revisor (subagente)

Preencher `briefing_revisor.md` desta pasta e disparar **um** agente `general-purpose` novo com o texto
inteiro, sem dizer o que se espera achar.

## 3. Conferir o que voltou

Para cada achado de gravidade alta ou média:
- abrir o trecho, a página ou a `Aba!Célula` citados e confirmar que estão lá e dizem o que o achado
  afirma; sem onde e trecho, o achado sai;
- todo número do achado refeito **por outro caminho, com a definição que o documento declara**; se
  divergir, levar a divergência, não um dos dois;
- número estimado (proporção, "cerca de") fica marcado `estimativa`, e não sustenta gravidade alta
  sozinho até ser medido.

## 4. Mostrar, no formato numerado

O mesmo formato da `/review:financial`, um documento (ou par de documentos) por bloco, conclusão primeiro:

```
1  <e-mail + PDF + planilhas do alvo>
 1.1  <tipo: Número, Universo, Narrativa ou Decisão sua>
  1.1.1  [Gravidade] uma linha do problema
         Onde: documento, página/trecho, Aba!Célula com coluna e letra
         Problema: o que o texto diz e o que a base mostra
         Sugestão: a correção proposta
         Conferido: sim (trecho e número refeitos) | estimativa
```

| Tipo | O que é |
|---|---|
| Número | o número do texto não se reproduz, ou diverge entre documentos |
| Universo | rótulo, denominador ou definição que conta outra história |
| Narrativa | ordem, termo sem definição, conclusão que não decorre do número, frase que contradiz outra |
| Decisão sua | o que o revisor marcou como `Método`: questiona premissa ou régua que já é decisão registrada; vai com a decisão citada e as saídas possíveis, nunca como defeito |

Depois, a lista do que não se conseguiu verificar. Fechar dizendo que o usuário responde item a item
("1.1.1 corrige; 1.4.1 mantém") e que o que não tocar fica como está. Sem rodada de perguntas por cima
da lista. Seguir as convenções de escrita que o ambiente declarar.

Corrigir só o que o usuário mandar, como tarefa normal.

## Erros comuns que esta skill evita

| Sem a skill | Com a skill |
|---|---|
| Reproduz um número com outra coluna da base e chega a outro valor | Reproduz com a definição que o documento declara; outra definição sai rotulada como outra métrica |
| Mistura crítica a uma régua já decidida com defeito de texto, na mesma lista | Tipo `Decisão sua`, separado, com a decisão citada |
| Gravidade alta apoiada em valor estimado por proporção | `estimativa` marcada; alta só com medição |
| Relatório longo sem conferência | Cada achado alto ou médio conferido no trecho e no número antes de chegar ao usuário |
