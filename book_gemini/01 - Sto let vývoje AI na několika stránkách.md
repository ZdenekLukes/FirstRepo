---
title: "1. Sto let vývoje AI na několika stránkách"
part: "I — Jak jsme se sem dostali"
status: final-draft
version: "0.2"
updated: 2026-08-07
---

# 1. Sto let vývoje AI na několika stránkách

<!-- visual:01-history-timeline.svg -->

![Časová osa vývoje AI](assets/diagrams/01-history-timeline.svg)

*Obrázek: Zlomové body od obecného výpočtu po agentní systémy.*


Dnešní AI může působit jako technologie, která se objevila téměř přes noc. Ještě před několika lety většina lidí velký jazykový model nikdy nepoužila. Dnes dokáže AI během několika sekund psát programy, analyzovat dokumenty, pracovat s obrazem a zvukem nebo používat externí nástroje.

Ve skutečnosti ale dnešní systémy nevznikly jedním objevem. Jsou výsledkem téměř století postupného vývoje matematiky, algoritmů, výpočetního hardware, dat a způsobů, jakými se stroje učí.

Tato kapitola proto nemá být úplnou historií Artificial Intelligence. Nechci zde vypisovat každou školu, algoritmus ani významného výzkumníka. Cílem je vytvořit jednoduchou časovou osu:

> **rok → co se změnilo → proč to bylo důležité pro to, co používáme dnes**

Při pohledu zpět je vidět několik opakujících se motivů.

AI se vždy posunula výrazně dopředu, když se současně zlepšily alespoň některé z těchto věcí:

```text
lepší myšlenka
+
více dat
+
větší výpočetní výkon
+
lepší způsob trénování
+
lepší přístup k reálnému světu
=
nová úroveň schopností AI
```

A stejně důležitá je druhá lekce:

> **Historie AI není souvislá cesta vzhůru. Je to střídání průlomů, přehnaných očekávání, zklamání a nových průlomů.**

To je užitečné mít na paměti i dnes.

---

## 1.1 Kořeny moderní AI

### 1936 — Alan Turing a obecný výpočet

Ještě neexistovalo označení Artificial Intelligence ani moderní digitální počítače v dnešním smyslu, když Alan Turing v roce 1936 popsal abstraktní stroj schopný provádět výpočet podle přesně definovaných pravidel.

Dnes mu říkáme **Turing machine**.

Pro tuto knihu není důležitá její matematická konstrukce. Důležitá je myšlenka:

> Jeden obecný stroj nemusí být postaven pouze pro jednu úlohu. Pokud dostane správný program a data, může vykonávat mnoho různých výpočtů.

To je jeden ze základů moderní informatiky.

Představme si rozdíl:

```text
mechanická kalkulačka
→ umí jednu úzkou skupinu operací
```

oproti:

```text
obecný počítač
+ program
→ textový editor
→ simulátor
→ databáze
→ webový prohlížeč
→ neuronová síť
→ LLM
```

Turing samozřejmě v roce 1936 nepopisoval ChatGPT. Pomohl ale vytvořit teoretický základ světa, ve kterém lze inteligentní chování implementovat jako výpočet.

---

### 1943 — McCulloch a Pitts: matematický neuron

Warren McCulloch a Walter Pitts v roce 1943 popsali velmi zjednodušený matematický model neuronu.

Biologický neuron je extrémně složitý. Jejich model jej redukoval na mnohem jednodušší princip:

```text
vstupy
  ↓
jednoduchá výpočetní jednotka
  ↓
výstup
```

Jedna taková jednotka není příliš zajímavá.

Důležitější bylo zjištění, že jejich propojením lze vytvářet sítě schopné reprezentovat logické vztahy.

Tady se poprvé objevuje myšlenka, která bude později zásadní:

> **Složité chování může vzniknout spojením velkého množství relativně jednoduchých výpočetních jednotek.**

Moderní neuronová síť je samozřejmě nesrovnatelně složitější. Přesto zde můžeme vidět jeden z jejích intelektuálních předků.

---

### 1950 — Turingova otázka: může stroj myslet?

V roce 1950 publikoval Alan Turing práci *Computing Machinery and Intelligence*.

Místo nekonečné filozofické diskuse o tom, co přesně znamená „myslet“, navrhl praktičtější otázku.

Pokud člověk komunikuje prostřednictvím textu a nedokáže spolehlivě poznat, zda odpovídá člověk nebo stroj, můžeme chování stroje považovat za dostatečně inteligentní pro účely testu.

