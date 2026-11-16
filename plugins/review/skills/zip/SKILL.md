---
name: zip
description: Lê um pacote (.zip ou pasta) entregue a outra pessoa, equipe ou agente de IA como o destinatário leria (um agente que só sabe o que está dentro) e CORRIGE sem perguntar o que ele não entendeu, entendeu errado ou achou quebrado, refazendo o pacote no fim; devolve só o relatório das alterações. Use só quando o usuário pedir, digitando /review:zip ou pedindo em palavras para "ver o que entenderam do zip" ou "revisar o pacote"; nunca por conta própria ao terminar uma entrega.
---

# /review:zip

Um pacote vai para quem não estava na conversa, muitas vezes outro agente de IA. A pergunta é se ele, só
com o que está dentro, entende o pedido, faz a coisa certa e consegue testar. Um agente lê o pacote **como o
destinatário**; a sessão compara com o que o pacote precisava transmitir e **conserta o pacote** até ele
transmitir. O usuário não revisa o laudo: recebe o pacote corrigido e a lista do que mudou.

A skill não traz régua própria: o que o pacote precisa transmitir e o que se protege vêm da conversa e das
notas do ambiente (`CLAUDE.md`, `MEMORIA.md`, `PENDENCIAS.md`, `LEIA-ME` do projeto, os que existirem).

**Autorização:** o pedido do usuário já autoriza corrigir sem perguntar, **só no pacote pedido e no que o
gera** (gerador, conferidor, documentos que vão dentro dele), e **dois agentes por pacote** (a leitura e a
releitura), em paralelo entre pacotes. Não perguntar antes.

## 0. Limites fixos

- ⛔ **Não inventar o que falta.** Número, regra de negócio, decisão ou fato que o pacote precisa e que não
  está no ambiente (código, base, notas com data) não se escreve no pacote: vai para "Ficou para você" no
  relatório, em uma linha. O que está no ambiente e só faltava no pacote entra, citando a origem.
- ⛔ **Arquivo que as regras do ambiente protegem não se altera** (dado bruto, pastas de envio a órgão,
  portal ou bureau, o que as notas marcarem como imutável). Rodar um gerador que regrava um desses também
  conta: regerar numa cópia temporária.
- ⛔ **Sem merge, push, PR ou escrita em banco** (banco só leitura). Commit também não, salvo regra do
  ambiente que diga o contrário para aquele repositório.
- ⛔ **Número que muda se recalcula por um segundo caminho.** Os dois divergem: não aplica, e a divergência
  vai ao relatório.
- Nada se abre no fim.

## 1. Fixar o alvo e lacrar o gabarito

1. Os pacotes e, para cada um, **quem recebe** e o que essa pessoa ou agente conhece. Citação ambígua:
   listar os candidatos com data e perguntar (é a única pergunta permitida).
2. Conferir que o pacote é a versão vigente (hash contra os arquivos de origem, data contra a última
   rodada que os gera). Origem mudou depois do pacote: o pacote refeito no fim sai da origem atual.
3. Escrever o **gabarito** de cada pacote num arquivo no scratchpad, antes de disparar: os itens que o
   destinatário precisa sair sabendo (o pedido, o que entra e o que **não** entra, a regra ou a conta,
   como testar, o que falta confirmar), um por linha, com um código (`P1`, `P2`). O gabarito não vai ao
   agente.

## 2. A leitura (subagente)

Preencher `briefing_leitor.md` desta pasta para cada pacote e disparar os agentes `general-purpose` **na
mesma mensagem**, sem dizer o que se espera achar nem mandar o gabarito.

## 3. Triar o que voltou

- Cada item do gabarito: `entendeu`, `entendeu errado` (com o trecho dele) ou `não viu`. Os dois últimos
  são defeito do pacote: o texto não transmite.
- Cada defeito que o leitor achou: refazer por outro caminho antes de aceitar (rodar o código, recontar a
  coluna). Não reproduziu: não corrige, e entra no relatório como "não reproduzi".
- Termo que o leitor precisou adivinhar e pergunta que ele mandaria de volta: defeito do pacote quando a
  resposta está no ambiente; "Ficou para você" quando não está.

## 4. Corrigir

