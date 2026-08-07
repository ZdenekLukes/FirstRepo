# A. Slovník AI pojmů

Tento slovník používá terminologii knihy. Anglický termín ponechávám tam, kde se běžně používá i v českém technickém prostředí.

| Pojem | Praktický význam v této knize |
|---|---|
| **AI — Artificial Intelligence** | Nejširší označení systémů, které vykonávají úlohy spojované s inteligentním chováním. AI není synonymum pro LLM. |
| **ML — Machine Learning** | Metody, které se učí vzory z dat místo ručního naprogramování všech pravidel. |
| **DL — Deep Learning** | Machine Learning založený na hlubokých neuronových sítích. |
| **Generative AI** | Modely vytvářející nový obsah: text, obraz, zvuk, video, kód nebo jiné reprezentace. |
| **Foundation Model** | Velký obecný model předtrénovaný na širokých datech a použitelný pro mnoho úloh. |
| **LLM — Large Language Model** | Foundation model zaměřený především na jazyk a tokenové reprezentace. Generuje odpověď po tokenech. |
| **LMM / multimodální model** | Model pracující s více modalitami, například textem, obrazem, zvukem nebo videem. |
| **Token** | Jednotka, na kterou tokenizer rozdělí vstup. Nemusí odpovídat celému slovu. |
| **Tokenizer** | Převádí text na token IDs a zpět. Ovlivňuje délku kontextu i efektivitu práce s různými jazyky. |
| **Parameter / parametr** | Naučená číselná hodnota modelu. Parametry nejsou databáze konkrétních dokumentů. |
| **Weights / váhy** | Praktické označení naučených parametrů uložených v modelových souborech. |
| **Embedding** | Vektorová reprezentace významu textu, obrázku nebo jiné entity. Používá se mimo jiné v semantic search a RAG. |
| **Transformer** | Architektura neuronové sítě založená na attention, která stojí za velkou částí moderních LLM. |
| **Attention** | Mechanismus, kterým model při výpočtu váží vztahy mezi částmi kontextu. |
| **Inference** | Běh již natrénovaného modelu při zpracování konkrétního vstupu. |
| **Training** | Proces učení parametrů modelu z trénovacích dat. |
| **Pre-training** | Rozsáhlé základní trénování foundation modelu před specializací. |
| **Fine-tuning** | Další trénink již existujícího modelu pro určité chování, styl nebo doménu. |
| **Quantization / kvantizace** | Uložení a výpočet vah s nižší přesností, typicky za cenu menší paměti a někdy malé ztráty kvality. |
| **Context / kontext** | Informace dostupné modelu při aktuálním inference: instrukce, prompt, historie, retrieved data a tool outputs. |
| **Context window** | Maximální rozsah tokenů, které model může v daném requestu zpracovat. Dlouhé okno neznamená dokonalou paměť. |
| **Prompt** | Zadání poslané modelu. V této knize je prompt součást širšího context engineeringu. |
| **System instruction** | Instrukce aplikace s vyšší prioritou než běžný user prompt. Není sama o sobě bezpečnostní hranicí. |
| **Context engineering** | Návrh toho, jaké instrukce, data, historie, retrieved knowledge a tool results model skutečně dostane. |
| **RAG — Retrieval-Augmented Generation** | Architektura, která před generováním vyhledá relevantní externí informace a vloží je do kontextu modelu. |
| **Retrieval** | Vyhledání relevantních dokumentů nebo chunků pro konkrétní dotaz. |
| **Chunk** | Menší část dokumentu uložená nebo vracená retrieval systémem. |
| **Vector database** | Databáze optimalizovaná pro ukládání vektorů a vyhledávání podle podobnosti. RAG ji může, ale nemusí používat. |
| **Reranker** | Model nebo algoritmus, který znovu seřadí retrieval kandidáty podle relevance. |
| **Knowledge base** | Organizovaná sada znalostních zdrojů. Není totožná s RAG; RAG je jeden způsob, jak knowledge base zpřístupnit modelu. |
| **Tool / nástroj** | Externí funkce, API, program, databáze nebo simulátor, který může AI systém použít. |
| **Tool calling** | Strukturovaný mechanismus, kterým model vybere nástroj a připraví jeho argumenty. |
| **MCP — Model Context Protocol** | Otevřený protokol pro standardizované připojování AI aplikací k nástrojům a zdrojům. |
| **Skill** | Znovupoužitelná instrukce nebo pracovní postup pro konkrétní úlohu. Význam se může lišit podle platformy. |
| **Plugin** | Balíček rozšíření konkrétní aplikace nebo platformy. Není obecný standard jako MCP. |
| **Connector** | Propojení AI systému s konkrétní externí službou nebo datovým zdrojem. |
| **Agent** | Software kolem modelu, který pracuje se stavem, vybírá akce nebo nástroje a opakuje kroky směrem k cíli. |
| **Agentní smyčka** | Cyklus observe → reason/plan → act → verify, který se opakuje do dosažení cíle nebo stop condition. |
| **State / stav** | Informace o aktuálním průběhu úlohy, které agent potřebuje mezi kroky. |
| **Memory / paměť** | Mechanismus pro uchování informace mimo aktuální krátkodobý kontext. Musí řešit aktuálnost, provenance a oprávnění. |
| **Multi-agentní systém** | Systém s více oddělenými agentními rolemi. Má smysl, když rozdělení přináší výhodu v kontextu, oprávněních, nástrojích nebo evaluaci. |
| **Orchestration / orchestrace** | Řízení pořadí kroků, agentů, nástrojů, stavů, retry a approval gates. |
| **MoE — Mixture of Experts** | Architektura, kde se pro konkrétní token aktivuje jen část expertních komponent modelu. Celkové váhy však stále mohou být velmi velké. |
| **Reasoning** | Schopnost modelu řešit vícekrokové úlohy s větším inference compute. Neznamená garanci správnosti. |
| **Multimodality / multimodalita** | Schopnost systému pracovat s více typy vstupu a výstupu. |
| **Open-weight** | Model, jehož váhy jsou dostupné ke stažení. Neznamená automaticky klasickou open-source licenci ani zveřejnění trénovacích dat. |
| **Benchmark** | Standardizovaný test schopností modelu. Výsledek benchmarku nemusí předpovědět kvalitu na našem use-case. |
| **Eval / evaluace** | Systematické měření kvality modelu nebo celého AI systému na definovaném test setu. |
| **Ground truth** | Referenční správný výsledek používaný pro evaluaci. |
| **Golden question** | Kritický testovací případ, který systém musí konzistentně zvládat po změně modelu, promptu nebo pipeline. |
| **LLM-as-a-judge** | Použití jednoho modelu k hodnocení výstupu jiného. Je užitečné, ale musí být kalibrováno proti lidskému hodnocení. |
| **Hallucination / halucinace** | Plynule formulované tvrzení, které není podpořené skutečností nebo dostupným zdrojem. |
| **Grounding** | Opření odpovědi o externí evidence, například dokument, databázi nebo výsledek nástroje. |
| **Prompt injection** | Útok nebo nežádoucí instrukce vložená do user inputu nebo externího obsahu s cílem změnit chování AI systému. |
| **Indirect prompt injection** | Prompt injection obsažená například ve webu, PDF, e-mailu nebo jiném zdroji, který agent automaticky načte. |
| **Guardrail** | Technické nebo procesní omezení snižující pravděpodobnost nebo dopad nežádoucí akce. |
| **Human-in-the-loop** | Workflow, kde člověk kontroluje nebo schvaluje vybrané kroky AI systému. |
| **Approval gate** | Explicitní bod, za který systém nesmí pokračovat bez požadovaného schválení. |
| **Sandbox** | Oddělené prostředí s omezenými oprávněními, ve kterém lze bezpečněji spouštět kód nebo agentní akce. |
| **Observability** | Logy, traces a metriky umožňující zjistit, co systém udělal, proč a s jakým výsledkem. |
| **Provenance** | Informace o původu dat, dokumentu, modelu nebo výsledku a jeho verzi. |

## Jak slovník používat

Při prvním výskytu v textu je vhodné uvést české vysvětlení a běžný anglický termín. Potom se kniha řídí pravidly v `STYLE_GUIDE.md`, aby se například `context`, `kontext`, `tool`, `nástroj`, `memory` a `paměť` nestřídaly náhodně.