Později se tento koncept začal označovat jako **Turing test**.

Důležité není, zda je Turingův test dnes ještě dobrým benchmarkem AI.

Důležitý byl posun:

```text
„Co je inteligence?“
        ↓
„Jaké pozorovatelné chování by inteligenci dokazovalo?“
```

Stejný princip používáme dodnes při evaluaci modelů.

Neptáme se pouze:

> Je tento model inteligentní?

Ptáme se například:

- dokáže napsat správný program?
- dokáže vyřešit matematický problém?
- dokáže najít informaci v dokumentech?
- dokáže ovládat počítač?
- dokáže splnit vícekrokový úkol?

Inteligenci tak nahrazujeme souborem měřitelných schopností.

---

### 1956 — Dartmouth a vznik Artificial Intelligence jako oboru

Léto 1956 je tradičně považováno za okamžik, kdy se Artificial Intelligence ustavila jako samostatný výzkumný obor.

Na Dartmouth College se sešla skupina vědců kolem Johna McCarthyho, Marvina Minského, Claudea Shannona, Nathaniela Rochestera a dalších.

Právě v návrhu tohoto projektu se objevil termín **Artificial Intelligence**.

Myšlenka byla mimořádně ambiciózní: vlastnosti lidské inteligence by mohly být popsány dostatečně přesně na to, aby je bylo možné simulovat strojem.

V kontextu padesátých let to bylo odvážné tvrzení.

Počítače byly obrovské, drahé, pomalé a jejich paměť byla z dnešního pohledu zanedbatelná.

Přesto zde vznikla výzkumná agenda, která je s námi dodnes:

- řešení problémů,
- používání jazyka,
- abstrakce,
- učení,
- kreativita,
- simulace inteligentního chování.

Rok 1956 je proto vhodné chápat ne jako okamžik, kdy byla AI „vynalezena“, ale jako okamžik, kdy dostala **jméno a vlastní výzkumný program**.

---

### 1958 — Rosenblattův perceptron: učení, ale jen lineární hranice

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

---

## 1.2 První velké nadšení: když jsme se snažili inteligenci naprogramovat

V 50. až 70. letech dominoval AI především přístup, kterému dnes říkáme **symbolic AI**.

Základní představa byla přibližně následující:

> Lidské myšlení pracuje se symboly a pravidly. Pokud dokážeme tato pravidla popsat, můžeme je naprogramovat.

Systém tedy mohl obsahovat například:

```text
IF podmínka A
AND podmínka B
THEN závěr C
```

Nebo mohl prohledávat prostor možných řešení, plánovat jednotlivé kroky nebo manipulovat s logickými výrazy.

Tento přístup přinesl řadu působivých výsledků.

---

### 1956 — Logic Theorist

Jedním z prvních známých AI programů byl Logic Theorist vytvořený Allenem Newellem, Herbertem Simonem a Cliffem Shawem.

Program dokázal automaticky dokazovat některé matematické věty.

To bylo mimořádně působivé, protože matematické dokazování bylo považováno za činnost vyžadující vysokou úroveň lidského rozumu.

Ukázalo se, že část toho, co považujeme za inteligentní činnost, lze převést na:

```text
reprezentaci problému
+
pravidla
+
vyhledávání mezi možnostmi
```

Tento princip používáme v různých formách dodnes.

---

### 1960s — symbolická AI

Symbolické systémy byly velmi dobré tam, kde bylo možné svět přesně popsat.

Například šachy mají:

- přesná pravidla,
- jasně definovaný stav,
- omezenou množinu akcí,
- jednoznačný cíl.

Reálný svět je ale mnohem horší.

Co přesně znamená:

> „Ten člověk vypadá nervózně.“

Jak algoritmicky popíšeme všechny způsoby, kterými může vypadat kočka?

Jak vytvoříme ručně pravidla pro všechny možné věty přirozeného jazyka?

Postupně se ukazovala zásadní slabina:

> **Ruční zapisování inteligence pomocí pravidel funguje dobře pouze tam, kde dokážeme pravidla světa opravdu popsat.**

A to u mnoha zajímavých problémů neumíme.

---

### 1966 — ELIZA

Joseph Weizenbaum vytvořil program ELIZA.

Nejslavnější režim simuloval psychoterapeuta a používal jednoduché vzory a přepisovací pravidla.

Například uživatel mohl napsat něco jako:

```text
Jsem dnes unavený.
```

A systém mohl odpovědět například otázkou vztahující se ke slovu „unavený“.