1. **Cópia antes de tocar:** cada arquivo, antes do primeiro byte alterado, vai para
   `<raiz do workspace>\_backups_projeto\review_zip_<assunto>\` (sem workspace, a pasta do projeto),
   mantendo o caminho relativo, com um `manifesto.csv` (arquivo, sha256 antes, sha256 depois, item). O
   pacote antigo vai junto.
2. **Na fonte, nunca no derivado:**
   - defeito em dado ou código se corrige no **gerador** e se trava no **conferidor**; a trava nova tem de
     **reprovar a versão antiga** antes de aprovar a nova (guardar a antiga para essa prova);
   - texto que não transmite (item `entendeu errado` ou `não viu`, termo adivinhado com resposta no
     ambiente, afirmação que o dado desmente, referência a arquivo que não está no pacote) se corrige no
     documento do pacote, escrito para o destinatário: o que ele precisa para agir, sem o que só serve a
     quem gera (como regerar, nomes de script e de tabela vão para uma seção à parte, marcada como do
     autor, ou saem);
   - contagem citada no texto se reconta no dado que vai no pacote, por um caminho diferente do gerador.
3. Rodar os testes e o conferidor do gerador. Teste que falhar desfaz a correção daquele item (volta a
   cópia) e o item vai como "não resolvido".
4. **Refazer o pacote** pelo mesmo caminho que o gerou (o script, se houver; senão, a mesma pasta com a mesma
   estrutura e os mesmos nomes) e conferir por hash que cada arquivo dentro dele é o da origem corrigida.

## 5. Reler uma vez

Um agente `general-purpose` novo recebe o mesmo `briefing_leitor.md` sobre o pacote refeito, sem saber o
que mudou. Conferir o que ele devolve contra o gabarito e contra a lista de correções: o que ainda aparecer
volta como "não resolvido". Defeito **novo** que a releitura achar e que se reproduz se corrige como na seção 4 e
refaz o pacote, sem terceira leitura; o que depende de regra que o ambiente não tem vai para o pacote como pergunta
em aberto (seção do documento que o destinatário lê) e para "Ficou para você".

## 6. Relatório (a única coisa que o usuário lê)

No chat, conclusão primeiro: o pacote refeito (caminho e data), quantos itens corrigidos, não resolvidos e
para você. Depois, no formato numerado:

```
1  <pacote> (para <quem recebe>)
 1.1  Alterações: uma linha cada, com o arquivo e o antes → depois (coluna e letra quando for planilha);
      trava nova: reprovou a antiga, aprovou a nova
 1.2  Releitura: X de Y itens do gabarito entendidos; o que ainda não foi entendido
 1.3  Não resolvido (teste falhou, não reproduzi, divergência entre os dois caminhos)
 1.4  Ficou para você: o que o pacote precisa e o ambiente não tem, em uma linha cada
 1.5  Cópia: _backups_projeto\review_zip_<assunto>\ (manifesto.csv)
```

Sem laudo do que estava certo, sem rodada de perguntas no fim. Seguir as convenções de escrita que o
ambiente declarar.

## Erros comuns que esta skill evita

| Sem a skill | Com a skill |
|---|---|
| O leitor herda o contexto do projeto e lê como quem fez o pacote: jargão interno passa sem pergunta | Persona do destinatário, que só sabe o que está no pacote, e lista de termos que precisou adivinhar |
| Laudo do que está certo e errado, que o usuário tem de ler e mandar corrigir item a item | A sessão corrige e refaz o pacote; o usuário lê só o que mudou e o que não tinha como resolver |
| Exemplo de teste conferido com folga de centavos: o pacote manda o destinatário reproduzir e ele reprova | O exemplo do pacote se reproduz exato, sem tolerância |
| Só os exemplos testados: a regra que o texto promete ("nunca passa do saldo") quebra em casos fora deles | Cada afirmação do texto testada no dado inteiro, em cada linguagem do código |
| Corrigir o texto sem tocar o dado, ou o dado sem trava: o defeito volta na próxima geração | Defeito de dado corrigido no gerador, com trava que reprova a versão antiga |
| Preencher o que falta com um valor plausível para o pacote "fechar" | O que o ambiente não tem vai para "Ficou para você", nunca para dentro do pacote |
| Gabarito escrito depois de ler a resposta, que se ajusta ao que o agente disse | Gabarito lacrado antes de disparar |
