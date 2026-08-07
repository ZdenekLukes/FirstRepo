# 3. Jak funguje LLM — bez matematiky

Velký jazykový model působí při používání téměř magicky. Napíšeme otázku a během několika sekund dostaneme odpověď, která může připomínat text napsaný člověkem. Model dokáže vysvětlovat, programovat, překládat, shrnovat dokumenty nebo diskutovat o problému.

Pod povrchem však není malý člověk, encyklopedie ani databáze předem připravených odpovědí.

Základní princip je překvapivě jednoduchý:

> **LLM dostane dosavadní text a opakovaně odhaduje, co by mělo následovat.**

Jeden token za druhým.

To samo o sobě zní téměř příliš primitivně. Důležité je však měřítko: model se tuto úlohu učil na obrovském množství textu a uvnitř má miliardy parametrů, které zachycují komplikované vztahy mezi slovy, pojmy, strukturami, jazyky a vzory.

Výsledkem už není obyčejné doplňování slov jako na mobilní klávesnici.

Vzniká systém, který si během tréninku vytvořil velmi rozsáhlou statistickou reprezentaci jazyka a světa popsaného v jazyce.

Tato kapitola nevysvětluje matematiku Transformeru. Cílem je vytvořit mentální model dostatečně přesný na to, abychom později pochopili:

- proč LLM někdy halucinuje,
- proč je důležitý context window,
- proč model potřebuje RAG a nástroje,
- proč nový chat začíná prakticky „od nuly“,
- co znamená training a inference,
- proč velký model potřebuje tolik GPU paměti,
- proč může stejná otázka dostat různé odpovědi,
- a proč samotný model ještě není agent.

---

## 3.1 LLM není databáze odpovědí

Jedna z nejčastějších chybných představ je:

> „Model má uvnitř obrovskou databázi textů a při otázce najde správnou odpověď.“

Takto běžný LLM nefunguje.

Při tréninku sice viděl obrovské množství textových dat, ale typicky si je neukládá jako dokumenty, ve kterých by později vyhledával.

Nemá uvnitř něco jako:

```text
Wikipedia/
    Prague.md
    Einstein.md
    Transformer.md

Books/
    Physics/
    History/
```

Místo toho se během tréninku mění miliardy číselných parametrů modelu.

Velmi zjednodušeně:

```text
trénovací data
      ↓
učení vztahů a vzorů
      ↓
miliardy parametrů
      ↓
model
```

Model tedy obsahuje něco spíše podobného **komprimovanému systému vztahů** než knihovně dokumentů.

Proto například může vědět, že:

- Praha je hlavní město České republiky,
- tranzistor MOSFET má gate, source a drain,
- Paříž souvisí s Francií,
- Python používá odsazování,
- slovo „pes“ významově souvisí se slovy „zvíře“, „štěně“ nebo „štěkat“.

Ale pokud se zeptáme:

> „Ve které větě dokumentu ABC.pdf jsme minulý měsíc změnili specifikaci LDO?“

model to bez přístupu k tomuto dokumentu vědět nemůže.

A právě tady později vstupují do hry:

- context,
- file search,
- RAG,
- databáze,
- web search,
- nástroje,
- agentní systémy.

---

## 3.2 Text se rozděluje na tokeny

LLM ve skutečnosti nepracuje přímo se slovy ani s písmeny.

Pracuje s **tokeny**.

Než se text dostane do neuronové sítě, tokenizer jej rozdělí na menší části.

Například věta:

> Umělá inteligence mění způsob práce.

může být rozdělena přibližně jako:

```text
Um
ělá
 inteligence
 mění
 způsob
 práce
.
```

Konkrétní rozdělení závisí na tokenizeru daného modelu.

Token tedy může být:

- celé slovo,
- část slova,
- interpunkční znaménko,
- číslo,
- kus programového kódu,
- někdy jen několik znaků.

Pro angličtinu lze jako velmi hrubé pravidlo použít:

> **1 token ≈ ¾ slova**

U češtiny může být situace méně výhodná, protože čeština má mnoho tvarů slov a tokenizace je často rozděluje na více částí.

---

## 3.3 Co je token

Token je základní jednotka, kterou model zpracovává.

To má několik praktických důsledků.

### Cena

Cloudové API služby často účtují právě počet tokenů.

Například:

```text
1 000 tokenů vstupu
+
500 tokenů výstupu
=
1 500 zpracovaných tokenů
```

### Context window

