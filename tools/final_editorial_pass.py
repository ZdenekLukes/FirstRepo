from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new, 1)
        path.write_text(text, encoding="utf-8")
        return True
    return False

# -----------------------------------------------------------------------------
# 1) Personal chapter: replace explicit placeholders only with experiences that
# were actually described during preparation of this book.
# -----------------------------------------------------------------------------
ch34 = BOOK / "34 - Co jsem se zatím naučil.md"
replace_once(
    ch34,
    "[DOPLNIT: vlastní konkrétní moment nebo experiment, kdy tento rozdíl začal být zřejmý.]",
    """Konkrétně se mi tento rozdíl začal skládat při práci s coding agenty a Git repository. Samotný model uměl navrhnout kus kódu už dříve. Mnohem zajímavější bylo, když agent dokázal přečíst existující projekt, najít správné soubory, změnit pouze potřebnou část, spustit kontroly a ponechat výsledek jako diff, který lze zkontrolovat.\n\nNajednou nebylo hlavní, zda model zná další syntaktický trik. Hodnota vznikla z kombinace:\n\n```text\nmodel\n+ repository context\n+ filesystem\n+ Git\n+ tests\n+ human review\n```\n\nStejný princip jsem pak začal přenášet na technické workflow: pokud má AI pracovat nad návrhem obvodu, nestačí jí o elektronice dobře mluvit. Potřebuje skutečná data, simulátor a možnost výsledek ověřit.""",
)

replace_once(
    ch34,
    "[DOPLNIT: konkrétní lokální model / coding / dokumentový experiment, který překvapil nejvíce.]",
    """Dobrou lekcí byly lokální modely. Na notebooku s 8 GB VRAM šlo rozumně experimentovat s menšími textovými modely, ale u náročnějších úloh se rychle ukázal paměťový limit a offload do systémové RAM výrazně zhoršoval interaktivnost.\n\nPřechod na kartu s 32 GB VRAM otevřel praktické experimenty s modely přibližně 30B–40B třídy. Vedle textového LLM jsem si mohl spojit lokální stack s Open WebUI, speech-to-text přes Whisper a text-to-speech. Nejdůležitější zjištění pro mě ale nebylo, že větší model \"běží\". Bylo to zjištění, že jednotlivé části stacku lze skládat a měřit odděleně.\n\nMalý model může být dostatečný pro jednu roli, zatímco těžší reasoning pošlu jinam. To je praktičtější než hledat jeden model, který musí umět všechno.""",
)

replace_once(
    ch34,
    "[DOPLNIT: vlastní zkušenosti s konkrétním hardware a modely — rychlost, VRAM, co už bylo překvapivě použitelné a co ne.]",
    """Moje vlastní experimenty mi tento pohled ještě posílily. Osm gigabajtů VRAM je dost na to, aby si člověk lokální AI skutečně osahal, ale zároveň velmi rychle ukáže rozdíl mezi \"model lze spustit\" a \"model je příjemné používat\". Jakmile část modelu nebo cache přeteče do pomalejší paměti, papírově funkční konfigurace může přestat být praktická.\n\nS 32 GB VRAM se otevře úplně jiná třída experimentů, včetně větších kvantizovaných modelů. Ani tam ale nedává smysl automaticky vybírat největší model, který se vejde. Pro mnoho úzkých úloh je menší model rychlejší a dostatečně kvalitní.\n\nProto dnes hardware neberu jako soutěž o maximální počet parametrů. Je to další routing constraint: která úloha má běžet lokálně, která na silnějším interním serveru a která si opravdu zaslouží frontier cloud.""",
)

text = ch34.read_text(encoding="utf-8")
text = text.replace("status: personal-draft", "status: final-draft")
text = text.replace('version: "0.2"', 'version: "0.4"', 1)
ch34.write_text(text, encoding="utf-8")

