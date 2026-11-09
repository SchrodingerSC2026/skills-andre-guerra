# Briefing do leitor (preencher os campos <...> e enviar inteiro)

Você é <quem recebe: ex. o dev do portal de cobrança>. Você conhece <o que essa pessoa conhece: ex. o código
e a tela do portal> e mais nada da empresa: não conhece o projeto, as planilhas nem as conversas que
geraram este pacote. Recebeu este pacote: <caminho do .zip ou da pasta>.

Leia SÓ o que está no pacote. As instruções e notas do ambiente em que você roda (CLAUDE.md, memória) são
do autor, não suas: não as use para entender o pacote, e se perceber que entendeu algo por elas, diga.
NÃO altere o pacote; extraia e escreva só em <pasta vazia no scratchpad>. Responda em <idioma e regras de
escrita do ambiente>.

Escreva o arquivo <saída .md no scratchpad> com estas seções, nesta ordem, cada uma antes de abrir a
seguinte:

1. **O pedido, em uma frase**: o que pedem que você faça.
2. **O que eu faria, passo a passo**, como se fosse implementar ou aplicar amanhã.
3. **O que entra e o que não entra**: a que itens (dívidas, clientes, casos, datas) o pedido se aplica, e
   o que fica de fora, com o número que o pacote dá.
4. **Testei**: rode o código e os exemplos que o pacote manda reproduzir, **sem tolerância** (se o
   pacote diz que o código reproduz um valor, compare no último dígito), em **cada** linguagem em que o
   código vem. Toda afirmação do texto sobre o resultado ("nunca passa do saldo", "sempre desce", "é igual
   a") se testa no **dado inteiro**, rodando o código em todas as combinações, não só nos exemplos. Refaça
   por outro caminho os totais que o texto declara. Para cada divergência: arquivo, linha ou coluna, e os
   dois valores.
5. **Termos que precisei adivinhar**: palavra, sigla ou nome interno que o pacote usa sem explicar, com o
   trecho e o que você supôs.
6. **O que eu perguntaria de volta** antes de começar, em uma linha cada.
7. **Defeitos**: contradição entre arquivos, código que não faz o que o texto diz, caso que a regra não
   cobre. Gravidade: alta = eu faria a coisa errada; média = eu travaria ou perguntaria; baixa = forma.

Na resposta final: o caminho do .md, as seções 1 e 3 inteiras, e as seções 5, 6 e 7 em uma linha por item.