Pokud model podporuje například context window 128 000 tokenů, neznamená to 128 000 slov.

Jde o 128 000 tokenů zahrnujících například:

- system prompt,
- historii konverzace,
- naši otázku,
- vložené dokumenty,
- výsledky nástrojů,
- předchozí odpovědi modelu.

### Výpočetní náročnost

Čím více tokenů model zpracovává, tím více práce musí během inference vykonat.

Proto může být:

```text
„Shrň tento odstavec.“
```

výrazně levnější a rychlejší úloha než:

```text
„Prostuduj těchto 300 stran dokumentace a porovnej všechny změny.“
```

---

## 3.4 Co znamenají embeddings

Model nemůže pracovat přímo se slovem:

```text
tranzistor
```

Neuronová síť pracuje s čísly.

Proto musí být každý token převeden na číselnou reprezentaci.

Vznikne takzvaný **embedding**.

Můžeme si jej představit jako dlouhý seznam čísel:

```text
tranzistor
      ↓
[0.13, -0.42, 0.78, ...]
```

Samotná čísla pro člověka nic intuitivního neznamenají.

Důležitá je jejich vzájemná struktura.

Podobné pojmy mají v tomto vícerozměrném prostoru podobné reprezentace.

Například:

```text
king
queen
man
woman
```

budou mít určité systematické vztahy.

Podobně:

```text
MOSFET
gate
transistor
semiconductor
```

budou významově blíže než například:

```text
MOSFET
banana
opera
volcano
```

Embedding je tedy jeden ze způsobů, jak převést význam do formy, se kterou může neuronová síť matematicky pracovat.

Stejný základní princip později využijeme také u RAG:

```text
dokument
→ embedding
→ hledání významově podobných částí
```

Je ale dobré rozlišovat:

- embeddings uvnitř LLM,
- embedding model používaný například pro vyhledávání dokumentů.

Princip je podobný, použití se liší.

---

## 3.5 Transformer

Moderní LLM stojí převážně na architektuře nazývané **Transformer**.

Transformer byl představen v roce 2017 v práci *Attention Is All You Need*.

Jeho zásadní vlastností je schopnost efektivně hledat vztahy mezi různými částmi vstupní sekvence.

Představme si větu:

> Petr dal knihu Pavlovi, protože ji už nepotřeboval.

Abychom větě rozuměli, musíme chápat vztahy mezi:

- Petrem,
- knihou,
- Pavlem,
- zájmenem „ji“,
- slovesem „potřeboval“.

Model tedy nemůže každé slovo zpracovávat zcela izolovaně.

Musí chápat jeho význam v kontextu ostatních slov.

Transformer právě toto umožňuje velmi efektivně.

---

## 3.6 Attention — proč je tak důležitá

Jedním z klíčových mechanismů Transformeru je **attention**.

Český překlad „pozornost“ může být trochu zavádějící, ale základní myšlenka je jednoduchá:

> Když model zpracovává určitý token, zjišťuje, které jiné tokeny jsou pro jeho interpretaci důležité.

Například:

> Kočka seděla na okně, protože **tam** bylo teplo.

Pro pochopení slova „tam“ je důležité slovo „okně“.

Attention může vytvořit silný vztah:

```text
tam
 ↑
okně
```

V jiné větě:

> Tranzistor M1 zvýšil proud, protože se zvýšilo jeho gate voltage.

budou důležité jiné vztahy.

Model má přitom mnoho attention mechanismů paralelně.

Jedna část může sledovat například:

- gramatické vztahy,

jiná:

- význam,

jiná:

- reference mezi vzdálenými částmi textu,

jiná:

- strukturu zdrojového kódu.

Nemusíme přesně vědět, co každý konkrétní attention head reprezentuje.

Pro náš mentální model stačí:

> **Attention umožňuje modelu průběžně zjišťovat, které části kontextu jsou pro aktuální výpočet relevantní.**

---

## 3.7 Jak model předpovídá další token

Teď přichází jádro celé věci.

Představme si vstup:

> Hlavním městem České republiky je

Model vytvoří pravděpodobnosti možných pokračování.

Velmi zjednodušeně:

```text
Praha       96 %
Brno         1 %
Evropa       0,2 %
Česko        0,1 %
...
```

Vybere další token:

```text
Praha
```

Text nyní vypadá:

> Hlavním městem České republiky je Praha

Model provede výpočet znovu.

Může následovat například:

```text
.        89 %
,         4 %
a         2 %
...
```

A znovu.

