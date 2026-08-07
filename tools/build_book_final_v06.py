from __future__ import annotations

from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
CLAUDE = ROOT / "book_claude"
GEMINI = ROOT / "book_gemini"
OUT = ROOT / "book_final"
DATE = "2026-08-07"
VERSION = "0.6"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def chapter(root: Path, n: int) -> Path:
    xs = sorted(root.glob(f"{n:02d} - *.md"))
    if len(xs) != 1:
        raise RuntimeError(f"expected exactly one chapter {n} in {root}, got {xs}")
    return xs[0]


def replace_section(text: str, heading_prefix: str, new_body: str) -> str:
    pat = re.compile(rf"^(###+|##)\s+{re.escape(heading_prefix)}.*$", re.M)
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"heading not found: {heading_prefix}")
    level = len(m.group(1))
    tail = text[m.end():]
    nxt = re.search(rf"^#{{1,{level}}}\s+", tail, re.M)
    end = m.end() + (nxt.start() if nxt else len(tail))
    return text[:m.start()] + new_body.rstrip() + "\n\n" + text[end:].lstrip("\n")


def insert_before(text: str, marker: str, block: str) -> str:
    if marker not in text:
        raise RuntimeError(f"marker not found: {marker}")
    return text.replace(marker, block.rstrip() + "\n\n" + marker, 1)


def insert_before_summary(text: str, block: str) -> str:
    for marker in ("\n## Co si z kapitoly odnést", "\n# Co si z kapitoly odnést"):
        if marker in text:
            return text.replace(marker, "\n" + block.rstrip() + "\n" + marker, 1)
    raise RuntimeError("summary marker not found")


def normalize_metadata(text: str) -> str:
    if text.startswith("---\n"):
        text = re.sub(r'^version:\s*.*$', f'version: "{VERSION}"', text, count=1, flags=re.M)
        text = re.sub(r'^updated:\s*.*$', f'updated: {DATE}', text, count=1, flags=re.M)
        text = re.sub(r'^status:\s*.*$', 'status: final-draft', text, count=1, flags=re.M)
    return text


def add_snapshot_after_h1(text: str) -> str:
    if "**[Snapshot 08/2026]**" in text:
        return text
    m = re.search(r"^#\s+.+$", text, re.M)
    if not m:
        return text
    return text[:m.end()] + "\n\n**[Snapshot 08/2026]**" + text[m.end():]


