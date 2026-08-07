from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "book"
DST = ROOT / "book_gemini"


def read(rel: str) -> str:
    return (DST / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    p = DST / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Marker not found: {label}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, new_body: str, label: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    m = pattern.search(text)
    if not m:
        raise RuntimeError(f"Section not found: {label}")
    return text[: m.start()] + new_body.rstrip() + "\n\n" + end + text[m.end() :]


def add_snapshot_after_h1(rel: str) -> None:
    text = read(rel)
    if "**[Snapshot 08/2026]**" in text:
        return
    m = re.search(r"(^# .+$)", text, flags=re.M)
    if not m:
        raise RuntimeError(f"H1 not found in {rel}")
    text = text[: m.end()] + "\n\n**[Snapshot 08/2026]**" + text[m.end() :]
    write(rel, text)


# Build a clean alternative manuscript. The old proof is deliberately excluded:
# it corresponds to book/, not to this revised variant.
if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns("proof"))

# -----------------------------------------------------------------------------
# 01 — history: explicitly separate perceptron, backprop and Transformer.
# -----------------------------------------------------------------------------
p = "01 - Sto let vývoje AI na několika stránkách.md"
t = read(p)
new_1958 = r'''### 1958 — Rosenblattův perceptron: učení, ale jen lineární hranice

Frank Rosenblatt představil perceptron, jeden z prvních prakticky známých učících se neuronových modelů. Parametry nebyly pouze ručně napsaná pravidla; systém je dokázal upravovat podle příkladů.

Zásadní omezení je důležité říct přesně: klasický Rosenblattův perceptron byl **jednovrstvý lineární klasifikátor**. Uměl oddělit pouze lineárně separovatelné třídy. Problémy typu XOR proto jedním perceptronem vyřešit nešlo. Marvin Minsky a Seymour Papert tato omezení v roce 1969 systematicky analyzovali; pozdější popularizace někdy jejich knihu zjednodušuje na tvrzení, že „zastavila neuronové sítě“, ale technické jádro problému bylo omezení tehdejších architektur a metod učení.

Praktický mentální model:

```text
PERCEPTRON 1958
vstupy → váhy → součet → práh → výstup

umí se naučit lineární rozhodovací hranici
neumí obecně naučit vícevrstvou nelineární reprezentaci
```

To je důležitý rozdíl proti dnešnímu Deep Learningu. Myšlenka učení z dat byla správná; chyběla dostatečně schopná vícevrstvá architektura, efektivní způsob trénování, data a výpočetní výkon.
'''
t = replace_section(t, "### 1958 — perceptron", "---\n\n## 1.2 První velké nadšení", new_1958, "chapter 1 perceptron")
new_2017 = r'''### 2017 — Transformer: Self-Attention mění práci se sekvencemi

Práce *Attention Is All You Need* představila architekturu **Transformer**. Její klíčovou inovací pro tento příběh byl mechanismus **self-attention**, který umožňuje přímo modelovat vztahy mezi tokeny v celé zpracovávané sekvenci a dobře paralelizovat trénování na moderním hardware.

Je důležité neplést dvě různé věci:

```text
BACKPROPAGATION
→ způsob, jak při trénování počítat gradienty a upravovat parametry

SELF-ATTENTION / TRANSFORMER
→ architektura a mechanismus, jak model zpracovává vztahy v sekvenci
```

Transformer tedy v roce 2017 „nevynalezl gradienty“ ani backpropagation. Ty byly pro vícevrstvé neuronové sítě zásadní už desítky let předtím. Transformer změnil především **architekturu zpracování sekvencí a její škálovatelnost**.

```text
Transformer + self-attention
        ↓
efektivnější paralelní trénování sekvenčních modelů
        ↓
velké pre-trained language models
        ↓
dnešní LLM
```

Bez Transformeru by dnešní generace LLM pravděpodobně nevypadala tak, jak ji známe.
'''
t = replace_section(t, "### 2017 — Transformer", "---\n\n### 2018 — BERT", new_2017, "chapter 1 transformer")
write(p, t)

# -----------------------------------------------------------------------------
# 03 — Czech tokenization: useful but tokenizer-dependent, no fake universal ratio.
# -----------------------------------------------------------------------------
p = "03 - Jak funguje LLM - bez matematiky.md"
t = read(p)
marker = "U češtiny může být situace méně výhodná, protože čeština má mnoho tvarů slov a tokenizace je často rozděluje na více částí."
insert = marker + r'''

### Praktická poznámka pro češtinu

Čeština bývá proti angličtině **tokenově méně úsporná**. Skloňování, časování, diakritika a menší zastoupení češtiny v některých trénovacích korpusech znamenají, že tokenizer častěji rozděluje slovo na více subtokenů.

Není ale správné používat jedno univerzální číslo typu „české slovo = přesně 1,7 tokenu“. Poměr závisí na:

- konkrétním tokenizeru,
- typu textu,
- množství čísel a kódu,
- odborné terminologii,
- kombinaci češtiny a angličtiny.

Pro rychlé plánování je rozumné počítat s tím, že český text může spotřebovat **výrazně více tokenů na stejné množství slov než anglický text**; u slovanských jazyků se v měřeních různých tokenizerů často objevují hodnoty zhruba kolem dvou a více tokenů na slovo. Pro skutečný sizing ale text vždy změřme tokenizerem cílového modelu.

Praktický dopad:

```text
stejný dokument v češtině
→ často více tokenů
→ menší efektivní context window v počtu slov
→ vyšší API cost
→ delší prefill
```

Proto u českých firemních dokumentů sledujme **tokeny, ne pouze stránky nebo slova**.'''
t = replace_once(t, marker, insert, "chapter 3 Czech tokenization")
write(p, t)