# -----------------------------------------------------------------------------
# 2) EU governance section in security chapter.
# -----------------------------------------------------------------------------
ch25 = BOOK / "25 - Bezpečnost AI.md"
text = ch25.read_text(encoding="utf-8")
anchor = "# Jednoduchý threat model agentního systému"
if "## 25.20 EU AI Act, GDPR a firemní governance" not in text and anchor in text:
    section = r'''## 25.20 EU AI Act, GDPR a firemní governance

Technická bezpečnost není totéž co compliance.

V evropské firmě potřebujeme vedle threat modelu řešit také dvě další vrstvy:

```text
SECURITY
→ kdo může systém zneužít a jak omezíme škodu

PRIVACY / GDPR
→ zda a proč smíme zpracovávat osobní údaje

AI GOVERNANCE / AI ACT
→ jakou roli a povinnosti má firma pro konkrétní AI use-case
```

Tyto oblasti se překrývají, ale jedna nenahrazuje druhou.

### GDPR: začíná u účelu a dat

Pokud AI workflow zpracovává osobní údaje, platí stejné základní principy jako u jiné IT aplikace.

Prakticky se ptejme:

- proč data zpracováváme,
- jaký je právní základ,
- zda neposíláme více dat, než úloha potřebuje,
- jak dlouho je ukládáme,
- komu je zpřístupňujeme,
- zda se osobní data nekopírují do debug logů nebo long-term memory.

Pro AI je zvlášť důležitá **data minimisation**.

Pokud model potřebuje pro odpověď tři odstavce z dokumentu, není dobrý default posílat mu celý personální archiv.

### EU AI Act: posuzujeme use-case, ne pouze model

AI Act pracuje s rolemi a rizikem konkrétního systému.

Firma může být podle situace například:

- **provider** — systém uvádí na trh nebo do provozu pod svým jménem,
- **deployer** — AI systém používá ve vlastní činnosti.

To znamená, že otázka:

> „Používáme GPT, Claude nebo lokální model?“

sama o sobě neurčuje regulatorní povinnosti.

Důležitější je:

```text
K ČEMU systém používáme?
KDO jej poskytuje?
KDO jej provozuje?
KOHO výsledek ovlivňuje?
JAKÁ rozhodnutí nebo obsah vytváří?
```

### Co je aktuální k 7. 8. 2026

Část pravidel AI Act se používá postupně. Pro tuto knihu je prakticky důležitý zejména fakt, že **transparentnostní povinnosti podle článku 50 se používají od 2. srpna 2026**.

Týkají se mimo jiné situací, kdy lidé přímo interagují s AI a vybraných případů AI-generated nebo manipulated content. Přesný rozsah závisí na roli provider/deployer a konkrétním use-case.

Proto má produkční AI checklist obsahovat alespoň:

```text
use-case owner
role: provider / deployer
risk classification
AI literacy
transparency requirement
human oversight
logging / evidence
change management
```

### AI literacy není jednorázové školení

Bezpečný provoz vyžaduje, aby uživatelé chápali alespoň:

- že model může halucinovat,
- rozdíl mezi modelem a nástrojem,
- jak zacházet s citlivými daty,
- kdy výsledek vyžaduje ověření,
- co agent smí a nesmí udělat.

To není obecná „AI osvěta“.

Je to provozní schopnost podobná security awareness.

### Praktické pravidlo pro firmu

Nechci z AI týmu dělat právní oddělení.

Chci ale, aby před produkčním nasazením vznikla malá karta systému:

| Položka | Otázka |
|---|---|
| Owner | Kdo za systém odpovídá? |
| Purpose | K čemu přesně slouží? |
| Data | Jaké datové třídy a osobní údaje zpracovává? |
| Provider / deployer | Jakou roli v use-case máme? |
| Risk | Jaký je dopad chyby? |
| Transparency | Musí uživatel vědět, že komunikuje s AI nebo že obsah vytvořila AI? |
| Human oversight | Které kroky člověk schvaluje? |
| Evidence | Jak prokážeme, co systém udělal? |
| Change control | Co se stane při změně modelu nebo workflow? |

Pokud firma tuto kartu neumí vyplnit, AI systém ještě není provozně dospělý.

### Primární zdroje k datu snapshotu

- European Commission — Guidelines on transparency obligations for providers and deployers of AI systems: https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- European Commission — Transparency obligations under Article 50 of the AI Act: https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- European Commission — GDPR principles: https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr_en

> **Tato část je praktický technicko-provozní přehled, ne právní stanovisko. Pro konkrétní nasazení musí firma použít aktuální právní a compliance posouzení.**

---

'''
    text = text.replace(anchor, section + anchor, 1)
    text = text.replace('version: "0.2"', 'version: "0.4"', 1)
    ch25.write_text(text, encoding="utf-8")