if "--audit-only" not in sys.argv:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(CLAUDE, OUT)

    # Review-only material does not belong in reader-facing final source.
    for name in ("REVIEW_REPORT.md", "REVIEW_CHANGELOG.md"):
        p = OUT / name
        if p.exists():
            p.unlink()
    for d in (OUT / "review", OUT / "proof"):
        if d.exists():
            shutil.rmtree(d)

    # 01 — retain Claude compression, repair the historical chain precisely.
    p = chapter(OUT, 1)
    t = read(p)
    t = replace_section(t, "1958", '''### 1958 — perceptron: učení ano, ale jen lineární hranice

Frank Rosenblatt představil perceptron — učící se model, u něhož se váhy upravují podle příkladů. To byl zásadní posun proti čistě ručně napsaným pravidlům.

Je ale důležité nepřeskočit jeho limit: klasický perceptron byl **jednovrstvý lineární klasifikátor**. Uměl oddělit pouze lineárně separabilní třídy. Funkce typu XOR jednou lineární rozhodovací hranicí oddělit nelze.

Kniha Minskyho a Paperta *Perceptrons* (1969) tyto limity jednovrstvých perceptronů formálně rozebrala. Historicky bývá někdy zjednodušeně prezentována jako „konec neuronových sítí“; přesnější je říct, že ukázala zásadní omezení tehdejší architektury a tehdejších praktických metod učení.

Mentální model:

```text
jednovrstvý perceptron
→ umí lineární hranici
→ nestačí na obecné nelineární vztahy
```
''')
    t = replace_section(t, "1986", '''### 1986 — backpropagation a praktické učení vícevrstvých sítí

Vícevrstvá síť umí reprezentovat nelineární vztahy, ale potřebujeme efektivně zjistit, **které váhy v jednotlivých vrstvách změnit**.

Backpropagation nevznikla jediným článkem ani v jediném roce. Pro moderní deep learning je ale zásadní práce Rumelharta, Hintona a Williamse z roku 1986, která metodu výrazně popularizovala pro trénování vícevrstvých neuronových sítí.

Zjednodušeně:

```text
forward pass
→ predikce
→ chyba
→ backpropagation spočítá gradienty přes vrstvy
→ optimizer upraví váhy
```

Tady je skutečný most od omezeného perceptronu k prakticky trénovatelným vícevrstvým sítím.
''')
    t = replace_section(t, "2017", '''### 2017 — Transformer: self-attention mění architekturu, ne princip gradientního učení

Práce *Attention Is All You Need* představila architekturu **Transformer**. Její klíčová inovace pro práci se sekvencemi byla zejména **self-attention**: každý token může při vytváření své reprezentace vážit relevanci ostatních tokenů v kontextu.

Transformer tedy nepřinesl backpropagation. Model se stále trénuje gradientní optimalizací; Transformer změnil hlavně **architekturu, ve které se tyto parametry učí**.

```text
backpropagation
→ jak při tréninku spočítat vliv chyby na parametry

self-attention / Transformer
→ jak model uvnitř reprezentuje a propojuje tokeny
```

Toto rozlišení je důležité, protože odděluje **trénovací mechanismus** od **architektury modelu**.
''')
    write(p, t)

    # 03 — short Czech tokenization note; detailed operational advice lives in 9.
    p = chapter(OUT, 3)
    t = read(p)
    if "Praktická poznámka: čeština a tokeny" not in t:
        t = insert_before_summary(t, '''## Praktická poznámka: čeština a tokeny

Čeština bývá u řady tokenizerů tokenově méně úsporná než angličtina, protože skloňování, delší tvary slov a diakritika mohou vést k jinému dělení na subword tokeny. **Neexistuje ale univerzální konstanta typu „1 české slovo = 1,5–2 tokeny“ pro všechny modely.**

Praktický důsledek je jednoduchý: při návrhu ceny a context window počítej tokeny **tokenizerem konkrétního modelu**. Praktické dopady pro prompting a české dokumenty rozebírá kapitola 9.
''')
    write(p, t)

    # 05 — current Anthropic snapshot + test-time compute mental model.
    p = chapter(OUT, 5)
    t = read(p)
    t = replace_section(t, "Anthropic / Claude", '''### Anthropic / Claude

**[Snapshot 08/2026]** Anthropic má několik výkonových tříd, které není vhodné zjednodušovat na jednu lineární řadu:

- **Claude Fable 5** — nejvýkonnější obecně dostupný model Anthropic pro dlouhé a náročné knowledge/coding úlohy,
- **Claude Sonnet 5** — workhorse třída s velmi silným codingem, tool use a agentními workflow,
- **Claude Opus 4.8** — stále významný komplexní model; Anthropic jej používá i jako fallback pro část požadavků, které Fable 5 kvůli safeguardům nepřebírá.

Důležitá redakční oprava: **„Claude Opus 5“ není k datu tohoto snapshotu správný veřejný název modelu.** Číslo generace a produktová třída už nejsou vždy jedna jednoduchá osa.

Pro návrh systému z toho plyne stejné pravidlo jako u ostatních providerů: model vybíráme podle vlastních evalů, ceny, latence, dostupných nástrojů a bezpečnostního profilu — ne podle názvu.
''')
    if "### Reasoning modely a test-time compute" not in t:
        marker = "\n## 5.2"
        block = '''### Reasoning modely a test-time compute

Po paradigmatech typu o1/o3 se rozšířily modely, které mohou při inference dynamicky spotřebovat více výpočtu na těžší problém. Prakticky tomu říkejme **test-time compute** nebo inference-time reasoning budget.

```text
jednoduchá úloha
→ nízký reasoning effort
→ rychlejší a levnější odpověď

složitá úloha
→ vyšší reasoning effort
→ více interních kroků / tokenů / času
→ vyšší šance na správné řešení
```

Analogie se „System 2 thinking“ je užitečná jako mentální model, ne jako tvrzení, že model myslí stejně jako člověk.

U těchto modelů obvykle méně pomáhá nutit model promptem typu „vypiš celý Chain-of-Thought krok za krokem“. Lepší je zadat cíl, constraints, dostupná data, požadovaný důkaz/verifikaci a případně nastavit podporovaný **reasoning effort**. Hodnotíme výsledek a evidence, ne délku zobrazeného uvažování.
'''
        if marker in t:
            t = t.replace(marker, "\n" + block + marker, 1)
        else:
            t = insert_before_summary(t, block)
    write(p, t)

    # 08 — practical VRAM model including KV cache and 70B reality.
    p = chapter(OUT, 8)
    t = read(p)
    if "Praktický VRAM vzorec" not in t:
        t = insert_before_summary(t, '''## Praktický VRAM vzorec

Samotná velikost souboru s kvantizovanými vahami nestačí. Pro inference potřebujeme řádově počítat:

```text
VRAM ≈
velikost vah podle kvantizace
+ KV cache podle délky kontextu a batch size
+ runtime / workspace buffers
+ cca 10 % provozní rezerva
```

Těch **10 % je orientační rezerva**, nikoli fyzikální konstanta. Některé runtime a dlouhé kontexty potřebují více.

Praktický sanity check pro dense 70B model v Q4:

```text
samotné 4-bit váhy ≈ desítky GB
+ metadata / quant overhead
+ KV cache
+ runtime
```

**16 GB VRAM nestačí.** Pro rozumný single-GPU provoz berme **48 GB jako praktickou minimální třídu**, a pro dlouhý kontext nebo vyšší batch může být potřeba ještě více. Menší VRAM může model spustit jen pomocí CPU/RAM offloadu, ale to je jiný výkonový režim.
''')
    write(p, t)

    # 09 — keep Claude Czech box and add production prompt anatomy; no false temp=0 rule.
    p = chapter(OUT, 9)
    t = read(p)
    if "### Anatomie produkčního promptu" not in t:
        block = '''### Anatomie produkčního promptu

Produkční request není jedna kouzelná věta. Je to sestavený kontrakt:

```text
┌──────────────────────────────────────────────┐
│ SYSTEM / DEVELOPER INSTRUCTIONS              │
│ role, policy, hranice a pravidla aplikace    │
├──────────────────────────────────────────────┤
│ RUNTIME CONTEXT                              │
│ dokumenty, RAG, stav workflow, tool outputs  │
├──────────────────────────────────────────────┤
│ FEW-SHOT EXAMPLES — jen pokud pomáhají       │
│ ukázky kategorií, stylu nebo formátu         │
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

Pro striktní JSON se nespoléhej na `temperature = 0`. Nízká temperature může u některých modelů snížit variabilitu, ale **validitu má vynucovat structured output / constrained decoding a následná schema validation**. Některé nové API sampling parametry dokonce ignorují nebo deprecují.
'''
        if "\n## 9.3" in t:
            t = t.replace("\n## 9.3", "\n" + block + "\n## 9.3", 1)
        else:
            t = insert_before_summary(t, block)
    write(p, t)

    # 11 — Claude fine-tuning tree + Gemini three-information bridge.
    p = chapter(OUT, 11)
    t = read(p)
    if "## 11.0 Tři druhy informací" not in t:
        block = '''## 11.0 Tři druhy informací

Než zvolíme technologii, rozlišme tři problémy:

| Co potřebuji | Typický zdroj | Správný mechanismus |
|---|---|---|
| obecnou naučenou schopnost | parametry modelu | model / případně fine-tuning chování |
| moje soukromá nebo firemní fakta | dokumenty, DB, knowledge base | context / search / RAG / API |
| právě aktuální stav | dnešní e-mail, Git, web, měření | live tool / API / databáze |

Nejčastější chyba je řešit druhý nebo třetí řádek „větším modelem“. **Aktuálnost a přístup k vlastním datům jsou vlastnosti systému, ne samotných vah modelu.**
'''
        t = t.replace("\n## 11.1", "\n" + block + "\n## 11.1", 1)
    write(p, t)

    # 12 — explicit semantic vs lexical retrieval.
    p = chapter(OUT, 12)
    t = read(p)
    if "Vector search vs. full-text" not in t:
        block = '''### Vector search vs. full-text: dva různé signály

| Typ vyhledávání | Co porovnává | Silná stránka | Typický failure mode |
|---|---|---|---|
| lexical / full-text | přesná slova, termy, fráze | ID, názvy signálů, čísla, přesné formulace | mine synonymum nebo parafrázi |
| vector / semantic | podobnost významu embeddingů | parafráze, podobné koncepty, přirozený dotaz | může vrátit významově blízký, ale fakticky špatný dokument |

Pro technická a firemní data často vyhrává **hybrid search**: lexical signal + vector similarity + metadata filters + případný reranker.
'''
        if "\n## 12.1" in t:
            t = t.replace("\n## 12.1", "\n" + block + "\n## 12.1", 1)
        else:
            t = insert_before_summary(t, block)
    write(p, t)

    # 15 — precise USB-C analogy and current MCP snapshot.
    p = chapter(OUT, 15)
    t = read(p)
    if "USB-C" not in t[:7000]:
        block = '''### Mentální model: Tool Use vs. MCP

> **Tool Use je jako vlastní ovladač pro konkrétní zařízení. MCP je standardizovaný konektor a protokol — podobně jako USB-C — který sjednocuje, jak klient zjišťuje a používá schopnosti serveru.**

Analogie má limit: konkrétní služba stále potřebuje MCP server nebo wrapper nad svým API. MCP tedy neodstraňuje integrační práci; **standardizuje rozhraní**, takže klient nemusí pro každou integraci vymýšlet jiný protokol.

**[Snapshot 08/2026]** Specifikace MCP `2026-07-28` přešla na stateless protocol core, přidala explicitnější discovery/routing, cache hints, authorization hardening a formální extensions framework. Princip knihy ale zůstává stabilní: MCP je interoperabilní vrstva mezi AI aplikací a externími capabilities.
'''
        if "\n## 15.1" in t:
            t = t.replace("\n## 15.1", "\n" + block + "\n## 15.1", 1)
        else:
            t = insert_before_summary(t, block)
    write(p, t)

    # 16+17 — Gemini compact merge + selected Claude didactics.
    gem16 = read(chapter(GEMINI, 16))
    approval = '''### Jak má vypadat approval dialog

Approval gate nemá být pouze:

```text
Allow action? YES / NO
```

Člověk musí vidět, **co přesně schvaluje**:

```text
Agent chce změnit:
config/prod.yaml

max_current: 10 → 15

Důvod:
aktuální limit blokuje test X

Dopad:
produkční konfigurace

Rollback:
revert commit abc123

[Approve] [Reject]
```

Tím se z approval stává skutečná kontrola rizika, ne habituální kliknutí.
'''
    recovery = '''### Error-recovery policy musí být explicitní

| Typ chyby | Výchozí reakce |
|---|---|
| transient network / 5xx | omezený retry + backoff |
| invalid tool arguments | jednou opravit argumenty, pak eskalovat |
| permission denied | **nerepeatovat**, eskalovat |
| stejný failure N× | stop / human review |
| neznámá chyba u destruktivní akce | okamžitý stop |

Retry policy patří do hostitelského software. Agent nesmí zaměnit vytrvalost za nekonečné opakování stejné chyby.
'''
    gem16 = gem16.replace("## 16.5 Failure Modes: jak se agent rozbije", approval + "\n\n## 16.5 Failure Modes: jak se agent rozbije", 1)
    gem16 = gem16.replace("### Budget explosion", recovery + "\n\n### Budget explosion", 1)
    # Add the second loop diagram retained from Claude.
    loop_img = '''\n\n![Agentní smyčka](assets/diagrams/16-agent-loop.svg)\n\n*Obrázek: Observe → reason → plan → act → verify → repeat.*\n'''
    gem16 = gem16.replace("## 16.2 Jedna smyčka: Observe → Reason → Plan → Act → Verify", "## 16.2 Jedna smyčka: Observe → Reason → Plan → Act → Verify" + loop_img, 1)
    write(chapter(OUT, 16), gem16)
    chapter(OUT, 17).unlink()

    # 22 — use Gemini enterprise-focused chapter; 31/32 — Gemini practical artifacts.
    write(chapter(OUT, 22), read(chapter(GEMINI, 22)))
    write(chapter(OUT, 31), read(chapter(GEMINI, 31)))
    write(chapter(OUT, 32), read(chapter(GEMINI, 32)))

    # 25 — Claude dedup base + explicit defense in depth.
    p = chapter(OUT, 25)
    t = read(p)
    if "System prompt není security boundary" not in t:
        t = insert_before_summary(t, '''## System prompt není security boundary

System prompt je důležitá behaviorální instrukce, ale **není neprolomitelná bezpečnostní bariéra proti prompt injection**. Nedůvěryhodný dokument, web nebo tool output může obsahovat instrukci, která se pokusí změnit chování modelu.

Proto bezpečnost stavíme jako **defense in depth**:

```text
identity + least privilege
→ oddělení trusted / untrusted contextu
→ input / content filtering podle use-case
→ úzká tool schemas + policy engine
→ sandbox / transakční writes
→ output validation
→ human approval před kritickou nebo nevratnou akcí
→ audit + monitoring
```

Kritické pravidlo: **LLM může navrhnout akci; hostitelský software rozhoduje, zda je akce povolená.**
''')
    write(p, t)

    # 26 — preserve the management chapter, but point technical UI/API detail to 22.
    p = chapter(OUT, 26)
    t = read(p)
    if "Technický rozdíl webového chatu" not in t:
        note = '''\n> **Technický rozdíl webového chatu proti API/script/agent workflow řeší kapitola 22.** Tato kapitola jde o úroveň výš: proč individuální chatbot adoption ještě nevytváří firemní AI operating capability.\n'''
        t = t.replace("\n## 26.1", note + "\n## 26.1", 1)
    write(p, t)

    # Appendix B — fresh, fact-checked snapshot from primary vendor sources.
    b = OUT / "appendices" / "B - Prehled modelu - snapshot 08-2026.md"
    write(b, '''---
title: "B. Přehled modelů — snapshot 08/2026"
part: "PŘÍLOHY"
status: final-draft
version: "0.6"
updated: 2026-08-07
---

# B. Přehled modelů — snapshot 08/2026

**[Snapshot 08/2026]**

> **Snapshot k 7. 8. 2026.** Jde o mapu trhu, ne žebříček. Názvy, ceny, dostupnost i licence se mění rychle; před nasazením ověř primární zdroj výrobce.

## B.1 Frontier a cloudové rodiny

| Provider | Aktuální příklady | Typická role | Poznámka |
|---|---|---|---|
| OpenAI | GPT-5.6 Sol / Terra / Luna | frontier reasoning až high-throughput | Sol je flagship; Terra/Luna snižují cenu a latency podle workloadu |
| Anthropic | Claude Fable 5 / Sonnet 5 / Opus 4.8 | long-horizon, coding, agents, knowledge work | **nepoužívat neověřený název „Opus 5“**; Fable 5 je aktuální nejvýkonnější GA třída |
| Google | Gemini 3.1 Pro / 3.6 Flash / 3.5 Flash-Lite | complex reasoning, multimodal, agentic throughput | 3.6 Flash a 3.5 Flash-Lite jsou GA od 07/2026 |
| xAI / SpaceXAI | Grok 4.5 | coding, agentic tasks, knowledge work | snapshot 07/2026 |
| Cohere | Command A+ | enterprise, multilingual, RAG, sovereign deployment | open weights, **Apache 2.0**, 218B total / 25B active |

## B.2 Významné open-weight rodiny

| Rodina | Ověřený snapshot 08/2026 | Licence / poznámka |
|---|---|---|
| Qwen | Qwen3.6, včetně 35B-A3B MoE | open weights; konkrétní release vždy ověřit |
| DeepSeek | DeepSeek-V4 Pro / V4 Flash | API V4 od 24. 4. 2026; deployment/licenci kontrolovat podle release |
| Gemma | Gemma 4: E2B, E4B, 12B, 26B A4B, 31B | **Apache 2.0**, open weights |
| Mistral | Mistral Small 4 | **Apache 2.0**, reasoning + multimodal + agentic coding |
| Llama | aktuální Llama rodiny | vlastní licence; open-weight ≠ automaticky open-source licence |

## B.3 Specializované modely, které stojí za sledování

- **Cohere Rerank 4.0** — varianty Pro/Fast pro reranking.
- **Cohere Transcribe (`cohere-transcribe-03-2026`)** — 2B ASR, 14 jazyků, Apache 2.0.
- embedding modely, speech, image a video modely vybírej jako samostatné komponenty, ne jako přílepky k jednomu „hlavnímu LLM“.

## B.4 Praktické velikostní kategorie pro lokální AI

| Kategorie | Typické použití | Poznámka |
|---|---|---|
| velmi malé / edge | routing, klasifikace, function calling | vysoký throughput, omezenější reasoning |
| ~7B–14B | lokální chat, extraction, lehčí coding, RAG generation | často vhodná třída pro 16 GB VRAM v kvantizaci |
| ~20B–40B | náročnější workstation použití | typicky více VRAM / unified memory |
| ~70B dense | server / 48 GB+ praktická GPU třída v Q4 | dlouhý context a KV cache mohou potřebovat více |
| velké MoE | serverové nasazení | active parameters ≠ velikost všech vah v paměti |

## B.5 Primární zdroje snapshotu

- OpenAI GPT-5.6: https://openai.com/index/gpt-5-6/
- Anthropic Fable 5: https://www.anthropic.com/claude/fable
- Anthropic Sonnet 5: https://www.anthropic.com/news/claude-sonnet-5
- Anthropic Opus 4.8: https://www.anthropic.com/news/claude-opus-4-8
- Google Gemini API releases: https://ai.google.dev/gemini-api/docs/changelog
- Google Gemini 3.6 Flash: https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash
- xAI Grok 4.5: https://x.ai/news/grok-4-5
- DeepSeek API updates: https://api-docs.deepseek.com/updates
- Qwen3.6: https://qwen.ai/blog?id=qwen3.6-35b-a3b
- Gemma 4: https://ai.google.dev/gemma/docs/core/model_card_4
- Mistral Small 4: https://mistral.ai/news/mistral-small-4/
- Cohere Command A+: https://cohere.com/blog/command-a-plus
- Cohere Rerank / Transcribe: https://docs.cohere.com/v2/changelog

## B.6 Pravidlo aktualizace

Před každým dalším vydáním znovu fact-checkuj kapitolu 5 a tuto přílohu. Principy knihy mají stárnout pomalu; tento snapshot má stárnout přiznaně.
''')

    # Appendix C — explicit snapshot label.
    c = OUT / "appendices" / "C - Prehled nastroju - snapshot 08-2026.md"
    write(c, add_snapshot_after_h1(read(c)))

    # Appendix D — same VRAM mental model in the hardware reference.
    d = OUT / "appendices" / "D - Hardware sizing.md"
    dt = read(d)
    if "## D.1a Praktický VRAM rozpočet" not in dt:
        dt = dt.replace("\n## D.2 Context stojí paměť", '''\n## D.1a Praktický VRAM rozpočet

```text
VRAM ≈ weights podle quantizace
     + KV cache podle context length a batch size
     + runtime / workspace buffers
     + orientačně ~10 % provozní rezerva
```

Pro dense **70B Q4** nepočítej s 16 GB. Samotné váhy jsou v desítkách GB; po započtení overheadu, KV cache a runtime je **48 GB praktická minimální single-GPU třída**, nikoli garance pro každý dlouhý context.
'''+"\n## D.2 Context stojí paměť", 1)
    write(d, dt)

    # Appendix G — no invented benchmark numbers. Use known hardware facts and explicitly mark unmeasured metrics as such.
    g = OUT / "appendices" / "G - Vlastni experimenty.md"
    gt = read(g)
    new_g6 = '''## G.6 Dokumentované experimenty

### EXP-001 — Co změnila 8 GB → 32 GB VRAM

**Status:** pozorovací experiment; ne publikovaný výkonový benchmark  
**Otázka:** Jaký rozdíl je mezi modelem, který se „nějak spustí“, a lokálním AI stackem, který je prakticky použitelný?

**Hardware A:** notebook s NVIDIA RTX 4060, 8 GB VRAM  
**Hardware B:** workstation s Radeon AI PRO R9700, 32 GB VRAM  
**Pozorovaný workload:** textové LLM; na 32 GB také Open WebUI + Whisper speech-to-text + Kokoro text-to-speech  
**Velikostní třída modelů na 32 GB:** přibližně 30B–40B podle konkrétního modelu a kvantizace

#### Co je doloženo

| Pozorování | 8 GB VRAM | 32 GB VRAM |
|---|---|---|
| menší lokální LLM | prakticky použitelné | bez problému |
| větší modely | při spill/offload do RAM výrazně horší interaktivita | výrazně větší prostor pro 30B–40B třídu |
| více AI komponent současně | velmi omezené | LLM + UI + STT + TTS lze skládat do jednoho stacku |

#### Co **není** doloženo a proto to nevymýšlím

Původní experiment nebyl od začátku veden jako benchmark, takže nemáme konzistentně archivované:

- přesné model ID a quantization pro každý běh,
- TTFT,
- tokens/s,
- power draw,
- stejný eval set na obou GPU.

Proto z něj **nedělám číselné tvrzení o rychlosti**. Jeho validní závěr je architektonický:

> **Kapacita VRAM neurčuje jen maximální velikost modelu. Určuje, zda můžeme vedle vah držet KV cache a další komponenty a stále mít interaktivní systém.**

Další experiment už musí být navržený předem jako reprodukovatelný benchmark.

---
'''
    m = re.search(r"^## G\.6 Dokumentované experimenty.*?(?=^## G\.7 )", gt, re.M | re.S)
    if not m:
        raise RuntimeError("G.6/G.7 markers not found")
    gt = gt[:m.start()] + new_g6 + gt[m.end():]
    # Remove any historical placeholders elsewhere; do not invent values.
    gt = re.sub(r"\[DOPLNIT[^\]]*\]", "nezaznamenáno", gt)
    write(g, gt)

    # Current-source bibliography addendum.
    bib = OUT / "BIBLIOGRAPHY.md"
    bt = read(bib)
    if "## Snapshot 08/2026 — primární vendor zdroje" not in bt:
        bt += '''\n\n## Snapshot 08/2026 — primární vendor zdroje\n\n- OpenAI — GPT-5.6: https://openai.com/index/gpt-5-6/\n- Anthropic — Claude Fable 5: https://www.anthropic.com/claude/fable\n- Anthropic — Claude Sonnet 5: https://www.anthropic.com/news/claude-sonnet-5\n- Anthropic — Claude Opus 4.8: https://www.anthropic.com/news/claude-opus-4-8\n- Google — Gemini API changelog: https://ai.google.dev/gemini-api/docs/changelog\n- xAI — Grok 4.5: https://x.ai/news/grok-4-5\n- DeepSeek — API updates: https://api-docs.deepseek.com/updates\n- Qwen — Qwen3.6: https://qwen.ai/blog?id=qwen3.6-35b-a3b\n- Google — Gemma 4 model card: https://ai.google.dev/gemma/docs/core/model_card_4\n- Mistral — Small 4: https://mistral.ai/news/mistral-small-4/\n- Cohere — Command A+: https://cohere.com/blog/command-a-plus\n- Model Context Protocol — spec 2026-07-28: https://blog.modelcontextprotocol.io/posts/2026-07-28/\n'''
    write(bib, bt)

    # Preserve old chapter-17 loop art as a second image in merged chapter; then renumber chapter art.
    for sub in ("diagrams", "diagrams-print"):
        ad = OUT / "assets" / sub
        old_loop = ad / "17-agent-loop.svg"
        if old_loop.exists():
            old_loop.rename(ad / "16-agent-loop.svg")
        for old in range(18, 38):
            for src in sorted(ad.glob(f"{old:02d}-*.svg")):
                dst = ad / (f"{old-1:02d}-" + src.name[3:])
                if dst.exists():
                    raise RuntimeError(f"asset collision: {dst}")
                src.rename(dst)

    # Renumber chapter files 18→17 ... 37→36; chapter 26 is retained, so final count is 36.
    for old in range(18, 38):
        src = chapter(OUT, old)
        new = old - 1
        txt = read(src)
        txt = re.sub(rf'^(title:\s*["\']?){old}\.', rf'\g<1>{new}.', txt, count=1, flags=re.M)
        txt = re.sub(rf'^#\s+{old}\.', f'# {new}.', txt, count=1, flags=re.M)
        txt = re.sub(rf'^(###+|##)\s+{old}\.', lambda m: m.group(1) + f' {new}.', txt, flags=re.M)
        txt = txt.replace(f"visual:{old:02d}-", f"visual:{new:02d}-")
        dst = OUT / (f"{new:02d} - " + src.name.split(" - ", 1)[1])
        write(dst, txt)
        src.unlink()

    # Cross-reference and asset-prefix remapping without cascading replacements.
    chapter_map = {17: 16, **{old: old-1 for old in range(18, 38)}}
    for p in list(OUT.rglob("*.md")):
        txt = read(p)
        # Exact old agent-loop wiki target.
        txt = txt.replace("[[17 - Agentní smyčka", "[[16 - Co je AI agent")
        placeholders = {}
        idx = 0
        def protect(value: str) -> str:
            nonlocal idx
            key = f"@@CHREF{idx}@@"; idx += 1; placeholders[key] = value; return key
        for old, new in sorted(chapter_map.items(), reverse=True):
            txt = re.sub(rf'(?i)(kapitol(?:a|y|e|u|ou)\s+){old}\b', lambda m, n=new: m.group(1) + protect(str(n)), txt)
            txt = re.sub(rf'(?i)(kap\.\s*){old}\b', lambda m, n=new: m.group(1) + protect(str(n)), txt)
            txt = txt.replace(f"[[{old:02d} - ", f"[[{protect(f'{new:02d}')} - ")
        for key, val in placeholders.items():
            txt = txt.replace(key, val)
        # Asset paths only.
        def amap(m):
            num = int(m.group(2))
            if num == 17:
                return m.group(1) + "16-" if "agent-loop" in m.group(3) else m.group(0)
            if 18 <= num <= 37:
                return m.group(1) + f"{num-1:02d}-" + m.group(3)
            return m.group(0)
        txt = re.sub(r'(assets/(?:diagrams|diagrams-print)/)(\d{2})-(\S+?\.svg)', amap, txt)
        write(p, txt)

    # Add chapter 32 trends diagram after renumbering (old chapter 33).
    screen_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="620" viewBox="0 0 1200 620" role="img" aria-labelledby="title desc"><title id="title">Kam se AI posouvá: od modelu k ověřenému systému</title><desc id="desc">Pět trendů: adaptivní reasoning, multimodalita, levnější inference, nástroje a agentní workflow, vše směřuje k ověřenému AI systému.</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#5e7188"/></marker></defs><rect width="1200" height="620" rx="28" fill="#0b1220"/><text x="60" y="66" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="34" font-weight="700" fill="#eef6ff">Kam se AI posouvá</text><text x="60" y="100" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="18" fill="#a9bbcf">Ne jeden „chytřejší model“, ale systém s více compute, modalitami, nástroji a verifikací.</text><g font-family="Inter,Segoe UI,Arial,sans-serif"><rect x="60" y="170" width="190" height="120" rx="18" fill="#111c30" stroke="#45c7ff" stroke-width="2"/><text x="155" y="210" text-anchor="middle" font-size="21" font-weight="700" fill="#eef6ff">Reasoning</text><text x="155" y="242" text-anchor="middle" font-size="16" fill="#a9bbcf">adaptivní compute</text><rect x="285" y="170" width="190" height="120" rx="18" fill="#111c30" stroke="#8b7cff" stroke-width="2"/><text x="380" y="210" text-anchor="middle" font-size="21" font-weight="700" fill="#eef6ff">Multimodalita</text><text x="380" y="242" text-anchor="middle" font-size="16" fill="#a9bbcf">text · obraz · audio</text><rect x="510" y="170" width="190" height="120" rx="18" fill="#111c30" stroke="#63d7a5" stroke-width="2"/><text x="605" y="210" text-anchor="middle" font-size="21" font-weight="700" fill="#eef6ff">Efektivita</text><text x="605" y="242" text-anchor="middle" font-size="16" fill="#a9bbcf">nižší cost / task</text><rect x="735" y="170" width="190" height="120" rx="18" fill="#111c30" stroke="#ffca6a" stroke-width="2"/><text x="830" y="210" text-anchor="middle" font-size="21" font-weight="700" fill="#eef6ff">Tools</text><text x="830" y="242" text-anchor="middle" font-size="16" fill="#a9bbcf">data + akce</text><rect x="960" y="170" width="180" height="120" rx="18" fill="#111c30" stroke="#45c7ff" stroke-width="2"/><text x="1050" y="210" text-anchor="middle" font-size="21" font-weight="700" fill="#eef6ff">Agents</text><text x="1050" y="242" text-anchor="middle" font-size="16" fill="#a9bbcf">delší workflow</text><line x1="155" y1="310" x2="570" y2="405" stroke="#5e7188" stroke-width="3" marker-end="url(#a)"/><line x1="380" y1="310" x2="585" y2="405" stroke="#5e7188" stroke-width="3" marker-end="url(#a)"/><line x1="605" y1="310" x2="605" y2="405" stroke="#5e7188" stroke-width="3" marker-end="url(#a)"/><line x1="830" y1="310" x2="625" y2="405" stroke="#5e7188" stroke-width="3" marker-end="url(#a)"/><line x1="1050" y1="310" x2="640" y2="405" stroke="#5e7188" stroke-width="3" marker-end="url(#a)"/><rect x="350" y="410" width="510" height="135" rx="22" fill="#111c30" stroke="#63d7a5" stroke-width="3"/><text x="605" y="458" text-anchor="middle" font-size="27" font-weight="700" fill="#eef6ff">OVĚŘENÝ AI SYSTÉM</text><text x="605" y="494" text-anchor="middle" font-size="18" fill="#a9bbcf">context + tools + policy + evals + observability</text><text x="605" y="524" text-anchor="middle" font-size="18" fill="#a9bbcf">schopnost ≠ spolehlivost</text></g></svg>'''
    print_svg = screen_svg.replace('fill="#0b1220"', 'fill="#ffffff"').replace('fill="#111c30"', 'fill="#f5f7fa"').replace('fill="#eef6ff"', 'fill="#17202b"').replace('fill="#a9bbcf"', 'fill="#4d5c6d"').replace('font-size="16"', 'font-size="18"')
    write(OUT / "assets" / "diagrams" / "32-ai-trends.svg", screen_svg)
    write(OUT / "assets" / "diagrams-print" / "32-ai-trends.svg", print_svg)
    p = chapter(OUT, 32)
    t = read(p)
    if "32-ai-trends.svg" not in t:
        m = re.search(r"^#\s+32\..+$", t, re.M)
        if not m:
            raise RuntimeError("chapter 32 H1 not found")
        visual = '''\n\n<!-- visual:32-ai-trends.svg -->\n\n![Mapa trendů AI](assets/diagrams/32-ai-trends.svg)\n\n*Obrázek: Trend nesměřuje jen k větším modelům, ale k ověřeným systémům s adaptivním compute, modalitami a nástroji.*\n'''
        t = t[:m.end()] + visual + t[m.end():]
    write(p, t)

    # Normalize v0.6 metadata after importing Gemini chapters and renumbering.
    for p in list(OUT.glob("[0-9][0-9] - *.md")) + list((OUT / "appendices").glob("*.md")):
        write(p, normalize_metadata(read(p)))

    # Regenerate reader-facing index from actual final files.
    final_chapters = sorted([p for p in OUT.glob("[0-9][0-9] - *.md") if not p.name.startswith("00 -")])
    if len(final_chapters) != 36:
        raise RuntimeError(f"expected 36 final chapters, got {len(final_chapters)}")
    part_order = []
    grouped = {}
    for p in final_chapters:
        txt = read(p)
        pm = re.search(r'^part:\s*["\']?(.+?)["\']?$', txt, re.M)
        h = re.search(r'^#\s+(.+)$', txt, re.M)
        part = pm.group(1).strip('"\'') if pm else "KNIHA"
        title = h.group(1).strip() if h else p.stem
        if part not in grouped:
            grouped[part] = []
            part_order.append(part)
        grouped[part].append((p, title))

    idx = ['---', 'title: "AI od základů k agentním systémům"', 'subtitle: "Co jsem se zatím naučil, jak AI chápu v srpnu 2026 a co mě ještě čeká"', 'version: "0.6"', f'date: {DATE}', 'status: release-candidate', '---', '', '# AI od základů k agentním systémům', '', '> **Obsidian master index — v0.6 final hybrid**  ', '> Claude redakční vrstva + Gemini technické doplňky + fact-check primárních zdrojů.', '', '## ÚVOD', '- [[00 - Uvod - Jak cist tuto knihu|Úvod — Pro koho je tato kniha a jak ji číst]]', '']
    for part in part_order:
        idx.append('## ' + part)
        for p, title in grouped[part]:
            idx.append(f'- [[{p.stem}|{title}]]')
        idx.append('')
    idx += ['## PŘÍLOHY']
    for p in sorted((OUT / 'appendices').glob('*.md')):
        h = re.search(r'^#\s+(.+)$', read(p), re.M)
        title = h.group(1).strip() if h else p.stem
        idx.append(f'- [[appendices/{p.stem}|{title}]]')
    idx += ['', '## ZDROJE A DALŠÍ ČTENÍ', '- [[BIBLIOGRAPHY|Zdroje a další čtení]]', '', '## REDAKČNÍ PODKLADY', '- [[STYLE_GUIDE|Style guide]]', '- [[PRINT_VISUAL_GUIDE|Print visual guide]]', '- [[FINAL_MERGE_REPORT|Final merge report v0.6]]', '']
    write(OUT / "00 - INDEX.md", "\n".join(idx))

    # Final folder README.
    write(OUT / "README.md", '''# book_final — v0.6\n\nFinální hybridní review varianta knihy **AI od základů k agentním systémům**.\n\n- základ: `book_claude` (úvod, deduplikace, heading hierarchy, trace),\n- technické doplňky: `book_gemini` (reasoning, VRAM, RAG, MCP, agent failure modes, enterprise data, security, evals, TCO),\n- snapshoty: fact-check proti primárním vendor zdrojům k 7. 8. 2026,\n- struktura: **36 kapitol + úvod + 7 příloh**; 16+17 jsou sloučené, manažerská kapitola „Proč nestačí máme ChatGPT“ zůstává zachována.\n\nPůvodní `book/`, `book_claude/` a `book_gemini/` zůstávají jako referenční verze.\n''')

    # Merge/fact-check report.
    write(OUT / "FINAL_MERGE_REPORT.md", '''# Final merge report — v0.6\n\n## Rozhodnutí\n\n- **16+17 sloučeno** do „Anatomie a smyčka AI agenta“, ale vrácen approval dialog a explicitní recovery policy.\n- **Kapitola „Proč nestačí máme ChatGPT“ zachována** jako manažerský vstup; technický web-chat vs API detail zůstává v enterprise kapitole.\n- Následující kapitoly byly souvisle přečíslovány; výsledkem je **36 kapitol**.\n- Claude úvod, heading cleanup, zkrácená historie/roadmapa a agent trace zachovány.\n- Gemini technické doplňky zapracovány podle adjudikace.\n\n## Fact-check snapshot 08/2026\n\n- GPT-5.6 Sol/Terra/Luna — potvrzeno primárním zdrojem OpenAI.\n- Anthropic: Fable 5, Sonnet 5, Opus 4.8 — **„Opus 5“ odmítnuto jako neověřený název**.\n- Gemini 3.1 Pro, 3.6 Flash, 3.5 Flash-Lite — potvrzeno Google zdroji.\n- Grok 4.5 — potvrzeno xAI.\n- DeepSeek-V4 Pro/Flash — potvrzeno DeepSeek API changelogem.\n- Qwen3.6 — potvrzeno Qwen Team.\n- Gemma 4 — potvrzeno Google; Apache 2.0.\n- Mistral Small 4 — potvrzeno Mistral; Apache 2.0.\n- Cohere Command A+ — potvrzeno Cohere; Apache 2.0.\n- Cohere Transcribe a Rerank 4.0 — potvrzeno Cohere.\n- MCP spec `2026-07-28` — potvrzena finální specifikace.\n\n## Autorská evidence\n\nEXP-001 je zachován jako **pozorovací experiment**, protože historické TTFT/tokens/s nebyly konzistentně archivovány. Chybějící čísla nejsou vymyšlena a rukopis neobsahuje `[DOPLNIT]` placeholdery. Pro budoucí kvantitativní vydání je vhodné experiment zopakovat s předem definovaným eval protokolem.\n''')