# -----------------------------------------------------------------------------
# 05 — reasoning models / test-time compute.
# -----------------------------------------------------------------------------
p = "05 - Mapa modelů.md"
t = read(p)
new_reasoning = r'''## 5.4 Reasoning modely a test-time compute

Reasoning modely představují posun, který se výrazně prosadil od paradigmatu o1/o3 a jeho následovníků. Praktická myšlenka je jednoduchá: **složitější úloze lze při inference přidělit více výpočtu**.

Tomu se říká **test-time compute** nebo **inference-time compute**.

```text
jednoduchý požadavek
→ nízký reasoning effort
→ rychlá a levná odpověď

složitý návrh / důkaz / debugging
→ vyšší reasoning effort
→ více interních kroků a výpočtu
→ vyšší šance na kvalitní řešení
```

Někdy se používá analogie se „System 2 thinking“: pomalejší, deliberativnější způsob řešení problému místo okamžité intuitivní odpovědi. Je to **analogie pro chování systému**, ne tvrzení, že model uvažuje biologicky jako člověk.

Moderní reasoning model si pracovní postup řešení generuje interně. Z toho plyne praktické pravidlo pro prompting:

> **Nesnažme se model nutit do dlouhého ručně předepsaného Chain-of-Thought, pokud to konkrétní model nepotřebuje.**

Místo „přemýšlej krok za krokem a vypiš všechny úvahy“ je obvykle užitečnější dodat:

- přesný cíl,
- kvalitní evidence,
- omezení,
- požadovaný výstup,
- kritéria úspěchu,
- dostatečný reasoning budget.

Manuální rozklad úlohy má stále smysl tam, kde chceme **řídit workflow** — například nejprve načíst data, potom provést výpočet a nakonec verifikaci. To ale není totéž jako požadovat zveřejnění interního chain-of-thought.

Pro agentní systémy je nastavitelné inference effort velmi cenné:

```text
router
├── jednoduchá klasifikace → levný/rychlý režim
├── běžný tool decision     → střední reasoning
└── kritický technický krok → vysoký reasoning + verification
```

Důsledek: model nevybíráme jen podle názvu. V roce 2026 stále častěji vybíráme také **kolik výpočtu mu dovolíme spotřebovat pro konkrétní krok**.
'''
t = replace_section(t, "## 5.4 Reasoning modely", "## 5.5 Coding modely", new_reasoning, "chapter 5 reasoning")
write(p, t)
add_snapshot_after_h1(p)

# -----------------------------------------------------------------------------
# 08 — realistic VRAM sizing including KV cache.
# -----------------------------------------------------------------------------
p = "08 - Jak provozovat LLM lokálně.md"
t = read(p)
marker = "### KV cache"
insert = r'''### Praktický VRAM vzorec

Pro rychlý sizing nepoužívejme jen velikost souboru s vahami. U běžící inference potřebujeme minimálně:

```text
VRAM ≈ velikost vah po kvantizaci
     + KV cache podle délky kontextu a batch size
     + runtime buffers / pracovní paměť
     + provozní rezerva
```

Jako první plánovací odhad lze k vypočtenému workloadu přidat přibližně **10 % rezervu**, ale není to fyzikální konstanta. Některé runtime, architektury, multimodální modely nebo dlouhé contexty potřebují více.

Pro 70B dense model v Q4 jsou samotné teoretické váhy přibližně 35 GB a reálný modelový soubor bývá větší. Po přidání KV cache a runtime je **16 GB VRAM zcela nedostatečných pro plný GPU residency**; pro praktický provoz bez CPU offloadu počítej spíše s **48GB třídou GPU nebo větší**, podle kvantizace a kontextu. Na menší GPU lze někdy použít CPU/RAM offload, ale za cenu výrazně nižšího výkonu.

> **Nejdřív spočítej celý workload, teprve potom vybírej GPU.**

'''+marker
t = replace_once(t, marker, insert, "chapter 8 VRAM formula")
write(p, t)

# -----------------------------------------------------------------------------
# 09 — production prompt anatomy + correct structured-output guidance.
# -----------------------------------------------------------------------------
p = "09 - Prompting.md"
t = read(p)
marker = "## 9.3 Role"
insert = r'''## Anatomie produkčního promptu

U produkčního systému je užitečné přestat chápat prompt jako jednu větu. Reálný request se skládá z několika vrstev:

```text
┌──────────────────────────────────────────────┐
│ SYSTEM / DEVELOPER INSTRUCTIONS              │
│ role, pravidla aplikace, bezpečnostní hranice│
├──────────────────────────────────────────────┤
│ RUNTIME CONTEXT                              │
│ dokumenty, RAG, stav workflow, tool outputs  │
├──────────────────────────────────────────────┤
│ FEW-SHOT EXAMPLES (jen pokud pomáhají)       │
│ ukázky požadovaného chování / formátu        │
├──────────────────────────────────────────────┤
│ USER REQUEST                                 │
│ konkrétní cíl uživatele                      │
├──────────────────────────────────────────────┤
│ OUTPUT / FORMAT CONSTRAINT                   │
│ schema, JSON, tabulka, citace, limity        │
└──────────────────────────────────────────────┘
                         ↓
                        LLM
```

V agentním systému se k tomu přidává ještě seznam dostupných nástrojů, policy a success criteria. Praktické pravidlo:

> **Produkční prompt je sestavený kontext a kontrakt výstupu, ne pouze text uživatele.**

---

'''+marker
t = replace_once(t, marker, insert, "chapter 9 prompt anatomy")
marker2 = "Moderní API často umějí schema vynutit na úrovni rozhraní.\n\nTo je výrazně spolehlivější než pouze napsat do promptu:"
replacement2 = "Moderní API často umějí schema vynutit na úrovni rozhraní.\n\nPro striktní JSON/schema výstup je správný postup **structured output / constrained decoding + schema validation**. Nízká nebo nulová `temperature` může u podporovaných modelů snížit variabilitu, ale sama o sobě negarantuje validní JSON ani shodu se schématem. Pro produkci proto nespoléhejme na `temperature = 0` jako na validační mechanismus.\n\nTo je výrazně spolehlivější než pouze napsat do promptu:"
t = replace_once(t, marker2, replacement2, "chapter 9 structured output")
write(p, t)

