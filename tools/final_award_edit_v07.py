from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'book_final'
DATE = '2026-08-07'
VERSION = '0.7'


def read(p): return p.read_text(encoding='utf-8')
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s,encoding='utf-8')

def chapter(n):
    xs=sorted(BOOK.glob(f'{n:02d} - *.md'))
    if len(xs)!=1: raise RuntimeError((n,xs))
    return xs[0]

def meta(s):
    if s.startswith('---\n'):
        s=re.sub(r'^version:\s*.*$',f'version: "{VERSION}"',s,count=1,flags=re.M)
        s=re.sub(r'^updated:\s*.*$',f'updated: {DATE}',s,count=1,flags=re.M)
    return s


def svg_screen(title, subtitle, boxes, arrows, footer=''):
    # boxes: [(x,y,w,h,head,body,stroke)]
    W,H=1200,700
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{title}</title><desc id="desc">{subtitle}</desc>',
           '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#60758b"/></marker></defs>',
           '<rect width="1200" height="700" rx="30" fill="#0b1220"/>',
           f'<text x="60" y="66" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="34" font-weight="700" fill="#eef6ff">{title}</text>',
           f'<text x="60" y="103" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="19" fill="#b5c6d8">{subtitle}</text>']
    for x1,y1,x2,y2 in arrows:
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#60758b" stroke-width="3" marker-end="url(#arrow)"/>')
    for x,y,w,h,head,body,stroke in boxes:
        parts += [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#111c30" stroke="{stroke}" stroke-width="2.5"/>',
                  f'<text x="{x+w/2}" y="{y+38}" text-anchor="middle" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="22" font-weight="700" fill="#eef6ff">{head}</text>']
        lines=body.split('|')
        start=y+72
        for i,line in enumerate(lines):
            parts.append(f'<text x="{x+w/2}" y="{start+i*27}" text-anchor="middle" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="18" fill="#b5c6d8">{line}</text>')
    if footer:
        parts.append(f'<text x="600" y="660" text-anchor="middle" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="20" font-weight="700" fill="#eef6ff">{footer}</text>')
    parts.append('</svg>')
    return ''.join(parts)

def printify(s):
    s=s.replace('fill="#0b1220"','fill="#ffffff"').replace('fill="#111c30"','fill="#f6f8fa"')
    s=s.replace('fill="#eef6ff"','fill="#17202b"').replace('fill="#b5c6d8"','fill="#445465"')
    # All body labels become at least 20 SVG units in print.
    s=s.replace('font-size="18"','font-size="20"').replace('font-size="19"','font-size="20"')
    return s