A znovu.

Celá odpověď vzniká **autoregresivně**:

```text
prompt
↓
token 1
↓
prompt + token 1
↓
token 2
↓
prompt + token 1 + token 2
↓
token 3
↓
...
```

Model tedy zpravidla nevytvoří celou odpověď najednou.

Generuje ji postupně.

---

## 3.8 Proč z jednoduchého principu vzniká složité chování

Právě zde vzniká jedna z nejzajímavějších otázek moderní AI.

Jak může systém pro předpovídání dalšího tokenu:

- programovat,
- překládat,
- sumarizovat,
- řešit logické problémy,
- analyzovat smlouvu,
- vysvětlovat fyziku?

Odpověď je v samotném problému, který musí při tréninku řešit.

Aby model správně dokončil například:

> Pokud je odpor 100 Ω a proud 10 mA, napětí je…

nestačí znát gramatiku.

Musí se naučit vztah mezi:

- napětím,
- proudem,
- odporem.

Aby správně dokončil program:

```python
for i in range(10):
```

musí se naučit mnoho struktur programovacího jazyka.

Aby dokončil příběh, musí se naučit něco o:

- lidech,
- chování,
- příčinách,
- čase,
- vztazích.

Extrémně dobré předpovídání textu tedy vyžaduje vytvoření velmi bohatého modelu struktur, které se v textu vyskytují.

To neznamená, že LLM rozumí světu stejně jako člověk.

Ale jednoduchá formulace:

> „LLM jen hádá další slovo.“

může být stejně zavádějící jako říci:

> „Počítač jen přepíná nuly a jedničky.“

Technicky je to do určité míry pravda.

Prakticky to téměř nic nevysvětluje.

---

## 3.9 Training vs. inference

Pro další kapitoly je zásadní rozlišovat dvě úplně odlišné fáze.

### Training

Training znamená vytváření nebo úpravu modelu.

```text
data
↓
výpočty
↓
změna parametrů modelu
↓
lepší model
```

Training velkého frontier LLM může vyžadovat:

- obrovské datasety,
- tisíce nebo desítky tisíc akcelerátorů,
- týdny až měsíce výpočtů,
- složitou infrastrukturu,
- obrovské finanční náklady.

### Inference

Inference znamená používání již natrénovaného modelu.

```text
hotový model
+
prompt
↓
odpověď
```

Když spustíme například lokální model přes Ollama, typicky **netrénujeme model**.

Provádíme inference.

Toto rozlišení je důležité, protože začátečníci často říkají:

> „Nahraju modelu svoje dokumenty a natrénuji ho na nich.“

Ve většině praktických systémů se nic takového neděje.

Dokumenty se spíše:

- vloží do context window,
- vyhledají pomocí RAG,
- připojí jako data,
- nebo zpřístupní přes nástroje.

Model samotný zůstane nezměněný.

---

## 3.10 Pre-training

První velká fáze tvorby LLM se obvykle nazývá **pre-training**.

Model dostává obrovské množství textu a učí se předpovídat další token.

Na začátku má parametry prakticky náhodné.

Jeho odpovědi by byly nesmyslné.

Postupně se učí.

Velmi schematicky:

```text
„Hlavním městem Francie je …“

model: „banana“

správný text: „Paříž“

↓
výpočet chyby
↓
malá změna parametrů
```

Toto proběhne nesčetněkrát.

Model postupně získává znalosti o:

- jazyce,
- světě,
- programování,
- stylu textů,
- vědě,
- logických strukturách,
- vztazích mezi pojmy.

Výsledkem však ještě nemusí být dobrý chatbot.

Máme hlavně velmi schopný **base model**.

---

## 3.11 Post-training

Base model umí pokračovat v textu, ale nemusí se chovat tak, jak očekává uživatel.

Když se například zeptáme:

> Jak funguje tranzistor?

base model může pokračovat jako internetová diskuse, článek nebo jiný text.

Chceme ale něco jiného:

```text
uživatel položí otázku
↓
model pochopí instrukci
↓
odpoví užitečně
```

Proto následuje **post-training**.

Jeho cílem může být například:

- lepší plnění instrukcí,
- reasoning,
- používání nástrojů,
- bezpečnější chování,
- preferovaný styl odpovědí,
- schopnost strukturovat výstup.

Moderní post-training je velmi významná část vývoje modelu.

Stejný základní model se může po rozdílném post-trainingu chovat výrazně odlišně.

---

## 3.12 Instruction tuning

