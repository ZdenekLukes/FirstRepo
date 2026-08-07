# Finální redakční a předtiskový audit — 2026-08-07

## Verdikt

**Stav: NO-GO DO TISKU / GO DO FINÁLNÍ REDAKČNÍ FÁZE.**

Rukopis má velmi dobrou pedagogickou architekturu, konzistentní technickou myšlenku a několik již velmi silných praktických kapitol. Není ale ještě kompletní a není připravený jako fyzická kniha. Největší riziko není v základní koncepci, ale v nerovnoměrné dokončenosti, chybějícím publikačním aparátu a v grafice optimalizované pro obrazovku místo sazby.

Audit kombinoval:

- mechanickou kontrolu všech 37 kapitol a 7 příloh,
- kontrolu Markdown struktury, obrázkových referencí, SVG a code fences,
- redakční kontrolu struktury a terminologie,
- ruční čtení reprezentativních a rizikových kapitol,
- kontrolu rychle stárnoucích snapshotů proti primárním zdrojům,
- kontrolu připravenosti vizuálů pro knižní tisk.

---

# 1. Co už je ve velmi dobrém stavu

## 1.1 Pedagogická osa knihy

Pořadí kapitol dává velmi dobrý smysl:

**historie → základní pojmy → LLM → schopnosti a limity → modely → cloud/local → prompting/context → data/RAG → tools/MCP → agenti → engineering → security → firemní adopce → evaluace/ekonomika → budoucnost → praktická kuchařka.**

Je to silnější než encyklopedické řazení podle buzzwordů. Čtenář postupně získává mentální model a teprve potom skládá celý systém.

## 1.2 Ústřední myšlenka je konzistentní

Napříč knihou se drží užitečné rozlišení:

- model,
- aplikace,
- celý AI systém,
- deterministické nástroje,
- data a context,
- verifikace,
- člověk jako decision maker.

To je dobrá páteř knihy a neměla by se v redakci ztratit.

## 1.3 Praktické engineering kapitoly fungují

Zvlášť dobře působí kapitoly o stavbě agenta, evaluaci, nástrojích a AI-assisted engineeringu. Mají konkrétní vstup, příklad, failure mode, pravidlo a takeaway. Není potřeba je uměle prodlužovat jen kvůli počtu stran.

## 1.4 Mechanická integrita je dobrá

Automatický audit nad celým rukopisem:

- 37 kapitol,
- 48 976 slov v hlavním textu,
- 39 SVG diagramů,
- 0 neexistujících image referencí,
- 0 strukturálně rozbitých SVG,
- 0 neuzavřených code fences,
- 0 přesně duplicitních dlouhých odstavců mezi soubory.

To je velmi dobrý technický základ pro další sazbu.

---

# 2. BLOCKERY — před tiskem nutně opravit

## B1 — Kapitola 37 není napsaná

`37 - Deset praktických projektů od začátečníka k agentnímu systému.md` má přibližně 70 slov. Obsahuje pouze názvy deseti projektů bez samotných projektů.

Přitom jde o závěrečnou „praktickou kuchařku“, která by měla být jedním z nejsilnějších důvodů knihu vlastnit.

### Požadavek před tiskem

Každý projekt musí minimálně obsahovat:

1. cíl,
2. co se čtenář naučí,
3. potřebné nástroje,
4. vstupní data,
5. postup krok za krokem,
6. expected result,
7. jak ověřit, že výsledek funguje,
8. typické chyby,
9. bezpečnostní omezení,
10. další rozšíření.

Doporučení: kapitola 37 může být klidně jedna z nejdelších kapitol knihy.

## B2 — Přílohy A–G jsou stále kostry

Celých sedm příloh má dohromady pouze přibližně 260 slov.

Konkrétně:

- A — slovník: jen seznam termínů bez definic,
- B — modely: prázdná tabulka,
- C — nástroje: kostra,
- D — hardware sizing: kostra,
- E — security checklist: kostra,
- F — agent checklist: velmi krátká kostra,
- G — experimenty: šablona.

