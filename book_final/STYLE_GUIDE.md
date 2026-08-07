# STYLE GUIDE — AI od základů k agentním systémům

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
| **halucinace** | v prose preferovat českou formu; anglicky (hallucinations) pouze při prvním výskytu a v názvech zdrojů |

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


## 12. Final-print pravidla

Ve čtenářském textu nesmí zůstat interní redakční proces:

- „budu doplňovat“, „průběžně aktualizovat“, „pracovní závěr“, „redakční oprava“ apod.;
- poznámky určené autorovi nebo reviewerovi;
- odkazy na neexistující / přejmenované sekce;
- verze kapitol, které odporují master indexu.

Tištěná verze je **časově označený snapshot**, ne otevřený TODO seznam. Budoucí aktualizace patří do další edice.

## 13. Jak kapitola končí

Kapitola má pokud možno skončit jednou z těchto věcí:

1. praktickým takeaway,
2. silnou syntézou,
3. otázkou, která přirozeně otevírá další kapitolu.

Samostatný seznam URL nemá být posledním dojmem z kapitoly. Primární URL soustřeďujeme do `BIBLIOGRAPHY.md` a snapshotových příloh.

## 14. WOW bez lacinosti

„WOW“ v této knize nevytváří dekorace, ale **komprese složité myšlenky do obrazu nebo věty**.

- žádní generičtí roboti, mozky, neonové AI motivy ani stocková ikonografie;
- podpisové diagramy mají být použitelné i samostatně a vysvětlit princip do 20 sekund;
- textový callout musí být pravdivý i bez typografického efektu;
- méně výrazných vizuálů, ale každý musí nést vlastní myšlenku.