# ------------------------------------------------------------------
# 0. Intro: stronger thesis, beginner-safe positioning, signature map.
# ------------------------------------------------------------------
intro = BOOK / '00 - Uvod - Jak cist tuto knihu.md'
intro_text = '''---
title: "Úvod — Pro koho je tato kniha a jak ji číst"
part: "ÚVOD"
status: final-draft
version: "0.7"
updated: 2026-08-07
---

# Úvod — Pro koho je tato kniha a jak ji číst

Nejtěžší na AI v roce 2026 není získat přístup k chytrému modelu. Během několika minut můžeme otevřít špičkový cloudový model nebo spustit menší model lokálně.

Těžší otázky přicházejí až potom:

> **Kdy modelu věřit? Co mu chybí? Odkud má fakta? Co smí udělat? A jak z působivé odpovědi udělat výsledek, za který jsme ochotni převzít odpovědnost?**

Právě o tom je tato kniha.

Není to akademická učebnice ani katalog produktů. Je to praktický zápisník mé cesty za pochopením AI, převedený do podoby technické příručky pro dalšího člověka. Zachycuje stav, jak AI chápu v srpnu 2026 — ale snaží se oddělit rychle stárnoucí názvy modelů od principů, které budou užitečné i poté, co dnešní produkty zmizí.

<!-- visual:00-ai-system-stack.svg -->

![Od modelu k hodnotě](assets/diagrams/00-ai-system-stack.svg)

*Obrázek: Model je jen jedna vrstva. Reálnou hodnotu určuje celý řetězec od dat přes nástroje a kontrolu až po verifikovaný výsledek.*

## Dvanáct pravidel praktické AI

Pokud chcete nejdřív mapu celé knihy, je v těchto dvanácti větách:

1. **Model není AI systém.** Schopnost vzniká až kombinací modelu, kontextu, dat, nástrojů a řízení.
2. **Lepší kontext často pomůže víc než větší model.** Špatný vstup nezachrání ani frontier reasoning.
3. **Aktuální a soukromá fakta musí přijít z externího zdroje.** Modelové váhy nejsou firemní databáze ani živý web.
4. **Co lze spolehlivě spočítat nebo ověřit klasickým programem, nenechávejme pouze na LLM.**
5. **U RAG měřme retrieval a generation odděleně.** Když jsme našli špatný zdroj, lepší formulace odpovědi problém neřeší.
6. **Správná odpověď bez provenance není u kritické práce dost.** Potřebujeme vědět, odkud tvrzení pochází.
7. **Úspěšný tool call není důkaz úspěšného úkolu.** Akci musí následovat verifikace skutečného výsledku.
8. **Agent má mít minimální oprávnění a explicitní stop podmínky.** Autonomie bez hranic není pokročilost, ale riziko.
9. **Nevratná nebo vysoce riziková akce potřebuje approval, dokud evidence neukáže bezpečnější režim.**
10. **Evals patří před scaling, ne až po něm.** Nejprve zjistěme, zda systém funguje; potom jej zrychlujme a rozšiřujme.
11. **Pokud jednodušší systém dosahuje stejného výsledku, vyhrává.** Multi-agent, memory ani nový framework nejsou cílem samy o sobě.
12. **Model vybírejme podle vlastního use-case, ne podle hype, benchmarkového titulku nebo nejvyššího čísla v názvu.**

Zbytek knihy tato pravidla postupně rozbalí, otestuje na konkrétních příkladech a ukáže jejich limity.

## Pro koho kniha je

Kniha je psaná hlavně pro technicky uvažujícího čtenáře, ale **nevyžaduje předchozí znalost AI, programování ani matematiku neuronových sítí**. Vyžaduje spíš ochotu ptát se: Co je vstup? Co je výstup? Odkud se vzala informace? Jak poznáme chybu?

Je tedy pro člověka, který:

- vstupuje do AI úplně od začátku a nechce začít hromadou buzzwordů,
- má technické uvažování, ale není AI specialista,
- chce pochopit souvislosti, ne jen názvy nástrojů,
- chce AI skutečně používat — od chatbotů přes lokální modely, RAG a nástroje až k agentním systémům,
- nebo potřebuje rozhodovat, kde AI dává smysl v reálné práci a kde je zatím jen působivé demo.

Pokud hledáte matematický výklad Transformeru nebo katalog všech frameworků, tato kniha to záměrně není. Chci jít dostatečně hluboko na to, aby čtenář rozuměl architektuře a trade-offům — ale bez rovnic, které pro praktické používání nepotřebuje.

## Co budete po přečtení umět

1. Vytvořit si správný základní mentální model AI — a poznat, kde se typicky rozbíjí.
2. Rozlišovat **model**, **AI aplikaci**, **agenta** a **celý AI systém**.
3. Chápat, jak fungují LLM bez matematiky a proč jejich plynulost není důkaz pravdy.
4. Orientovat se mezi cloudovými a lokálními modely a vytvořit si vlastní benchmark.
5. Pracovat s promptingem a context engineeringem jako se specifikací úlohy, ne jako s magickou formulí.
6. Rozumět RAG, provenance a práci s vlastními daty.
7. Chápat tool use, MCP a integrační vrstvy.
8. Rozumět agentům a agentním systémům — včetně stop conditions, failure modes a situací, kdy je vůbec nestavět.
9. Navrhnout bezpečnost, evaluaci a observability jako součást systému od začátku.
10. Začít stavět vlastní praktické AI workflow a měřit, zda skutečně přináší hodnotu.

## Jak je kniha stavěná

Kniha postupuje po vrstvách. Každá odpovídá na jinou otázku:

```text
co se historicky změnilo
↓
co je model a jak funguje
↓
jaký model vybrat a kde jej provozovat
↓
co model při práci skutečně vidí
↓
jak mu dodat vlastní data
↓
jak mu dát nástroje
↓
jak z toho vzniká agentní smyčka
↓
jak systém omezit, změřit a ověřit
↓
jak jej nasadit do skutečné práce
```

Každá technická kapitola končí shrnutím nebo jasným přechodem k další otázce. Kdo spěchá, může nejprve číst závěry kapitol a vracet se do detailu tam, kde jej potřebuje.

## Tři čtenářské cesty

Kniha je lineární, ale nemusíte ji tak číst.

### Úplný začátečník

Začněte částí II — kapitoly 2–4 jsou základní mentální model. Historickou kapitolu 1 můžete při prvním čtení přeskočit. Potom pokračujte lineárně. Kdykoli narazíte na termín, který není jasný, použijte slovník v příloze A.

### Inženýr nebo AI geek, který chce stavět

Proleťte části II–V, důkladně čtěte části VI–IX a XII: RAG, nástroje, agenti, práce nad dokumenty, engineering a evals. Pak jděte do části XIV — kapitola 36 obsahuje deset projektů seřazených od jednoho dokumentu po agentní systém. Přílohy D, E a F jsou určené k přímému použití.

### Manažer nebo člověk zavádějící AI do firmy

Přečtěte kapitoly 2–4, potom části X–XII: bezpečnost, AI readiness, adopci, evaluaci a ekonomiku. Kapitola 25 vysvětluje, proč „máme ChatGPT“ ještě není AI operating capability. Technické části VI–VIII čtěte podle potřeby; jejich shrnutí stačí k orientaci.

## Jak kniha zachází se stárnutím obsahu

AI se mění rychle. Proto kniha odděluje dvě vrstvy:

- **Principy** — jak LLM funguje, co je RAG, jak navrhovat nástroje, agenty, bezpečnost a evals. Ty stárnou pomaleji a tvoří většinu knihy.
- **Snapshoty** — konkrétní modely, nástroje, hardware a regulace k 7. 8. 2026. Rychle se měnící fakta jsou označená datem a primární zdroje jsou soustředěné v bibliografii a přílohách B a C. Typickými snapshotovými částmi jsou zejména kapitoly 5, 8, 15, 24, 31, 32 a 35.

Pokud knihu čtete později, snapshoty berte jako mapu tehdejšího terénu. Architektonické principy, rozhodovací pravidla a failure modes jsou to, co má vydržet.

## Jedna věta, kterou kniha opakuje záměrně

> **Nejdůležitější není mít nejchytřejší model, ale umět mu ve správný okamžik dodat správný kontext a nástroje — a jeho výsledek spolehlivě ověřit.**

A ještě jeden obraz:

```text
MODEL ≠ AI APLIKACE ≠ AGENT ≠ AI SYSTÉM
```

Pokud po přečtení začnete u každého AI dema automaticky hledat **data, kontext, nástroje, oprávnění a verifikaci**, kniha splnila svůj hlavní účel.

Teď můžeme začít od začátku: jak jsme se do dnešního bodu vůbec dostali.
'''
write(intro,intro_text)