# -----------------------------------------------------------------------------
# 11 — intentionally shortened bridge to RAG (~half the original length).
# -----------------------------------------------------------------------------
write("11 - Proč model nezná moje data.md", r'''---
title: "11. Proč model nezná moje data"
part: "VI — Data, RAG a druhý mozek"
status: final-draft
version: "0.5-gemini"
updated: 2026-08-07
---

# 11. Proč model nezná moje data

<!-- visual:11-external-data-bridge.svg -->

![Připojení modelu k vlastním datům](assets/diagrams/11-external-data-bridge.svg)

*Obrázek: Soukromá a aktuální data musí být do kontextu přivedena externí vrstvou.*

LLM může mít rozsáhlé obecné znalosti a současně neumět odpovědět na jednoduchou firemní otázku:

> „Co jsme minulý týden rozhodli o projektu ABC?“

Důvod je architektonický. Model automaticky nevidí naše soubory, e-maily, databáze ani poslední commit.

```text
ZNALOSTI V PARAMETRECH MODELU
≠
DATA DOSTUPNÁ SYSTÉMU PRÁVĚ TEĎ
```

Model může obecně znát bandgap reference, ale bez externího zdroje nezná naši topologii, aktuální PVT výsledky ani důvod poslední změny.

---

## 11.1 Tři typy informací, které musíme dodat zvenku

### Soukromá data

```text
specifikace
repozitář
meeting notes
měření
interní databáze
```

Model je nemá mít automaticky. Přístup musí řídit identita a oprávnění.

### Aktuální data

```text
dnešní e-mail
nový release
aktuální cena
poslední simulation run
```

Aktuálnost je vlastnost připojeného systému, ne samotných vah modelu.

### Přesná autoritativní data

I když informace existuje, musíme vědět, **které verzi věřit**:

```text
spec_rev_A.pdf
spec_rev_B.pdf
spec_FINAL_old.pdf
spec_current.pdf
```

Proto knowledge systém potřebuje metadata jako `revision`, `status`, `owner`, `valid_from` a `obsolete`.

> **Retrieval řeší „najdi informaci“. Governance řeší „které informaci smíme věřit“.**

---

## 11.2 Jak data připojit

Neexistuje jeden univerzální mechanismus.

| Typ potřeby | Vhodný mechanismus |
|---|---|
| jeden známý dokument | vložit relevantní část do kontextu |
| přesný identifikátor / fráze | full-text / keyword search |
| významové hledání ve velké dokumentaci | RAG / semantic retrieval |
| strukturovaná čísla | SQL / API / deterministický nástroj |
| aktuální stav systému | API / tool call |
| mnoho zdrojů a více kroků | agentní workflow |

To je důležité: **ne všechno má být RAG**. SQL databázi nepřevádíme automaticky na embeddings jen proto, že systém obsahuje LLM.

---

## 11.3 Proč obvykle netrénujeme model na každé nové dokumentaci

Pro často se měnící znalost nechceme při každé revizi znovu měnit váhy modelu.

```text
nová revize specifikace
→ aktualizovat zdroj / index
→ další dotaz už používá nová data
```

Fine-tuning může být užitečný pro chování, styl, formát nebo specializovanou schopnost. Pro živou firemní dokumentaci je ale obvykle vhodnější **externí zdroj + retrieval + LLM**.

---

## 11.4 Můstek k RAG

Pokud máme jeden dokument, můžeme jej vložit ručně. Pokud máme desetitisíce dokumentů, potřebujeme automaticky vybrat pouze relevantní části.

```text
OTÁZKA
   ↓
NAJÍT RELEVANTNÍ EVIDENCE
   ↓
VLOŽIT JE DO KONTEXTU
   ↓
LLM
   ↓
ODPOVĚĎ + ZDROJE
```

Tento vzor se jmenuje **RAG — Retrieval-Augmented Generation** a je tématem následující kapitoly.

## Co si z kapitoly odnést

1. **Model automaticky nezná naše soukromá ani nová data.**
2. **Obecná znalost modelu a pracovní data systému jsou dvě různé vrstvy.**
3. **Data připojujeme podle typu: kontext, search, RAG, databáze nebo tool.**
4. **Často se měnící dokumentaci obvykle neřešíme přetrénováním modelu.**
5. **Autorita zdroje, verze a oprávnění jsou stejně důležité jako samotný retrieval.**
''')