Přílohy jsou v aktuálním obsahu slíbené čtenáři, takže buď musí být skutečně dokončeny, nebo je nutné je z finálního obsahu odstranit.

## B3 — Kapitola 34 obsahuje explicitní placeholdery

V osobní kapitole zůstávají tři bloky `[DOPLNIT: ...]`:

- konkrétní moment, kdy se změnilo chápání model vs. systém,
- konkrétní experiment, který překvapil,
- vlastní zkušenost s hardwarem/modely a VRAM.

Tato kapitola má potenciál být jedním z největších odlišení knihy od generického AI handbooku. Bez skutečných osobních experimentů ale působí spíš jako další shrnutí předchozích kapitol.

### Doporučení

Buď ji opravdu personalizovat konkrétními daty, chybami a změnami názoru, nebo ji výrazně zkrátit. Nevymýšlet zkušenosti jen proto, aby kapitola působila osobně.

## B4 — Chybí finální citační a bibliografický systém

Snapshotové kapitoly 5, 15 a 25 mají dobré primární odkazy. Velká část knihy však nemá žádný systematický zdrojový aparát; například historická část pracuje s desítkami faktických milníků bez zdrojové sekce.

Technická popularizační kniha nepotřebuje akademickou citaci za každou větou. Potřebuje ale jednotné pravidlo.

### Navržený systém

- u rychle se měnících tvrzení: konkrétní zdroj + datum ověření,
- u historických/technických kapitol: 3–8 primárních nebo autoritativních zdrojů na konci kapitoly,
- na konci knihy: souhrnná bibliografie a doporučená literatura,
- u převzatých obrázků nebo dat vždy jasná licence/zdroj; vlastní diagramy označit jako vlastní.

## B5 — Chybí evropská governance/regulační vrstva

Kniha má rozsáhlou část o bezpečné firemní adopci AI, ale v současném rukopisu není zpracovaný EU AI Act ani GDPR jako součást rozhodování o firemním použití.

Pro českého/evropského čtenáře v srpnu 2026 je to významná mezera. Není nutné psát právnickou učebnici. Je ale potřeba vysvětlit minimálně:

- role provider / deployer,
- risk-based přístup,
- AI literacy,
- transparentnost při interakci s AI a AI-generated content,
- rozdíl mezi AI security, privacy a compliance,
- vztah k osobním údajům/GDPR,
- proč governance není totéž jako technická security,
- že konkrétní právní posouzení patří právníkovi/compliance.

Doporučené umístění: samostatná podkapitola v části X nebo krátká samostatná kapitola mezi bezpečností a firemní strategií.

## B6 — Diagramy jsou screen-first, ne print-ready

Všech 39 diagramů používá jednotný tmavý RGB design. To je výborné pro HTML a obrazovku, ale ne automaticky pro fyzickou knihu.

Generátor používá šířku 1200 jednotek a typické velikosti textu 12–21 jednotek. Při běžném vložení obrázku na cca 140–160 mm šířky vychází nejmenší text zhruba kolem 4–6 pt.

To je pro knihu příliš malé.

### Povinné před tiskem

- vytvořit print/light variantu diagramů,
- zvětšit minimální velikost textu při cílové sazbě alespoň přibližně na 7,5–9 pt,
- provést grayscale proof,
- zkontrolovat RGB/CMYK workflow podle požadavků tiskárny,
- zkontrolovat, zda jsou fonty v PDF skutečně vložené,
- ověřit všechny diagramy v reálné velikosti na vytištěné stránce.

## B7 — Není hotová finální sazba, takže skutečný preflight zatím nelze dokončit

Markdown a SVG mohou být perfektní a přesto může finální PDF obsahovat:

- špatné page breaks,
- sirotky a vdovy,
- nadpis na konci stránky,
- rozdělenou tabulku,
- příliš malý code block,
- obrázek oddělený od popisku,
- font substitution,
- problém s okraji nebo spadem,
- neaktuální čísla stran v TOC.

Proto musí po redakci vzniknout skutečný **print proof PDF** a nad ním druhý preflight audit.

---