ELIZA nerozuměla textu způsobem, jakým pracují dnešní modely. Přesto byla pro mnoho lidí překvapivě přesvědčivá.

To odhalilo něco, co zůstává důležité dodnes:

> **Člověk velmi snadno přisoudí stroji porozumění, pokud stroj komunikuje dostatečně přesvědčivě.**

Dnes je toto riziko ještě větší, protože jazykové modely jsou mnohonásobně schopnější.

Plynulá odpověď proto nesmí být zaměňována za důkaz správnosti.

K tomuto problému se budeme vracet v kapitole o hallucinations a důvěře v AI.

---

### 1960s–1970s — plánování a první roboti

AI se nezabývala pouze textem.

Výzkumníci vytvářeli také systémy schopné:

- plánovat cestu,
- řešit logické úlohy,
- pohybovat robotem,
- pracovat s jednoduchou reprezentací okolního světa.

Známým příkladem byl robot **Shakey**, který dokázal kombinovat vnímání prostředí, plánování a fyzickou akci.

V malém kontrolovaném světě to byl zásadní úspěch.

Současně ale opět ukázal problém celé tehdejší AI:

```text
malý dobře popsaný svět
→ funguje překvapivě dobře

skutečný svět
→ počet možností exploduje
```

To je problém, se kterým agentní systémy bojují i dnes, jen na úplně jiné technologické úrovni.

---

### Expert systems

V 60. a zejména 70. a 80. letech získaly velkou pozornost **expert systems**.

Myšlenka byla velmi praktická:

> Pokud neumíme vytvořit obecnou inteligenci, zachyťme alespoň znalosti špičkového experta v jedné úzké oblasti.

Systém mohl obsahovat stovky nebo tisíce pravidel:

```text
pokud platí A a B
→ zvaž C

pokud platí C a D
→ doporuč E
```

Vznikly například systémy pro:

- chemickou analýzu,
- diagnostiku,
- konfiguraci technických systémů,
- rozhodovací podporu.

To byl jeden z prvních pokusů převést **znalosti organizace nebo experta do počítačově použitelné podoby**.

V tomto smyslu mají expert systems překvapivě blízko k některým dnešním AI projektům.

Rozdíl je v tom, že tehdy musel znalostní inženýr pravidla převážně zapsat ručně.

Dnes můžeme část znalostí zpřístupnit modelu například prostřednictvím:

- dokumentů,
- RAG,
- databází,
- nástrojů,
- firemní knowledge base.

Cíl je podobný.

Technologie je zásadně jiná.

---

## 1.3 AI winters — když očekávání předběhla technologii

Historie AI je důležitá také proto, že ukazuje nebezpečí příliš rychlých očekávání.

V několika obdobích se zdálo, že obecně inteligentní stroje jsou téměř za rohem.

Pak se ukázalo, že demonstrace fungující v malém laboratorním problému se velmi obtížně přenáší do reálného světa.

Následoval pokles financování, zájmu i optimismu.

Tato období označujeme jako **AI winters**.

---

### První AI winter — přibližně 70. léta

Rané AI programy byly působivé, ale měly zásadní omezení.

Chyběl jim především:

- výpočetní výkon,
- paměť,
- dostatek digitálních dat,
- robustní algoritmy,
- schopnost pracovat s nejistotou skutečného světa.

Problém, který fungoval s několika objekty, mohl být při stovkách nebo tisících možností prakticky neřešitelný.

Navíc počítače byly proti dnešku extrémně pomalé a drahé.

Očekávání však byla vysoká.

Když výsledky neodpovídaly slibům, financování části AI výzkumu kleslo.

První velká lekce tedy zní:

> **Demonstrace schopnosti není totéž jako škálovatelný systém použitelný v reálném světě.**

To platí i dnes u agentů, autonomních systémů nebo AI v engineeringu.

---

### Návrat díky expert systems

V 80. letech se AI vrátila do centra pozornosti díky komerčnímu úspěchu expert systems.

Místo snahy postavit obecnou inteligenci se řešily úzké problémy s jasnou ekonomickou hodnotou.

To fungovalo podstatně lépe.

Firmy začaly investovat do systémů, které zachycovaly expertní znalost v konkrétní oblasti.

Znovu se zdálo, že AI bude rychle expandovat do většiny podnikových procesů.

Jenže i zde se postupně objevila omezení.

---

### Druhý AI winter — konec 80. a začátek 90. let

Velké rule-based systémy byly drahé na tvorbu a ještě dražší na údržbu.