# -----------------------------------------------------------------------------
# 12 — explicit semantic vs lexical/full-text distinction.
# -----------------------------------------------------------------------------
p = "12 - RAG - Retrieval-Augmented Generation.md"
t = read(p)
marker = "## 12.9 Hybrid search"
insert = r'''## Praktické srovnání: vector search vs. full-text

Tyto dva mechanismy řeší jiný typ podobnosti:

| | Vector / semantic search | Full-text / inverted index |
|---|---|---|
| Hledá podle | významové podobnosti embeddingů | slov, tokenů, frází a jejich indexu |
| Silný pro | parafráze, synonyma, přirozený jazyk | ID, názvy signálů, přesné fráze, čísla |
| Typický dotaz | „problém při studeném startu“ | `REQ-1743`, `BG_TRIM[4:0]` |
| Slabina | může minout přesný symbol/ID | nemusí zachytit stejný význam jinými slovy |
| Výstup skóre | vektorová podobnost | lexical relevance / exact match |

Vector database tedy není „chytřejší náhrada databáze“. Je to infrastruktura optimalizovaná na práci s embeddingy a podobností. Full-text engine používá typicky **invertovaný index**, který přesně ví, ve kterých dokumentech se dané termy vyskytují.

Pro technická data proto často vyhrává kombinace obou metod.

---

'''+marker
t = replace_once(t, marker, insert, "chapter 12 search comparison")
write(p, t)

# -----------------------------------------------------------------------------
# 15 — make the USB-C analogy operationally precise.
# -----------------------------------------------------------------------------
p = "15 - MCP, skills, plugins a connectors.md"
t = read(p)
marker = "## 15.2 Co je MCP"
insert = r'''### Mentální model: vlastní ovladač vs. společný konektor

Praktická analogie:

```text
PŘÍMÁ TOOL INTEGRACE
AI aplikace → vlastní adaptér → konkrétní služba

MCP
AI aplikace → společný protokol → MCP server → konkrétní služba
```

Přímý Tool Use je podobný situaci, kdy pro každé zařízení píšeme vlastní ovladač přímo do každé aplikace. **MCP je společný standard podobný USB-C:** klient může standardním způsobem objevit připojené tools/resources a komunikovat s nimi.

Analogie má jednu důležitou hranici: USB-C také neodstraňuje elektroniku uvnitř zařízení. Stejně tak MCP neznamená, že není potřeba žádný adaptér. Pro konkrétní službu stále někdo musí vytvořit nebo provozovat **MCP server/wrapper**, který ji propojí s jejím API nebo lokálním rozhraním. Přínos je v tom, že tento adaptér není nutné znovu implementovat pro každou AI aplikaci.

```text
bez standardu: M aplikací × N služeb → mnoho unikátních integrací
s MCP:        M klientů + N serverů → sdílené rozhraní
```

---

'''+marker
t = replace_once(t, marker, insert, "chapter 15 analogy")
write(p, t)

