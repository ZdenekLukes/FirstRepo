---
title: "16. Co je AI agent"
part: "VIII — Agentní AI"
status: final-draft
version: "0.2"
updated: 2026-08-07
---

# 16. Co je AI agent

<!-- visual:16-agent-anatomy.svg -->

![Anatomie AI agenta](assets/diagrams/16-agent-anatomy.svg)

*Obrázek: Agent je software kolem LLM: cíl, stav, nástroje, kontroly a smyčka.*


Slovo **agent** se v roce 2026 používá téměř všude.

Někdy označuje skutečný autonomnější systém.

Jindy je to pouze nový název pro chatbot s několika tlačítky.

Proto potřebujeme jednoduchou praktickou definici.

> **AI agent je software, který dostane cíl, dokáže podle situace vybrat další krok, použít nástroje, pozorovat výsledek a pokračovat, dokud úkol nedokončí nebo nenarazí na podmínku, kdy má skončit.**

Nejdůležitější slovo je zde **smyčka**.

Chatbot typicky funguje:

```text
vstup
 ↓
LLM
 ↓
odpověď
```

Agent:

```text
cíl
 ↓
LLM rozhodne další krok
 ↓
akce
 ↓
výsledek akce
 ↓
LLM rozhodne další krok
 ↓
...
 ↓
hotovo
```

Model tedy není celý agent.

Je jednou z jeho komponent.

---

## 16.1 Chatbot vs. agent

Představme si jednoduchou otázku:

> „Jak bych měl opravit tuto chybu v Pythonu?“

Chatbot může:

1. přečíst vložený kód,
2. vysvětlit příčinu,
3. navrhnout změnu.

Tím práce končí.

Coding agent může:

1. otevřít repository,
2. najít relevantní soubor,
3. přečíst okolní kód,
4. upravit soubor,
5. spustit test,
6. přečíst chybu,
7. změnu opravit,
8. znovu spustit test,
9. vytvořit diff.

Rozdíl není pouze ve „vyšší inteligenci“.

Rozdíl je v architektuře.

```text
CHATBOT
model + conversation

AGENT
model + tools + state + loop + control logic
```

To je velmi důležitý mentální model.

---

## 16.2 LLM + instrukce + nástroje + stav + smyčka

Jednoduchého agenta můžeme popsat rovnicí bez matematiky:

```text
AGENT =
LLM
+
instrukce
+
nástroje
+
stav
+
smyčka
+
pravidla ukončení
```

### LLM

Rozumí zadání a rozhoduje o dalším kroku.

### Instrukce

Určují roli, omezení a způsob práce.

### Nástroje

Umožňují agentovi něco zjistit nebo vykonat.

### Stav

Obsahuje informace o tom, kde se workflow právě nachází.

Například:

```json
{
  "goal": "fix failing unit test",
  "attempt": 2,
  "last_test": "FAIL",
  "modified_files": ["parser.py"]
}
```

### Smyčka

Po každém kroku agent znovu vyhodnotí situaci.

### Pravidla ukončení

Určují, kdy práce skončila nebo musí přejít na člověka.

Pokud některá z těchto částí chybí, systém může stále působit agentně, ale bude omezenější.

---

## 16.3 Cíl

Agent potřebuje cíl.

Ne pouze téma.

Špatně:

```text
Zabývej se simulacemi LDO.
```

Lépe:

```text
Ověř, zda poslední LDO design splňuje všechny DC parametry
ve specifikovaných PVT corners, a vytvoř tabulku PASS/FAIL.
```

Cíl by měl obsahovat něco, podle čeho agent pozná úspěch.

Například:

```text
DONE WHEN:
- byly spuštěny všechny požadované corners
- každý parametr má výsledek
- FAIL má zdroj limitu
- report je uložen
```

Bez jasného cíle může agent pokračovat zbytečně dlouho nebo skončit příliš brzy.

---

## 16.4 Plán

U složitějšího úkolu může agent vytvořit plán.

Například:

```text
CÍL:
porovnat dvě revize technické specifikace

PLÁN:
1. najít obě revize
2. ověřit jejich metadata
3. extrahovat requirement sections
4. porovnat hodnoty
5. identifikovat přidané a odstraněné požadavky
6. vytvořit report
```

Plán nemusí být vždy explicitně vypsaný uživateli.

Důležité je, že systém dokáže složitý cíl rozdělit na menší kroky.

Ale příliš rigidní plán může být také problém.

Po třetím kroku může agent zjistit něco, co původní plán mění.

Proto je často lepší:

```text
plán
↓
provedení kroku
↓
nová informace
↓
aktualizovaný plán
```

Agentní plánování je dynamické.

---

## 16.5 Akce

Akce je konkrétní krok ve světě.

Může být pouze čtecí:

```text
read_file()
search_documents()
query_database()
```

nebo zapisovací:

```text
edit_file()
create_ticket()
send_email()
```

Akce může být také dlouhotrvající:

```text
run_simulation()
compile_project()
execute_test_suite()
```

Dobrý agent má co nejmenší, dobře definovaný action surface.

Například pro verifikace agenta je lepší:

```text
run_testbench(testbench, corner)
```

než:

```text
execute_any_shell_command(command)
```

První nástroj je omezenější.

A právě proto bezpečnější.

---

## 16.6 Pozorování výsledku