# Intro signature diagram.
boxes=[
(55,185,165,120,'MODEL','jazyk|reasoning','#45c7ff'),
(245,185,165,120,'KONTEXT','úloha|evidence','#8b7cff'),
(435,185,165,120,'DATA','fakta|provenance','#63d7a5'),
(625,185,165,120,'TOOLS','search|code · API','#ffca6a'),
(815,185,165,120,'CONTROL','state|permissions','#ff8e7a'),
(1005,185,140,120,'EVALS','verify|measure','#45c7ff'),
(330,440,540,130,'HODNOTA','správný výsledek · bezpečná akce|důkaz, že systém funguje','#63d7a5')]
arrows=[(137,320,420,435),(327,320,470,435),(517,320,520,435),(707,320,570,435),(897,320,620,435),(1075,320,675,435)]
s=svg_screen('Od modelu k hodnotě','Schopnost modelu je jen začátek. Reálný výsledek určuje celý systém.',boxes,arrows,'Nejslabší vrstva často určí kvalitu celého výsledku.')
write(BOOK/'assets/diagrams/00-ai-system-stack.svg',s)
write(BOOK/'assets/diagrams-print/00-ai-system-stack.svg',printify(s))

# ------------------------------------------------------------------
# 5. Remove editorial-process language and raw source dump.
# ------------------------------------------------------------------
p=chapter(5); t=read(p)
t=t.replace('Důležitá redakční oprava: **„Opus 5“ není k datu tohoto snapshotu správný veřejný název modelu.** Číslo generace a produktová třída už nejsou vždy jedna jednoduchá osa.',
'''Pozor na názvosloví: **„Opus 5“ není k datu tohoto snapshotu veřejný název modelu Anthropic.** Generace a produktové třídy už netvoří jednu jednoduchou číselnou řadu, takže názvy je lepší ověřovat než odvozovat.''')
t=re.sub(r'\n---\n\n## Zdroje pro snapshot 08/2026.*\Z','\n\n*Primární zdroje pro tento snapshot jsou soustředěné v příloze B a v bibliografii.*\n',t,flags=re.S)
write(p,meta(t))

# ------------------------------------------------------------------
# 15 / 24 / 35. Let the chapter end on a thought, not a URL dump.
# ------------------------------------------------------------------
for n, heading, note in [
    (15,'Zdroje pro snapshot 08/2026','*Primární MCP specifikace a dokumentace použitá pro snapshot 08/2026 jsou uvedené v bibliografii.*'),
    (24,'Zdroje pro snapshot 08/2026','*Primární bezpečnostní, regulatorní a OWASP zdroje jsou soustředěné v bibliografii.*'),
    (35,'Zdroje a projekty pro snapshot 08/2026','*Aktuální odkazy na runtime, frameworky a observability nástroje jsou soustředěné v bibliografii a příloze C.*')]:
    p=chapter(n); t=read(p)
    t=re.sub(rf'\n---\n\n## {re.escape(heading)}.*\Z','\n\n'+note+'\n',t,flags=re.S)
    write(p,meta(t))