Jednou z metod post-trainingu je **instruction tuning**.

Model se učí na příkladech typu:

```text
Instrukce:
Shrň následující text do tří bodů.

Text:
...

Očekávaná odpověď:
1. ...
2. ...
3. ...
```

Nebo:

```text
Uživatel:
Napiš Python funkci pro výpočet průměru.

Asistent:
def average(...):
```

Model se tak neučí pouze jazyk.

Učí se vzor:

> **instrukce → požadovaná akce**

To je jeden z důvodů, proč dnešní assistant modely reagují přirozeně na věty jako:

- shrň,
- porovnej,
- oprav,
- vysvětli,
- napiš,
- analyzuj,
- vytvoř tabulku.

---

## 3.13 Reinforcement learning

Další skupina metod využívá zpětnou vazbu k tomu, aby model preferoval lepší chování.

Zjednodušeně si můžeme představit:

```text
otázka
↓
několik možných odpovědí
↓
hodnocení
↓
model se učí preferovat lepší odpověď
```

Hodnocení může pocházet:

- od lidí,
- od jiných modelů,
- z automaticky ověřitelného výsledku,
- z kombinace několika metod.

U matematického problému lze například ověřit správnost výsledku.

U programování lze spustit testy.

U reasoning modelů se post-training používá mimo jiné k posílení schopnosti řešit problémy ve více krocích.

Důležité je uvědomit si:

> schopnosti modelu nevznikají pouze pre-trainingem.

V roce 2026 je právě kvalita post-trainingu jedním z významných rozdílů mezi modely.

---

## 3.14 Context window

Model má při každém požadavku omezené množství informací, které může současně zpracovat.

Tento prostor nazýváme **context window**.

Můžeme si jej představit jako pracovní stůl.

Model může mít ve své „hlavě“ mnoho obecných znalostí získaných tréninkem, ale při řešení konkrétní úlohy má před sebou právě obsah tohoto pracovního stolu.

Na něm mohou být:

```text
INSTRUKCE APLIKACE

HISTORIE KONVERZACE

DOKUMENT

VÝSLEDEK WEB SEARCH

VÝSLEDEK RAG

UŽIVATELSKÁ OTÁZKA

PŘEDCHOZÍ KROKY AGENTA
```

To všechno spotřebovává tokeny.

Pokud je context window například 128k tokenů, všechny tyto informace se musí vejít do tohoto limitu.

---

## 3.15 System prompt, user prompt a další části kontextu

To, co uživatel napíše do chatovacího okna, nemusí být celý prompt, který model skutečně dostane.

Reálná aplikace může sestavit například tento kontext:

```text
INSTRUKCE APLIKACE:
Technický asistent, odpovědi česky.

PRAVIDLA PRÁCE S DOKUMENTY:
Při odpovědi uvést zdroj.

PAMĚŤ:
Uživatel pracuje na projektu X.

DOKUMENT:
[relevantní část dokumentu]

VÝSLEDEK NÁSTROJE:
[výsledek databázového dotazu]

OTÁZKA UŽIVATELE:
Jaká byla maximální teplota v testu?
```

Model dostane tento výsledný kontext a na jeho základě generuje odpověď.

To je velmi důležitý mentální posun:

> **LLM aplikace není jen model. Je to systém, který modelu připravuje správný kontext.**

Právě tato myšlenka nás později dovede ke **context engineeringu**.

---

## 3.16 Temperature a sampling

Model při generování nevytváří pouze jeden možný další token.

Vytváří distribuci pravděpodobností.

Například:

```text
rychlý       38 %
výkonný      27 %
moderní      15 %
nový          8 %
...
```

Aplikace musí rozhodnout, který token skutečně vybere.

K tomu existují různé sampling parametry.

Nejznámější je **temperature**.

Velmi zjednodušeně:

### Nízká temperature

Model více preferuje nejpravděpodobnější varianty.

Výstup bývá:

- konzistentnější,
- předvídatelnější,
- méně kreativní.

### Vyšší temperature

Model více připouští méně pravděpodobné možnosti.

Výstup může být:

- pestřejší,
- kreativnější,
- ale také méně stabilní.

Proto může být vhodné jiné nastavení pro:

```text
extrakci hodnot ze specifikace
```

a jiné pro:

```text
vymysli deset neobvyklých názvů produktu
```

---

## 3.17 Proč stejný prompt nemusí dát stejnou odpověď

Klasický software si často představujeme deterministicky.

Například:

```python
2 + 2
```

vždy vrátí:

```text
4
```

LLM však pracuje s pravděpodobnostmi.

Proto dvě spuštění stejného promptu mohou vytvořit mírně nebo výrazně odlišný text.

To má zásadní význam pro firemní automatizaci.

Pokud postavíme systém:

```text
LLM → důležité obchodní rozhodnutí
```

nemůžeme automaticky očekávat absolutně stabilní výsledek.

Potřebujeme například:

- validaci,
- structured output,
- deterministické nástroje,
- testy,
- guardrails,
- human approval,
- evaluaci.

Čím důležitější je úloha, tím méně bychom měli spoléhat pouze na volně generovaný text.

---

## 3.18 Co se děje od stisku Enter po odpověď

Spojme si nyní celý proces.

Napíšeme například:

> Vysvětli mi rozdíl mezi RAM a VRAM.

### Krok 1 — Aplikace sestaví kontext

Chatovací aplikace může spojit:

```text
instrukce aplikace
+
historii konverzace
+
memory
+
uživatelskou otázku
```

Výsledkem je vstup pro model.

### Krok 2 — Tokenizace

Text se převede na tokeny.

```text
text
↓
tokenizer
↓
[1543, 81, 9921, ...]
```

Čísla zde reprezentují jednotlivé tokeny ve slovníku modelu.

### Krok 3 — Embeddings

Každý token se převede na numerickou reprezentaci, se kterou může neuronová síť pracovat.

### Krok 4 — Transformer zpracuje kontext

Informace procházejí mnoha vrstvami neuronové sítě.

Attention mechanismy průběžně vyhodnocují vztahy mezi tokeny.

Vzniká interní reprezentace významu aktuálního kontextu.

### Krok 5 — Model vypočítá možné pokračování

Na konci vznikne rozdělení pravděpodobností pro další token.

Například:

```text
RAM     ...
VRAM    ...
Paměť   ...
Rozdíl  ...
```

Podle sampling strategie je vybrán jeden token.

### Krok 6 — Token se přidá k odpovědi

Například:

```text
RAM
```

Nyní už máme:

```text
Vysvětli mi rozdíl mezi RAM a VRAM.

RAM
```

### Krok 7 — Výpočet se opakuje

Model vypočítá další token:

```text
je
```

Potom:

```text
obecná
```

Potom:

```text
operační
```

A pokračuje.

Na obrazovce proto odpověď často vidíme přicházet postupně.

### Krok 8 — Model skončí

Generování se zastaví například:

- dosažením vhodného konce odpovědi,
- speciálním end tokenem,
- dosažením limitu tokenů,
- rozhodnutím aplikace,
- nebo požadavkem na použití nástroje.

Výsledkem je odpověď, kterou vidíme.

---

# Jeden obrázek, který vysvětluje téměř celou kapitolu

Celý základ LLM lze shrnout takto:

```text
                    TRAINING
                       │
                       ▼
             obrovské množství dat
                       │
                       ▼
              učení parametrů
                       │
                       ▼
                HOTOVÝ MODEL
                       │
───────────────────────┼──────────────────────
                       │
                   INFERENCE
                       │
                       ▼
                  instrukce
                       +
                   kontext
                       │
                       ▼
                  tokenizer
                       │
                       ▼
                  embeddings
                       │
                       ▼
                  Transformer
                       │
                       ▼
              pravděpodobnosti
              dalšího tokenu
                       │
                       ▼
                vybraný token
                       │
                 ┌─────┘
                 │
                 └────────→ znovu
                       │
                       ▼
                    odpověď
```

---

# Ještě důležitější obrázek: model není systém

Po pochopení této kapitoly bychom měli vidět rozdíl mezi třemi věcmi.

## Samotný model

```text
PROMPT
   ↓
  LLM
   ↓
TEXT
```

To je nejjednodušší varianta.

## AI aplikace

```text
                 ┌── memory
                 │
                 ├── dokumenty
USER ──→ APP ────┼── web
                 │
                 ├── RAG
                 │
                 └── instructions
                         │
                         ▼
                        LLM
                         │
                         ▼
                      RESPONSE
```

Model už je pouze jednou součástí systému.

## Agent

Agent přidává další zásadní věc:

**smyčku a akce.**

```text
             ┌───────────────────┐
             │                   │
             ▼                   │
         OBSERVE                 │
             │                   │
             ▼                   │
           PLAN                  │
             │                   │
             ▼                   │
            ACT                  │
             │                   │
             ▼                   │
       TOOL / SYSTEM             │
             │                   │
             ▼                   │
           RESULT ───────────────┘
```

