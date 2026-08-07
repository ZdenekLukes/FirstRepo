# REVIEW REPORT

> Hloubkové redakční, obsahové a technické review knihy **„AI od základů k agentním systémům"** (v0.4, release candidate, snapshot 7. 8. 2026). Review provedeno nad plným textem všech 37 kapitol, 7 příloh, bibliografie a style guide. Reviewer: Claude (Anthropic), 7. 8. 2026.

---

## 1. Executive verdict

- **Celkové hodnocení:** Nadprůměrně kvalitní, konzistentní a prakticky orientovaný rukopis. Kniha plní svůj hlavní slib — vybudovat správný mentální model AI od LLM po agentní systémy — lépe než většina srovnatelných titulů. Hlavní slabinou není kvalita obsahu, ale jeho **hustota**: klíčové myšlenky se opakují napříč kapitolami a fragmentovaný sloupcový styl nafukuje rozsah.
- **Připravenost k publikaci:** **CONDITIONAL GO** — po (1) deduplikačním průchodu, (2) doplnění úvodu knihy, (3) fact-checku snapshot kapitol k datu vydání a (4) rozhodnutí o prázdné příloze G.
- **Největší síla knihy:** Důsledně budovaný a nikdy neporušený mentální model `MODEL ≠ APLIKACE ≠ RAG ≠ AGENT ≠ AGENTNÍ SYSTÉM` + verifikace jako červená nit. Čtenář z knihy odejde s správným obrazem, ne s katalogem buzzwordů.
- **Největší slabina knihy:** Nízká koncentrace na stránku. Stejná jádrová myšlenka („model + context + tools + verification = systém", „cena za dokončenou úlohu, ne za token", „benchmark ≠ váš use-case") je plně rozvinuta na 4–7 místech. Kniha deklaruje „100 stran koncentrovaných informací před 300 stranami" — aktuální text je blíže druhému pólu.
- **Tři nejdůležitější změny před vydáním:**
  1. **Deduplikační průchod** — pro každou z ~8 opakovaných jádrových myšlenek určit jedno kanonické místo a ostatní výskyty zkrátit na jednu větu s odkazem (detailně sekce 6). Odhadovaná úspora 15–20 % rozsahu bez ztráty obsahu.
  2. **Napsat úvod knihy.** Kniha nemá předmluvu — začíná rovnou historií. Chybí: pro koho kniha je, co bude čtenář umět, jak knihu číst (např. tři čtenářské cesty: úplný začátečník / inženýr / manažer zavádějící AI). Zadání pro cílového čtenáře existuje jen mimo knihu.
  3. **Vyřešit rozpor mezi slibem a obsahem osobní vrstvy.** Podtitul zní „Co jsem se zatím naučil", ale příloha G (Vlastní experimenty) je prázdná šablona a kap. 35 je roadmapa budoucích experimentů. Buď doplnit 3–5 skutečných experiment write-upů (stačí malé, s čísly), nebo upravit framing.

---

## 2. Hodnocení knihy

| Oblast | Hodnocení 1–10 | Komentář |
|---|---:|---|
| Struktura | 8 | Logická progrese model→context→data→tools→agent→firma. Slabiny: chybějící úvod, duplicita 35↔37, kap. 11 příliš tenká na samostatnou kapitolu. |
| Srozumitelnost | 9 | Vynikající. Krátké věty, příklady, analogie (pracovní stůl, USB-C, motor≠automobil) fungují. |
| Technická správnost | 8 | Nenašel jsem prokazatelně chybné tvrzení. Několik položek NEEDS FACT CHECK (názvy modelů v snapshot kapitolách — viz sekce 9). Paměťové výpočty, MoE, KV cache, AI Act čl. 50 — vše správně. |
| Hloubka | 7 | Rámec CO→PROČ→JAK→KDY (ne)POUŽÍT je dodržen u většiny témat. Mělčí místa: fine-tuning (kdy ano), chybí jeden kompletní reálný trace agentního běhu. |
| Praktická hodnota | 8 | Checklisty, scorecardy, projektový žebřík a přílohy E/F jsou přímo použitelné. Sráží ji absence vlastních experimentálních dat. |
| Koncentrace informací | 6 | Hlavní slabina. Opakování jader + trojitá shrnutí kapitol + jednoslovné code-bloky. |
| Konzistence | 9 | Terminologie dle style guide dodržena téměř bezchybně. Jednotný formát kapitol. Drobnosti: nekonzistentní úroveň nadpisů závěrečných sekcí (H1 vs H2). |
| Aktuálnost | 8 | Vzorná snapshot disciplína (kap. 5, 15, 25, 33, 36, přílohy B/C s primárními zdroji). Nutný finální fact-check názvů modelů k datu vydání. |
| Vizuální vysvětlení | 7 | SVG diagramy pro většinu kapitol + funkční ASCII schémata. Kap. 33 a 34 diagram nemají; některá ASCII schémata jsou dekorace, ne vysvětlení. |
| Celkový přínos | 8 | Pro cílového čtenáře reálně užitečná příručka. Po deduplikaci a doplnění úvodu 9. |

---

## 3. P0 — Blockers

**Žádný potvrzený P0.** Nenašel jsem faktickou, bezpečnostní ani regulatorní chybu, která by blokovala vydání. Jediná podmínka s charakterem brány: **před vydáním musí proběhnout fact-check snapshot kapitol (5, B) proti stavu trhu k datu tisku** — viz [FC-01]–[FC-03] v sekci 9. Pokud by kniha vyšla s neaktuálním přehledem frontier modelů v kapitole explicitně datované na 08/2026, poškodí to důvěryhodnost celé snapshot vrstvy.

---

## 4. P1 — Major issues

### [P1-1] Systémové opakování jádrových myšlenek
- **Kapitola / stránka:** napříč celou knihou (detailní mapa v sekci 6)
- **Problém:** Nejméně 8 klíčových myšlenek je plně rozvinuto na 4–7 místech. Nejde o záměrné pedagogické připomenutí (to by byla jedna věta s odkazem), ale o opakované několika­odstavcové výklady téhož.
- **Proč je důležitý:** Kniha sama deklaruje jako zásadní redakční princip koncentraci. Aktuální stav tento princip porušuje nejvíc ze všech nalezených problémů.
- **Dopad na čtenáře:** Pocit „tohle už jsem četl", klesající pozornost ve druhé polovině knihy, delší čas čtení bez přidané hodnoty.
- **Doporučená změna:** Deduplikační průchod dle tabulky v sekci 6. Pravidlo: každá jádrová myšlenka má jedno kanonické místo; jinde max. 1 věta + odkaz na kapitolu.

### [P1-2] Chybí úvod knihy
- **Kapitola / stránka:** před kap. 1 (soubor 00 je jen index)
- **Problém:** Kniha nemá předmluvu ani „jak číst tuto knihu". Čtenář vstupuje rovnou do 4 500 slov historie, aniž ví, co mu kniha slíbila a jak je stavěná.
- **Proč je důležitý:** Definice cílového čtenáře a cílů (přesně to, co je v zadání tohoto review) v knize samotné neexistuje. První kapitola je přitom nejdelší v knize — nejrizikovější místo pro ztrátu čtenáře.
- **Dopad na čtenáře:** Manažer neví, že může přeskočit na část XI; inženýr neví, že části II–V může proletět. Nikdo neví, že kniha končí praktickou kuchařkou.
- **Doporučená změna:** 3–5 stran úvodu: pro koho, co budu umět (10 bodů z autorova zadání je hotový materiál), struktura knihy, tři čtenářské cesty, poznámka o snapshot kapitolách a stárnutí obsahu.

### [P1-3] Prázdná osobní/experimentální vrstva vs. slib podtitulu
- **Kapitola / stránka:** příloha G, kap. 34, kap. 35
- **Problém:** Podtitul a rámování slibují zápisník zkušeností a experimentů. Reálně: příloha G je prázdná šablona s backlogem *budoucích* experimentů, kap. 35 je roadmapa co *teprve* přijde, a konkrétní zkušenost s čísly je v knize jediná (8 GB → 32 GB VRAM příběh v 34.3, bez tabulky výsledků).
- **Proč je důležitý:** Osobní evidence je deklarovaná diferenciace knihy proti generické učebnici. Bez ní působí kapitoly jako 34.4 („co se ukázalo jako opravdu užitečné") jako obecná tvrzení bez důkazu — přesně typ obsahu, který kniha sama kritizuje („demo bez baseline").
- **Dopad na čtenáře:** Čtenář, který si koupí „co jsem se naučil", dostane dobře napsanou příručku, ale učebnicového typu. Rozpor si všimne.
- **Doporučená změna:** Varianta A (lepší): doplnit do přílohy G 3–5 vyplněných experimentů dle vlastní šablony (EXP-001 hardwarový srovnávací test se v 34.3 zjevně už odehrál — stačí ho zpětně zdokumentovat). Varianta B: zmírnit podtitul/rámování a přílohu G explicitně označit jako šablonu pro čtenáře.

### [P1-4] Duplicita kapitol 35 a 37
- **Kapitola / stránka:** kap. 35 (Co mě ještě čeká) vs. kap. 37 (Deset praktických projektů)
- **Problém:** Obě kapitoly obsahují týž žebřík: local stack → benchmark → RAG → tools → single agent → evals/observability → memory → multi-agent → firemní pilot → produkce. Kap. 35 jej podává jako osobní roadmapu (14 kroků), kap. 37 jako projekty pro čtenáře (10 projektů). Překryv je ~80 %.
- **Proč je důležitý:** Jde o dvě z posledních čtyř kapitol — čtenář narazí na duplicitu v místě, kde má kniha gradovat.
- **Dopad na čtenáře:** Kapitola 37 (silnější, konkrétnější) působí jako opakování 35.
- **Doporučená změna:** Kap. 35 zkrátit na 2–3 strany čistě osobního rámování („proč tyto projekty a v jakém pořadí je plánuji já") a odkazovat do 37, kde zůstane veškerá substance. Alternativně 35 zcela rozpustit do úvodu části XIV.

### [P1-5] Kapitola 1 je nejdelší v knize a končí trojím shrnutím
- **Kapitola / stránka:** kap. 1 (4 564 slov; sekce 1.6 + „Co nás historie AI učí" + „Mentální model celé historie")
- **Problém:** Tři po sobě jdoucí sumarizační sekce téže kapitoly říkají totéž (algoritmy+data+compute; schopnost≠spolehlivost; kombinace technologií). Navíc pasáže 2022–2026 (ChatGPT, multimodalita, agenti) duplikují látku kapitol 5, 15–17 a 33.
- **Proč je důležitý:** Nejdelší kapitola stojí na začátku, před jakoukoli praktickou hodnotou — v rozporu s deklarovaným principem knihy.
- **Dopad na čtenáře:** Riziko, že netechnický čtenář knihu odloží dřív, než dojde k jádru (kap. 3–4).
- **Doporučená změna:** Zkrátit o ~30 %: sloučit tři závěrečná shrnutí do jednoho, roky 2023–2026 zhustit na 1–2 strany s odkazem „detailně v kap. 5 a 33".

---

## 5. P2 — Minor issues

### [P2-1] Kapitola 11 je příliš tenká na samostatnou kapitolu
843 slov, obsahově z poloviny rekapitulace 10.10 a předjímka 12. Sloučit jako úvodní sekci kapitoly 12 („Proč model nezná moje data → proto RAG"), nebo přiznat roli jednostránkového „mostu".

### [P2-2] Nekonzistentní hierarchie nadpisů
Závěrečné sekce („Co si z kapitoly odnést", praktické příklady) jsou v některých kapitolách `#` (kap. 4, 6, 7, 8, 16–22…), jinde `##` (kap. 2, 3). V kap. 11 jsou H1 nadpisy uprostřed kapitoly. Ovlivní generování TOC a sazbu. Sjednotit na `##`.

### [P2-3] Jednoslovné a dekorativní code-bloky
Desítky ```text``` bloků obsahují jedno slovo či frázi („Praha", „rychlý", „consumer chat"), nebo šipkové řetězce, kde žádná sekvence není (úvod kap. 4: „text ↓ shrnutí ↓ extrakce…" — jde o výčet, ne pipeline). V tištěné sazbě budou působit jako slide-deck. Projít a převést na běžný text/odrážky tam, kde blok nenese strukturu.

### [P2-4] Typo v kap. 15
`SKILL: verify-lDO-design` → `verify-LDO-design` (praktický příklad na konci kap. 15).

### [P2-5] Kapitola 8 nemá snapshot hlavičku
Kap. 8 jmenuje konkrétní nástroje (Ollama, llama.cpp, vLLM, Open WebUI) a hardware třídy, ale na rozdíl od kap. 5/15/25/36 nemá snapshot poznámku. Doplnit `snapshot: 2026-08-07` a jednu větu o stárnutí.

### [P2-6] Kap. 5.10 Video generation
Sekce sama přiznává, že „pro většinu firemních agentních systémů není video generation zatím centrální komponenta". Pro cílového čtenáře stačí odstavec, ne celá sekce. Zkrátit.

### [P2-7] Měření/metriky vyloženy třikrát
26.9 (měření výsledků), 29.4 (metriky pilotu) a kap. 31 (evaluace) se překrývají v ~40 %. Kanonickým místem je kap. 31; v 26.9 a 29.4 ponechat jen specifika (business baseline, go/no-go) a odkázat.

### [P2-8] Čtyři téměř identické „žebříky autonomie"
Tool permission ladder (kap. 14), stupně engineering autonomie (kap. 23), progressive trust (25.19), fáze rolloutu e-mailu (14.8). Jde o týž koncept s jiným číslováním. Definovat jeden kanonický žebřík (ideálně v kap. 14) a jinde na něj odkazovat s doménovou konkretizací.

### [P2-9] Kap. 33 a 34 nemají diagram
Jediné kapitoly bez vizuálu (mimo záměrně osobní 34). Pro 33 by „mapa trendů" (osa spolehlivost × autonomie, nebo timeline trendů) měla vysokou hodnotu — je to kapitola, kterou budou čtenáři citovat.

### [P2-10] Terminologie hallucination/halucinace
Kap. 4.11 nadpis „Hallucinations", slovník „Hallucination / halucinace", style guide neurčuje preferovanou formu. Doplnit do style guide a sjednotit (doporučuji „halucinace" v prose, anglicky při prvním výskytu).

---

## 6. Opakování a místa ke zkrácení

| Kapitola | Opakovaná myšlenka | Kde už byla vysvětlena | Doporučení |
|---|---|---|---|
| 1.8, 3 (2×), 4.16, 10.1, 14 úvod, 16.10, 26.1, 33 úvod, 34.1, 34.10 | „Model ≠ systém; AI SYSTEM = model + context + data + tools + verification" vč. opakované ASCII rovnice | plný výklad 2.11 a 3 (závěr) | Kanonicky: 2.11 + 3. Jinde 1 věta + odkaz. Rovnici v ASCII tisknout max. 2× v celé knize. |
| 4.11, 4.12, 30.6, 34.2 | „Plynulá/sebevědomá odpověď ≠ pravdivá" | 1 (ELIZA), 3.17 | Kanonicky: 4.11–4.12. V kap. 1 ponechat (historická pointa ELIZA), jinde zkrátit. |
| 4.14, 6.7, 10.7 | „Context window = pracovní stůl, ne dokonalá paměť" | 3.14 | Metaforu vyslovit 1×(3.14), rozvinout 1× (4.14). V 6.7 a 10.7 jen odkaz. |
| 8.19, 20.12, 29.7, 32.10, B.3 | „Cena za dokončenou úlohu, ne za token / tokens-per-second nejsou produktivita" | 6.9 | Kanonicky: 6.9 (výběr) + 32 (ekonomika detailně). Ostatní zkrátit na větu. |
| 26.9, 28 úvod, 31.1, 34.5, B.3 | „Veřejný benchmark ≠ váš use-case; rozhoduje vlastní test set" | 1 (Deep Blue), 6.2 | Kanonicky: 6.2. Jinde věta + odkaz. |
| 35.7, 36.9, 37 (projekt 10), G (EXP-005) | „Multi-agent jen s měřitelným důvodem; vždy proti single-agent baseline" | 19 (celá kapitola) | Kanonicky: 19. V 37/G ponechat (praktická aplikace), v 35 a 36 zkrátit. |
| 14.7, 15.11, 25.13 | Least privilege (výklad principu) | 14.7 první plný výklad | Kanonicky: 25.13 (security kapitola). V 14/15 jedna věta. Checklisty E/F beze změny. |
| 25.1, 27.5 | Data classification PUBLIC/INTERNAL/CONFIDENTIAL/RESTRICTED vč. téže tabulky | 7.8 | Kanonicky: 7.8 (tabulka) + E.1 (checklist). V 25.1 a 27.5 odkaz. |
| 1 (2025–2026 sekce) | Chatbot vs. agent, smyčka, tool use | plně v 16–17 | Zhustit, odkázat dopředu. |
| 3 závěr | Čtyři uzávěry kapitoly (2 obrázky + zapamatovat + mentální model) | tatáž kapitola | Sloučit do jednoho závěru; úspora ~15 % kapitoly. |

---

## 7. Co v knize chybí

Pouze položky s vysokou praktickou hodnotou pro cílového čtenáře:

1. **Úvod / jak číst tuto knihu** — viz [P1-2]. Nejvyšší hodnota za nejméně práce.
2. **Rozhodovací box „kdy fine-tuning"** — kniha správně říká, že training není cesta ke znalostem (kap. 11), ale nikde neříká, kdy fine-tuning/LoRA *dává* smysl (styl, formát, úzká klasifikace, latence malého modelu). Půl strany s rozhodovacím stromem `prompt → context/RAG → tools → až pak fine-tuning` uzavře díru v jinak kompletním rámci. Slovník pojem definuje, text ho nikdy nerozvine.
3. **Jeden kompletní reálný trace agentního běhu** — kniha má pseudokód (16.9, 18) a mini-trace (18.10), ale ani jeden skutečný end-to-end záznam: prompt → tool cally s argumenty → výsledky → oprava → výstup. Jedna dvoustrana s reálným (byť zkráceným) během by zhmotnila celou část VIII lépe než další diagram. Ideální umístění: kap. 18.
4. **Box „AI a čeština"** — kniha je česky pro české čtenáře, ale česko-specifika jsou roztroušena v půlvětách (tokenizace češtiny 3.2, čeština u STT 5.7). Sjednotit na půl strany: dopad tokenizace na cenu/kontext, výběr embedding modelu pro češtinu, STT/diarizace česky, kdy psát prompty anglicky.
5. **Vyplněné experimenty v příloze G** — viz [P1-3].

Vědomě **nenavrhuji** přidávat: etiku AI, dějiny filozofie AI, matematiku transformerů, přehled všech frameworků — kniha je správně vynechává.

---

## 8. Co bych naopak odstranil

1. Dvě ze tří závěrečných sumarizačních sekcí kap. 1 ([P1-5]).
2. Dva ze čtyř uzávěrů kap. 3 (ponechat „model není systém" + jedno shrnutí).
3. Kap. 5.10 Video generation zredukovat na odstavec ([P2-6]).
4. Kap. 11 jako samostatnou kapitolu ([P2-1]) — obsah z ~60 % přesunout/sloučit.
5. Kap. 35 v současném rozsahu ([P1-4]).
6. Duplikované výklady dle tabulky v sekci 6 (odhad úspory 8–12 tisíc slov).
7. Jednoslovné a čistě dekorativní ```text``` bloky ([P2-3]).
8. V 26.9 duplikát metrik (odkázat na 31).

Celkový potenciál: **zkrácení knihy o ~15–20 % bez ztráty jediné myšlenky** — přímé naplnění vlastního redakčního principu knihy.

---

## 9. Technický fact-check seznam

Pozn.: můj znalostní cutoff je leden 2026; vydání modelů po tomto datu nemohu potvrdit ani vyvrátit — tyto položky značím NEEDS FACT CHECK s doporučením ověřit proti primárním zdrojům (které kniha chvályhodně cituje) těsně před tiskem.

| Kapitola | Tvrzení | Stav | Doporučení |
|---|---|---|---|
| 5, B | „Významnými modely jsou Claude Sonnet 5 a **Claude Opus 4.8**" (Opus 4.8 jako top Anthropic) | **OUTDATED / NEEDS FACT CHECK** | K 08/2026 je podle dostupných informací aktuální řada Claude 5 (vč. Opus 5). Ověřit na anthropic.com a aktualizovat kap. 5 + přílohu B. Toto je nejrizikovější položka snapshotu. |
| 5 | „GPT-5.6 / GPT-5.6 Sol jako hlavní frontier rodina OpenAI" | NEEDS FACT CHECK | Po cutoffu; ověřit proti OpenAI release notes (odkaz v knize). |
| 5 | Gemini „3.1 Pro / 3.1 Deep Think / **3.6 Flash** / 3.5 Flash-Lite" | NEEDS FACT CHECK | Číslování působí nekonzistentně (Flash 3.6 novější než Pro 3.1?). Ověřit; pokud je správně, přidat půlvětu vysvětlení, jinak čtenář uvidí překlep. |
| 5 | Grok 4.5 (uveden 07/2026), DeepSeek V4 Pro/Flash (04/2026), Qwen3.6, Gemma 4, Mistral Small 4 (Apache 2.0), Llama 4 | NEEDS FACT CHECK (Llama 4 OK) | Llama 4 s nativní multimodalitou potvrzuji. Ostatní po cutoffu — ověřit verze a licence proti citovaným zdrojům. |
| 5, B | „Cohere Command A+ pod Apache 2.0" | NEEDS FACT CHECK | Pozor: Command A (2025) měl **nekomerční** licenci (CC-BY-NC). Apache 2.0 u A+ by byl významný obrat — ověřit pečlivě, chyba v licenci je pro firemního čtenáře závažná. |
| 5.7 | „Cohere Transcribe" jako STT produkt | NEEDS FACT CHECK | Produkt tohoto jména neznám; ověřit existenci a název. |
| 5.12 | „Cohere Rerank 4 uveden koncem 2025" | NEEDS FACT CHECK | K mému cutoffu byla aktuální Rerank 3.5. |
| 15 | MCP specifikace 2026-07-28 (stateless core, extensions, tasks, header routing) | NEEDS FACT CHECK | Po cutoffu; primární zdroje citovány — ověřit, že popis odpovídá finální spec. |
| 25.20 | Transparentnostní povinnosti čl. 50 AI Act se použijí od 2. 8. 2026; role provider/deployer | **OK** | Správně, včetně opatrného rámování „není právní stanovisko". |
| 1 | Historická data (1936 Turing, 1943 McCulloch–Pitts, 1950, 1956 Dartmouth, 1958 perceptron, 1966 ELIZA, 1986 backprop, 1997 Deep Blue, 2012 AlexNet, 2014 GAN, 2016 AlphaGo, 2017 Transformer, 2018 BERT, 2020 GPT-3, 2022 ChatGPT) | **OK** | Vše správně; formulace „pomohla popularizovat" u backprop je korektně opatrná. |
| 3.2 | „1 token ≈ ¾ slova (angličtina); čeština méně výhodná" | **OK** | Správná hrubá heuristika. |
| 8.5, 8.7, D.1 | Paměťové výpočty (8B×16 bit ≈ 16 GB; Q4 tabulka; KV cache navíc) | **OK** | Aritmetika sedí, rozsahy rozumné, KV cache správně zdůrazněna. |
| 6.13, B.4 | MoE: aktivní vs. celkové parametry; celkové váhy musí být v paměti | **OK** | Správně a prakticky důležité. |
| 8.9 | „32B Q4 váhy ~16–20 GB, na 16GB VRAM na hranici" | **OK** | Konzistentní s vlastní tabulkou 8.7. |
| 3.4 | Vstupní embedding jako počáteční reprezentace, měnící se v průběhu Transformeru; odlišení od RAG embedding modelu | **OK** | Nadstandardně přesné pro popularizační text. |
| 12 | RAG pipeline, hybrid search, reranking, permission-aware retrieval | **OK** | Technicky správné, best practice. |
| 24 | gm/ID metodika, characterization DB, deterministický comparator | **OK** | Věrohodné a konzistentní. |
| 20.8 | Idempotence write operací, retry taxonomie | **OK** | Správně. |
| 36 | Nástroje (Ollama, llama.cpp, vLLM, Open WebUI, Obsidian, Langfuse, n8n, MacWhisper, OpenAI Agents SDK, Pydantic AI, LangGraph) | **OK** | Vše existující produkty se správnou charakteristikou (k mému cutoffu). |

---

## 10. Review jednotlivých částí knihy

### Část I — Jak jsme se sem dostali (kap. 1)
- **Funguje:** výběr milníků, poctivé opravy mýtů (Deep Blue ≠ předchůdce LLM, backprop „popularizován" 1986), motiv AI winters jako lekce pro dnešek.
- **Nefunguje:** délka (nejdelší kapitola knihy na jejím začátku), trojité shrnutí, sekce 2023–2026 duplikuje pozdější kapitoly.
- **Zkrátit:** o ~30 % ([P1-5]).
- **Doplnit:** nic — po zkrácení bude kapitola výborná.

### Část II — Co vlastně dnešní AI je (kap. 2–4)
- **Funguje:** jádro knihy. Taxonomie s přiznanou nedokonalostí, kap. 3 je jedno z nejlepších „LLM bez matematiky" vysvětlení, jaké jsem v češtině viděl; kap. 4 správně rámuje limity dřív, než čtenář propadne nadšení.
- **Nefunguje:** kap. 3 má čtyři uzávěry; „pracovní stůl" metafora se odsud rozlévá do tří dalších kapitol.
- **Zkrátit:** závěry kap. 3.
- **Doplnit:** v kap. 4 půlvětu odkazu na budoucí box „kdy fine-tuning" (pokud vznikne).

### Část III — Svět AI modelů (kap. 5–6)
- **Funguje:** kap. 6 je vynikající a nadčasová (profil místo jednoho čísla, vlastní benchmark, scorecard). Kap. 5 má správnou strukturu „mapa, ne žebříček" a vzornou snapshot disciplínu se zdroji.
- **Nefunguje:** kap. 5 ponese největší náklady na stárnutí; položky NEEDS FACT CHECK; sekce 5.10 nadbytečná.
- **Zkrátit:** 5.10; zvážit zkrácení per-vendor detailů ve prospěch tabulky v příloze B (aby stárnul jen jeden artefakt).
- **Doplnit:** fact-check před tiskem ([FC řádky výše]).

### Část IV — Cloud, lokální AI a hardware (kap. 7–8)
- **Funguje:** hybrid jako routing problém (ne ideologie), data classification tabulka, kap. 8 správně odděluje váhy vs. celý workload (KV cache).
- **Nefunguje:** chybí snapshot hlavička kap. 8 ([P2-5]); mírný překryv 8.18–8.19 s 6.8/6.15.
- **Zkrátit:** 8.19 na odkaz do 6.
- **Doplnit:** nic zásadního.

### Část V — Prompting a Context Engineering (kap. 9–10)
- **Funguje:** demytizace promptingu, „prompt jako specifikace", context pollution — přesně to, co cílový čtenář potřebuje.
- **Nefunguje:** 10.1 znovu plně vykládá „model × context" rovnici z kap. 3.
- **Zkrátit:** 10.1 o polovinu.
- **Doplnit:** case „AI a čeština" by logicky patřil sem (viz sekce 7, bod 4).

### Část VI — Data, RAG a druhý mozek (kap. 11–13)
- **Funguje:** kap. 12 je nejlépe koncentrovaná technická kapitola knihy (ingestion→retrieval→generation, debugging po vrstvách, permission-aware retrieval). Kap. 13 dobře odlišuje archiv/knowledge/working.
- **Nefunguje:** kap. 11 je tenký most ([P2-1]).
- **Zkrátit:** kap. 11 sloučit do 12.
- **Doplnit:** nic.

### Část VII — Nástroje (kap. 14–15)
- **Funguje:** function calling jako oddělení rozhodnutí od výkonu, permission ladder, MCP vysvětleno správně (protokol, ne produkt) a rozlišení tool/skill/plugin/connector je unikátně užitečné.
- **Nefunguje:** typo verify-lDO-design; least-privilege výklad se opakuje se 25.
- **Zkrátit:** bezpečnostní pasáže 15.11 zhustit s odkazem na 25.
- **Doplnit:** nic.

### Část VIII — Agentní AI (kap. 16–20)
- **Funguje:** nejsilnější část knihy. Definice agenta smyčkou, stop conditions, verify ≠ tool success, multi-agent skepse s jasnými kritérii, orchestrace jako distributed systems problém — vše správně a v dobrém pořadí.
- **Nefunguje:** drobné opakování agent-rovnice mezi 16/17/18.
- **Zkrátit:** minimálně.
- **Doplnit:** reálný trace běhu agenta do kap. 18 (sekce 7, bod 3).

### Část IX — AI jako pracovní systém (kap. 21–24)
- **Funguje:** kap. 21 správně generalizuje coding→knowledge work; kap. 22 „evidence first, narrative second"; kap. 24 je nejlepší kapitola knihy — konkrétní, poctivá k limitům (24.15 „co automatizovat nechceme"), s realistickou cestou demo→pilot.
- **Nefunguje:** kap. 23 se místy překrývá s 24 (simulace, verifikace) — snesitelné.
- **Zkrátit:** drobně 23.6–23.7.
- **Doplnit:** nic.

### Část X — Bezpečnost a firemní provoz (kap. 25–26)
- **Funguje:** kap. 25 je referenčně kvalitní (prompt ≠ security boundary, indirect injection, secrets mimo kontext, defense in depth, AI Act/GDPR s primárními zdroji a disclaimer). Kap. 26 dobře rámuje capability vs. tool adoption.
- **Nefunguje:** data classification potřetí ([sekce 6]).
- **Zkrátit:** 25.1 odkazem na 7.8.
- **Doplnit:** nic.

### Část XI — Zavádění AI do firmy (kap. 27–30)
- **Funguje:** readiness matrix, prioritizační scorecard, pilot jako experiment s go/no-go, „no-go je legitimní výsledek", skeptik jako reviewer — prakticky nejhodnotnější manažerská část.
- **Nefunguje:** metriky se vykládají ve 26.9, 29.4 i 31 ([P2-7]).
- **Zkrátit:** dle [P2-7].
- **Doplnit:** nic.

### Část XII — Evaluace a ekonomika (kap. 31–32)
- **Funguje:** evaluation pyramid, failure-driven eval development, error taxonomy (false PASS vs. false FAIL), cost per successful task, „kdy je dražší model levnější".
- **Nefunguje:** „cena za úlohu" již počtvrté.
- **Zkrátit:** křížové odkazy místo opakování.
- **Doplnit:** nic.

### Část XIII — Co přijde dál (kap. 33–35)
- **Funguje:** kap. 33 je disciplinovaná (trendy, ne věštění; „stavět capability, ne systém kolem jednoho modelu"). Kap. 34 má nejlepší osobní pasáže knihy (34.2 „co se ukázalo jako mylné", VRAM příběh).
- **Nefunguje:** kap. 35 duplikuje 37 ([P1-4]); kap. 34 opakuje systémovou rovnici dvakrát.
- **Zkrátit:** 35 radikálně.
- **Doplnit:** diagram do 33 ([P2-9]); čísla k VRAM příběhu ve 34.3.

### Část XIV — Praktická kuchařka (kap. 36–37)
- **Funguje:** kap. 36 „minimální setup na jeden den" + „co záměrně nedávám hned" je výborný závěr; kap. 37 s projektovým žebříkem, metrikami a failure modes je nejlepší možné zakončení knihy.
- **Nefunguje:** nic zásadního.
- **Zkrátit:** drobné opakování multi-agent skepse.
- **Doplnit:** nic.

### Přílohy
- **Funguje:** slovník je konzistentní s textem (vzácnost!); checklisty E a F jsou samostatně publikovatelné artefakty; D (hardware sizing) prakticky výborná; B/C mají správnou snapshot disciplínu.
- **Nefunguje:** G je prázdná šablona ([P1-3]).
- **Zkrátit:** nic.
- **Doplnit:** G naplnit; v B aktualizovat řádky dle fact-checku.

---

## 11. Top 20 konkrétních změn

Seřazeno podle poměru **přínos / práce**:

1. **Fact-check a aktualizace snapshot řádků kap. 5 + přílohy B** (zejména Claude Opus 4.8→?, Command A+ licence, Gemini číslování) — malá práce, chrání důvěryhodnost celé knihy.
2. **Napsat úvod knihy** (3–5 stran; materiál už existuje v autorově zadání) — [P1-2].
3. **Zkrátit kap. 35 na osobní rámování a odkázat na 37** — [P1-4].
4. **Sloučit tři závěrečná shrnutí kap. 1 do jednoho + zhustit 2023–2026** — [P1-5].
5. **Sloučit uzávěry kap. 3 do jednoho** — sekce 8, bod 2.
6. **Deduplikace „model ≠ systém" rovnice** (kanonicky 2.11+3, jinde věta) — největší jednotlivá úspora.
7. **Deduplikace „cena za úlohu / benchmark ≠ use-case / pracovní stůl"** dle tabulky v sekci 6.
8. **Doplnit 3–5 vyplněných experimentů do přílohy G** (min. zpětně zdokumentovat 8→32 GB VRAM test z 34.3) — [P1-3].
9. **Přidat reálný trace agentního běhu do kap. 18** — sekce 7, bod 3.
10. **Sloučit kap. 11 do kap. 12** — [P2-1].
11. **Sjednotit čtyři žebříky autonomie do jednoho kanonického** — [P2-8].
12. **Opravit hierarchii nadpisů (H1→H2 u závěrečných sekcí)** — [P2-2]; nutné před sazbou.
13. **Box „kdy fine-tuning" (rozhodovací strom)** — sekce 7, bod 2.
14. **Box „AI a čeština"** — sekce 7, bod 4.
15. **Snapshot hlavička pro kap. 8** — [P2-5].
16. **Redukce jednoslovných code-bloků** — [P2-3]; pracnější, ale výrazně zvedne koncentraci.
17. **Zkrátit 5.10 Video generation na odstavec** — [P2-6].
18. **26.9 a 29.4 odkázat na kap. 31 místo duplikace metrik** — [P2-7].
19. **Diagram pro kap. 33** — [P2-9].
20. **Typo verify-lDO-design + sjednotit halucinace/hallucinations ve style guide** — [P2-4], [P2-10].

---

## 12. Co bych rozhodně NEMĚNIL

1. **Páteřní progrese knihy** (model → context → data → tools → agent → firma → ekonomika → kuchařka) — je to nejsilnější strukturní rozhodnutí knihy.
2. **Důsledné rozlišení MODEL ≠ APLIKACE ≠ RAG ≠ AGENT** — deduplikovat výklady ano, ale samotný princip opakovaného připomínání (jednou větou) zachovat; je to hlavní ochrana čtenáře před chybným mentálním modelem.
3. **Verifikace jako červená nit** („když lze ověřit deterministicky, neptej se LLM") — konzistentně od kap. 4 po 37.
4. **Snapshot disciplínu** — explicitní datování rychle stárnoucích kapitol + primární zdroje + pravidlo B.6 („aktualizuj nejprve kap. 5 a přílohu B") je vzorové řešení problému stárnutí AI knih.
5. **Kapitolu 24 (analog IC case study)** — včetně sekce „co automatizovat nechceme"; je to nejsilnější diferenciátor knihy.
6. **Kapitolu 25 a přílohy E/F** — bezpečnostní obsah je aktuální, správný a použitelný jako samostatný artefakt.
7. **Skepsi k multi-agentům a k hype** (19.17, 34.5) — vzácně poctivé a pro čtenáře cennější než nadšení.
8. **Rozhodnutí neuvádět absolutní ceny a benchmarková čísla** — kniha díky tomu zestárne pomaleji.
9. **Formát „Co si z kapitoly odnést" + můstek do další kapitoly** — drží tah knihy.
10. **Style guide a terminologickou disciplínu** — čeština s technickými anglicismy je konzistentní a přirozená; nepřekládat víc.

---

## 13. Finální verdikt

> **Kdyby tato kniha vyšla zítra, byla by skutečně užitečná technicky orientovanému člověku, který se chce v AI rychle a hluboce zorientovat?**

**Ano — a to i v současném stavu.** Čtenář z ní odejde se správným mentálním modelem (model vs. systém, context, verifikace, autonomie po vrstvách), s použitelnými checklisty a s realistickým projektovým žebříkem. Technicky jsem nenašel nic prokazatelně chybného; sporná místa jsou omezena na rychle stárnoucí názvy modelů v explicitně označených snapshot kapitolách, které mají definovaný aktualizační proces.

Dvě výhrady k „zítřejšímu" vydání:

1. **„Rychle" by platilo víc po deduplikaci.** Kniha dnes vyžaduje ~20 % času navíc kvůli opakování — v přímém rozporu s vlastním slibem koncentrace. To je řešitelné jedním redakčním průchodem bez zásahu do obsahu.
2. **„Hluboce" má jeden nevyplněný šek: vlastní evidence.** Kniha učí čtenáře „demo bez baseline nevěř" — a sama zatím svá klíčová tvrzení dokládá jedinou konkrétní zkušeností. Doplnění několika skutečných experimentů (příloha G) by knihu posunulo z „výborně napsané příručky" na „příručku, které věřím, protože autor ukazuje svá data".

Souhrnně: **CONDITIONAL GO.** Podmínky nejsou obsahové, ale redakční — deduplikace, úvod, fact-check snapshotů, rozhodnutí o příloze G. Po jejich splnění jde o knihu, kterou bych českému inženýrovi vstupujícímu do AI doporučil bez výhrad.
