---
name: all
description: Roda de uma vez as revisões cabíveis de um entregável financeiro (financeira, premissas e narrativa), um agente por revisão em paralelo, e devolve um relatório único numerado. Use só quando o usuário pedir, digitando /review:all <alvo> ou pedindo em palavras a revisão completa; nunca por conta própria ao terminar uma entrega. Para uma revisão só, /review:financial, /review:premises ou /review:narrative; para revisar e corrigir sem perguntar, /review:go.
---

# /review:all

Orquestra as três revisões do plugin `review`. `RV` é a pasta-mãe desta skill (a pasta `skills` do
plugin, com `financial`, `premises` e `narrative` dentro), qualquer que seja a máquina.
O método de cada uma mora no `SKILL.md` dela; aqui está só o que muda quando rodam juntas.
Notas do projeto que não existirem na máquina (`MEMORIA.md`, `PENDENCIAS.md`, `CLAUDE.md`, `LEIA-ME.md`)
são puladas, e o relatório diz quais faltaram.

**Autorização:** o pedido do usuário, digitado ou em palavras, já autoriza **um
agente por revisão cabível** (até três) e a medição dos itens `Erro`. Não perguntar antes. Não autoriza
corrigir nada: a revisão só aponta (quem corrige é o `/review:go`).

## 1. Fixar o alvo e as revisões cabíveis

1. Os artefatos: planilhas e, se houver, o e-mail e o PDF. Citação ambígua: listar candidatos com data e
   origem e perguntar. Dizer em uma linha o que **não** será tocado.
2. Quais revisões se aplicam:

| Revisão | Roda quando |
|---|---|
| `RV\financial` | há planilha com lógica (gerador achado, ou fórmula) |
| `RV\premises` | há planilha com lógica (uma ou o conjunto, com a cadeia de geradores) |
| `RV\narrative` | há e-mail ou PDF que o leitor abre antes da planilha |

   Sem e-mail nem PDF: roda as duas financeiras e **avisa no topo** que a narrativa ficou de fora por
   falta do que ler. Planilha só com número colado, sem gerador nem fórmula: as duas
   financeiras não têm lógica a revisar; dizer isso e rodar só o que sobrar.

## 2. Preparo comum (uma vez só)

Seguir a seção 1 de `RV\financial\SKILL.md` e a seção 1 de `RV\premises\SKILL.md` **juntas**: o
`mapa_planilha.py` e o `acha_gerador.py` (em `RV\financial`) rodam uma vez por planilha, e o resultado
serve aos dois briefings. As notas do projeto (`MEMORIA.md`, `PENDENCIAS.md`, `CLAUDE.md`, `LEIA-ME.md`)
se levantam uma vez e vão aos três.

## 3. Os agentes, em paralelo

Preencher os briefings (`RV\financial\briefing_revisor.md`, `RV\premises\briefing_levantador.md`,
`RV\narrative\briefing_revisor.md`) e disparar os agentes `general-purpose` **na mesma mensagem**, um
por revisão cabível, cada um com o texto inteiro do seu briefing e nada sobre o que se espera achar.

## 4. Conferir e medir

Para cada retorno, a seção 3 da skill de origem (trecho literal no `arquivo:linha` ou `Aba!Célula`; o que não
bate sai). Depois, a seção 4 da `RV\financial` (medir os itens `Erro` por dois caminhos, na sessão
principal) e o complemento de lugares da seção 3 da `RV\premises` (busca própria pelo valor em todas as
grafias). Medir não se delega.

## 4b. Tirar da lista o que já foi respondido

Antes de montar o relatório, cruzar cada item que pede resposta (`Erro`, `Precisa de prova`, `Opaco`,
`Decisão sua`, os conflitos e os achados `Método`) com as decisões registradas no projeto: o arquivo de
pendências (inclusive as respostas de uma revisão anterior, item a item), a memória e o `CLAUDE.md`.

| O que se acha | Vai para |
|---|---|
| a nota decidiu e o código, a planilha ou o texto seguem a nota | linha `Já decidido`, com a nota e a data; não é item a responder |
| a nota decidiu e o código, a planilha ou o texto fazem outra coisa | item `Erro` (código contra decisão), com os dois trechos: é falha de execução |
| duas notas divergem e a mais nova revoga a velha em palavras | linha `Nota desatualizada`, para atualizar a nota; não é pergunta |
| nenhuma nota decidiu | segue como item |

Abrir a nota citada e conferir a data e o texto antes de mover o item. Dizer no topo quantos itens
saíram por já estarem decididos, para o usuário ver que o filtro rodou.

## 5. Um relatório, três blocos

Conclusão primeiro (quantos itens por veredito em cada bloco, e a revisão que ficou de fora, se houver).
Depois, no formato numerado da `RV\financial`:

```
1  Financeira: <planilha>
 1.1  <etapa>
  1.1.1  [Veredito] ...
2  Premissas: <conjunto>
 2.1  <premissa>
  2.1.1  [Veredito] ...
3  Narrativa: <e-mail + PDF>
 3.1  <tipo>
  3.1.1  [Gravidade] ...
```

Cada bloco segue o detalhe da skill de origem (campos de cada item, `Certo` e `Já decidido` juntos numa
linha cada, o
inventário de premissas também no `.md` da pasta das planilhas). Item que aparece em duas revisões (a
mesma taxa achada como `Erro` na financeira e como `Valores diferentes` nas premissas) sai **uma vez**,
no bloco que tem a prova mais forte, com "também em 2.x.y" no outro. Fechar dizendo que o usuário responde
item a item ("1.1.1 corrige; 3.2.1 mantém") e que o que não tocar fica como está. Sem rodada de
perguntas por cima da lista. Seguir as convenções de escrita que o ambiente declarar.

## 6. Depois da resposta

A seção 6 da `RV\financial` (armadilha nova confirmada vira proposta de linha para o catálogo) e a seção 5 da
`RV\premises` (cada resposta sobre premissa vai na hora ao arquivo de pendências do projeto, se houver). A correção é
tarefa normal, fora desta skill, e só com a ordem do usuário.