Když se změnilo prostředí nebo pravidla firmy, bylo nutné znalostní bázi ručně aktualizovat.

Systém také často nevěděl, jak reagovat na situaci, kterou jeho tvůrci předem nepopsali.

Typický problém vypadal přibližně takto:

```text
více funkcí
→ více pravidel
→ více vazeb mezi pravidly
→ složitější údržba
→ více neočekávaných interakcí
```

Ekonomika velkých expert systems přestala v mnoha případech dávat smysl.

Zájem o AI znovu ochladl.

Druhá důležitá lekce:

> **Nestačí, aby AI fungovala. Musí být také provozovatelná, udržovatelná a ekonomicky výhodná.**

Toto bude velmi důležité později při návrhu firemních agentních systémů.

---

## 1.4 Machine Learning přebírá vedení

Postupně se začal prosazovat jiný přístup.

Místo otázky:

> Jaká pravidla máme naprogramovat?

se stále více používala otázka:

> Jak můžeme nechat systém, aby se potřebná pravidla naučil z dat?

To je jeden z největších přechodů v historii AI.

```text
SYMBOLICKÝ PŘÍSTUP
člověk zapisuje pravidla
        ↓
      systém

MACHINE LEARNING
člověk dodá data a cíl
        ↓
    trénování
        ↓
      model
```

---

### 1986 — backpropagation vrací neuronové sítě do hry

Myšlenka backpropagation nevznikla v roce 1986 z ničeho. Práce Davida Rumelharta, Geoffreyho Hintona a Ronalda Williamse ale výrazně pomohla metodu popularizovat pro trénování vícevrstvých neuronových sítí.

Princip je opět možné pochopit bez matematiky.

Síť vytvoří výstup.

Ten porovnáme se správným výsledkem.

Potom vypočítáme, jak by se měly jednotlivé parametry sítě mírně změnit, aby příště byla chyba menší.

```text
vstup
  ↓
neuronová síť
  ↓
výstup
  ↓
chyba
  ↓
backpropagation
  ↓
úprava parametrů
```

Tento cyklus se opakuje obrovské množství krát.

Backpropagation se stal jedním ze základních mechanismů moderního Deep Learningu.

Neuronové sítě však stále narážely na praktické limity tehdejšího hardware a dostupných dat.

Potřebovaly ještě několik dalších technologických změn.

---

### 1997 — Deep Blue poráží Garryho Kasparova

V roce 1997 porazil počítač IBM Deep Blue úřadujícího mistra světa v šachu Garryho Kasparova v šestipartiovém zápase.

Pro veřejnost to byl jeden z nejviditelnějších AI momentů své doby.

Šachy byly dlouho považovány za symbol lidského strategického myšlení.

Najednou nejlepší člověk prohrál se strojem.

Je ale důležité chápat, **co Deep Blue byl a co nebyl**.

Nebyl to předchůdce dnešního LLM v přímém smyslu.

Jeho síla vycházela z kombinace:

- extrémně rychlého vyhledávání,
- specializovaného hardware,
- heuristik,
- znalosti šachových pozic.

Deep Blue je proto skvělým příkladem důležitého principu:

> **Stroj nemusí řešit problém stejným způsobem jako člověk, aby člověka v daném problému překonal.**

To platí pro velkou část AI dodnes.

---

### 2006 — moderní návrat Deep Learningu

Rok 2006 se někdy zjednodušeně označuje za začátek Deep Learningu.

Přesnější je říct, že šlo o významný **návrat hlubších neuronových sítí** do centra výzkumu.

Geoffrey Hinton a další ukázali nové způsoby, jak lze vícevrstvé neuronové sítě efektivněji trénovat.

Samotný algoritmický pokrok ale nestačil.

Začínaly se současně skládat tři klíčové podmínky:

```text
lepší algoritmy
+
více digitálních dat
+
výkonnější hardware
```

A právě jejich kombinace během několika let zásadně změnila AI.

---

### 2009 — ImageNet: data se stávají strategickou surovinou

Jedním z velmi důležitých projektů byl **ImageNet** — obrovský dataset označených obrázků určený pro výzkum rozpoznávání obrazu.

Na první pohled může dataset působit méně zajímavě než nový algoritmus.

Ve skutečnosti ale ukázal jednu z nejdůležitějších vlastností moderního Machine Learningu:

> **Kvalita a množství dat může být stejně důležité jako samotný algoritmus.**

