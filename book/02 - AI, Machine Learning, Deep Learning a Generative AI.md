# 2. AI, Machine Learning, Deep Learning a Generative AI

Když se dnes řekne **AI**, často se tím myslí ChatGPT, Claude, Gemini nebo jiný velký jazykový model. To je ale jen malá část mnohem širšího oboru.

Pojmy **Artificial Intelligence, Machine Learning, Neural Networks, Deep Learning, Generative AI, Foundation Model, LLM, Reasoning Model** a **Agentic AI** spolu souvisejí, ale nejsou zaměnitelné.

Nejjednodušší mentální model je představit si je jako postupně užší nebo specializovanější vrstvy:

```text
Artificial Intelligence (AI)
│
├── klasické algoritmické a pravidlové systémy
│
└── Machine Learning
    │
    ├── klasické ML metody
    │
    └── Neural Networks
        │
        └── Deep Learning
            │
            └── Generative AI
                │
                └── Foundation Models
                    │
                    ├── Large Language Models
                    ├── multimodální modely
                    ├── obrazové modely
                    └── další obecné modely
```

Tento obrázek není dokonalou akademickou taxonomií, ale jako praktický mentální model funguje velmi dobře. Důležité je pochopit, že dnešní generativní AI nevznikla jako úplně nový obor. Je výsledkem několika desetiletí vývoje strojového učení, neuronových sítí, hardwaru a dostupnosti obrovského množství dat.

---

## 2.1 Co znamená „AI“

**Artificial Intelligence neboli umělá inteligence** je nejširší pojem. Označuje systémy, které vykonávají činnosti, jež bychom při jejich vykonávání člověkem obvykle spojovali s inteligencí.

Může jít například o:

- rozpoznání objektu na fotografii,
- překlad textu,
- plánování trasy,
- hraní šachů,
- rozpoznání řeči,
- doporučení produktu,
- řízení robota,
- odpověď na otázku,
- napsání programu,
- nebo naplánování několika kroků potřebných ke splnění úkolu.

Důležité je, že **AI nemusí znamenat neuronovou síť ani LLM**.

Starší AI systémy byly často založené na ručně vytvořených pravidlech. Typickým příkladem byly expertní systémy:

```text
IF teplota > limit
AND tlak klesá
THEN vyhodnoť stav jako poruchový
```

Takový systém může působit inteligentně, přesto se nic neučí. Pouze vykonává logiku vytvořenou člověkem.

Proto je užitečné oddělit dvě věci:

> **AI je cíl nebo schopnost systému. Machine Learning je jeden ze způsobů, jak této schopnosti dosáhnout.**

Dnešní prudký rozvoj AI je způsoben především tím, že se velká část oboru přesunula od ručně programovaných pravidel k modelům, které se potřebné vzory naučí z dat.

---

## 2.2 Machine Learning

**Machine Learning (ML), neboli strojové učení**, je část AI, ve které systém neprogramujeme pouze pomocí explicitních pravidel. Místo toho mu poskytneme data a algoritmus z nich vytvoří model.

Klasický program může fungovat například takto:

```text
pravidla + vstupní data → výsledek
```

U Machine Learningu je princip jiný:

```text
data + příklady správných výsledků → trénování → model
```

A potom:

```text
nová data + model → predikce
```

Příklad může být jednoduchý filtr nevyžádané pošty.

Namísto ručního zapisování tisíců pravidel typu:

```text
pokud e-mail obsahuje „vyhráli jste milion“ → spam
```

můžeme modelu ukázat velké množství e-mailů označených jako **spam** nebo **not spam**. Model si během trénování najde statistické vzory, podle kterých dokáže klasifikovat nové zprávy.

Machine Learning tedy není databáze naučených odpovědí. Model se snaží zachytit **vztahy a vzory v datech**, které následně používá na nové vstupy.

Klasické ML se používá například pro:

- klasifikaci,
- predikci hodnot,
- detekci anomálií,
- doporučovací systémy,
- odhad rizika,
- rozpoznávání vzorů v měřeních,
- prediktivní údržbu.

Mnoho velmi užitečných AI systémů dodnes používá klasické ML a vůbec nepotřebuje LLM.

---

## 2.3 Neural Networks

**Neuronové sítě** jsou jednou z metod Machine Learningu.