# ------------------------------------------------------------------
# 33. Turn a living-note residue into a definitive personal essay.
# ------------------------------------------------------------------
p=chapter(33); t=read(p)
t=t.replace('> Osobní kapitola — průběžně doplňovat konkrétními experimenty, chybami a změnami názoru.\n\n','')
# Insert personal signature diagram after H1 if absent.
if '33-model-to-system.svg' not in t:
    m=re.search(r'^# 33\..+$',t,re.M)
    block='''\n\n<!-- visual:33-model-to-system.svg -->\n\n![Od model-centric k system-centric pohledu](assets/diagrams/33-model-to-system.svg)\n\n*Obrázek: Největší posun v mém chápání AI nebyl k větším modelům, ale od modelu k systému kolem něj.*\n'''
    t=t[:m.end()]+block+t[m.end():]
t=t.replace('(celý obrázek v sekci 34.10)','(celý obrázek v sekci 33.10)')
t=t.replace('RAG je search pipeline a její kvalita závisí na parsing, chunking, metadata, oprávnění a reranking.',
'''RAG není kouzelná „paměť modelu“. Jeho kvalitu zásadně určuje retrieval pipeline: parsing, chunking, metadata, oprávnění, vyhledávání a případný reranking.''')
t=t.replace('Přidáme simulator:','Přidáme simulátor:')
t=t.replace('a vznikne základ engineering loopu.','a vznikne základ inženýrské closed-loop smyčky.')
t=t.replace('cloud vs. local — jak se změnil můj pohled','cloud vs. lokální AI — jak se změnil můj pohled')
t=t.replace('Cloud a local je snadné chápat jako souboj dvou táborů.','Cloud a lokální AI je snadné chápat jako souboj dvou táborů.')
t=t.replace('### Local\n','### Lokální provoz\n')
t=t.replace('Je to další routing constraint: která úloha má běžet lokálně, která na silnějším interním serveru a která si opravdu zaslouží frontier cloud.',
'''Je to další omezení pro routing: která úloha má běžet lokálně, která na silnějším interním serveru a která si opravdu zaslouží frontier cloud.''')
t=t.replace('Potřebuje memory nebo access k našim notes.','Potřebuje paměť nebo přístup k našim poznámkám.')
t=t.replace('Když nezná dnešní data, potřebuje search.','Když nezná dnešní data, potřebuje search nebo jiný živý zdroj.')
t=t.replace('Když má ověřit obvod, potřebuje simulator.','Když má ověřit obvod, potřebuje simulátor.')
t=t.replace('- tool,\n- permission,\n- verifier.','- nástroj,\n- oprávnění,\n- verifier.')
t=t.replace('DATA PROBLEM','DATA PROBLEM')
# Replace the provisional ending completely.
marker='## Pracovní závěr'
if marker in t:
    t=t[:t.index(marker)] + '''## 33.12 Sedm věcí, které bych si dnes napsal na první stránku

Kdybych začínal znovu, chtěl bych mít před sebou těchto sedm vět:

1. **Nehledej nejdřív nejlepší model. Nejdřív přesně definuj úlohu.**
2. **Když výsledek není dobrý, zjisti, zda selhal model, data, kontext, nástroj nebo verifier.**
3. **Co můžeš ověřit externím systémem, ověř externím systémem.** Test, simulátor a databáze jsou silnější evidence než sebejistý text.
4. **Stav malé end-to-end experimenty.** Jedna funkční uzavřená smyčka naučí víc než deset demonstračních chatbotů.
5. **Menší model v dobře navrženém workflow může být hodnotnější než frontier model bez kontextu a nástrojů.**
6. **Autonomii přidávej až tam, kde máš evals, limity a možnost zastavit systém.**
7. **Investuj do dat, integrací a evalů tak, aby model šel zítra vyměnit.** To je trvalejší aktivum než dnešní jméno vítěze benchmarku.

Kdybych měl svůj dnešní pohled zkrátit do jedné věty, zůstává tato:

> **Nejdůležitější není mít nejchytřejší model, ale umět mu ve správný okamžik dodat správný kontext a nástroje — a jeho výsledek spolehlivě ověřit.**

To pro mě není závěr debaty o AI. Je to pracovní kompas.

Modely se budou měnit. Stejně tak ceny, frameworky i rozhraní. Ale pokaždé se můžeme vrátit k několika stabilním otázkám: **Co je cíl? Jaká evidence je potřeba? Co má rozhodnout model? Co má udělat nástroj? Jaké jsou hranice oprávnění? A jak poznáme, že výsledek je správně?**

Jakmile na ně umíme odpovědět, AI přestává být kouzelná skříňka a začíná být inženýrský materiál.
'''
write(p,meta(t))

