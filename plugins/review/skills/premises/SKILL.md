---
name: premises
description: Levanta as premissas por trás de planilhas financeiras (taxas, datas, réguas, valores cravados) e aponta as que contradizem outra, contradizem uma decisão registrada ou não têm fonte. Use só quando o usuário pedir, digitando /review:premises ou pedindo em palavras a revisão de premissas; nunca por conta própria ao terminar uma entrega.
---

# /review:premises

Irmã da `/review:financial`. Roteiro da sessão principal. Dentro do `/review:all` e do `/review:go`,
o preparo da seção 1 é feito uma vez pelo orquestrador e o agente da seção 2 sai em paralelo com os
outros.

A skill não traz premissa nenhuma: ela levanta as do ambiente (código, planilhas, notas do projeto) e
compara umas com as outras e com as decisões registradas ali. Nenhum valor é "o certo" de antemão.

**Autorização:** o pedido do usuário, digitado ou em palavras, já autoriza **um** agente levantador.
Não autoriza corrigir nada (quem corrige é o `/review:go`). `PY` é o Python com `openpyxl` (o do venv
do workspace, se houver; senão o `python` que tiver o pacote); `FR` é a pasta irmã desta,
`..\financial` (a da `/review:financial`), cujos scripts esta skill reaproveita.

## 1. Das planilhas à cadeia

1. Planilha citada de forma ambígua: listar as candidatas com data e perguntar.
2. Para cada planilha: `PY FR\mapa_planilha.py <planilha>` (JSON numa pasta temporária) e
   `PY FR\acha_gerador.py <planilha> <raiz>`. Separar o gerador de quem só cita; mais de um gerador
   possível: listar e perguntar; script mais novo que a planilha: aviso no topo.
3. **A cadeia:** abrir cada gerador e anotar as planilhas e arquivos que ele lê; os geradores desses
   entram também.
4. **As notas:** as do projeto e da raiz do workspace que existirem (`MEMORIA.md`, `PENDENCIAS.md`,
   `CLAUDE.md`, README). A que não existir é pulada, e o relatório diz quais faltaram.

## 2. O levantador

Preencher `briefing_levantador.md` (planilhas, geradores, mapas, notas) e disparar **um** agente
`general-purpose` novo com o texto inteiro. Nada sobre o que se espera achar.

## 3. Conferir o que voltou

- Cada linha do inventário e cada lado de cada conflito: abrir o `arquivo:linha` e conferir o trecho
  literal. Sem trecho que bata, sai.
- **Completar a lista de lugares** de cada premissa com número (taxa, data, fator): busca própria
  (`Grep`) pelo valor em todas as grafias (`0.25`, `0,25`, `25%`, e o complemento: `0.75`, `/ 0.75`) e
  pelo nome, em todos os scripts do projeto e nos que eles importam. O lugar que o agente não listou
  entra, e o que contradiz vira conflito `MESMA PREMISSA, VALORES DIFERENTES`. É aqui que mora o erro
  de escala: a mesma taxa espalhada por cinco scripts.
- Conflito `CÓDIGO CONTRA DECISÃO`: abrir a nota citada e conferir a data e o texto da decisão.

## 4. Mostrar, no modelo da /review:financial

O inventário inteiro e os conflitos com os dois lados vão para um arquivo `.md` na pasta das planilhas
(`premissas_<conjunto>.md`). No chat, o mesmo formato numerado da `/review:financial`, uma planilha
(ou etapa transversal) por bloco:

```
1  <planilha ou etapa transversal>
 1.1  <premissa>
  1.1.1  [Veredito] uma linha do que está em jogo
         O que é: a premissa em linguagem de negócio e o que ela faz no resultado
         O problema: o que um lado faz e o outro faz, sem nome de função
         Exemplo: um caso concreto com número (medido na base, ou fictício pequeno declarado como fictício)
         Quanto pesa: efeito medido (quantos casos, quanto dinheiro) ou "não medido"
         Para decidir: as saídas possíveis e a recomendada
         Onde: arquivo:linha `trecho` (data) | outro lado: arquivo:linha `trecho` (data)
```

Item sem contexto, exemplo e peso não se mostra: leitor que recebe só "valores diferentes" não entende
o problema. Antes de mostrar, medir o peso de cada item (leitura na base ou na planilha, nunca de
cabeça) e tirar da lista o que é diferença **por desenho** (cada canal com o seu calendário, por
exemplo) ou de peso desprezível: esses vão juntos numa linha "Conferido, sem problema", com o porquê em
meia frase.

Vereditos: `Certo` (tem fonte e não conflita), `Valores diferentes`, `Código contra decisão`, `Texto
contra cálculo`, `Sem fonte` e `Já decidido` (o conflito existe, mas uma decisão registrada mais
recente já escolheu o lado). Os `Certo` vão juntos, numa linha cada. Todo conflito é decisão do
usuário: a skill nunca escolhe o lado, e o "vigente pela data" vai na Prova. Seguir as convenções de
escrita que o ambiente declarar.

## 5. Decidir

Fechar dizendo que o usuário responde item a item ("1.2.1 corrige para o código; 2.1.1 mede antes") e
que o que não tocar fica como está. Não abrir rodada de perguntas por cima da lista. Se o projeto
tiver arquivo de pendências, cada resposta é gravada **na hora** nele, com a especificação completa (o
que muda, em que arquivos e linhas, o que conferir depois).

A correção em si é tarefa normal, fora desta skill, e só com a ordem do usuário.