# 3. MAJOR — redakční problémy vysoké priority

## M1 — Terminologie potřebuje style sheet

Automatický audit ukazuje výrazné střídání českých a anglických forem. Orientačně:

| Koncept | EN forma | CZ forma |
|---|---:|---:|
| context / kontext | 118 | 65 |
| tool / nástroj | 203 | 196 |
| workflow / pracovní postup | 105 | 1 |
| use-case / případ použití | 92 | 0 |
| local / lokální | 33 | 75 |
| memory / paměť | 71 | 27 |
| knowledge base / znalostní báze | 22 | 2 |
| reasoning / uvažování | 79 | 1 |
| permissions / oprávnění | 54 | 28 |
| verification / ověření/verifikace | 64 | 23 |

To samo o sobě není chyba — technické publikum běžně používá anglické termíny. Chyba by byla nechat varianty bez pravidla.

### Doporučený princip

Při prvním výskytu:

**český popis + zavedený anglický termín v závorce**

Potom používat jednu zvolenou formu konzistentně.

Například lze ponechat `workflow`, `reasoning`, `tool use`, `context window`, `RAG`, `agent`, ale běžnou českou větu není nutné plnit anglickými plurály typu `tools`, `permissions`, `results`, pokud nepřinášejí přesnější význam.

## M2 — První kapitoly používají jiný závěrečný formát

Kapitoly 2–3 používají `Shrnutí kapitoly`, většina dalších `Co si z kapitoly odnést`. Kapitola 1 má vlastní mentální model a přechod.

Obsahově je to v pořádku, vizuálně/redakčně je vhodné vybrat jednu konvenci nebo záměrně definovat dvě různé kategorie.

## M3 — Koncepční opakování v agentní části

Kapitoly 14–20 správně navazují, ale několikrát znovu vysvětlují podobnou rovnici:

`model + tools + state + loop + verification`.

Přesná duplicita odstavců nebyla nalezena, takže nejde o copy-paste problém. Jde o významové opakování.

### Doporučení

- kapitola 14: nástroje,
- 15: standardizace integrací,
- 16: definice agenta,
- 17: loop,
- 18: implementační cookbook,
- 19: multi-agent trade-offs,
- 20: orchestrace/reliability.

Při finálním redakčním kole odstranit z každé kapitoly vše, co pouze znovu definuje předchozí vrstvu, a nahradit to krátkým cross-reference.

## M4 — Podobná kumulace v části o firemní adopci

Kapitoly 26–30 opakovaně zdůrazňují, že AI není chatbot, ale proces + data + nástroje + governance + lidé.

Myšlenka je správná. Potřebuje ale jasné rozdělení rolí kapitol:

- 26 = strategický argument,
- 27 = readiness assessment,
- 28 = portfolio use-cases,
- 29 = experimentální metoda pilotu,
- 30 = people/change management.

## M5 — Kapitola 34 potřebuje být skutečně osobní, jinak opakuje knihu

Po doplnění reálných experimentů se opakování stane hodnotným: čtenář uvidí, jak se abstraktní myšlenky promítly do skutečné zkušenosti. Bez nich je kapitola převážně rekapitulací.

## M6 — Kapitola 1 stále obsahuje velká ASCII schémata navzdory novému timeline obrázku

Na konci kapitoly je dlouhý ASCII „Mentální model celé historie“ a ještě další řetězec `PROGRAM → MODEL → ... → AI SYSTEM`.

Není nutné odstranit všechny ASCII bloky v knize. Zde ale nový timeline SVG už část stejné práce dělá. Doporučení: ponechat jeden silný celostránkový vizuál a text zkrátit.

## M7 — Obrázky nejsou číslované

Popisky mají jednotnou formu `Obrázek: ...`, ale chybí například:

- Obrázek 3.1,
- Obrázek 3.2,
- Obrázek 12.1.

Pro tištěnou knihu je číslování výhodné pro cross-reference v textu i pozdější úpravy sazby.

## M8 — Jazyk diagramů je směs češtiny a angličtiny