# Personal shift diagram.
boxes=[
(70,205,300,170,'MODEL-CENTRIC','Který model je nejlepší?|Kolik má parametrů?|Kdo vede benchmark?','#ff8e7a'),
(450,205,300,170,'SYSTEM-CENTRIC','Jaká data vidí?|Jaké má nástroje?|Jak výsledek ověřím?','#63d7a5'),
(830,205,300,170,'VALUE-CENTRIC','Je výsledek správný?|Je bezpečný?|Je lepší než baseline?','#45c7ff'),
(350,455,500,115,'POSUN','model → systém → měřitelný výsledek','#8b7cff')]
arrows=[(380,290,440,290),(760,290,820,290),(600,390,600,445)]
s=svg_screen('Od modelu k systému','Nejdůležitější změna pohledu není větší model, ale lepší otázky kolem něj.',boxes,arrows,'Schopnost modelu je vstup. Hodnota je vlastnost celého workflow.')
write(BOOK/'assets/diagrams/33-model-to-system.svg',s)
write(BOOK/'assets/diagrams-print/33-model-to-system.svg',printify(s))

# ------------------------------------------------------------------
# 34. Make roadmap print-stable + explicit takeaways.
# ------------------------------------------------------------------
p=chapter(34); t=read(p)
t=t.replace('To jsou zkušenosti, které se z tutorialu získávají těžko — a přesně ty budu průběžně doplňovat do přílohy G.',
'''To jsou zkušenosti, které se z tutorialu získávají těžko. Příloha G proto používá stejný experimentální formát: konfigurace, metriky, selhání, evidence a to, co se po výsledku změnilo.''')
if '## Co si z kapitoly odnést' not in t:
    closing='''\n## Co si z kapitoly odnést\n\n1. **Další učení má končit artefaktem nebo měřením, ne pouze další poznámkou.**\n2. **Nejdřív stavím jednoduchý systém, který umím změřit; teprve potom přidávám memory, multi-agent nebo větší autonomii.**\n3. **Důkaz porozumění není počet přečtených článků, ale schopnost vysvětlit konkrétní failure mode z evidence.**\n4. **Experiment log je součást znalosti — bez konfigurace, metrik a selhání se zkušenost těžko reprodukuje.**\n\n'''
    marker='Poslední část knihy už není teorie.'
    t=t.replace(marker,closing+marker,1)
write(p,meta(t))

# ------------------------------------------------------------------
# 36. Add the diagnostic model that readers can reuse after the book.
# ------------------------------------------------------------------
p=chapter(36); t=read(p)
if '## Když AI selže: kde hledat chybu' not in t:
    marker='\n## Kdy přejít na další projekt\n'
    block='''\n## Když AI selže: kde hledat chybu\n\nJedna z nejdražších reakcí na špatný AI výsledek je automaticky říct: **potřebujeme chytřejší model**. Někdy je to pravda. Často ale selhala jiná vrstva.\n\n<!-- visual:36-debug-ai-system.svg -->\n\n![Diagnostika AI systému](assets/diagrams/36-debug-ai-system.svg)\n\n*Obrázek: Výměna modelu je až jedna z možných oprav. Produkční chyba často vzniká v datech, retrievalu, nástroji, oprávněních nebo verifikaci.*\n\nPři debuggingu bych šel v tomto pořadí:\n\n| Vrstva | První otázka | Typická oprava |\n|---|---|---|\n| **Data / provenance** | Pracujeme se správnou revizí a autoritativním zdrojem? | metadata, ownership, versioning |\n| **Retrieval / context** | Dostal model právě ty informace, které potřeboval? | filtering, hybrid search, reranking, menší context |\n| **Tools** | Zavolal správný nástroj se správnými argumenty a četl správný výstup? | užší schema, validace, lepší error contract |\n| **Permissions / policy** | Směl udělat správnou akci — a nebyl action space zbytečně široký? | least privilege, policy gate, approval |\n| **State / orchestration** | Neztratil stav, neopakuje krok nebo nepracuje se starým výsledkem? | explicitní state, checkpoint, idempotence |\n| **Verification / evals** | Umíme vůbec poznat, že odpověď nebo akce je chybná? | test, rule, simulator, judge, human rubric |\n| **Model** | Teprve teď: chybí skutečně schopnost reasoning, codingu nebo modality? | jiný model, reasoning budget, specializace |\n\n> **Nejprve oprav vrstvu, která selhala. Větší model není univerzální náplast na špatně navržený systém.**\n\nTento diagnostický postup je možná nejpraktičtější zkratka celé knihy.\n'''
    if marker not in t: raise RuntimeError('ch36 marker missing')
    t=t.replace(marker,'\n'+block+marker,1)
