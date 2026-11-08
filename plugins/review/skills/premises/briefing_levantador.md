# Briefing do agente levantador da /financial-review-premises

A sessão principal preenche os campos `{...}` e manda o texto abaixo, inteiro, a um agente `general-purpose` novo.
Não acrescentar nada sobre o que se espera achar.

---

Você vai levantar as **premissas** por trás de um conjunto de planilhas e dizer onde elas se contradizem. Premissa é
todo valor ou regra que o resultado assume e que não vem do dado: taxa (CDI, spread, mezz, escritório, comissão), data
(acordo, corte, data-base), régua (base de dias, juros simples ou compostos, arredondamento), regra de universo (quem
entra, quem sai), regra de agrupamento (par, carteira, fluxo só), valor cravado (mediana, tabela colada, total digitado
à mão). Inclui premissa sem nome: um número solto no meio de uma conta (`* 0.93`) ou o valor padrão de um argumento.

**Material (leia só isto e o que os geradores importam ou leem):**
- Planilhas: {planilhas}
- Geradores: {geradores}
- Mapas das planilhas (fórmulas e dependências): {mapas}
- Notas do projeto: {notas} (decisões, com data)
Não rode os geradores. Não grave nada no projeto. Conta de conferência, se precisar, num script seu em pasta temporária.

**A resposta tem exatamente estas três partes, nesta ordem:**

1. **Inventário.** Uma linha por premissa, em tabela: `Premissa` | `Valor` | `Onde` (arquivo:linha com o trecho
   literal, ou Aba!Célula) | `Atua em` (planilha e coluna com a letra) | `Fonte`. A fonte é uma de quatro:
   `DECISÃO dd/mm/aaaa (onde está registrada)`, `MEDIÇÃO dd/mm/aaaa (onde)`, `DOCUMENTO (qual)` ou `SEM FONTE`. A mesma
   premissa em vários lugares é uma linha só, com todos os lugares no `Onde`.
2. **Conflitos**, numerados `1`, `2`, ..., cada um de um destes quatro tipos, com o tipo escrito:
   - `MESMA PREMISSA, VALORES DIFERENTES`: dois lugares assumem valores diferentes para a mesma coisa;
   - `CÓDIGO CONTRA DECISÃO`: o código faz uma coisa e uma nota registra outra decisão;
   - `TEXTO CONTRA CÁLCULO`: uma aba de premissas ou um rótulo descreve uma conta diferente da feita;
   - `SEM FONTE`: premissa que muda resultado e não tem decisão, medição nem documento;
   - `BASE DIFERENTE ENTRE PARTES`: duas partes que o material apresenta como a mesma conta (o mecanismo
     central e a sua aplicação em outro canal, prazo ou cenário) partem de grandezas diferentes, como uma
     da oferta de cada período e a outra do piso ou do máximo. Mostre a base de cada uma (arquivo:linha).
   Cada conflito traz os dois lados (arquivo:linha e trecho literal de cada um), a data de cada lado quando houver, e
   qual lado parece vigente pela data da decisão. Não decida qual está certo: isso é de quem lê.
   ⛔ Quando os dois lados são **notas** e a mais nova revoga a mais velha em palavras, e o código segue a mais nova,
   não é conflito: vai para uma lista à parte, **Notas desatualizadas** (a nota velha, a nova e as datas), que é
   manutenção de nota e não pergunta a quem lê. Se o código segue a nota velha, é `CÓDIGO CONTRA DECISÃO`.
3. **Bloco JSON**, um só, no fim:
```json
{"inventario": [{"premissa": "...", "valor": "...", "onde": ["arquivo:linha `trecho`"], "atua_em": "...",
                 "fonte": "DECISÃO 01/11/2026 (MEMORIA.md:7)"}],
 "conflitos": [{"id": 1, "tipo": "CÓDIGO CONTRA DECISÃO ou BASE DIFERENTE ENTRE PARTES etc.", "resumo": "...",
                "lados": [{"onde": "arquivo:linha", "trecho": "...", "data": "dd/mm/aaaa ou null"}],
                "vigente_pela_data": "..."}],
 "notas_desatualizadas": [{"velha": "arquivo:linha `trecho` (data)", "nova": "arquivo:linha `trecho` (data)"}]}
```

**Escrita:** as convenções do ambiente (preenchidas por quem envia este briefing: idioma, moeda, data); o que não der para saber sai `INDETERMINADO`.
