---
title: "F. Checklist pro návrh agenta"
part: "PŘÍLOHY"
status: final-draft
version: "0.7"
updated: 2026-08-07
---

# F. Checklist pro návrh agenta

Tento checklist je určený pro review před tím, než se z prototypu stane agentní systém s reálnými oprávněními.

## F.1 Úloha

- [ ] Jaký je přesný cíl?
- [ ] Jaký problém řeší dnes člověk nebo klasický software?
- [ ] Jaká je baseline bez AI?
- [ ] Jak poznám úspěch?
- [ ] Jaké případy musí agent umět odmítnout nebo označit jako UNKNOWN?

Dobrá definice:

```text
INPUT
→ očekávaný PROCESS
→ OUTPUT
→ SUCCESS CRITERIA
```

Špatná definice:

```text
„agent pro engineering“
```

## F.2 Vstupy a context

- [ ] Jaké informace agent potřebuje?
- [ ] Které zdroje jsou autoritativní?
- [ ] Jak pozná aktuální revizi?
- [ ] Jaká metadata potřebuje retrieval?
- [ ] Co dělat, když vstup chybí?
- [ ] Co dělat, když si dva zdroje odporují?
- [ ] Jak je context omezený, aby nebyl zbytečně velký a hlučný?

## F.3 Model

- [ ] Jaké schopnosti model skutečně potřebuje?
- [ ] Máme alespoň dva kandidáty pro benchmark?
- [ ] Je menší / levnější / lokální model dostatečný?
- [ ] Umí požadované structured output?
- [ ] Umí spolehlivě tool calling?
- [ ] Máme přesně evidovanou model version?

## F.4 Tools

Pro každý nástroj:

- [ ] Proč jej agent potřebuje?
- [ ] Jaké má schema?
- [ ] Jak validujeme argumenty?
- [ ] Je volání idempotentní, nebo může opakováním způsobit problém?
- [ ] Co vrací při chybě?
- [ ] Má timeout?
- [ ] Jak se testuje bez produkčních dat?

Pokud tool není potřeba, nepřidávej jej „pro jistotu“.

## F.5 Oprávnění

- [ ] Jaká oprávnění skutečně potřebuje?
- [ ] Co může pouze číst?
- [ ] Co může měnit?
- [ ] Je write scope omezený?
- [ ] Má oddělené credentials pro read a write?
- [ ] Může volat internet?
- [ ] Může posílat externí komunikaci?
- [ ] Je root / admin přístup skutečně nezbytný?

Princip:

> **Agent má dostat nejmenší action space, ve kterém ještě dokáže splnit cíl.**

## F.6 Stav a memory

- [ ] Potřebuje agent stav mezi kroky jednoho runu?
- [ ] Potřebuje long-term memory mezi runy?
- [ ] Co přesně se ukládá?
- [ ] Jak se informace aktualizuje nebo zapomíná?
- [ ] Je u memory provenance a timestamp?
- [ ] Jak se zabrání tomu, aby se chyba stala „trvalou znalostí“?

Pokud agent nepotřebuje long-term memory, je její absence výhoda.

## F.7 Smyčka a stop conditions

- [ ] Jak agent pozná, že úkol dokončil?
- [ ] Jaký je maximální počet kroků?
- [ ] Jaký je time limit?
- [ ] Jaký je cost / token budget?
- [ ] Co se stane při opakovaném stejném tool callu?
- [ ] Jak se detekuje loop?
- [ ] Kdy se eskaluje člověku?

## F.8 Verification

- [ ] Jak se kontroluje výsledek?
- [ ] Co lze ověřit deterministicky?
- [ ] Máme schema validation?
- [ ] Máme unit / rule checks?
- [ ] Máme external verifier, simulátor nebo test suite?
- [ ] Je LLM judge používán jen tam, kde klasické pravidlo nestačí?
- [ ] Je potřeba human review?

Preferované pořadí:

```text
schema
↓
rules
↓
external tool / test
↓
LLM review
↓
human review
```

## F.9 Human approval

- [ ] Co vyžaduje lidské potvrzení?
- [ ] Vidí schvalující člověk navrhovanou akci i její důvody?
- [ ] Vidí zdroje a diff?
- [ ] Může akci odmítnout nebo upravit?
- [ ] Je approval zaznamenán v auditu?

## F.10 Logging a observability

- [ ] Jak se logují kroky?
- [ ] Má každý run ID?
- [ ] Evidujeme model a workflow version?
- [ ] Vidíme retrieved documents?
- [ ] Vidíme tool calls?
- [ ] Vidíme retry a chyby?
- [ ] Nelogujeme zbytečně citlivý obsah?

Agentní debugging bez trace je hádání.

## F.11 Evals

- [ ] Máme reprezentativní test set?
- [ ] Obsahuje běžné i edge cases?
- [ ] Obsahuje missing-data případy?
- [ ] Obsahuje conflicting-data případy?
- [ ] Obsahuje security / injection testy?
- [ ] Máme ground truth nebo rubric?
- [ ] Měříme end-to-end success?
- [ ] Měříme false positive / false negative tam, kde jsou důležité?
- [ ] Měříme cost a latency?

## F.12 Failure handling

- [ ] Co se stane při chybě modelu?
- [ ] Co se stane při timeoutu toolu?
- [ ] Co se stane při nedostupném zdroji?
- [ ] Je retry bezpečný?
- [ ] Existuje fallback model nebo deterministic path?
- [ ] Existuje stav `UNKNOWN` místo vymyšlené odpovědi?
- [ ] Umí systém bezpečně skončit bez výsledku?

## F.13 Security

- [ ] Testujeme direct prompt injection?
- [ ] Testujeme indirect injection z dokumentů nebo webu?
- [ ] Jsou secrets mimo model context?
- [ ] Tool policy je vynucená mimo prompt?
- [ ] Agent běží v sandboxu tam, kde je to možné?
- [ ] Má omezený network egress?
- [ ] Je možné systém rychle vypnout?

## F.14 Ekonomika

- [ ] Kolik jedna úloha stojí?
- [ ] Kolik lidského času šetří?
- [ ] Jaká je cena lidské kontroly?
- [ ] Jaký je očekávaný volume?
- [ ] Jak se změní TCO při 10× vyšším využití?
- [ ] Je dražší model skutečně o tolik lepší na našem test setu?

## F.15 Production readiness

Před produkcí bych chtěl mít odpověď **ano** minimálně na toto:

1. [ ] Use-case je přesně definovaný.
2. [ ] Máme baseline.
3. [ ] Máme eval set.
4. [ ] Oprávnění jsou minimální.
5. [ ] Výstup se ověřuje.
6. [ ] Kritické akce mají approval.
7. [ ] Každý run je auditovatelný.
8. [ ] Failure mode je bezpečný.
9. [ ] Máme rollback / kill switch.
10. [ ] Známe provozní cenu.

Pokud některá odpověď zní „nevím“, není to automaticky zákaz projektu. Je to konkrétní položka, kterou máme vyřešit před zvýšením autonomie.