# Stronger final landing.
old='''Tím se kruh knihy uzavírá.\n\nZačali jsme otázkou, co vlastně AI je.\n\nKončíme systémem, který dokážeme postavit, změřit, omezit, ověřit a postupně zlepšovat.'''
new='''Tím se kruh knihy uzavírá.\n\nZačali jsme otázkou, co vlastně AI je. Končíme systémem, který dokážeme postavit, změřit, omezit, ověřit a postupně zlepšovat.\n\nAž příště uvidíte působivé AI demo, zkuste se nezeptat pouze:\n\n> „Jaký model to je?“\n\nPoložte ještě pět otázek:\n\n> **Odkud má data? Co skutečně vidí? Jaké má nástroje? Co smí udělat? A jak víme, že výsledek je správně?**\n\nV těchto otázkách podle mě leží rozdíl mezi AI, která umí udělat dojem, a AI, na které lze stavět skutečnou práci.'''
t=t.replace(old,new)
write(p,meta(t))

# Debug signature diagram.
boxes=[]
labels=[
('1','DATA','správný zdroj · revize','#63d7a5'),
('2','CONTEXT','retrieval · relevance','#8b7cff'),
('3','TOOLS','arguments · outputs','#ffca6a'),
('4','POLICY','permissions · approval','#ff8e7a'),
('5','STATE','loop · checkpoint','#45c7ff'),
('6','VERIFY','tests · evals','#63d7a5'),
('7','MODEL','capability · reasoning','#8b7cff')]
for i,(num,head,body,stroke) in enumerate(labels):
    x=45+i*164
    boxes.append((x,220,145,150,f'{num} · {head}',body.replace(' · ','|'),stroke))
arrows=[]
for i in range(6): arrows.append((190+i*164,295,205+i*164,295))
s=svg_screen('Když AI selže, kde hledat chybu','Nehledám automaticky „lepší model“. Nejprve lokalizuji vrstvu, která selhala.',boxes,arrows,'Model je až jedna z možných příčin. Debugujeme systém, ne značku.')
write(BOOK/'assets/diagrams/36-debug-ai-system.svg',s)
write(BOOK/'assets/diagrams-print/36-debug-ai-system.svg',printify(s))