# -----------------------------------------------------------------------------
# 16 + 17 — merged chapter. 17 is removed from the variant.
# -----------------------------------------------------------------------------
write("16 - Co je AI agent.md", r'''---
title: "16. Anatomie a smyčka AI agenta"
part: "VIII — Agentní AI"
status: final-draft
version: "0.5-gemini"
updated: 2026-08-07
---

# 16. Anatomie a smyčka AI agenta

<!-- visual:16-agent-anatomy.svg -->

![Anatomie AI agenta](assets/diagrams/16-agent-anatomy.svg)

*Obrázek: Agent je software kolem LLM: cíl, stav, nástroje, kontroly a smyčka.*

Slovo **agent** se používá velmi volně. Pro tuto knihu potřebujeme engineering definici:

> **AI agent je software, který dostane cíl, podle aktuálního stavu zvolí další krok, použije nástroj, pozoruje výsledek a proces opakuje, dokud cíl nesplní nebo nenastane podmínka pro bezpečné ukončení či eskalaci.**

```text
CHATBOT
vstup → LLM → odpověď

AGENT
cíl
 ↓
observe → reason/plan → act → verify
 ↑                         ↓
 └──────── nový stav ──────┘
```

Model není agent. Je rozhodovací komponenta uvnitř širšího software.

---

## 16.1 Anatomie agenta

Praktická rovnice:

```text
AGENT =
MODEL
+ INSTRUCTIONS / POLICY
+ TOOLS
+ STATE / MEMORY
+ CONTROL LOOP
+ VERIFICATION
+ STOP CONDITIONS
+ OBSERVABILITY
```

### Cíl

Cíl musí popsat hotový stav, ne pouze téma.

```text
špatně:
„Zabývej se LDO simulacemi.“

dobře:
„Ověř všechny DC parametry posledního LDO designu
přes specifikované PVT corners a vytvoř PASS/FAIL tabulku
s odkazem na limit a simulation run.“
```

### Nástroje

Akce mají být co nejužší:

```text
run_testbench(testbench, corner)
```

je bezpečnější než:

```text
execute_any_shell_command(command)
```

### Stav

Agent musí vědět, kde se nachází:

```json
{
  "goal": "fix failing unit test",
  "step": 6,
  "attempt": 2,
  "last_result": "FAIL",
  "modified_files": ["parser.py"]
}
```

Stav nemá být schovaný jen v dlouhé konverzaci. U produkčního workflow je lepší důležité položky držet explicitně a strukturovaně.

---

## 16.2 Jedna smyčka: Observe → Reason → Plan → Act → Verify

Různé frameworky používají různé názvy — ReAct, planner/executor, tool loop. Princip je stejný: rozhodnutí se musí uzavírat zpětnou vazbou z reálného výsledku.

### 1. Observe

Agent získá relevantní stav:

- výsledek testu,
- obsah souboru,
- odpověď API,
- simulation measurement,
- chybu nástroje.

Lepší tool output:

```json
{
  "status": "failed",
  "test": "test_parse_voltage",
  "error": "expected 1.8, got None"
}
```

než deset megabajtů neuspořádaného logu.

### 2. Reason

Model interpretuje evidence a navrhne další krok. Produkční systém nepotřebuje ukládat dlouhý proud interních úvah; potřebuje auditovatelný výsledek rozhodnutí:

```text
observed: parser returns None for input containing unit
hypothesis: unit handling is broken
next_action: inspect parse_voltage()
```

### 3. Plan

U delšího úkolu vznikne pracovní plán. Plán není neměnná smlouva:

```text
nová evidence → replan
```

Agentní výhoda je právě schopnost změnit cestu, když realita nepotvrdí původní hypotézu.

### 4. Act

Model navrhne tool call. Mezi modelem a skutečnou akcí má být klasický software:

```text
LLM decision
→ schema validation
→ authorization / policy
→ případný human approval
→ execute
```

LLM není poslední bezpečnostní autorita.

### 5. Verify

Úspěšný tool call není totéž jako úspěšný úkol.

```text
edit_file() returned success
≠
bug fixed
```

Správnost ověří například:

- test suite,
- compiler,
- simulator,
- schema validator,
- databázová constraint,
- měření.

> **Když lze správnost ověřit deterministicky, nenechávejme ji pouze na úsudku LLM.**

### 6. Repeat / Finish

FAIL se stane novým observation a smyčka pokračuje. PASS je konec pouze tehdy, když splňuje **celý success criteria set**, ne jeden vybraný parametr.

---

## 16.3 Agent vs. pevný workflow

```text
WORKFLOW
A → B → C → D
cestu určil programátor

AGENT
A → model vybere B/C/D podle stavu
```

Nejrobustnější produkční architektura bývá hybrid:

```text
pevný workflow
+
agentní rozhodování jen tam, kde je skutečně potřeba
```

Deterministicky nechme:

- oprávnění,
- schémata,
- výpočty, které umíme přesně naprogramovat,
- kritické safety gates.

Model použijme na:

- interpretaci nejasného vstupu,
- výběr strategie,
- syntézu více evidencí,
- rozhodnutí, který povolený nástroj použít.

---

## 16.4 Human-in-the-loop a approval gates

Člověk nemusí potvrzovat každý `read_file()`. Má vstoupit tam, kde nese rozhodnutí vysoké riziko nebo odpovědnost.

Typické approval gates:

```text
send_external_email()
merge_to_main()
production_write()
release_design()
financial_transaction()
```

Approval musí ukázat **co, proč a s jakým dopadem** agent navrhuje. Pouhé „Allow? Yes/No“ vede časem k bezmyšlenkovitému klikání.

---

## 16.5 Failure Modes: jak se agent rozbije

Agentní smyčka přidává chyby, které jednorázový chatbot nemá.

### Infinite loop

```text
search → nenalezeno → search jinými slovy
→ nenalezeno → search → ...
```

Pojistky:

- `max_steps`,
- wall-clock timeout,
- detekce opakovaného stavu nebo stejného tool callu,
- podmínka „po N neúspěších eskaluj člověku“.

### Runaway retries

Tool vrací `permission denied` a agent jej zkouší znovu.

```text
transient network error → omezený retry + backoff
invalid arguments       → jednou opravit argumenty
permission denied       → nerepeatovat, eskalovat
unknown destructive fail→ stop
```

### Budget explosion

Silný reasoning model + dlouhý context + desítky kroků může z jednoho úkolu udělat drahý run.

Pojistky:

```text
max model calls
max input/output tokens
max cost per run
max tool cost
reasoning budget by step
```

### Oscilace mezi dvěma akcemi

```text
A → B → A → B → A...
```

Systém má sledovat historii stavu a detekovat, že se nepřibližuje cíli.

### Side effects při opakování

Retry `read_file()` je jiný problém než retry `send_payment()`.

Write tools mají být podle možnosti:

- idempotentní,
- transakční,
- opatřené request/run ID,
- před nevratnou akcí schválené.

### Stop token není stop condition agenta

Stop token může ukončit **jednu generaci modelu**. Nezabrání orchestrátoru, aby model zavolal znovu. Bezpečné ukončení agentní smyčky proto musí řídit hostitelský software pomocí limitů, policy a explicitního stavu `DONE / STOP / ESCALATE`.

---

## 16.6 Logging a audit trail

Pro debugging logujme minimálně:

```text
run_id
timestamp
user / service identity
agent + model version
step
tool + arguments
result
latency
cost
status
```

Audit trail má navíc odpovědět:

```text
Kdo úkol inicioval?
Jaké zdroje agent četl?
Kdo schválil citlivou akci?
Co se skutečně změnilo?
```

Citlivý obsah se nemá bezmyšlenkovitě kopírovat do observability systému. Logujme identifikátory a redigované výstupy, pokud plný obsah není potřebný.

---

## 16.7 Praktický engineering příklad

```text
GOAL
ověřit startup přes PVT

OBSERVE
načti specification + testbenches

PLAN
vytvoř seznam required corners

ACT
run_simulation(...)

VERIFY
measurement vs. limit

REPEAT
všechny corners

GUARDRAILS
max_steps = 30
max_failed_runs = 3
budget = definovaný
production write = žádný

ESCALATE
chybí model / testbench / nejasná specifikace

FINISH
PASS/FAIL report + evidence + run IDs
```

To už není chatbot. Je to kontrolovaná uzavřená pracovní smyčka.

## Co si z kapitoly odnést

1. **Agent = software kolem modelu, ne samotný LLM.**
2. **Jádrem je uzavřená smyčka Observe → Reason/Plan → Act → Verify.**
3. **State, tools, stop conditions a verification jsou stejně důležité jako model.**
4. **Úspěšný tool call není důkaz úspěšného úkolu.**
5. **Produkční systémy kombinují deterministický workflow s agentní flexibilitou.**
6. **Infinite loops, runaway retries a budget explosion jsou normální engineering failure modes.**
7. **`max_steps`, timeout, budget guardrails, retry policy a repeated-state detection musí vynucovat hostitelský software.**
8. **Human approval patří k rizikovým a nevratným akcím.**
9. **Logging slouží debugování; audit trail prokazuje, kdo a co skutečně provedl.**

V další kapitole v pořadí přejdeme od anatomie k receptu: **jak postavit prvního jednoduchého agenta tak, aby byl užitečný, měřitelný a bezpečný.**
''')
(DST / "17 - Agentní smyčka.md").unlink(missing_ok=True)