V jednom diagramu mohou být české nadpisy a anglické labely (`Observe`, `Reason`, `Plan`, `Act`, `Verify`, `Knowledge base`, `Tool call`, `Working memory`).

Pro technickou knihu to může být záměr. Musí to ale odpovídat style sheetu celé knihy.

---

# 4. CONTENT CHECK — po částech

## ČÁST I — Historie

**Hodnocení: obsahově silná, ale potřebuje zdroje a vizuální zjednodušení.**

Plus:

- historie není samoúčelná,
- dobře vede k dnešnímu model + tool + system pohledu,
- technické milníky jsou správně seřazené.

Před tiskem:

- zdrojová sekce,
- zredukovat duplicitní ASCII timeline,
- překontrolovat každý letopočet v jedné finální fact-check pass.

## ČÁST II — Základy dnešní AI

**Hodnocení: jedna z nejsilnějších částí.**

Kapitoly 2–4 vytvářejí dobrý mentální model bez matematiky. Doporučuji hlavně sjednotit závěrečný formát a terminologii.

## ČÁST III — Modely a jejich porovnávání

**Hodnocení: dobrý snapshot, vysoké riziko zastarávání.**

Kapitola 5 je správně označena konkrétním datem a používá primární zdroje. Spot-check hlavních modelových rodin k 7. 8. 2026 neukázal zásadní rozpor.

Před vydáním se musí snapshot znovu zmrazit přesně v den content freeze.

## ČÁST IV — Cloud, local a hardware

**Hodnocení: praktická a relevantní.**

Doporučení:

- u hardwarových čísel jasně odlišit hrubé sizing rule od benchmarku,
- v příloze D skutečně dodat sizing tabulku,
- vysvětlit, že délka contextu/KV cache může měnit reálnou paměťovou potřebu.

## ČÁST V–VI — Prompting, context, RAG, second brain

**Hodnocení: logická návaznost.**

Dobré je, že kniha nepřehání prompt engineering a posouvá čtenáře ke context engineeringu.

Redakčně pohlídat překryv embeddings mezi kapitolami 3 a 12 a rozdíl mezi token embeddings a retrieval embedding modely.

## ČÁST VII–VIII — Tools, MCP, agenti

**Hodnocení: technicky aktuální a praktická, ale nejvíce potřebuje de-duplication.**

MCP část odpovídá aktuální specifikaci 2026-07-28 včetně stateless core, header-based routing a cacheable list results.

Před tiskem je vhodné explicitně připomenout, že `skills`, `plugins` a `connectors` jsou často platform-specific pojmy a nejsou všechny součástí MCP core standardu.

## ČÁST IX — AI jako pracovní systém / engineering

**Hodnocení: hlavní diferenciátor knihy.**

Kapitola 24 o analog IC designu dává knize vlastní identitu. Tento směr bych spíš posílil než zkracoval.

Technická korekce k formulacím typu „simulátor je deterministický model reality“: přesnější je říct, že simulátor poskytuje externě ověřitelný výsledek podle definovaného modelu a jeho předpokladů. Simulace není sama o sobě realita a nemusí být vždy deterministická.

## ČÁST X — Security

**Hodnocení: technicky velmi dobrý základ.**

Silné body:

- prompt injection není security boundary,
- least privilege,
- sandbox,
- human approval,
- memory/context poisoning,
- supply chain,
- model provenance,
- defense in depth.

Aktuální OWASP směr je s textem dobře kompatibilní.

Chybí ale governance / AI Act / GDPR vrstva — viz blocker B5.

## ČÁST XI — Firemní adopce

**Hodnocení: užitečná, potřebuje odstranit rétorické opakování.**

Největší přidaná hodnota bude ve skutečných maticích, formulářích a příkladech. Proto je důležité dokončit přílohy.

## ČÁST XII — Evaluace a ekonomika

**Hodnocení: velmi dobrá.**

Kapitola 31 je stručná, ale obsahově hutná. Dobře rozlišuje deterministic evals, LLM-as-a-judge, RAG eval, agent eval a business metric.

Ekonomiku před tiskem aktualizovat přesně k content freeze, pokud se použijí konkrétní ceny modelů/GPU.