A právě proto není:

> **LLM = agent**

Stejně jako není:

> **motor = automobil**

LLM může být nejdůležitější inteligentní komponenta systému, ale celý užitečný systém potřebuje mnohem více.

---

# Praktický příklad: návrh integrovaného obvodu

Představme si otázku:

> Navrhni mi LDO se vstupním napětím 3,3 V, výstupem 1,8 V a proudem 100 mA.

Samotný LLM může ze svých naučených znalostí:

- vysvětlit vhodné topologie,
- navrhnout blokové schéma,
- diskutovat stabilitu,
- navrhnout testbench,
- napsat SPICE skeleton,
- upozornit na některé trade-offy.

Ale nemá automaticky:

- konkrétní PDK,
- modely tranzistorů,
- aktuální process corner,
- charakterizační data,
- Spectre,
- výsledky simulací,
- firemní design rules.

Samotný model tedy může například tvrdit:

> Toto řešení má phase margin přibližně 65°.

Pokud hodnotu pouze odhadl, není to engineering výsledek.

Správný systém vypadá spíše:

```text
               SPECIFIKACE
                    │
                    ▼
                   LLM
                    │
              návrh kandidáta
                    │
                    ▼
             Spectre / SPICE
                    │
                    ▼
            výsledky simulace
                    │
                    ▼
                   LLM
                    │
          interpretace výsledků
                    │
                    ▼
              změna návrhu
                    │
                    └─────────┐
                              │
                              ▼
                           simulace
```

Tady se dostáváme od:

**generativní AI**

k:

**AI-assisted engineering systému**

a později až k:

**agentnímu systému**.

---

# Co si z kapitoly zapamatovat

Pokud si čtenář z celé kapitoly odnese pouze několik myšlenek, měly by to být tyto:

### 1. LLM není databáze dokumentů

Znalosti jsou zakódované v parametrech modelu, nikoli uložené jako snadno dohledatelné stránky.

### 2. LLM pracuje s tokeny

Text se před zpracováním rozdělí na menší části.

### 3. Model generuje odpověď postupně

Předpovídá jeden další token a proces opakuje.

### 4. Transformer a attention umožňují pracovat s kontextem

Model hledá vztahy mezi různými částmi textu.

### 5. Training a inference jsou úplně jiné věci

Používání lokálního LLM obvykle není jeho trénování.

### 6. Context je pracovní paměť aktuální úlohy

Model vidí pouze informace, které mu aplikace v daném okamžiku předloží.

### 7. Výstup je pravděpodobnostní

LLM není klasická deterministická funkce.

### 8. Model může znít jistě, i když nemá správná data

Plynulost jazyka není důkaz pravdivosti.

### 9. Schopnost modelu závisí nejen na pre-trainingu

Velkou roli hraje post-training, instruction tuning a další optimalizace.

### 10. LLM není celý AI systém

Praktický systém obvykle vypadá spíše:

```text
MODEL
+
CONTEXT
+
DATA
+
MEMORY
+
TOOLS
+
WORKFLOW
+
VERIFICATION
+
HUMAN
```

A právě tato rovnice bude jedním z hlavních témat zbytku knihy.

---

# Mentální model kapitoly

Na začátku jsme měli:

> AI dostane otázku a nějak vymyslí odpověď.

Po této kapitole bychom měli mít mnohem přesnější představu:

```text
                 CO SE MODEL NAUČIL
                       TRAINING
                          │
                          ▼
                     PARAMETERS
                          │
                          │
                          ▼
USER ──→ CONTEXT ──→ TOKENIZER ──→ LLM
                                      │
                                      ▼
                              NEXT TOKEN
                                      │
                                      ▼
                              NEXT TOKEN
                                      │
                                      ▼
                                   ...
                                      │
                                      ▼
                                  RESPONSE
```

A ještě důležitější:

```text
                   AI SYSTEM

            ┌────── MODEL ──────┐
            │                   │
DATA ───────┤                   │
RAG ────────┤                   │
MEMORY ─────┤      CONTEXT      ├──→ RESULT
TOOLS ──────┤                   │
RULES ──────┤                   │
            │                   │
            └───────────────────┘
```

Samotný LLM je fascinující technologie.

Ale největší praktická hodnota začíná vznikat teprve tehdy, když jej správně zasadíme do celého systému.