# -----------------------------------------------------------------------------
# 22 — enterprise document practice, no re-teaching generic RAG.
# -----------------------------------------------------------------------------
p = "22 - AI nad dokumenty a firemními daty.md"
t = read(p)
marker = "---\n\n## 22.1 PDF"
insert = r'''---

## Od webového chatu k firemnímu systému

Webový chat je výborné rozhraní pro člověka, který ručně položí otázku a přečte odpověď. Firemní proces ale často potřebuje něco jiného:

```text
WEB CHAT
člověk ručně vloží data
→ model odpoví
→ člověk výsledek ručně přenese dál

API / SCRIPT / AGENT
identita + data source + strukturovaný vstup
→ model / nástroje
→ validovaný výstup
→ audit / další krok workflow
```

API nebo skript umožní zejména:

- opakovatelnost stejného procesu,
- batch zpracování,
- technicky vynucená oprávnění,
- structured output,
- přímé napojení na dokumentové zdroje a nástroje,
- logging, metriky a evals.

Proto „máme přístup k chatbota“ a „máme AI workflow nad firemními daty“ nejsou stejná capability.

Obecný princip chunkingu, embeddings, vector search a hybridního retrievalu už řeší kapitola 12. Tady se soustředíme na **to, co se pokazí při skutečném firemním nasazení**: parsing, OCR, tabulky, ACL, provenance, citlivá data a audit.

---

## 22.1 PDF'''
t = replace_once(t, marker, insert, "chapter 22 chat vs API")
t = t.replace("Chunking po jednotlivých zprávách je proto často špatný nápad.\n\nLepší jednotka může být:\n\n- thread,\n- časové okno,\n- topic cluster.", "Jednotku retrievalu řeší obecně kapitola 12. Pro chat je prakticky důležité zachovat konverzační celek; samostatná zpráva často bez okolního threadu nedává dostatečný význam. Vhodnou jednotkou může být thread, časové okno nebo topic cluster.")
marker2 = "# Doporučená architektura pro firemní dokumenty"
insert2 = r'''## 22.13 Permissioning: AI nesmí vytvořit nový boční vchod k datům

Nejčastější enterprise chyba není špatný embedding. Je to situace, kdy centrální AI index vidí více dokumentů než uživatel.

Správný princip:

```text
user / service identity
        ↓
authorization / ACL
        ↓
povolené zdroje a dokumenty
        ↓
retrieval / tool call
        ↓
LLM context
```

Permission check má proběhnout **předtím**, než se nepovolený obsah dostane do kontextu modelu. Nestačí vyhledat přes všechna data a doufat, že LLM tajnou pasáž „neprozradí“.

Prakticky je potřeba řešit:

- synchronizaci ACL ze zdrojového systému,
- group membership a změny rolí,
- odstranění obsahu z indexu po ztrátě přístupu,
- service accounts s minimálními právy,
- oddělení projektů a datových klasifikací.

## 22.14 OCR, citlivá data a audit ingestion pipeline

OCR a parsing nejsou jen quality problém. Jsou i security a audit problém.

Pipeline by měla zaznamenat:

```text
source_id
source_revision
parser/OCR version
ingestion timestamp
content hash
access policy
extracted tables/images
index version
```

U citlivých dat platí data minimisation: do modelového kontextu posílejme **jen evidence potřebná pro konkrétní úkol**, ne automaticky celý dokument nebo celý mailbox.

Dobrý audit umí zpětně odpovědět:

- jaký originální soubor byl použit,
- jakou měl revizi,
- kdo k němu měl přístup,
- jakým parserem prošel,
- které části byly vloženy do kontextu,
- jaký report z nich vznikl.

To je základ reprodukovatelného firemního AI systému.

---

'''+marker2
t = replace_once(t, marker2, insert2, "chapter 22 permissions")
write(p, t)

