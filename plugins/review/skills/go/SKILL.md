---
name: go
description: Revisa um entregável financeiro com todas as revisões cabíveis (financeira, premissas, narrativa) e CORRIGE sem perguntar o que for defeito comprovado, entregando no fim só o relatório das alterações. Use só quando o usuário pedir, digitando /review:go <alvo> ou pedindo em palavras para revisar e já corrigir; nunca por conta própria ao terminar uma entrega.
---

# /review:go

Faz o `/review:all` (`..\all\SKILL.md`, pasta irmã desta; seções 1 a 4) e, em vez de mostrar a lista e
esperar, aplica as correções e devolve só o relatório do que mudou.

**Autorização:** o pedido do usuário, digitado ou em palavras, é a ordem para corrigir sem perguntar,
**só dentro desta execução e só no alvo pedido**. Autoriza um agente por revisão cabível e um agente a
mais na reconferência (seção 5).

A skill não traz premissa nem regra de negócio própria: o que se protege e o que vale vem do ambiente.
Antes de tocar em qualquer arquivo, ler as regras do ambiente (`CLAUDE.md` do usuário, da raiz e do projeto;
`MEMORIA.md`, `PENDENCIAS.md` e `LEIA-ME` do projeto, os que existirem).

## 0. Limites fixos (não se negociam, nem com o pedido)

- ⛔ **Arquivo que vai para fora não se altera:** lista ou arquivo enviado (ou a enviar) a órgão,
  portal, bureau, cliente ou sistema externo, e as pastas de envio. Alvo assim: só revisa e aponta,
  como o `/review:all`. Rodar um gerador que regrava um desses arquivos também conta como alterar:
  regerar numa cópia temporária e trazer só o entregável.
- ⛔ **Arquivo que as regras do ambiente protegem não se altera:** o que o `CLAUDE.md` ou as notas do
  projeto marcarem como proibido, imutável ou dado bruto.
- ⛔ **Sem merge, push, PR ou escrita em banco** (banco só leitura). Commit também não.
- ⛔ **Entregável já enviado a alguém não se regrava por cima:** a versão corrigida sai ao lado, com
  sufixo `_revisado`. Conta como enviado: está numa pasta de envio, é citado como enviado nas notas do
  projeto, ou o gerador tem trava contra sobrescrever. Na dúvida, trata como enviado.
- ⛔ **Número corrigido se recalcula por um segundo caminho.** Os dois divergem: **não aplica**, e a
  divergência vai ao relatório.
- Nada se abre no fim.

## 1. Revisar

Seções 1 a 4 do `/review:all`: alvo, revisões cabíveis, preparo comum, agentes em paralelo, conferência e
medição. Citação ambígua do alvo ainda se pergunta (é a única pergunta permitida).

## 2. O que se corrige e o que não

| Item | Faz |
|---|---|
| `Erro` (financeira) conferido e medido, os dois caminhos batendo | corrige |
| `Número`, `Universo`, `Narrativa` (narrativa) conferidos, sem `estimativa` | corrige |
| Conflito de premissa (`Valores diferentes`, `Código contra decisão`, `Texto contra cálculo`) | corrige **só se o usuário decidiu o lado nesta mesma sessão**; senão, lista |
| `Decisão sua`, `Método`, convenção financeira | aplica **só decisão do usuário tomada nesta mesma sessão**; senão, lista |
| `Já decidido` por decisão registrada em sessão anterior | **não aplica** (o usuário pode não lembrar dela); lista, citando a decisão e a data |
| `Precisa de prova`, `Opaco`, `Sem fonte`, item `estimativa` | não corrige; lista |
| `Certo` | nada |
| Melhoria que nenhuma revisão apontou como item (trava de sobrescrita, refatoração, nome, estilo) | não faz; entra como sugestão na seção 3 do relatório |

Decisão "desta mesma sessão" é a que o usuário disse nesta conversa; arquivo de memória ou pendência não conta.
O conjunto do que se altera é exatamente a lista de itens corrigíveis da tabela acima: cada linha mudada
num arquivo pertence a um desses itens.

## 3. Cópia antes de tocar

Antes do primeiro byte alterado em cada arquivo, copiar o original para
`<raiz do workspace>\_backups_projeto\review_go_<assunto>\`
(sem workspace, a pasta do projeto do alvo), mantendo o caminho relativo à
raiz, e gravar ali um `manifesto.csv` (arquivo, sha256 antes, sha256 depois, item).

## 4. Corrigir

- **Na fonte, nunca no derivado:** erro de cálculo se corrige no gerador (script ou fórmula), não no
  número da planilha; texto do PDF se corrige na fonte dele (o `.tex`, o `.md` ou o documento que o gera), e o PDF se refaz pelo processo do projeto; e-mail no
  `.html`/`.txt` dele.
- Script corrigido: rodar os testes que houver ao lado dele. Teste que falhar desfaz a correção daquele
  item (volta a cópia) e o item vai como "não resolvido".
- **Regerar** a planilha e o PDF afetados (respeitando o sufixo `_revisado` dos já enviados) e conferir
  o número novo pelo segundo caminho da seção 0.
- Arquivo de saída: edição com `Edit`/`Write`, nunca `Set-Content`; planilha conferida exportando para PDF
  quando houver texto em célula com quebra.

## 5. Reconferir uma vez

Um agente `general-purpose` novo recebe o briefing da revisão de origem restrito **aos itens
corrigidos**, sobre os arquivos já regerados. O que ainda aparecer volta como "não resolvido" (não há
segunda rodada de correção). Conferir o que ele devolver como na seção 3 de cada skill.

## 6. Relatório (a única coisa que o usuário lê)

No chat, conclusão primeiro: quantos itens corrigidos, não resolvidos, para decidir e barrados. Depois:

```
1  Alterações
 1.1  <arquivo>
  1.1.1  <o que mudou, em uma linha>
         Item de origem: <revisão e veredito>
         Antes → depois: <trecho ou número, com coluna e letra>
         Prova: <os dois caminhos e a data do dado> | testes: OK n de n
2  Não resolvido (corrigido e ainda presente na reconferência, ou teste falhou)
3  Ficou para você decidir (com as saídas possíveis e a recomendada)
4  Barrado por limite fixo (arquivo que vai para fora, protegido ou já enviado, divergência entre os dois caminhos)
5  Onde está a cópia: _backups_projeto\review_go_<assunto>\ (manifesto.csv)
6  Inventário de premissas: <caminho do .md gravado ao lado das planilhas> | não rodou: <motivo>
```

Onde cada item entra:

| O item é | Seção |
|---|---|
| Escolha do usuário (conflito de premissa, `Decisão sua`, `Já decidido`, sugestão de melhoria), **mesmo que a escolha também toque arquivo que vai para fora ou entregável enviado** | 3, com o limite citado dentro do item |
| Defeito comprovado que seria corrigido, mas o limite fixo impediu | 4 |

A seção 6 é obrigatória sempre que a revisão de premissas rodou: o `.md` do inventário (seção 4 da
`/review:premises`) é gravado antes do relatório, e o caminho dele vai na linha 6.

Os caminhos dos arquivos alterados e regerados vão em texto. Sem rodada de perguntas no fim. Seguir as
convenções de escrita que o ambiente declarar. Armadilha nova corrigida como `Erro` vira proposta de
linha para o catálogo da `/review:financial` (seção 6 dela).