## ČÁST XIII — Budoucnost a osobní reflexe

**Hodnocení: kapitola 33 dobrá, 34 zatím nedokončená.**

Kapitola 33 správně používá opatrný jazyk a rozlišuje trend od jisté předpovědi.

Kapitola 34 musí získat reálný osobní obsah.

## ČÁST XIV — Praktická kuchařka

**Hodnocení: 36 dobrá, 37 blocker.**

Kapitola 36 je dobrý snapshot nástrojového stacku a správně zdůrazňuje minimalismus.

Kapitola 37 zatím neexistuje jako skutečná kapitola.

---

# 5. FACT CHECK A AKTUÁLNOST

## PASS

Při spot-checku proti primárním zdrojům byly aktuální:

- GPT-5.6 Sol,
- Claude Opus 4.8 / Sonnet 5 family,
- Gemini 3.x / 3.6 Flash,
- Grok 4.5,
- hlavní open-weight rodiny uváděné v kapitole 5,
- MCP specifikace 2026-07-28,
- OWASP agentic AI security témata.

## Riziko

Nejrychleji stárnou kapitoly:

- 5 — modely,
- 8 — lokální provoz a hardware,
- 15 — MCP,
- 25 — security landscape,
- 33 — trendy,
- 36 — nástroje.

### Publikační pravidlo

Při content freeze přidat do každé z nich jednotný box:

> Snapshot ověřen: YYYY-MM-DD. Konkrétní modely, ceny, verze a produkty se mohou změnit.

---

# 6. VISUAL CHECK

## PASS

- všech 39 SVG má validní strukturu,
- všechny image reference existují,
- SVG mají `viewBox`, `<title>` a `<desc>`,
- vizuální styl je velmi konzistentní,
- diagramy skutečně podporují hlavní mentální model knihy.

## Před tiskem opravit

1. **Print/light theme.**
2. **Minimální fyzická velikost textu.**
3. **Číslování obrázků.**
4. **Cross-reference z textu.**
5. **Grayscale proof.**
6. **Font embedding.**
7. **CMYK/RGB podle tiskového workflow.**
8. **Kontrola na skutečné vytištěné stránce 100 %.**

Kapitola 33 nemá obrázek — není to chyba. Jeden finální „mapa trendů“ by ale mohl pomoci.

Kapitola 34 může zůstat textovější; osobní část nepotřebuje diagram jen kvůli konzistenci.

---

# 7. COPYEDIT / TYPOGRAFIE

Před sazbou provést jednotný copyedit:

- české uvozovky vs. ASCII quotes mimo code blocks,
- em dash / en dash / hyphen,
- zápis `on-prem`, `open-weight`, `multi-agentní`, `AI-assisted`,
- `context window` vs. `kontextové okno`,
- jednotný zápis `use-case` nebo `use case`,
- singular/plural anglických technických termínů,
- procenta a mezery (`95 %`),
- GB / MB / token/s,
- `16 GB VRAM` místo různých variant,
- názvy produktů s přesným casingem,
- jednotky SI a µ symbol,
- jednotné tabulkové hlavičky,
- jednotné názvy sekcí `Co si z kapitoly odnést`.

Doporučení: vytvořit `STYLE_GUIDE.md` a podle něj následně automaticky i ručně projít všech 37 kapitol.

---

# 8. FRONT MATTER / BACK MATTER — zatím chybí publikační vrstva

`00 - INDEX.md` je dnes správně pracovní Obsidian index, nikoli finální obsah knihy.

Pro skutečnou publikaci bude potřeba rozhodnout a doplnit:

## Front matter

- titulní strana,
- autor,
- podtitul,
- copyright / licence,
- edice a datum snapshotu,
- ISBN, pokud bude,
- disclaimer k rychle se měnícím technologiím,
- případně disclaimer k bezpečnosti/právním informacím,
- předmluva / „Jak tuto knihu číst“,
- finální TOC s čísly stran.

## Back matter