# -----------------------------------------------------------------------------
# 25 — strengthen defense-in-depth and transition after deleted chapter 26.
# -----------------------------------------------------------------------------
p = "25 - Bezpečnost AI.md"
t = read(p)
marker = "Prompt není security boundary."
replacement = r'''System prompt ani jiná textová instrukce **není neprolomitelná security boundary**. Je to důležitá behaviorální vrstva, ale prompt injection a nedůvěryhodný obsah mohou model ovlivnit. Proto potřebujeme defense-in-depth:

```text
input validation / sanitization
+ oddělení trusted instructions od untrusted content
+ nejmenší potřebný context
+ structured output validation
+ tool-call policy a allowlist
+ deterministic authorization
+ sandbox
+ output guardrails
+ explicitní human approval před kritickou akcí
+ audit
```

Ani input sanitization sama o sobě není kompletní obrana — útočná instrukce může vypadat jako legitimní text dokumentu. Rozhodující je, že **nedůvěryhodný text nikdy nesmí získat pravomoc měnit oprávnění nebo obejít policy layer**.'''
t = replace_once(t, marker, replacement, "chapter 25 prompt boundary")
old_end = "Další kapitola se přesune z technické bezpečnosti na strategickou otázku:\n\n> **Proč firma nemá AI strategii jen proto, že zaměstnancům zpřístupnila ChatGPT nebo jiný chatbot?**"
new_end = "Další kapitola v pořadí se přesune od bezpečnosti k zavádění AI do firmy:\n\n> **Jak poznat, zda jsou procesy, data, oprávnění a způsob měření vůbec připravené na praktické AI nasazení?**"
t = replace_once(t, old_end, new_end, "chapter 25 transition")
write(p, t)
(DST / "26 - Proč nestačí „máme ChatGPT“.md").unlink(missing_ok=True)

# -----------------------------------------------------------------------------
# 31 — concrete LLM-as-a-judge prompt.
# -----------------------------------------------------------------------------
p = "31 - Evaluace.md"
t = read(p)
new_judge = r'''## 31.6 LLM-as-a-judge

Jeden silnější model může hodnotit výstup jiného modelu tam, kde nestačí exact match nebo unit test. Typicky hodnotíme factual correctness, relevance, completeness a adherence to instructions.

Konkrétní hodnoticí prompt může vypadat takto:

```text
SYSTEM
Jsi nezávislý evaluator. Neopravuj odpověď a neodměňuj styl.
Hodnoť pouze podle REFERENCE a RUBRIC.
Pokud reference tvrzení nepodporuje, považuj je za unsupported.

QUESTION
{question}

REFERENCE / GROUND TRUTH
{reference}

CANDIDATE ANSWER
{answer}

RUBRIC
1. factual_correctness: 0–4
   4 = všechna podstatná tvrzení jsou správná a podložená
   2 = menší chyba nebo opomenutí
   0 = zásadní chyba / opačný závěr

2. relevance: 0–2
   2 = odpovídá přímo na otázku
   1 = částečně relevantní
   0 = mimo zadání

3. completeness: 0–2
   2 = pokrývá všechny povinné body
   1 = něco podstatného chybí
   0 = většina chybí

4. unsupported_claims: integer
   počet faktických tvrzení, která nelze doložit z REFERENCE

OUTPUT
Vrať pouze JSON podle tohoto schématu:
{
  "factual_correctness": 0,
  "relevance": 0,
  "completeness": 0,
  "unsupported_claims": 0,
  "verdict": "PASS|FAIL",
  "evidence": ["krátké odkazy na konkrétní problém"]
}
```

Produkčně je vhodné použít schema-constrained output, aby evaluator vždy vrátil strojově čitelný výsledek.

Judge není objektivní pravda. Může mít bias, preferovat určitý styl nebo dělat stejné chyby jako hodnocený model. Proto:

- kalibruj jeho score proti lidskému hodnocení,
- nesděluj mu zbytečně identitu výrobce/modelu, pokud by mohla hodnocení ovlivnit,
- pro kritická fakta preferuj deterministické ověření,
- pravidelně kontroluj disagreement cases.

Například na 100 případech porovnej:

```text
human rating
vs.
LLM judge rating
```

Teprve pokud judge dostatečně souhlasí s experty na našem use-case, použijme jej pro velké regression runs.
'''
t = replace_section(t, "## 31.6 LLM-as-a-judge", "## 31.7 Human evaluation", new_judge, "chapter 31 judge")
write(p, t)

# -----------------------------------------------------------------------------
# 32 — worked TCO comparison, explicitly illustrative snapshot.
# -----------------------------------------------------------------------------
p = "32 - Ekonomika AI.md"
t = read(p)
marker = "## 32.10 Kdy je dražší model ve skutečnosti levnější"
insert = r'''## 32.9.1 Konkrétní TCO příklad: API vs. dedicated GPU

**[Snapshot 08/2026 — ilustrativní model, nikoli ceník konkrétního poskytovatele.]**

Příklad slouží k postupu výpočtu. Před rozhodnutím dosaď aktuální ceny API, elektřiny, hardware a skutečný throughput vlastního modelu.

Předpokládejme 100 000 úloh za měsíc. Jedna úloha má průměrně:

```text
6 000 input tokenů
1 000 output tokenů
```

### Varianta A — cloud API

Ilustrativní ceny:

```text
input  = 2 EUR / 1M tokenů
output = 8 EUR / 1M tokenů
```

Měsíční tokeny:

```text
input:  100 000 × 6 000 = 600M
output: 100 000 × 1 000 = 100M
```

Model cost:

```text
600 × 2 EUR + 100 × 8 EUR
= 1 200 + 800
= 2 000 EUR / měsíc
```

Přidejme například 200 EUR za další placené API/tools:

```text
CLOUD VARIABLE COST ≈ 2 200 EUR / měsíc
```

### Varianta B — vlastní dedicated GPU server

Ilustrativní tříletý model:

```text
GPU server                  12 000 EUR / 36 měsíců = 333 EUR/měsíc
průměrná elektřina            100 EUR/měsíc
cooling / power overhead       30 EUR/měsíc
admin 4 h × 60 EUR            240 EUR/měsíc
maintenance reserve           100 EUR/měsíc
-------------------------------------------------------------
LOCAL TCO                    ≈ 803 EUR/měsíc
```

Na první pohled lokální varianta vyhrává. Tento závěr ale platí jen tehdy, když:

- server zvládne požadovaný throughput,
- lokální model má dostatečnou kvalitu,
- využití GPU je dost vysoké,
- nepotřebujeme další redundantní server,
- lidská korekce není kvůli slabšímu modelu dražší.

Proto porovnání dokončíme až takto:

```text
COST PER SUCCESSFUL TASK =
(total compute + tools + infra + admin + human correction)
/
počet skutečně úspěšně dokončených úloh
```

Například pokud cloud dosáhne 98 % success rate a lokální model jen 80 %, zdánlivá úspora GPU může zmizet v lidské opravě a retry.

Break-even tedy není univerzální počet tokenů. Je to průsečík konkrétního workloadu, utilization, kvality modelu a nákladů na chybu.

---

'''+marker
t = replace_once(t, marker, insert, "chapter 32 TCO example")
write(p, t)