# ------------------------------------------------------------------
# Bibliography: final-book wording + centralized fast-changing sources.
# ------------------------------------------------------------------
bib=BOOK/'BIBLIOGRAPHY.md'
write(bib,'''# Zdroje, primární dokumentace a další čtení

Tato kniha rozlišuje **stabilnější principy** a **rychle se měnící snapshoty**. U historie a základních konceptů proto uvádím původní nebo kanonické práce; u modelů, nástrojů, bezpečnosti a regulace dávám přednost primární dokumentaci výrobce, standardu nebo regulátora.

U rychle se měnících produktových faktů platí jednoduché pravidlo: **aktuální primární zdroj má vždy přednost před tištěným snapshotem této knihy.**

## Historie a základy

1. Alan M. Turing — *On Computable Numbers, with an Application to the Entscheidungsproblem*, 1936.
2. Warren McCulloch, Walter Pitts — *A Logical Calculus of the Ideas Immanent in Nervous Activity*, 1943.
3. Alan M. Turing — *Computing Machinery and Intelligence*, Mind, 1950.
4. John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon — *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 1955/1956.
5. Frank Rosenblatt — práce o perceptronu, 1957–1958.
6. Marvin Minsky, Seymour Papert — *Perceptrons*, 1969.
7. David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams — *Learning representations by back-propagating errors*, Nature, 1986.
8. Yann LeCun et al. — *Gradient-Based Learning Applied to Document Recognition*, 1998.
9. Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton — *ImageNet Classification with Deep Convolutional Neural Networks*, 2012.

## Transformers, LLM a post-training

10. Ashish Vaswani et al. — *Attention Is All You Need*, 2017 — https://arxiv.org/abs/1706.03762
11. Tom B. Brown et al. — *Language Models are Few-Shot Learners*, 2020 — https://arxiv.org/abs/2005.14165
12. Long Ouyang et al. — *Training language models to follow instructions with human feedback*, 2022 — https://arxiv.org/abs/2203.02155

## Retrieval a RAG

13. Patrick Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, 2020 — https://arxiv.org/abs/2005.11401

## Agenti, tool use a orchestrace

14. Shunyu Yao et al. — *ReAct: Synergizing Reasoning and Acting in Language Models*, 2022/2023 — https://arxiv.org/abs/2210.03629
15. Model Context Protocol — official documentation — https://modelcontextprotocol.io/
16. Model Context Protocol — specification release 2026-07-28 — https://blog.modelcontextprotocol.io/posts/2026-07-28/
17. MCP Architecture — https://modelcontextprotocol.io/docs/learn/architecture
18. MCP server concepts — https://modelcontextprotocol.io/docs/learn/server-concepts
19. MCP Agent Skills — https://modelcontextprotocol.io/docs/2026-07-28/develop/build-with-agent-skills
20. OpenAI Agents SDK — https://openai.github.io/openai-agents-python/
21. Pydantic AI — https://ai.pydantic.dev/
22. LangGraph — https://docs.langchain.com/oss/python/langgraph/overview

## Lokální inference a praktický stack

23. llama.cpp — https://github.com/ggml-org/llama.cpp
24. Ollama — https://ollama.com/
25. vLLM — https://vllm.ai/
26. Open WebUI — https://openwebui.com/
27. Obsidian — https://obsidian.md/
28. Langfuse — https://langfuse.com/docs

## Security

29. OWASP GenAI Security Project — https://genai.owasp.org/
30. OWASP — Agentic AI threats and mitigations — https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
31. OWASP — GenAI Data Security Risks & Mitigations 2026 — https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
32. OWASP — State of Agentic AI Security and Governance — https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/

## Evropská regulace a privacy

33. European Commission — AI Act overview — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
34. European Commission — Guidelines on transparency obligations for providers and deployers of AI systems — https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
35. European Commission — Transparency obligations under Article 50 — https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
36. European Commission — GDPR principles — https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/principles-gdpr_en

## Snapshot modelů — 7. 8. 2026

37. OpenAI — GPT-5.6 — https://openai.com/index/gpt-5-6/
38. OpenAI — Model Release Notes — https://help.openai.com/en/articles/9624314-model-release-notes
39. Anthropic — Claude Fable 5 — https://www.anthropic.com/claude/fable
40. Anthropic — Claude Sonnet 5 — https://www.anthropic.com/news/claude-sonnet-5
41. Anthropic — Claude Opus 4.8 — https://www.anthropic.com/news/claude-opus-4-8
42. Google — Gemini API changelog — https://ai.google.dev/gemini-api/docs/changelog
43. Google — Gemini 3.6 Flash — https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash
44. xAI — Grok 4.5 — https://x.ai/news/grok-4-5
45. DeepSeek — API updates — https://api-docs.deepseek.com/updates
46. Qwen — Qwen3.6 — https://qwen.ai/blog?id=qwen3.6-35b-a3b
47. Google — Gemma 4 model card — https://ai.google.dev/gemma/docs/core/model_card_4
48. Mistral — Mistral Small 4 — https://mistral.ai/news/mistral-small-4/
49. Cohere — Command A+ — https://cohere.com/blog/command-a-plus
50. Cohere — Rerank / Transcribe changelog — https://docs.cohere.com/v2/changelog

## Jak tuto bibliografii používat

Pro pochopení principu začněte paperem nebo stabilní dokumentací. Pro rozhodnutí, co nasadit dnes, otevřete aktuální dokumentaci produktu a proveďte vlastní eval na svém use-case. **Kniha má být kompas; vendor stránka je aktuální mapa počasí.**
''')

# ------------------------------------------------------------------
# Style guide: add final-print and references rules.
# ------------------------------------------------------------------
p=BOOK/'STYLE_GUIDE.md'; t=read(p)
if '## 12. Final-print pravidla' not in t:
    t += '''\n\n## 12. Final-print pravidla\n\nVe čtenářském textu nesmí zůstat interní redakční proces:\n\n- „budu doplňovat“, „průběžně aktualizovat“, „pracovní závěr“, „redakční oprava“ apod.;\n- poznámky určené autorovi nebo reviewerovi;\n- odkazy na neexistující / přejmenované sekce;\n- verze kapitol, které odporují master indexu.\n\nTištěná verze je **časově označený snapshot**, ne otevřený TODO seznam. Budoucí aktualizace patří do další edice.\n\n## 13. Jak kapitola končí\n\nKapitola má pokud možno skončit jednou z těchto věcí:\n\n1. praktickým takeaway,\n2. silnou syntézou,\n3. otázkou, která přirozeně otevírá další kapitolu.\n\nSamostatný seznam URL nemá být posledním dojmem z kapitoly. Primární URL soustřeďujeme do `BIBLIOGRAPHY.md` a snapshotových příloh.\n\n## 14. WOW bez lacinosti\n\n„WOW“ v této knize nevytváří dekorace, ale **komprese složité myšlenky do obrazu nebo věty**.\n\n- žádní generičtí roboti, mozky, neonové AI motivy ani stocková ikonografie;\n- podpisové diagramy mají být použitelné i samostatně a vysvětlit princip do 20 sekund;\n- textový callout musí být pravdivý i bez typografického efektu;\n- méně výrazných vizuálů, ale každý musí nést vlastní myšlenku.\n'''
write(p,t)

