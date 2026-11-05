# skills-andre-guerra

Loja de skills do Claude Code mantida por André Guerra. As skills não trazem premissa nem regra de
negócio de nenhuma empresa: cada uma lê o ambiente onde roda (código, planilhas e as notas do projeto,
como `CLAUDE.md`, `MEMORIA.md` e `LEIA-ME`) e tira de lá o que vale.

## Plugin `review`

| Comando | O que faz |
|---|---|
| `/review:all <alvo>` | roda as revisões cabíveis (financeira, premissas e narrativa), um agente cada, e devolve um relatório único |
| `/review:financial <planilha>` | revisa a lógica financeira de uma planilha (TIR, MOIC, recebimento, custo) |
| `/review:premises <planilhas>` | levanta as premissas e aponta as que se contradizem ou não têm fonte |
| `/review:narrative` | revisa e-mail, PDF e planilhas como o leitor lê, do número final de volta à base |
| `/review:go <alvo>` | revisa e **corrige sozinho** o que for defeito comprovado; devolve só o relatório das alterações |

Pedir a revisão (digitando o comando ou em palavras) já autoriza os agentes dela. Nenhuma dispara
sozinha ao fim de uma entrega.

## Instalar (uma vez)

1. No Claude Code:
   ```
   /plugin marketplace add SchrodingerSC2026/skills-andre-guerra
   /plugin install review@skills-andre-guerra
   ```
2. Ligue a atualização automática: `/plugin`, aba de lojas, `skills-andre-guerra`,
   **Enable auto-update**. A partir daí, cada abertura do Claude Code puxa a versão nova.
3. Tenha um Python com `openpyxl` (`python -m pip install openpyxl`).
4. Abra uma sessão nova do Claude Code.

## Atualizar à mão

```
claude plugin marketplace update skills-andre-guerra
```

## Versão

O `plugin.json` do `review` não tem o campo `version` de propósito: assim cada commit enviado vira uma
versão nova e chega aos instalados (com a atualização automática ligada) na abertura seguinte do
Claude Code. Com `version` fixo, a mudança só chega quando o número muda (medido em 05/11/2026).