# -----------------------------------------------------------------------------
# Visible snapshot labels for dynamic appendices.
# -----------------------------------------------------------------------------
add_snapshot_after_h1("appendices/B - Prehled modelu - snapshot 08-2026.md")
add_snapshot_after_h1("appendices/C - Prehled nastroju - snapshot 08-2026.md")

# -----------------------------------------------------------------------------
# INDEX: keep stable numbering, remove only merged/deleted files.
# -----------------------------------------------------------------------------
p = "00 - INDEX.md"
t = read(p)
t = t.replace('version: "0.4"', 'version: "0.5-gemini"', 1)
t = t.replace('status: release-candidate', 'status: review-variant', 1)
t = t.replace('> **Obsidian master index — v0.4**  \n> Verze 0.4 je release candidate po redakčním, obsahovém, vizuálním a proof auditu. Každá kapitola je samostatný Markdown soubor; společně s přílohami a bibliografií tvoří aktuální knižní rukopis.', '> **Obsidian review variant — v0.5-gemini**  \n> Alternativní revidovaná verze vytvořená nad release candidate `book/`. Původní rukopis zůstává beze změny; tato větev zapracovává Gemini review a následný technický fact-check.')
t = t.replace('- [[16 - Co je AI agent|16. Co je AI agent]]', '- [[16 - Co je AI agent|16. Anatomie a smyčka AI agenta]]')
t = t.replace('- [[17 - Agentní smyčka|17. Agentní smyčka]]\n', '')
t = t.replace('- [[26 - Proč nestačí „máme ChatGPT“|26. Proč nestačí „máme ChatGPT“]]\n', '')
t = t.replace('- [[FINAL_EDITORIAL_AUDIT_2026-08-07|Finální redakční audit]]', '- [[GEMINI_REVIEW_IMPLEMENTATION|Gemini review — zapracování a fact-check]]\n- [[FINAL_EDITORIAL_AUDIT_2026-08-07|Původní finální redakční audit]]')
write(p, t)

# Reader-facing note for the alternative copy.
write("README.md", r'''# book_gemini

Alternativní revidovaná varianta rukopisu vytvořená z `book/` podle Gemini review.

- `book/` zůstává původním release candidate.
- `book_gemini/` je srovnávací review varianta.
- Kapitoly 16 a 17 jsou sloučeny do kapitoly 16.
- Kapitola 26 byla odstraněna; její praktická myšlenka web chat vs. API/script byla přesunuta do kapitoly 22.
- Číslování ostatních kapitol se záměrně nemění, aby nevznikla lavina rozbitých referencí.
- Původní proof PDF nebyl kopírován, protože po obsahových změnách by byl zastaralý.

Začni souborem [[00 - INDEX]].
''')

write("GEMINI_REVIEW_IMPLEMENTATION.md", r'''# Gemini review — zapracování a fact-check

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
''')

# -----------------------------------------------------------------------------
# Final automated controls.
# -----------------------------------------------------------------------------
assert not (DST / "17 - Agentní smyčka.md").exists(), "Chapter 17 must be removed"
assert not (DST / "26 - Proč nestačí „máme ChatGPT“.md").exists(), "Chapter 26 must be removed"
assert "16. Anatomie a smyčka AI agenta" in read("16 - Co je AI agent.md")
assert "## 16.5 Failure Modes" in read("16 - Co je AI agent.md")
assert "[Snapshot 08/2026]" in read("appendices/B - Prehled modelu - snapshot 08-2026.md")
assert "[Snapshot 08/2026]" in read("appendices/C - Prehled nastroju - snapshot 08-2026.md")
assert "[[17 - Agentní smyčka" not in read("00 - INDEX.md")
assert "[[26 - Proč nestačí" not in read("00 - INDEX.md")

# Check all reader manuscript markdown for stale direct references to removed chapter files.
stale = []
for f in DST.glob("*.md"):
    if f.name.startswith(("FINAL_", "PREPRESS_")):
        continue
    s = f.read_text(encoding="utf-8")
    if "[[17 - Agentní smyčka" in s or "[[26 - Proč nestačí" in s:
        stale.append(f.name)
if stale:
    raise RuntimeError(f"Stale links to removed chapters: {stale}")

# Placeholder guard.
placeholders = []
for f in list(DST.glob("*.md")) + list((DST / "appendices").glob("*.md")):
    s = f.read_text(encoding="utf-8")
    if "[DOPLNIT]" in s or "TODO:" in s:
        placeholders.append(f.name)
if placeholders:
    raise RuntimeError(f"Placeholders found: {placeholders}")

print("book_gemini build: PASS")
print("chapter 17: removed")
print("chapter 26: removed")
print("chapter 16: merged")
print("snapshot B/C: present")
print("stale removed-chapter wiki links: 0")
print("placeholders: 0")