Jejich název byl inspirován biologickými neurony, ale je dobré tuto podobnost nepřeceňovat. Umělá neuronová síť není digitální kopie lidského mozku. Jde o matematický výpočetní model sestavený z velkého množství jednoduchých propojených výpočetních jednotek.

Jednotlivé části sítě přijímají vstupy, transformují je a předávají dál. Během trénování se upravují hodnoty parametrů sítě tak, aby její výstupy stále lépe odpovídaly požadovanému výsledku.

Velkou výhodou neuronových sítí je schopnost naučit se složité vztahy, které bychom jen velmi obtížně zapisovali ručně.

Například při rozpoznávání fotografie kočky nemusíme programu popsat:

- jak přesně vypadá ucho,
- jaký tvar má oko,
- jak mají být rozmístěné vousy,
- jak kočka vypadá z různých úhlů,
- jak vypadá při různém osvětlení.

Síť může tyto charakteristické vzory postupně získat z velkého množství příkladů.

To byl zásadní posun: člověk již nemusel vždy přesně definovat **jak problém vyřešit**. Mohl definovat problém, dodat data a nechat model naučit se vhodnou reprezentaci sám.

---

## 2.4 Deep Learning

**Deep Learning** je část Machine Learningu založená na hlubokých neuronových sítích.

Slovo **deep** zde neznamená, že systém „hluboce přemýšlí“. Odkazuje na to, že síť obsahuje více vrstev zpracování.

Velmi zjednodušeně si lze představit, že jednotlivé vrstvy postupně vytvářejí složitější reprezentace vstupu.

U obrazu může první část sítě reagovat na jednoduché hrany a přechody. Další vrstvy mohou kombinovat tyto informace do složitějších tvarů a ještě vyšší vrstvy do reprezentací celých objektů.

Podobný princip funguje i u textu, zvuku a dalších dat.

Deep Learning se stal mimořádně úspěšný zejména díky kombinaci tří faktorů:

1. **velkého množství dat,**
2. **výkonnějšího hardware, zejména GPU,**
3. **lepších architektur a trénovacích metod.**

Právě Deep Learning umožnil prudký pokrok například v:

- počítačovém vidění,
- rozpoznávání řeči,
- strojovém překladu,
- generování obrazu,
- zpracování přirozeného jazyka,
- a nakonec i ve velkých jazykových modelech.

Generativní AI, kterou používáme dnes, tedy stojí přímo na základech Deep Learningu.

---

## 2.5 Generative AI

Dlouhou dobu byly AI modely používány hlavně k tomu, aby něco **rozpoznaly, klasifikovaly nebo předpověděly**.

Například:

```text
fotografie → kočka / pes
```

nebo:

```text
měření stroje → normální stav / pravděpodobná porucha
```

**Generative AI** přidává jiný typ schopnosti: dokáže vytvářet nový obsah.

Může generovat například:

- text,
- programový kód,
- obrázky,
- řeč,
- hudbu,
- video,
- 3D obsah,
- nebo kombinaci několika typů dat.

U jazykového modelu může vstup a výstup vypadat například takto:

```text
„Napiš stručné vysvětlení tranzistoru pro začátečníka.“
                     ↓
                AI model
                     ↓
           nově vytvořený text
```

Slovo **generativní** však někdy vede k chybnému dojmu, že model tvoří stejným způsobem jako člověk. Ve skutečnosti generuje výstup pomocí statistických vztahů naučených během trénování.

Důležitým důsledkem je, že výstup není uložená odpověď vytažená z databáze. Model vytváří odpověď znovu při každém spuštění.

Proto může:

- formulovat stejnou myšlenku různými způsoby,
- kombinovat znalosti z různých oblastí,
- přizpůsobit styl odpovědi,
- ale také vytvořit věrohodně znějící chybnou informaci.

Generativní schopnost je tedy velmi mocná, ale sama o sobě nezaručuje pravdivost.

---

## 2.6 Foundation Models

Další důležitý pojem je **Foundation Model**.

Dřívější modely byly často vytrénovány pro jeden konkrétní úkol. Jeden model například rozpoznával obličej, jiný určoval sentiment textu a další detekoval vadný výrobek.

Foundation Model se snaží být mnohem obecnější základnou.

Je vytrénován na velkém a různorodém množství dat a následně jej lze použít pro mnoho různých úloh.

Jeden základní model může například:

- odpovídat na otázky,
- shrnovat dokumenty,
- překládat,
- psát programy,
- analyzovat text,
- vytvářet strukturovaná data,
- pracovat s obrázky,
- používat nástroje.