- plný slovník,
- bibliografie / zdroje,
- doporučená literatura,
- praktické checklisty,
- rejstřík, pokud bude fyzická kniha delší,
- autor bio,
- případně odkaz na online aktualizace / repository companion.

---

# 9. PŘEDTISKOVÝ PDF PREFLIGHT — až po sazbě

Na finálním exportu zkontrolovat:

- trim size,
- bleed, pokud bude potřeba,
- bezpečnou zónu u hřbetu,
- embedded fonts,
- image effective DPI,
- přetékání textu,
- page breaks,
- widows/orphans,
- nadpisy osamocené na konci stránky,
- dělení tabulek,
- dělení code blocků,
- obrázek + caption na stejné stránce,
- čitelnost diagramů při 100% fyzickém tisku,
- grayscale/CMYK,
- aktivní a správné odkazy pro ebook/PDF,
- čísla stran a TOC,
- running headers/footers,
- případné prázdné stránky mezi částmi,
- PDF/X profil požadovaný tiskárnou.

Bez tohoto kroku nelze seriózně říct „ready to print“.

---

# 10. Doporučené pořadí oprav

## Fáze 1 — dokončit obsah

1. Napsat kapitolu 37.
2. Dokončit přílohy A–G.
3. Doplnit reálné osobní zkušenosti v kapitole 34.
4. Doplnit EU AI Act / GDPR / governance.

## Fáze 2 — strukturální redakce

5. Zredukovat významové překryvy 14–20.
6. Zredukovat překryvy 26–30.
7. Upravit 33–34 tak, aby budoucnost a osobní reflexe měly rozdílnou funkci.
8. Zjednodušit zbylá velká ASCII schémata, zejména v kapitole 1.

## Fáze 3 — zdroje a fact check

9. Doplnit jednotné chapter sources.
10. Udělat finální fact-check všech snapshotů k content freeze.
11. Doplnit bibliografii.

## Fáze 4 — language pass

12. Vytvořit style sheet.
13. Sjednotit terminologii, názvy sekcí, jednotky, punctuation a produktový casing.

## Fáze 5 — print visual pass

14. Vytvořit print verzi SVG.
15. Číslovat obrázky a doplnit cross-reference.
16. Zkontrolovat velikost textu a grayscale.

## Fáze 6 — sazba a proof

17. Vytvořit finální PDF.
18. Udělat page-by-page visual proof.
19. Provést technický PDF preflight.
20. Content freeze + release tag v GitHubu.

---

# 11. Acceptance criteria pro stav READY TO PRINT

Knihu označit `READY TO PRINT` teprve když:

- [ ] žádná kapitola není pouze osnova,
- [ ] žádný `[DOPLNIT]`, TODO nebo placeholder,
- [ ] přílohy uvedené v TOC skutečně existují,
- [ ] všechny časově citlivé kapitoly mají freeze date,
- [ ] dokončený source/bibliography pass,
- [ ] governance/regulatory gap je vyřešen nebo vědomě vymezen scope,
- [ ] terminologie je sjednocena style guide,
- [ ] všechny figure mají finální číslo/caption,
- [ ] všechny diagramy jsou čitelné v cílové fyzické velikosti,
- [ ] finální PDF prošlo font/image/page preflightem,
- [ ] proveden ruční proof každé stránky,
- [ ] README/index už neoznačují vydávanou verzi jako rough draft,
- [ ] vytvořen release tag odpovídající přesně vytištěné verzi.

---

# Závěr

Největší pozitivní zjištění auditu je, že **není potřeba měnit základní koncepci knihy**. Její osa je dobrá a některé kapitoly už mají kvalitu blízkou finálnímu textu.

Největší problém je, že rukopis kombinuje tři různé stupně dokončenosti:

1. téměř hotové praktické kapitoly,
2. kvalitní, ale stále redakčně neučesané drafty,
3. čisté kostry — zejména kapitola 37 a přílohy.

Proto další správný krok není „sázet knihu“, ale **udělat jeden řízený final-edit pass podle blockerů výše**. Teprve po něm má smysl vytvořit skutečný print proof a provést poslední stránkovou korekturu.