# ------------------------------------------------------------------
# Print visual guide count and philosophy.
# ------------------------------------------------------------------
p=BOOK/'PRINT_VISUAL_GUIDE.md'; t=read(p)
t=t.replace('Vygenerováno variant: **39**.','Vygenerováno variant: **43 screen + 43 print**.')
if '## Podpisové diagramy' not in t:
    t += '''\n\n## Podpisové diagramy\n\nTři vizuály mají fungovat jako mentální páteř knihy:\n\n- `00-ai-system-stack.svg` — **Od modelu k hodnotě**;\n- `33-model-to-system.svg` — **Od model-centric k system-centric pohledu**;\n- `36-debug-ai-system.svg` — **Když AI selže, kde hledat chybu**.\n\nNejsou dekorací. Každý komprimuje rozhodovací princip, který se opakuje napříč knihou.\n'''
write(p,t)

# ------------------------------------------------------------------
# Index / README positioning and version.
# ------------------------------------------------------------------
p=BOOK/'00 - INDEX.md'; t=read(p)
t=re.sub(r'^subtitle:.*$', 'subtitle: "Jak AI skutečně funguje, jak ji používat a jak z modelů stavět spolehlivé systémy"', t, count=1, flags=re.M)
t=re.sub(r'^version:.*$', 'version: "0.7"', t, count=1, flags=re.M)
t=t.replace('> **Obsidian master index — v0.6 final hybrid**  \n> Claude redakční vrstva + Gemini technické doplňky + fact-check primárních zdrojů.',
'''> **Obsidian master index — v0.7 print candidate**  
> Finální redakční pass: technická hloubka, autorský hlas, podpisové diagramy a centralizované zdroje.''')
write(p,t)

p=BOOK/'README.md'
if p.exists():
    t=read(p)
    t=t.replace('book_final — v0.6','book_final — v0.7')
    t=t.replace('Finální hybridní review varianta','Finální redakční print-candidate varianta')
    t=t.replace('**36 kapitol + úvod + 7 příloh**','**36 kapitol + úvod + 7 příloh**')
    write(p,t)

# Normalize metadata versions on manuscripts and appendices.
for p in [intro]+sorted([x for x in BOOK.glob('[0-9][0-9] - *.md') if not x.name.startswith('00 -')])+sorted((BOOK/'appendices').glob('*.md')):
    write(p,meta(read(p)))

# Permanent editorial report draft; audit scripts may add numbers later.
write(BOOK/'FINAL_EDITORIAL_AUDIT_V07.md','''# Finální redakční audit před tiskem — v0.7\n\n## Redakční záměr\n\nCílem této verze není přidat další obsah pro obsah samotný. Cílem je, aby rukopis fungoval současně jako:\n\n- vstup do AI pro nováčka s technickým uvažováním,\n- praktický manuál pro člověka, který už AI používá,\n- engineering reference pro návrh RAG, tool-use a agentních systémů,\n- autorská kniha s jasnou tezí, nikoli anonymní katalog technologií.\n\n## Co bylo změněno\n\n- zesílen úvod a hlavní teze knihy;\n- přidáno **Dvanáct pravidel praktické AI** jako mentální mapa;\n- přidány tři podpisové diagramy bez dekorativního „AI art“ stylu;\n- odstraněny interní redakční poznámky a living-draft formulace;\n- opraveny číselné cross-reference po předchozím merge;\n- osobní kapitola 33 dostala definitivní závěr a silnější autorský hlas;\n- kapitola 36 dostala praktický diagnostický model pro debugging AI systémů;\n- surové URL seznamy byly přesunuty z konců kapitol do centrální bibliografie;\n- bibliografie byla přepsána jako finální zdrojová vrstva, nikoli pracovní seznam;\n- subtitle byl změněn z pracovního deníkového rámování na jasný čtenářský příslib.\n\n## Hlavní teze\n\n> **Nejdůležitější není mít nejchytřejší model, ale umět mu ve správný okamžik dodat správný kontext a nástroje — a jeho výsledek spolehlivě ověřit.**\n\n## Co zůstává záměrně beze změny\n\nNejsilnější technické kapitoly nebyly „literárně přepisovány“ jen proto, aby vypadaly nové. Zejména enterprise data/RAG, agentní smyčka, bezpečnost a evaluace už mají správnou informační hustotu a engineering charakter.\n\n## Produkční věci, které nejsou redakční chybou rukopisu\n\nPřed skutečným tiskem ještě musí být definitivně rozhodnuto / ověřeno:\n\n- přesné autorské jméno na titulní straně a obálce;\n- tiráž, copyright, vydavatel/imprint a ISBN;\n- finální obálka, hřbet a zadní strana;\n- parametry konkrétní tiskárny, bleed a případný CMYK workflow;\n- fyzický nátisk a kontrola čitelnosti diagramů a tabulek na papíře.\n\nTyto body nejsou důvodem k dalšímu přepisování textu. Jsou to poslední výrobní gates.\n''')

print('final award edit v0.7 applied')