Proto se používá označení **foundation** — model vytváří základ, na kterém lze stavět další aplikace.

Právě tato obecnost je jednou z největších změn, které současná AI přinesla.

Dříve byl typický přístup:

```text
jeden problém → jeden model
```

Dnes je často možné:

```text
jeden obecný model → stovky různých úloh
```

To dramaticky snižuje bariéru pro tvorbu AI aplikací.

---

## 2.7 LLM

**Large Language Model (LLM)** je velký model specializovaný především na práci s jazykem.

Slovo **large** může označovat několik věcí současně:

- velmi vysoký počet parametrů,
- velké množství trénovacích dat,
- vysokou výpočetní náročnost trénování.

Základní princip moderního LLM je překvapivě jednoduchý: model se učí předpovídat, jaký další token pravděpodobně následuje v určitém kontextu.

Například:

```text
Praha je hlavní město ...
```

model vyhodnotí jako velmi pravděpodobné pokračování například token odpovídající slovu **České republiky**.

Na první pohled to nevypadá jako základ systému schopného programovat, vysvětlovat fyziku nebo analyzovat dokumenty. Při velmi velkém množství dat a parametrů ale tento proces vede ke vzniku mnohem obecnější reprezentace jazyka a vztahů, které jsou v textu obsažené.

Proto dnešní LLM dokážou například:

- psát,
- překládat,
- shrnovat,
- programovat,
- klasifikovat,
- extrahovat informace,
- vysvětlovat,
- pracovat se strukturou textu,
- a do určité míry řešit problémy krok za krokem.

Je však důležité nepřisuzovat zkratce LLM více, než skutečně znamená.

> **LLM je model. ChatGPT, Claude nebo podobná služba je aplikace postavená kolem modelu.**

Aplikace může kromě modelu obsahovat také webové vyhledávání, paměť, práci se soubory, Python, databáze, bezpečnostní vrstvy nebo další nástroje.

Toto rozlišení bude důležité v celé knize.

---

## 2.8 Multimodal Models

Člověk nepracuje pouze s textem. Vidí obraz, slyší zvuk, čte dokumenty, sleduje video a kombinuje několik druhů informací současně.

Podobným směrem se posouvají i moderní AI modely.

**Multimodální model** dokáže pracovat s více typy dat neboli modalitami.

Může například přijmout:

```text
text + obrázek
```

nebo:

```text
text + obrázek + zvuk + video
```

a vytvořit odpověď s využitím kombinace těchto informací.

Praktické příklady:

- uživatel pošle fotografii zařízení a zeptá se, co na ní vidí,
- model přečte graf z technického dokumentu a vysvětlí jeho význam,
- model poslouchá hlasový vstup a odpovídá řečí,
- AI analyzuje screenshot aplikace a navrhne další krok,
- systém kombinuje textovou specifikaci se schématem nebo měřením.

Multimodalita je důležitá, protože reálná práce téměř nikdy neprobíhá pouze v čistém textu.

---

## 2.9 Reasoning Models

Od poloviny 20. let se stále více používá označení **Reasoning Model**.

Nejde o úplně jiný druh AI oddělený od LLM. Typicky jde o jazykový nebo multimodální model a způsob jeho natrénování a používání, který je optimalizovaný pro složitější řešení problémů.

Běžný model může často odpovědět téměř okamžitě. Reasoning model může před vytvořením finální odpovědi použít více výpočetního času na rozpracování problému, kontrolu kandidátních řešení nebo plánování dalšího postupu.

Prakticky je rozdíl podobný situaci:

```text
rychlá otázka → rychlá odpověď
```

oproti:

```text
složitý problém
   ↓
rozložení problému
   ↓
řešení dílčích kroků
   ↓
kontrola
   ↓
finální odpověď
```

Reasoning modely mají největší přínos například u:

- matematiky,
- programování,
- logických úloh,
- plánování,
- technických problémů,
- práce s větším množstvím omezení.

Ani zde ale neplatí, že delší přemýšlení automaticky znamená správnou odpověď. Model může složitě uvažovat a přesto vycházet z chybného předpokladu.

Proto reasoning nezbavuje systém potřeby ověřování.

---

## 2.10 Agentic AI

Pojem **Agentic AI** bývá používán velmi volně a často marketingově. Je proto důležité přesně říct, co jím budeme v této knize myslet.