Po akci musí agent získat výsledek.

Například:

```text
ACTION:
run_simulation("startup", "SS_-40C")

OBSERVATION:
status = completed
startup_time = 147 µs
```

Toto pozorování se vrátí do pracovního kontextu.

Model jej musí interpretovat.

Například:

```text
limit = 120 µs
measured = 147 µs
→ FAIL
```

Agentní systém bez spolehlivé zpětné vazby je velmi nebezpečný.

Pokud agent neví, zda předchozí akce uspěla, může pokračovat na základě falešného předpokladu.

Proto má tool output ideálně jasnou strukturu:

```json
{
  "status": "success",
  "run_id": "2041",
  "startup_us": 147.0
}
```

Ne pouze dlouhý neformátovaný log.

---

## 16.7 Další krok

Po každém pozorování agent rozhodne:

```text
Co mám udělat teď?
```

Možnosti mohou být například:

- pokračovat podle plánu,
- zopakovat krok,
- použít jiný nástroj,
- změnit plán,
- požádat člověka,
- skončit.

Například:

```text
startup FAIL
   ↓
agent zjistí, že jeden corner nesplňuje limit
   ↓
spustí sousední temperature points
   ↓
zjistí trend
   ↓
vytvoří doporučení pro designera
```

Tato adaptivita je hlavní rozdíl proti pevnému workflow.

Klasický script udělá přesně to, co jsme naprogramovali.

Agent může podle výsledků volit další cestu.

---

## 16.8 Kdy agent skončí

Agent potřebuje jasné stop conditions.

Jinak může vzniknout:

```text
search
→ search
→ search
→ další search
→ další úvaha
→ další search
```

bez skutečného dokončení.

Typické podmínky ukončení:

### Cíl splněn

```text
všechny tests completed
report generated
```

### Limit kroků

```text
max_steps = 20
```

### Limit ceny

```text
budget exceeded
```

### Limit času

```text
timeout
```

### Opakovaná chyba

```text
3× stejný failure
→ escalate
```

### Nutný lidský vstup

```text
chybí specification decision
→ ask human
```

Dobrý agent ví nejen, jak pokračovat.

Musí také vědět, **kdy nepokračovat**.

---

## 16.9 Agent není magie

Agent může působit mnohem inteligentněji než samotný model.

Ale pod kapotou je stále software.

Příklad velmi jednoduché smyčky:

```text
while not done:
    context = build_context(state)
    decision = llm(context)
    action = validate(decision)
    result = execute(action)
    state = update(state, result)
```

Kolem toho potřebujeme klasický engineering:

- datové struktury,
- API,
- retry,
- timeouts,
- oprávnění,
- logging,
- monitoring,
- testy.

LLM řeší části, které jsou obtížně programovatelné pevnými pravidly.

Není náhradou všech pravidel.

> **Dobrý agent kombinuje flexibilitu LLM s determinismem klasického software.**

---

## 16.10 Agent jako software s LLM uvnitř

Toto je možná nejdůležitější pohled celé části o agentech.

Marketing často prezentuje agenta jako autonomní digitální bytost.

Engineering pohled je praktičtější:

```text
              AGENT APPLICATION

┌───────────────────────────────────────┐
│ policy / permissions                  │
│                                       │
│             LLM                       │
│              ↓                        │
│ planner / decision logic              │
│              ↓                        │
│ tools / APIs                          │
│              ↓                        │
│ state / memory                        │
│              ↓                        │
│ verification                          │
│              ↓                        │
│ logs / observability                  │
└───────────────────────────────────────┘
```

LLM je velmi důležitý.

Ale spolehlivost systému závisí stejně tak na všem kolem něj.

Proto výměna modelu:

```text
Model A → Model B
```

nemusí opravit špatně navrženého agenta.

Pokud agent:

- dostává špatný context,
- má příliš široká oprávnění,
- nemá stop condition,
- neověřuje výsledky,

silnější model problém pouze částečně zamaskuje.

---

## Agent vs. workflow

Je užitečné si už teď uvědomit rozdíl.

### Workflow

Cestu určil programátor:

```text
A → B → C → D
```

### Agent

Programátor definuje prostor možností a model volí cestu:

```text
A
↓
LLM rozhodne
├→ B
├→ C
└→ D
```

Mnoho nejlepších produkčních systémů kombinuje obojí:

```text
pevný workflow
+
agentní rozhodování pouze tam, kde je potřebné
```

To je bezpečnější a lépe testovatelné než úplná autonomie.

---

## Co si z kapitoly odnést

1. **Agent není synonymum pro LLM nebo chatbot.**
2. **Základem agenta je smyčka: rozhodnutí → akce → pozorování → další rozhodnutí.**
3. **Agent potřebuje cíl, nástroje, stav a stop conditions.**
4. **Plán může být dynamický a měnit se podle výsledků.**
5. **Tool outputs musí být co nejvíce strukturované a ověřitelné.**
6. **Agent musí umět nejen pokračovat, ale také bezpečně skončit nebo eskalovat problém.**
7. **Agent je software s LLM uvnitř, ne magická autonomní bytost.**
8. **Nejrobustnější systémy kombinují deterministický workflow s agentní flexibilitou.**

V další kapitole rozebereme samotnou agentní smyčku podrobněji:

> **Observe → Reason → Plan → Act → Verify → Repeat.**