# -----------------------------------------------------------------------------
# 3) Editorial style guide.
# -----------------------------------------------------------------------------
style = r'''# STYLE GUIDE — AI od základů k agentním systémům

> Redakční pravidla pro finální vydání. Cíl: technická čeština, která zní přirozeně lidem z engineeringu a současně nevytváří náhodný mix češtiny a angličtiny.

## 1. Hlas knihy

- píšeme v první osobě tam, kde jde o osobní zkušenost nebo názor;
- technické vysvětlení může používat „my“ jako společný postup autora a čtenáře;
- krátké odstavce jsou záměrné;
- preferujeme konkrétní příklad před abstraktní definicí;
- nepoužíváme marketingové superlativy bez evidence;
- rozlišujeme fakt, zkušenost, odhad a názor.

## 2. Terminologie

Při prvním výskytu použij české vysvětlení a běžný anglický termín. Potom používej preferovanou formu konzistentně.

| Preferovaná forma | Při prvním výskytu / poznámka |
|---|---|
| **kontext** | `context`; `context window` ponechat jako odborný termín, případně „kontextové okno“ |
| **nástroj** | `tool`; spojení **tool use** lze ponechat jako název konceptu/kapitoly |
| **workflow** | ponechat v technickém textu; nestřídat náhodně s „pracovním postupem“ v jedné pasáži |
| **use-case** | ponechat; v běžné větě lze jednou vysvětlit „případ použití“ |
| **lokální / local** | český text: **lokální**; názvy produktů a citace neměnit |
| **paměť** | `memory`; `working memory`, `long-term memory` lze při prvním použití uvést dvojjazyčně |
| **knowledge base** | ponechat jako technický termín; při prvním výskytu „znalostní báze (knowledge base)“ |
| **reasoning** | ponechat; vysvětlit jako vícekrokové řešení / inference compute, ne překládat střídavě jako „uvažování“ |
| **oprávnění** | `permissions`; v prose preferovat českou formu |
| **verifikace** | `verification`; v engineering kontextu preferovat „verifikace“, ne střídat s „ověřením“ bez důvodu |
| **simulace** | česká forma |
| **open-weight** | preferovat před nepřesným „open-source model“, pokud mluvíme pouze o dostupnosti vah |
| **agentní** | preferovat před „agentic“, kromě názvů produktů/specifikací |
| **multimodální** | česká forma |

## 3. Co nepřekládat

Bez potřeby nepřekládat:

- RAG,
- LLM,
- MCP,
- API,
- Git,
- JSON,
- Python,
- embeddings,
- reranker,
- benchmark,
- eval / evals,
- prompt injection.

U termínů, které mohou být pro nováčka nejasné, stačí vysvětlení ve slovníku a při prvním použití.

## 4. Model vs. celý systém

Vždy rozlišuj:

```text
MODEL
≠
AI APPLICATION
≠
AI SYSTEM
```

Nepřipisuj samotnému modelu schopnost používat web, soubory, shell, Git nebo databázi, pokud jde ve skutečnosti o nástroj aplikace.

## 5. Jistota tvrzení

### Fakt

Piš bez kvalifikace pouze tehdy, když je tvrzení stabilní nebo podložené zdrojem.

### Snapshot

Rychle se měnící fakta označ datem:

```text
Snapshot k 7. 8. 2026
```

### Odhad / budoucnost

Používej:

- „pravděpodobně“,
- „očekávám“,
- „dává mi smysl“,
- „v současnosti je vidět trend“.

Nezaměňuj trend za jistou předpověď.

## 6. Simulace a verifikace

Nepoužívat absolutní formulaci:

```text
simulátor = realita
```

Preferovat:

> Simulátor poskytuje externě ověřitelný výsledek podle definovaného modelu a jeho předpokladů.

Deterministický výpočet může být spolehlivější verifier než LLM, ale i model simulátoru má omezení.

## 7. Čísla a jednotky

- mezi číslem a jednotkou používat mezeru: `16 GB`, `120 µs`;
- desetinná čárka v českém prose, tečka v kódu a API hodnotách;
- ceny a benchmarky vždy s datem nebo snapshotem, pokud mohou rychle stárnout;
- rychlost lokálního modelu uvádět spolu s hardware, runtime, quantization a context length.

## 8. Kapitola

Preferovaná stavba:

1. proč téma potřebujeme,
2. jednoduchý mentální model,
3. praktický příklad,
4. failure modes / limity,
5. důsledek pro návrh systému,
6. „Co si z kapitoly odnést“,
7. přirozený most k další kapitole, pokud dává smysl.

Ne každá kapitola musí mít stejný počet podnadpisů.

## 9. Vizuály

- obrázek musí něco vysvětlovat, ne pouze dekorovat;
- jeden diagram = jedna hlavní myšlenka;
- screen verze může být tmavá;
- print verze musí být čitelná na bílé stránce a v grayscale;
- minimální praktická velikost textu po sazbě: přibližně 8–9 pt, preferovat 9–10 pt;
- caption začíná `Obrázek:` a vysvětluje pointu, ne pouze opakuje nadpis.

## 10. Citace

- rychle se měnící produktová fakta: primární vendor source;
- bezpečnost a standardy: primární standard / OWASP / regulatorní zdroj;
- historie: původní paper nebo důvěryhodný historický zdroj;
- u obecných didaktických vysvětlení není nutné citovat každou větu;
- kapitola se snapshotem má mít sekci `Zdroje pro snapshot`;
- společné akademické a standardizační zdroje jsou v `BIBLIOGRAPHY.md`.

## 11. Co před finálním exportem hledat

```text
DOPLNIT
TODO
FIXME
placeholder
example.com
rough-draft
personal-draft
roadmap-draft
```

Výjimkou je `example.com` uvnitř explicitně označeného demonstračního kódu.
'''
(BOOK / "STYLE_GUIDE.md").write_text(style, encoding="utf-8")