Samotný LLM typicky dostane vstup a vrátí výstup:

```text
prompt → model → odpověď
```

Agentní systém přidává možnost provádět další kroky:

```text
cíl
 ↓
model
 ↓
rozhodnutí o dalším kroku
 ↓
nástroj / akce
 ↓
výsledek akce
 ↓
model
 ↓
další rozhodnutí
 ↓
...
```

Agent tedy může například:

1. dostat úkol,
2. vytvořit plán,
3. vyhledat informace,
4. otevřít soubor,
5. spustit program,
6. zkontrolovat výsledek,
7. opravit chybu,
8. pokračovat, dokud není úkol splněn.

To je zásadní rozdíl proti klasickému chatbotu.

Důležité ale je:

> **Agentic AI není vlastnost samotného modelu. Je to vlastnost celého systému postaveného kolem modelu.**

Silný model může být důležitou součástí agenta, ale agent potřebuje také nástroje, instrukce, stav, oprávnění, zpětnou vazbu a pravidla, kdy pokračovat nebo skončit.

Tomuto tématu bude věnována samostatná část knihy.

---

## 2.11 Co je model a co už je celý AI systém

Toto rozlišení je možná nejdůležitější myšlenkou celé kapitoly.

Když používáme moderní AI službu, velmi snadno získáme dojem, že všechny schopnosti má samotný model.

Ve skutečnosti může architektura vypadat například takto:

```text
                    AI APLIKACE
                        │
       ┌────────────────┼────────────────┐
       │                │                │
   instrukce          LLM/model       kontext
       │                │                │
       └────────────────┼────────────────┘
                        │
              orchestrace systému
                        │
       ┌────────────────┼────────────────┐
       │                │                │
   web search        databáze         soubory
       │                │                │
   kalkulačka         RAG             Python
       │                │                │
       └────────────────┼────────────────┘
                        │
                    odpověď
```

Samotný model může například vědět, jak napsat Python program. To ale ještě neznamená, že jej dokáže spustit.

K tomu potřebuje systém nástroj:

```text
LLM: „Potřebuji provést výpočet.“
              ↓
        Python nástroj
              ↓
        skutečný výsledek
              ↓
LLM: interpretuje výsledek
```

Stejně tak může model znát obecné informace o internetu, ale bez webového nástroje nemusí znát dnešní cenu akcie nebo právě zveřejněnou zprávu.

Tento rozdíl vysvětluje, proč dvě aplikace používající podobně schopný model mohou v praxi fungovat velmi rozdílně.

Výslednou kvalitu AI systému neurčuje pouze:

```text
jak dobrý je model
```

ale spíše:

```text
model
+ kvalitní kontext
+ správné nástroje
+ přístup k relevantním datům
+ orchestrace
+ kontrola výsledku
+ bezpečnostní pravidla
= schopnost celého AI systému
```

A právě tímto směrem se bude ubírat zbytek knihy: od pochopení samotného modelu k pochopení celého systému.

---

## Shrnutí kapitoly

Pokud si z této kapitoly odnést jen několik věcí, pak tyto:

1. **AI je nejširší pojem.** Ne každá AI používá Machine Learning.
2. **Machine Learning** umožňuje systému učit se vzory z dat místo ručního programování všech pravidel.
3. **Neuronové sítě** jsou jednou z metod Machine Learningu.
4. **Deep Learning** používá hlubší neuronové sítě a stojí za velkou částí současného pokroku AI.
5. **Generative AI** nevytváří pouze klasifikaci nebo predikci, ale generuje nový obsah.
6. **Foundation Model** je obecný model použitelný pro mnoho různých úloh.
7. **LLM** je Foundation Model zaměřený především na jazyk a práci s textovou reprezentací informací.
8. **Multimodální modely** kombinují text, obraz, zvuk a další modality.
9. **Reasoning modely** jsou optimalizované pro složitější vícekrokové řešení problémů, ale stále mohou chybovat.
10. **Agentic AI není jen model.** Agent vzniká až kombinací modelu, nástrojů, instrukcí, stavu a řídicí smyčky.
11. Při hodnocení AI je potřeba vždy rozlišovat **model** a **celý AI systém**.

V další kapitole se podíváme podrobněji na to, **jak LLM funguje uvnitř** — od tokenů a embeddings přes Transformer a attention až po vznik výsledné odpovědi.