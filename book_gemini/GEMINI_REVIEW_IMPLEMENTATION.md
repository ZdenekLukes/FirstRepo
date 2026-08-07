# Gemini review — zapracování a fact-check

Datum: 2026-08-07

Tento dokument popisuje, jak byla doporučení z Gemini review zapracována do varianty `book_gemini/`. Původní `book/` nebyl změněn.

## Strukturální změny

- Kapitoly 16 + 17 sloučeny do **16. Anatomie a smyčka AI agenta**.
- Samostatný soubor kapitoly 17 odstraněn.
- Samostatná kapitola 26 odstraněna.
- Praktické rozlišení webového chatu vs. API/script/agent přesunuto do úvodu kapitoly 22.
- Ostatní čísla kapitol zůstala stabilní.

## Obsahové změny

- 01: perceptron, lineární separabilita, Minsky & Papert, backprop vs. Transformer/self-attention.
- 03: praktický dopad tokenizace češtiny.
- 05: reasoning models, test-time compute a práce s reasoning effort.
- 08: VRAM = weights + KV cache + runtime + rezerva; praktická 70B Q4 hranice.
- 09: anatomie produkčního promptu a správný structured-output pattern.
- 11: zkrácena na stručný můstek k RAG.
- 12: explicitní semantic/vector vs. lexical/full-text srovnání.
- 15: přesnější USB-C/MCP mentální model.
- 16: sloučený agent + loop + failure modes + guardrails.
- 22: enterprise parsing, OCR, ACL, provenance, audit, citlivá data.
- 25: system prompt není security boundary; defense-in-depth.
- 31: konkrétní LLM-as-a-judge prompt a kalibrace.
- 32: konkrétní TCO výpočet cloud API vs. dedicated GPU.
- Přílohy B/C: explicitní `[Snapshot 08/2026]`.

## Dvě doporučení review byla technicky zpřesněna

### `temperature = 0`

Nebyla zapsána jako podmínka validního JSON. Nízká temperature může snížit variabilitu, ale validitu schématu má zajišťovat **structured output / constrained decoding + schema validation**.

### Počet tokenů na české slovo

Nebyla zapsána univerzální konstanta `1.5–2`. Tokenizace silně závisí na tokenizeru a typu textu. Kniha proto uvádí praktické pravidlo: čeština je proti angličtině často tokenově méně úsporná a sizing se má měřit cílovým tokenizerem.

### MCP

Analogie USB-C je zachována, ale zpřesněna: MCP snižuje počet unikátních integrací; konkrétní služba stále potřebuje MCP server/wrapper nad svým API nebo lokálním rozhraním.

## Stav

Toto je obsahová review varianta. Před případným nahrazením `book/` má následovat diff review proti původnímu release candidate a nový proof build.
