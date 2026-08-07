---
title: "E. Bezpečnostní checklist"
part: "PŘÍLOHY"
status: final-draft
version: "0.4"
updated: 2026-08-07
---

# E. Bezpečnostní checklist

Tento checklist je určený pro návrh a review AI systému před pilotem a před produkčním nasazením. Není náhradou právního, bezpečnostního ani privacy review.

## E.1 Data classification

- [ ] Víme, jaké datové třídy systém zpracovává: PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED?
- [ ] Víme, zda vstupy obsahují osobní údaje, obchodní tajemství, source code nebo zákaznická data?
- [ ] Má každý datový zdroj vlastníka a autoritativní verzi?
- [ ] Je retrieval filtrován podle identity uživatele, ne jen relevance?
- [ ] Systém neposílá modelu více dat, než úloha potřebuje?
- [ ] Je jasné, co se smí ukládat do memory a co ne?

## E.2 Cloud policy

- [ ] Je schválen konkrétní provider **a konkrétní produkt / tarif**?
- [ ] Známe aktuální podmínky pro training on customer data?
- [ ] Známe retention policy?
- [ ] Víme, kde jsou data zpracována a zda se používají subprocessors?
- [ ] Existuje DPA nebo jiný potřebný smluvní rámec?
- [ ] Máme pravidla, která data smějí do cloudu a která musí zůstat lokálně?
- [ ] Je cloud fallback explicitní, nebo může aplikace nepozorovaně přepnout provider?

## E.3 GDPR / personal data

- [ ] Má zpracování osobních údajů jasný účel a právní základ?
- [ ] Uplatňujeme data minimisation?
- [ ] Máme definovanou retention a deletion policy?
- [ ] Víme, komu se data zpřístupňují?
- [ ] Jsou logy a traces zahrnuté do privacy posouzení?
- [ ] Je jasné, jak se řeší práva subjektů údajů, pokud jsou relevantní?
- [ ] Pokud systém provádí nebo podporuje automatizované rozhodování s významným dopadem, proběhlo odpovídající právní/privacy review?

## E.4 EU AI Act / governance

- [ ] Víme, zda jsme v daném use-case provider, deployer nebo obojí?
- [ ] Má systém definovaný účel a vlastníka?
- [ ] Máme risk classification use-case, ne pouze modelu?
- [ ] Je zajištěná AI literacy lidí, kteří systém používají nebo provozují?
- [ ] Pokud se na systém vztahují transparency obligations, jsou implementovány?
- [ ] U high-impact use-cases je dokumentovaná human oversight, logging a evidence?
- [ ] Máme proces pro změny modelu nebo workflow, které mohou změnit risk profile?

## E.5 Model policy

- [ ] Evidujeme přesný název a verzi modelu?
- [ ] U open-weight modelu známe původ, licenci a hash?
- [ ] Je model schválen pro příslušnou datovou třídu?
- [ ] Máme eval set pro náš use-case?
- [ ] Je definováno, co se stane po automatickém nebo ručním upgrade modelu?
- [ ] Umíme se vrátit na předchozí verzi?

## E.6 Tool oprávnění

Pro každý tool:

- [ ] Je jasné, co smí číst?
- [ ] Je jasné, co smí zapisovat?
- [ ] Je scope omezený na konkrétní službu / adresář / projekt?
- [ ] Používá least privilege?
- [ ] Je možné oddělit READ a WRITE credentials?
- [ ] Existuje timeout?
- [ ] Existuje limit počtu volání?
- [ ] Má tool validaci argumentů?
- [ ] Je výstup toolu považován za data, ne automaticky za důvěryhodnou instrukci?

## E.7 Secrets

- [ ] Nejsou API keys, passwords nebo tokens přímo v promptu?
- [ ] Nejsou secrets ukládány do agent memory?
- [ ] Tool runtime může použít secret bez jeho zpřístupnění modelu?
- [ ] Jsou secrets rotovatelné?
- [ ] Jsou logy redigované?
- [ ] Nevrací chybová hláška omylem credential nebo celý environment?

## E.8 Prompt injection

- [ ] Rozlišujeme trusted instructions a untrusted content?
- [ ] Testujeme direct prompt injection?
- [ ] Testujeme indirect injection z PDF, webu, e-mailu a RAG dokumentů?
- [ ] Nemůže obsah dokumentu sám rozšířit oprávnění?
- [ ] Je tool policy vynucená mimo prompt?
- [ ] Umí agent zastavit a eskalovat nejasný konflikt instrukcí?

## E.9 Agent memory

- [ ] Je definováno, co se ukládá?
- [ ] Je u každé důležité položky provenance?
- [ ] Má informace timestamp / validity?
- [ ] Lze starou informaci nahradit bez ztráty historie?
- [ ] Jsou oprávnění aplikované i na memory retrieval?
- [ ] Testujeme memory poisoning?

## E.10 Human approval

Approval vyžaduj především pro:

- [ ] destructive write,
- [ ] production configuration change,
- [ ] publish / release,
- [ ] externí e-mail nebo veřejnou komunikaci,
- [ ] finanční transakci,
- [ ] změnu kritického engineering artefaktu,
- [ ] práci s vysokým právním nebo bezpečnostním dopadem.

U approval musí člověk vidět:

```text
co se má stát
proč
jaké zdroje byly použity
jaká data se změní
jak akci vrátit zpět
```

## E.11 Audit a observability

- [ ] Každý run má ID?
- [ ] Evidujeme model version?
- [ ] Evidujeme instruction / workflow version?
- [ ] Evidujeme tool calls a status?
- [ ] Je možné dohledat zdroje použitých faktů?
- [ ] Logujeme pouze data, která skutečně potřebujeme?
- [ ] Má audit trail chráněný přístup?
- [ ] Máme metriky latency, error rate a cost?

## E.12 External communication

- [ ] Agent nesmí sám odesílat data na libovolnou URL?
- [ ] Egress je omezený na schválené služby?
- [ ] U e-mailu / Slacku / ticketingu je jasné, zda AI vytváří draft, nebo skutečně publikuje?
- [ ] Je označeno, kdy uživatel komunikuje s AI, pokud je to podle use-case požadováno?
- [ ] Je řešeno označení AI-generated nebo manipulated content tam, kde to vyžadují pravidla?

## E.13 Production deployment

- [ ] Existuje owner systému?
- [ ] Existuje on-call nebo support path?
- [ ] Máme kill switch?
- [ ] Máme rollback?
- [ ] Máme rate limit?
- [ ] Máme budget / cost limit?
- [ ] Máme incident process?
- [ ] Máme regression eval před každým releasem?
- [ ] Máme periodické security review?

## E.14 Supply chain

- [ ] Dependencies jsou pinované?
- [ ] Container images mají důvěryhodný původ?
- [ ] Neumožňujeme libovolný remote code bez review?
- [ ] Model weights mají evidovaný source a hash, pokud je to možné?
- [ ] MCP servery / plugins procházejí stejným security review jako jiné integrace?
- [ ] Víme, kdo může instalovat nové tools nebo connectors?

## E.15 Minimální threat model

Před pilotem musí být možné jednou větou odpovědět:

1. Co chráníme?
2. Kdo může ovlivnit vstup?
3. Co agent může číst?
4. Co může měnit?
5. Kam může odeslat data?
6. Jaká secrets používá?
7. Co se stane při prompt injection?
8. Co vyžaduje approval?
9. Jak provedeme rollback?
10. Co bude v audit trailu?

> **Bezpečnost agentního systému není jeden filtr. Je to kombinace identity, datových oprávnění, tool policy, sandboxu, verifikace, approval a auditu.**