---
name: zip
description: Confere se um pacote (.zip ou pasta) entregue a outra pessoa ou equipe (dev, responsável por sistema, parceiro) se entende sozinho, com um agente que lê como o destinatário e diz o que entendeu e o que faria. Use só quando o usuário pedir, digitando /review:zip ou pedindo em palavras para "ver o que entenderam do zip"; nunca por conta própria ao terminar uma entrega.
---

# /review:zip

Um pacote vai para quem não estava na conversa. A pergunta é se ele, só com o que está dentro, entende o
pedido, faz a coisa certa e consegue testar. Um agente lê o pacote **como o destinatário** e diz o que
entendeu; a sessão compara com o que o pacote precisava transmitir, escrito **antes** de ler a resposta.

A skill não traz régua própria: o que o pacote precisa transmitir vem da conversa e das notas do projeto.

**Autorização:** o pedido do usuário já autoriza **um agente por pacote**, em paralelo. Não perguntar antes.

## 1. Fixar o alvo e lacrar o gabarito

1. Os pacotes e, para cada um, **quem recebe** e o que essa pessoa conhece (o dev do portal conhece o
   portal, não o pricing). Citação ambígua: listar os candidatos com data e perguntar.
2. Escrever o **gabarito** de cada pacote num arquivo no scratchpad, antes de disparar: os itens que o
   destinatário precisa sair sabendo (o pedido, o que entra e o que **não** entra, a regra ou a conta,
   como testar, o que falta confirmar), um por linha, com um código (`P1`, `P2`). O gabarito não vai ao
   agente.

## 2. O leitor (subagente)

Preencher `briefing_leitor.md` desta pasta para cada pacote e disparar os agentes `general-purpose`
**na mesma mensagem**, sem dizer o que se espera achar nem mandar o gabarito.

## 3. Conferir o que voltou

- Cada item do gabarito: `entendeu`, `entendeu errado` (com o trecho dele) ou `não viu`.
- Cada defeito que o leitor achou: refazer por outro caminho antes de aceitar (rodar o código, recontar
  a coluna). Defeito confirmado em código ou em dado do pacote se corrige no **gerador** e se trava no
  **conferidor**, e a trava nova tem de reprovar o pacote antigo antes de aprovar o novo.
- Termo que o leitor precisou adivinhar e pergunta que ele mandaria de volta: entram como achado.

## 4. Mostrar, no formato numerado

```
1  <pacote> (para <quem recebe>)
 1.1  Gabarito: X de Y entendidos; os errados e os não vistos, um por linha com o trecho
 1.2  Defeitos: [Gravidade] uma linha, Onde (arquivo, linha ou coluna), Conferido: sim | não reproduzi
 1.3  Termos e perguntas do destinatário
```

Depois, o que não se conseguiu verificar. O usuário responde item a item; o que não tocar fica como está.

## Erros comuns que esta skill evita

| Sem a skill | Com a skill |
|---|---|
| O leitor herda o contexto do projeto e lê como quem fez o pacote: jargão interno passa sem pergunta | Persona do destinatário, que só sabe o que está no pacote, e lista de termos que precisou adivinhar |
| Resposta de auditor (números batem), que não diz se o pedido foi entendido | Primeiro o pedido e o que ele faria, depois a conferência, comparados a um gabarito escrito antes |
| Exemplo de teste conferido com folga de centavos: o pacote manda o destinatário reproduzir e ele reprova | O exemplo do pacote se reproduz exato, sem tolerância |
| Só os exemplos testados: a regra que o texto promete ("nunca passa do saldo") quebra em casos fora deles | Cada afirmação do texto testada no dado inteiro, em cada linguagem do código |
| Gabarito escrito depois de ler a resposta, que se ajusta ao que o agente disse | Gabarito lacrado antes de disparar |