Pokud chceme, aby se systém naučil rozpoznávat tisíce druhů objektů, potřebujeme obrovské množství příkladů.

Internet vytvořil prostředí, ve kterém bylo možné taková data shromažďovat v dříve nepředstavitelném měřítku.

To byl jeden z předpokladů pozdějšího úspěchu velkých modelů.

---

### 2012 — AlexNet a okamžik, kdy se Deep Learning stal těžko ignorovatelný

V roce 2012 AlexNet výrazně překonal konkurenci v soutěži ImageNet Large Scale Visual Recognition Challenge.

Použil hlubokou convolutional neural network a efektivně využil GPU.

Tady se spojily tři věci:

```text
neuronové sítě
+
velký dataset
+
GPU
```

Výsledek byl natolik výrazný, že se Deep Learning rychle stal dominantním přístupem v computer vision a později v řadě dalších oblastí.

GPU byla původně navržena pro grafiku.

Ukázalo se ale, že jejich schopnost provádět obrovské množství podobných operací paralelně se skvěle hodí také pro neuronové sítě.

Tady začíná přímá cesta k dnešnímu světu obrovských AI clusterů.

---

## 1.5 Od Deep Learningu ke generativní AI

Po roce 2012 už vývoj začíná zrychlovat.

Neuronové sítě se zlepšují v obrazu, řeči i jazyce.

Roste množství dat.

Roste počet parametrů modelů.

Roste výkon GPU a později specializovaných AI akcelerátorů.

Výzkum se postupně přesouvá od modelů, které pouze něco klasifikují, k modelům, které dokážou **generovat nový obsah**.

---

### 2014 — GAN: modely začínají přesvědčivě generovat

Ian Goodfellow a jeho spolupracovníci představili **Generative Adversarial Networks (GAN)**.

Myšlenka používá dva modely v určitém druhu soutěže.

Velmi zjednodušeně:

```text
GENERATOR
snaží se vytvořit přesvědčivý obsah

        proti

DISCRIMINATOR
snaží se poznat, co je skutečné a co vytvořené
```

Jak se oba systémy zlepšují, generator se učí vytvářet stále realističtější výstupy.

GAN nebyly první generativní modely, ale významně urychlily zájem o generativní AI, především v oblasti obrazu.

Ukázaly, že neuronová síť nemusí pouze odpovědět:

```text
„na obrázku je člověk“
```

Může také vytvořit:

```text
nový obrázek člověka,
který nikdy neexistoval
```

To je zásadní změna typu schopnosti.

---

### 2016 — AlphaGo

V roce 2016 systém AlphaGo společnosti DeepMind porazil Lee Sedola, jednoho z nejlepších hráčů hry Go.

Go bylo pro AI mimořádně obtížné kvůli obrovskému počtu možných pozic.

Hrubé prohledávání všech možností jako u jednodušších her nestačí.

AlphaGo kombinovalo několik technik:

- Deep Learning,
- reinforcement learning,
- vyhledávání,
- Monte Carlo Tree Search.

To je důležité i pro dnešní AI systémy.

Nejlepší řešení totiž často není:

> jeden model vyřeší všechno.

Ale spíše:

> **model + další algoritmy + nástroje + zpětná vazba**

Tento způsob uvažování nás později dovede přímo k agentním systémům.

---

### 2017 — Transformer: Self-Attention mění práci se sekvencemi

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

---

### 2018 — BERT a síla pre-trainingu

Google představil model **BERT**.

BERT nebyl chatbot podobný dnešnímu ChatGPT.

Byl ale důležitým důkazem síly nového paradigmatu:

```text
nejprve model natrénovat obecně
na obrovském množství textu
        ↓
a potom jej použít nebo upravit
pro mnoho různých úloh
```

Namísto jednoho modelu pro každou jednotlivou jazykovou úlohu začala být stále důležitější myšlenka **pre-trained foundation modelu**.

Tento princip je základem dnešních LLM.

---

### 2020 — GPT-3 a síla škálování

GPT-3 ukázal, jak dramaticky mohou schopnosti jazykového modelu růst s velikostí modelu, množstvím dat a výpočetním výkonem.

Model dokázal plnit překvapivě široké spektrum úloh pouze podle textové instrukce nebo několika příkladů vložených přímo do promptu.

Začalo být zřejmé, že jeden velký model může fungovat jinak než klasický přístup:

```text
starší přístup:
1 úloha → 1 specializovaný model

novější přístup:
1 foundation model → mnoho úloh
```

To zásadně snížilo bariéru používání AI.