# -----------------------------------------------------------------------------
# 4) Central bibliography / further reading.
# -----------------------------------------------------------------------------
biblio = r'''# BIBLIOGRAPHY — primární zdroje a další čtení

> Tato bibliografie doplňuje zdroje uvedené přímo u snapshotových kapitol. Není cílem citovat každou didaktickou větu, ale umožnit čtenáři dohledat primární zdroje klíčových konceptů.

## Historie a základy

1. Alan M. Turing — *Computing Machinery and Intelligence*, Mind, 1950.
2. John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon — *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 1955/1956.
3. Warren McCulloch, Walter Pitts — *A Logical Calculus of the Ideas Immanent in Nervous Activity*, 1943.
4. David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams — *Learning representations by back-propagating errors*, Nature, 1986.
5. Yann LeCun et al. — *Gradient-Based Learning Applied to Document Recognition*, 1998.
6. Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton — *ImageNet Classification with Deep Convolutional Neural Networks*, 2012.

## Transformers, LLM a instruction tuning

7. Ashish Vaswani et al. — *Attention Is All You Need*, 2017 — https://arxiv.org/abs/1706.03762
8. Tom B. Brown et al. — *Language Models are Few-Shot Learners*, 2020 — https://arxiv.org/abs/2005.14165
9. Long Ouyang et al. — *Training language models to follow instructions with human feedback*, 2022 — https://arxiv.org/abs/2203.02155

## Retrieval a RAG

10. Patrick Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, 2020 — https://arxiv.org/abs/2005.11401

## Agentní systémy a tools

11. Model Context Protocol — official documentation — https://modelcontextprotocol.io/
12. OpenAI Agents SDK — https://openai.github.io/openai-agents-python/
13. Pydantic AI — https://ai.pydantic.dev/
14. LangGraph — https://docs.langchain.com/oss/python/langgraph/overview

## Local inference

15. llama.cpp — https://github.com/ggml-org/llama.cpp
16. Ollama — https://ollama.com/
17. vLLM — https://vllm.ai/

## Security

18. OWASP GenAI Security Project — https://genai.owasp.org/
19. OWASP — Agentic AI threats and mitigations — https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
20. OWASP — GenAI Data Security Risks & Mitigations 2026 — https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/

## Evropská regulace a privacy

21. European Commission — AI Act overview — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
22. European Commission — Guidelines on transparency obligations for providers and deployers of AI systems — https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
23. European Commission — Transparency obligations under Article 50 — https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
24. European Commission — GDPR principles — https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr_en

## Snapshot modelů — 7. 8. 2026

Aktuální vendor odkazy jsou u kapitoly 5 a v příloze B. U modelů, cen a produktových schopností má vždy přednost aktuální primární zdroj před touto knihou.

## Poznámka k citacím

Při sazbě lze tuto pracovní bibliografii převést do jednotného citačního stylu vydavatele. Markdown verze záměrně preferuje dohledatelnost a jednoduchou údržbu před akademickým formátováním.
'''
(BOOK / "BIBLIOGRAPHY.md").write_text(biblio, encoding="utf-8")

# -----------------------------------------------------------------------------
# 5) Print variants of SVG diagrams.
# -----------------------------------------------------------------------------
src_dir = BOOK / "assets" / "diagrams"
dst_dir = BOOK / "assets" / "diagrams-print"
dst_dir.mkdir(parents=True, exist_ok=True)

