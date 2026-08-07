# Finální redakční audit před tiskem — v0.7

## Verdikt

**EDITORIAL GO / PRINT CANDIDATE.**

Rukopis je po finálním redakčním průchodu obsahově uzamčený. Další plošné přepisování by v této fázi spíš zvyšovalo riziko ztráty autorského hlasu, redundance a nových chyb než kvalitu knihy.

Tento verdikt není tvrzení, že kniha automaticky získá literární cenu nebo bude „nejlepší na světě“. Znamená, že z pohledu obsahu, struktury, informační hustoty, technického rámování a mechanických předtiskových kontrol už nevidím důvod k další velké redakční iteraci.

## Co má být charakter knihy

Kniha má fungovat současně jako:

- vstup do AI pro úplného nováčka s technickým uvažováním,
- praktický manuál pro člověka, který už AI používá,
- engineering reference pro RAG, tool use, agenty, bezpečnost a evaluaci,
- autorská kniha s vlastní tezí a zkušeností, nikoli anonymní katalog produktů.

Hlavní čtenářský příslib je:

> **Jak AI skutečně funguje, jak ji používat a jak z modelů stavět spolehlivé systémy.**

## Hlavní teze

> **Nejdůležitější není mít nejchytřejší model, ale umět mu ve správný okamžik dodat správný kontext a nástroje — a jeho výsledek spolehlivě ověřit.**

Tato věta je záměrně zopakována v úvodu a v osobní syntéze kapitoly 33. Na začátku funguje jako hypotéza knihy; po technických kapitolách jako závěr zkušenosti.

## Největší změny finálního passu

- úvod dostal silnější autorskou tezi a jasnější důvod, proč knihu číst;
- vzniklo **Dvanáct pravidel praktické AI** jako mentální mapa celé knihy;
- první pravidla byla formulována tak, aby neztratila technickou přesnost, ale neblokovala úplného nováčka nevysvětleným jargonem;
- byly přidány tři podpisové diagramy: **Od modelu k hodnotě**, **Od modelu k systému** a **Když AI selže, kde hledat chybu**;
- nebyla přidávána generická „AI art“ grafika, roboti, mozky ani dekorativní neonový cyberpunk;
- odstranily se interní redakční poznámky, living-draft formulace a zastaralé cross-reference;
- kapitola 33 dostala definitivní osobní syntézu místo pracovního závěru;
- kapitola 36 dostala znovupoužitelný diagnostický model pro debugging AI systémů;
- kapitoly už nekončí seznamem surových URL; rychle stárnoucí zdroje jsou soustředěné v bibliografii a snapshotových přílohách;
- bibliografie byla přepsána do podoby finální zdrojové vrstvy s preferencí primárních zdrojů;
- subtitle byl změněn z pracovního deníkového rámování na jasný čtenářský příslib.

## Co zůstalo záměrně beze změny

Nejsilnější technické kapitoly nebyly „literárně přepisovány“ jen proto, aby vypadaly nové. Zejména:

- enterprise data a RAG,
- anatomie a smyčka agenta,
- bezpečnost,
- evaluace,
- praktické projekty

už mají správnou informační hustotu a engineering charakter. Jejich síla je v konkrétnosti, ne v efektnějším stylu.

## Finální redakční scan

Samostatný kvalitativní scan celého rukopisu po úpravách našel:

- **0 interních redakčních zbytků**,
- **0 chybných číselných cross-reference**,
- **0 přesně duplicitních dlouhých odstavců mezi soubory** v mechanickém prepress auditu,
- jediný vědomě opakovaný podpisový motiv mezi úvodem a kapitolou 33 je ponechán záměrně.

## Source / prepress stav

Finální automatizovaný předtiskový audit v0.7:

- **36 kapitol** + samostatný úvod,
- **7 příloh**,
- **43 screen SVG + 43 print SVG**,
- **50 576 slov v číslovaných kapitolách**,
- **5 295 slov v přílohách**,
- neexistující image reference: **0**,
- strukturální chyby screen SVG: **0**,
- print SVG problémy: **0**,
- explicitní TODO / placeholder markery: **0**,
- neuzavřené code fences: **0**,
- **Final-editorial gate: PASS**.

## Finální proof PDF

`AI-book-proof-v0.7.pdf`:

- **548 stran**,
- formát **170 × 240 mm**,
- **73 478 extrahovaných word tokens**,
- nejmenší textový span **7,18 pt**,
- text pod 6,5 pt: **0**,
- úplně prázdné strany: **0**,
- bloky mimo stránku: **0**,
- možné orphan headings: **0**,
- text uvnitř 7mm safety margin: **0**,
- potenciální text overlaps: **0**,
- **Automated proof gate: PASS**,
- **Automated layout gate: PASS**.

Sedm sparse-page kandidátů je ponecháno k fyzické vizuální kontrole; automatický audit je nevyhodnotil jako mechanický blocker.

## Grafická redakce

Tři nové podpisové diagramy byly samostatně vyrenderovány a zkontrolovány ve screen i print variantě. Jejich význam není závislý na barvě a print verze používají zvětšené popisky.

Grafické pravidlo pro tuto knihu zůstává:

> **WOW nevytváří dekorace. WOW vzniká, když složitou myšlenku dokážeme pravdivě zkomprimovat do obrazu, který si čtenář zapamatuje a použije.**

Proto v této fázi nedoporučuji přidávat další dekorativní AI ilustrace.

## Co už teď neměnit

- nekomprimovat rukopis na arbitrární počet stran za cenu ztráty praktických příkladů;
- nepřidávat každý nový model nebo framework, který vyjde mezi proofem a tiskem;
- nehomogenizovat dalšími přepisy osobní hlas kapitoly 33;
- neměnit knihu v katalog API, vendorů a nástrojů;
- nepřidávat vizuální efekty bez informační funkce;
- nepřepisovat silné technické kapitoly jen proto, aby byl „vidět další edit“.

## Co zbývá před skutečným tiskem

Tohle už nejsou redakční chyby rukopisu, ale výrobní gates:

- definitivní autorské jméno a jeho typografická podoba na titulní straně a obálce;
- tiráž, copyright, vydavatel/imprint a ISBN;
- finální obálka, hřbet a zadní strana;
- potvrzení parametrů konkrétní tiskárny, bleed a případného CMYK workflow;
- fyzický nátisk a kontrola tabulek, přechodových stran, diagramů a nejmenších monospace bloků na papíře.

## Doporučení k anglické verzi

Anglická edice by neměla vzniknout mechanickým překladem větu po větě. Má zachovat stejnou koncepční páteř, ale projít **native technical editingem**: idiomatická angličtina, terminologie pro mezinárodní publikum, revize českých firemních příkladů a nový fact-check snapshotů k datu vydání.

Koncepční základ pro anglickou edici je ale v této verzi dostatečně silný: kniha není postavená na lokálních názvech produktů, nýbrž na přenosném modelu **model → context/data → tools → control → verification → value**.

## Finální rozhodnutí

**Obsah zamknout.**

Další krok je knižní výroba a fyzický proof, ne další plošný AI rewrite.