Uživatel už nemusel být Machine Learning expert.

Často stačilo popsat požadovaný úkol přirozeným jazykem.

---

### 2022 — ChatGPT: AI dostává univerzální uživatelské rozhraní

Velké jazykové modely existovaly již před ChatGPT.

ChatGPT ale na konci roku 2022 udělal něco mimořádně důležitého:

> **zpřístupnil schopnosti LLM běžnému člověku prostřednictvím jednoduché konverzace.**

Uživatel nepotřeboval API, Python ani znalost Machine Learningu.

Napsal otázku.

Dostal odpověď.

A mohl pokračovat.

To změnilo způsob, jakým veřejnost AI vnímala.

AI přestala být pouze technologií schovanou uvnitř doporučovacího algoritmu nebo vyhledávače.

Stala se nástrojem, se kterým člověk přímo komunikuje.

To je možná stejně důležitá změna **interface** jako změna samotného modelu.

---

### 2023 — multimodální frontier modely a exploze open-weight LLM

Rok 2023 přinesl rychlé zlepšování velkých modelů, výraznější multimodalitu a současně prudký rozvoj modelů, které bylo možné provozovat mimo infrastrukturu jejich původního výrobce.

Začala se rychle rozvíjet dvě paralelní větve:

```text
FRONTIER CLOUD MODELS
velké, velmi schopné,
provozované poskytovatelem

        a

OPEN-WEIGHT / LOCAL MODELS
stále schopnější,
provozovatelné na vlastní infrastruktuře
```

Tento rozdíl bude později zásadní pro rozhodování mezi cloud, on-prem a hybridní architekturou.

Současně se ukázalo, že model nemusí zpracovávat jen text.

Moderní AI začala spojovat:

- text,
- obraz,
- dokumenty,
- zvuk,
- programový kód.

---

### 2024 — multimodalita, delší context a test-time reasoning

Během roku 2024 se několik trendů stalo výrazně praktičtějšími.

Modely získávaly:

- delší context window,
- lepší práci s obrazem a zvukem,
- výrazně lepší coding,
- efektivnější malé modely,
- schopnost využít více výpočtu při řešení složitějšího problému.

Začíná být důležitý koncept **test-time compute**.

Namísto toho, aby model vždy okamžitě vytvořil první odpověď, může systém při složitější úloze investovat více výpočtu do hledání lepšího řešení.

To vede k nové generaci reasoning modelů.

Důležitá je ale také druhá část příběhu.

Modely se nezlepšují pouze tím, že jsou větší.

Výrazně se zlepšuje:

- architektura,
- trénování,
- post-training,
- datová kvalita,
- inference,
- kvantizace.

Proto začínají relativně malé modely dosahovat výkonu, který dříve vyžadoval mnohonásobně větší systémy.

To je zásadní pro lokální AI.

---

### 2025 — reasoning, tool use a agentní práce

V roce 2025 už hlavní otázka není pouze:

> Jak dobrou odpověď model napíše?

Stále častěji zní:

> Dokáže model **něco skutečně udělat**?

AI systémy začínají výrazně lépe:

- používat nástroje,
- vyhledávat informace,
- pracovat se soubory,
- programovat ve větších codebase,
- opravovat vlastní chyby,
- plánovat několik kroků dopředu,
- ovládat část uživatelského rozhraní.

Začíná se prakticky prosazovat pojem **agent**.

Rozdíl můžeme zjednodušit:

```text
CHATBOT
otázka
 ↓
odpověď

AGENTNÍ SYSTÉM
cíl
 ↓
rozhodnutí
 ↓
nástroj
 ↓
výsledek
 ↓
kontrola
 ↓
další krok
```

Coding je jednou z prvních oblastí, kde je tento posun mimořádně viditelný.

Program je totiž možné nejen vytvořit, ale také:

- spustit,
- otestovat,
- změřit,
- opravit.

AI tak dostává automatickou zpětnou vazbu.

To je důvod, proč coding agents často ukazují budoucnost širšího knowledge work.

---

### 2026 — od modelu k celému AI systému

K srpnu 2026 už není nejzajímavější otázkou pouze to, který model má nejlepší benchmark.

Rozdíl mezi špičkovými modely se v mnoha úlohách zmenšuje a stále důležitější je celý systém kolem nich.

Praktická AI se skládá například z:

```text
MODEL
+
CONTEXT
+
DATA
+
MEMORY
+
SEARCH
+
TOOLS
+
WORKFLOW
+
VERIFICATION
+
HUMAN APPROVAL
```