colors = {
    "#0b1220": "#ffffff",
    "#111c30": "#f5f7fa",
    "#eef6ff": "#111827",
    "#a9bbcf": "#374151",
    "#5e7188": "#6b7280",
    "#45c7ff": "#0077a8",
    "#8b7cff": "#5b4bc4",
    "#63d7a5": "#16805d",
    "#ffca6a": "#8a5a00",
    "#ff7a8a": "#b4233b",
}


def bump_font(m):
    # At the 170 x 240 mm proof trim, 25 SVG units render at ~8 pt.
    # Keep larger titles larger, but never let diagram body text fall below 25.
    n = int(m.group(1))
    n = max(n, 25)
    return f'font-size="{n}"'

for svg in sorted(src_dir.glob("*.svg")):
    s = svg.read_text(encoding="utf-8")
    for a, b in colors.items():
        s = s.replace(a, b)
    s = re.sub(r'font-size="(\d+)"', bump_font, s)
    dst = dst_dir / svg.name
    dst.write_text(s, encoding="utf-8")

manifest = [
    "# Print diagram assets",
    "",
    "> Světlé varianty SVG pro knižní sazbu. Vznikají z obrazovkových diagramů změnou palety a zvětšením nejmenších fontů.",
    "",
    "## Pravidla",
    "",
    "- Pro web/Obsidian používat `assets/diagrams/`.",
    "- Pro PDF/tisk preferovat `assets/diagrams-print/`.",
    "- Po skutečné sazbě ověřit minimálně 8–9 pt výslednou velikost popisků.",
    "- Udělat grayscale proof; význam nesmí být zakódován pouze barvou.",
    "- Tmavé full-bleed plochy nepoužívat jako default pro běžné stránky knihy.",
    "",
    f"Vygenerováno variant: **{len(list(dst_dir.glob('*.svg')))}**.",
]
(BOOK / "PRINT_VISUAL_GUIDE.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")

# -----------------------------------------------------------------------------
# 6) Index + README status.
# -----------------------------------------------------------------------------
index = BOOK / "00 - INDEX.md"
t = index.read_text(encoding="utf-8")
t = t.replace('version: "0.3"', 'version: "0.4"')
t = t.replace('status: rough-draft', 'status: final-editorial-draft')
t = t.replace('> **Obsidian master index — v0.3**', '> **Obsidian master index — v0.4**')
t = t.replace('Verze 0.3 je záměrně hrubá: cílem je mít celý obsah knihy před očima, mazat, přesouvat a teprve potom jednotlivé části detailně rozepisovat.', 'Verze 0.4 je finální redakční draft před sazbou: hlavní kapitoly i přílohy jsou rozepsané, proběhl content/visual audit a další kontrola se má dělat nad vysázeným proof PDF.')
if "## REDAKČNÍ PODKLADY" not in t:
    t += "\n\n## REDAKČNÍ PODKLADY\n- [[STYLE_GUIDE|Style guide]]\n- [[BIBLIOGRAPHY|Bibliografie a další čtení]]\n- [[PRINT_VISUAL_GUIDE|Print visual guide]]\n- [[FINAL_EDITORIAL_AUDIT_2026-08-07|Finální redakční audit]]\n"
index.write_text(t, encoding="utf-8")

readme = ROOT / "README.md"
r = readme.read_text(encoding="utf-8")
r = r.replace("Stav: **kompletní první pracovní draft kapitol 1–37**", "Stav: **finální redakční draft před sazbou**")
r = r.replace("Aktuální pracovní verze kapitol: **0.2 draft**", "Aktuální pracovní verze knihy: **0.4 final-editorial-draft**")
r = r.replace("Všech **37 hlavních kapitol** je nyní rozepsaných z původních koster do souvislého prvního draftu ve společném stylu knihy:", "Všech **37 hlavních kapitol** je nyní rozepsaných; kapitola 37 byla doplněna do plné praktické kuchařky a přílohy A–G jsou použitelné referenční materiály. Proběhl předtiskový content a visual audit:")
r = r.replace("- `book/appendices/` — přílohy A–G; zatím pracovní kostry pro další rozpracování", "- `book/appendices/` — rozpracované přílohy A–G\n- `book/STYLE_GUIDE.md` — redakční terminologie a styl\n- `book/BIBLIOGRAPHY.md` — společné primární zdroje\n- `book/assets/diagrams-print/` — světlé SVG varianty pro sazbu")
readme.write_text(r, encoding="utf-8")

print("Final editorial pass complete")