---
name: financial
description: Revisa o raciocínio financeiro por trás de uma planilha (TIR, MOIC, duration, breakeven, aderência, recebimento, custo) e devolve itens numerados com veredito e prova. Use só quando o usuário pedir, digitando /review:financial <planilha> ou pedindo em palavras a revisão financeira ("usa minha skill para revisar a planilha"); nunca por conta própria ao terminar uma entrega.
---

# /review:financial

Roteiro da sessão principal. Dentro do `/review:all` e do `/review:go`, esta skill roda como uma das
revisões: o preparo da seção 1 é feito uma vez pelo orquestrador e o agente da seção 2 sai em paralelo
com os outros.

A skill não traz premissa nenhuma (taxa, data, régua, valor): toda premissa e toda decisão vêm do
ambiente onde ela roda (o código, a planilha e as notas do projeto).

**Autorização:** o pedido do usuário, digitado ou em palavras, já autoriza **um** agente revisor e a
medição dos itens `Erro` (em cópia, banco só leitura). Não autoriza corrigir nada: a revisão só aponta
(quem corrige é o `/review:go`). `PY` abaixo é um Python com `openpyxl` (o do venv do workspace, se
houver; senão o `python` que tiver o pacote, ou `python -m pip install openpyxl`) e `SKILL_DIR` é esta
pasta.

## 1. Da planilha à lógica

1. Planilha não informada ou citada de forma ambígua: listar as candidatas com data e perguntar.
2. `PY SKILL_DIR\mapa_planilha.py <planilha>` → `tipo` (`valor` ou `formula`) e as dependências.
   Guardar o JSON numa pasta temporária (vai para o revisor).
3. `PY SKILL_DIR\acha_gerador.py <planilha> <raiz>` (raiz: a pasta do projeto, ou a raiz
   do workspace se a planilha estiver fora de projeto; leva até 30 s numa raiz grande).
   - Separar o **gerador** (o que grava a planilha: `save`, `to_excel`, `ExcelWriter` com o nome)
     de quem só a cita (conferidor, consumidor, documentação). Abrir o trecho de cada candidato.
   - Mais de um gerador possível: listar com data e perguntar qual.
   - Nenhum gerador e `tipo == "valor"`: **parar** e dizer que não há lógica para revisar (só
     números colados); não revisar no escuro.
   - Nenhum gerador e `tipo == "formula"`: revisão pelas fórmulas.
   - Gerador e `tipo == "formula"`: **mista**; cada coluna pelo seu caminho.
   - `mais_novo_que_planilha: true` no gerador: **aviso no topo** da revisão ("o script mudou
     depois que a planilha foi gerada; o código revisado pode não ser o que gerou o entregável").
4. Achar as notas do projeto (dicionário da base, decisões): `MEMORIA.md`, `CLAUDE.md`, README ou a
   documentação mais próxima da planilha, as que existirem. Sem nenhuma, dizer ao revisor que não há
   dicionário, e o que depender dele sai `Precisa de prova`.

## 2. O revisor

Preencher `SKILL_DIR\briefing_revisor.md` (planilha, gerador, caminho do JSON do mapa, as notas do
projeto, `SKILL_DIR\catalogo.md`) e disparar **um** agente `general-purpose` novo com o texto
inteiro. Nada sobre o que se espera achar.

## 3. Conferir o que voltou

Para cada item: abrir o `arquivo:linha` ou a `Aba!Célula` citados e conferir que o trecho literal
está lá e diz o que o item afirma. Item sem onde e trecho, ou com trecho que não bate, é
**descartado**. Convenção marcada como `Erro` vira `Decisão sua`.

## 4. Medir os itens Erro (só eles)

Na sessão principal (medir não se delega): efeito = premissa atual x premissa corrigida, **as duas
sobre a base de hoje**, por **dois caminhos** diferentes (ex.: cópia do gerador com a premissa
trocada numa pasta temporária, e conta direta sobre a base). Nunca rodar o gerador sobre o
entregável; banco só leitura. Os dois caminhos divergem: levar a divergência, não um número.
Sempre com a data do dado. Grande demais para medir agora: `INDETERMINADO`, dizendo o porquê.

## 5. Mostrar

No chat:

```
1  <planilha>
 1.1  <etapa: recebimentos, custo, unidade/breakeven, relógio, derivação>
  1.1.1  [Veredito] uma linha
         Onde: arquivo:linha ou Aba!Célula, coluna com letra, campo de origem
         Prova: exemplo pequeno | efeito medido (2 caminhos) | derivação
```

Os itens `Certo` vão juntos, numa linha cada, para se ver o que foi conferido. Fechar dizendo que
o usuário responde item a item ("1.1.1 corrige; 1.3.1 quero a prova") e que o que não tocar fica
como está. Seguir as convenções de escrita que o ambiente declarar (idioma, moeda, data, coluna com
letra).

## 6. Depois da resposta

- `corrige` ou `é erro` num item `Erro`: conta como confirmado. Se a armadilha **não** está no
  catálogo, propor a linha nova (chave, armadilha, como detectar, sem nome de projeto, planilha ou
  valor) para o `catalogo.md` do repositório da skill, e dizer isso ao usuário: a cópia instalada é
  substituída a cada atualização. A correção em si é tarefa normal, fora desta skill.
- Nada é corrigido sem a ordem do usuário.