Agentní systémy se zlepšují v práci s počítačem a v plnění reálných úloh, ale stále nejsou spolehlivé tak, aby bylo bezpečné jednoduše jim dát neomezená oprávnění a očekávat bezchybný výsledek.

To je velmi důležitý stav roku 2026:

> **AI už dokáže provádět stále delší řetězce užitečných akcí, ale autonomie roste rychleji než spolehlivost.**

Proto začínají být stejně důležité jako samotný model také:

- evaluace,
- observability,
- oprávnění,
- sandboxing,
- audit trail,
- human-in-the-loop.

Moderní AI se tak postupně mění z jednoho modelu na **novou softwarovou vrstvu**, která propojuje jazykový model s klasickými deterministickými systémy.

A právě tomuto přechodu je věnována velká část této knihy.

---

## 1.6 Co je na této historii nejdůležitější

Když odstraníme jednotlivá jména a produkty, zůstane několik trendů, které vysvětlují téměř celý vývoj AI.

### 1. Algoritmy

Nové architektury a metody opakovaně odstranily omezení předchozí generace.

Například:

```text
perceptron
↓
vícevrstvé neuronové sítě
↓
backpropagation
↓
Deep Learning
↓
Transformer
↓
moderní foundation models
```

Samotný algoritmus ale téměř nikdy nestačil.

---

### 2. Data

Machine Learning změnil způsob tvorby inteligentních systémů.

Místo ručního zapisování všech pravidel můžeme velkou část požadovaného chování získat z dat.

Internet potom vytvořil bezprecedentní množství:

- textu,
- obrazů,
- videí,
- programového kódu,
- dokumentů.

Data se stala jednou ze strategických surovin AI.

---

### 3. Výpočetní výkon

Mnoho myšlenek existovalo desítky let předtím, než se staly prakticky použitelnými.

Rozdíl často vytvořil hardware.

```text
CPU
↓
GPU
↓
specializované AI akcelerátory
↓
obrovské distribuované clustery
```

Velká část moderního AI boomu by bez dramatického růstu dostupného výpočetního výkonu nebyla možná.

---

### 4. Škálování

Jedno z překvapení moderní AI bylo, jak dlouho se schopnosti modelů zlepšovaly s rostoucím:

- počtem parametrů,
- množstvím dat,
- množstvím výpočtu.

Z relativně úzkých jazykových modelů začaly vznikat foundation models schopné řešit široké spektrum problémů.

Škálování ale neznamená pouze „udělejme model větší“.

V roce 2026 je stále důležitější také efektivita.

Menší model, který je:

- rychlejší,
- levnější,
- lokální,
- dobře specializovaný,

může být pro konkrétní úlohu lepší než největší dostupný model.

---

### 5. Internet

Internet měl dvojí efekt.

Nejprve vytvořil obrovské množství digitálních dat vhodných pro training.

Později se stal také nástrojem, který může AI používat během inference.

To je zásadní rozdíl:

```text
MODEL
má znalosti získané trainingem

MODEL + WEB SEARCH
může získat informace právě teď
```

Stejný princip platí pro interní firemní data.

---

### 6. Lidská a automatická zpětná vazba

Pre-training vytvoří velmi schopný model, ale ne nutně dobrého asistenta.

Post-training, instruction tuning a různé formy zpětné vazby pomáhají model naučit například:

- následovat instrukce,
- lépe řešit problémy,
- používat nástroje,
- vytvářet užitečnější odpovědi.

Další zásadní krok nastává, když lze výsledek automaticky ověřit.

Například:

```text
AI napíše program
↓
spustí test
↓
test selže
↓
AI vidí chybu
↓
opraví program
```

Nebo později v našem engineering příkladu:

```text
AI navrhne změnu obvodu
↓
SPICE / Spectre simulace
↓
výsledek
↓
AI vyhodnotí rozdíl proti specifikaci
↓
další iterace
```

Tady se generování mění na uzavřenou optimalizační smyčku.

---

### 7. Schopnost používat nástroje

Samotný model pouze generující text má zásadní omezení.

Jakmile ale dostane nástroje, může například:

- hledat na webu,
- číst databázi,
- spustit Python,
- upravit soubor,
- spustit simulátor,
- pracovat s Git,
- poslat požadavek do API.

To je jeden z největších posunů poloviny 20. let.

Model už není pouze zdroj odpovědí.

Může se stát **řídicí vrstvou nad dalšími systémy**.

---