def audit() -> None:
    chapters = sorted([p for p in OUT.glob("[0-9][0-9] - *.md") if not p.name.startswith("00 -")])
    nums = [int(p.name[:2]) for p in chapters]
    appendices = sorted((OUT / "appendices").glob("*.md"))
    manuscripts = chapters + appendices + [OUT / "00 - Uvod - Jak cist tuto knihu.md"]
    text_all = "\n".join(read(p) for p in manuscripts if p.exists())
    blockers = []
    if nums != list(range(1, 37)):
        blockers.append(f"chapter numbering {nums}")
    if len(appendices) != 7:
        blockers.append(f"appendices={len(appendices)}")
    if re.search(r'\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b|\[\s*DOPLNIT[^\]]*\]', text_all):
        blockers.append("TODO/placeholder remains")
    if "Claude Opus 5" in text_all:
        blockers.append("unverified Claude Opus 5 remains")
    for letter in ("B", "C"):
        p = next((OUT / "appendices").glob(f"{letter} - *.md"))
        if "[Snapshot 08/2026]" not in read(p):
            blockers.append(f"snapshot label missing in {letter}")
    # Image existence.
    missing = []
    for p in manuscripts:
        if not p.exists():
            continue
        for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', read(p)):
            if not (p.parent / ref).resolve().exists():
                missing.append(f"{p.name}: {ref}")
    if missing:
        blockers.append("missing images: " + "; ".join(missing[:10]))
    screens = sorted((OUT / "assets" / "diagrams").glob("*.svg"))
    prints = sorted((OUT / "assets" / "diagrams-print").glob("*.svg"))
    if len(screens) != len(prints):
        blockers.append(f"screen/print svg mismatch {len(screens)}/{len(prints)}")
    # Index chapter links.
    idx = read(OUT / "00 - INDEX.md")
    linked = sorted(set(int(x) for x in re.findall(r'\[\[(\d{2}) - ', idx)))
    if linked != list(range(1, 37)):
        blockers.append(f"index numbers {linked}")
    # No stale exact old removed target.
    if "[[17 - Agentní smyčka" in text_all:
        blockers.append("stale chapter-17 agent-loop link")
    # Report counts.
    word_re = re.compile(r"[A-Za-zÀ-ž0-9µ/+-]+")
    words = sum(len(word_re.findall(re.sub(r'```.*?```', ' ', read(p), flags=re.S))) for p in chapters + appendices)
    report = ['# Source QA — book_final v0.6', '', f'- Chapters: **{len(chapters)}**', f'- Appendices: **{len(appendices)}**', f'- Screen SVG: **{len(screens)}**', f'- Print SVG: **{len(prints)}**', f'- Approx. prose words: **{words}**', f'- Blockers: **{len(blockers)}**', '']
    if blockers:
        report += ['## FAIL'] + [f'- {x}' for x in blockers]
    else:
        report += ['## PASS', '', 'Contiguous 1–36 numbering, no explicit placeholders, snapshot labels present, all referenced images exist, screen/print SVG counts match.']
    write(OUT / "SOURCE_QA_V06.md", "\n".join(report) + "\n")
    print("BOOK_FINAL_QA", "PASS" if not blockers else "FAIL", "chapters", len(chapters), "words", words, "blockers", blockers)
    if blockers:
        raise SystemExit(2)


audit()