### 8. AI jako systém místo samotného modelu

Historie začala jednoduchou představou:

```text
vytvoříme inteligentní program
```

Dnešní praktický systém vypadá stále častěji takto:

```text
                    AI SYSTEM

        ┌──────────── MODEL ────────────┐
        │                              │
        │      reasoning / language    │
        │                              │
        └──────────────┬───────────────┘
                       │
       ┌───────────────┼────────────────┐
       │               │                │
     DATA            TOOLS            MEMORY
       │               │                │
       └───────────────┼────────────────┘
                       │
                   WORKFLOW
                       │
                   VERIFY
                       │
                    HUMAN
```

Toto je možná nejdůležitější výsledek celé časové osy.

Nejde už pouze o otázku:

> Jak inteligentní je model?

Ale:

> **Jak dobře je navržen celý systém, ve kterém model pracuje?**

---

## Co nás historie AI učí

Z téměř století vývoje lze vyvodit několik praktických pravidel.

### Schopnost není totéž jako spolehlivost

AI může předvést mimořádně působivý výkon a současně selhat v překvapivě jednoduché situaci.

To platilo pro rané AI systémy a platí to i v roce 2026.

---

### Benchmark není totéž jako reálný use-case

Deep Blue byl lepší než člověk v šachu.

To neznamenalo, že uměl řídit firmu.

Moderní model může excelovat v benchmarku a přesto selhat při práci s konkrétní firemní dokumentací.

Proto budeme v této knize preferovat **reálné experimenty a vlastní evaluace** před marketingovými čísly.

---

### Hardware může změnit hodnotu starého nápadu

Neuronové sítě existovaly dlouho před rokem 2012.

Teprve kombinace vhodných algoritmů, dat a GPU z nich udělala dominantní technologii.

Podobná změna může nastat i u dnešních agentních systémů.

Nápad může být známý několik let, ale teprve dostatečně schopný a levný model jej udělá prakticky použitelným.

---

### Hype cycles nejsou důkaz, že technologie nefunguje

AI winters neznamenaly, že základní myšlenka AI byla chybná.

Znamenaly, že očekávání předběhla tehdejší technické možnosti.

Stejnou otázku je dobré klást i dnes:

> Je daná věc nemožná, nebo pouze ještě není dostatečně spolehlivá, levná nebo rychlá?

---

### Největší hodnota vzniká kombinací technologií

AlphaGo nebylo „jen neuronová síť“.

Moderní coding agent není „jen LLM“.

A budoucí AI-assisted engineering nebude „jen chatbot“.

Opakovaně se ukazuje:

```text
silný model
+
deterministické nástroje
+
data
+
ověření
=
mnohem schopnější systém
```

To je jedna z hlavních myšlenek celé knihy.

---

## Mentální model celé historie

Pokud bychom téměř století AI museli zredukovat na jediný obrázek, mohl by vypadat takto:

```text
1930s–1950s
MŮŽE BÝT INTELIGENCE VÝPOČET?
        ↓
1950s–1970s
ZKUSME INTELIGENCI NAPSAT JAKO PRAVIDLA
        ↓
1970s–1990s
ZJIŠŤUJEME LIMITY RUČNĚ PSANÝCH PRAVIDEL
        ↓
1980s–2010s
NECHME MODELY UČIT SE Z DAT
        ↓
2012+
DEEP LEARNING + DATA + GPU
        ↓
2017+
TRANSFORMER + PRE-TRAINING + SCALE
        ↓
2022+
LLM JAKO UNIVERZÁLNÍ ROZHRANÍ
        ↓
2024+
REASONING + MULTIMODALITA + TOOL USE
        ↓
2025–2026
AGENTNÍ SYSTÉMY
        ↓
MODEL SE STÁVÁ SOUČÁSTÍ CELÉHO AI SYSTÉMU
```

Nejdůležitější změna tedy možná není, že modely „umějí více odpovídat“.

Je to postupný přechod:

```text
PROGRAM
↓
MODEL
↓
FOUNDATION MODEL
↓
MODEL + DATA
↓
MODEL + TOOLS
↓
AGENT
↓
AI SYSTEM
```

A právě od tohoto bodu budeme pokračovat dál.

V další kapitole si nejprve přesně ujasníme, co znamenají pojmy **AI, Machine Learning, Neural Networks, Deep Learning, Generative AI, Foundation Model, LLM, Reasoning Model a Agentic AI**. Bez tohoto slovníku by se další části knihy rychle změnily v hromadu buzzwords.
