from pathlib import Path
import re

ROOT=Path('.')
CZ=ROOT/'book_final'
EN=ROOT/'book_final_eng'
changes=[]

def replace(path, old, new, expected=None):
    p=Path(path); s=p.read_text(encoding='utf-8'); n=s.count(old)
    if expected is not None and n != expected:
        raise SystemExit(f'{p}: expected {expected} occurrences of {old!r}, found {n}')
    if n:
        p.write_text(s.replace(old,new),encoding='utf-8')
        changes.append((str(p), old, new, n))
    return n

R={
'02 - AI, Machine Learning, Deep Learning a Generative AI.md':[
('Pokud si z této kapitoly odnést jen několik věcí, pak tyto:', 'Pokud si z této kapitoly odnesete jen několik věcí, pak tyto:'),
],
'06 - Jak modely porovnávat.md':[
('Například pro engineering knowledge assistant:', 'Například pro asistenta nad inženýrskými znalostmi:'),
],
'07 - Cloud vs. on-prem vs. hybrid.md':[
('- customer specifications,', '- zákaznické specifikace,'),
('Místo ideologického sporu cloud versus local můžeme každou úlohu ohodnotit.', 'Místo ideologického sporu cloud versus lokální provoz můžeme každou úlohu ohodnotit.'),
],
'14 - Tool Use.md':[
('Může je **orchestravat**.', 'Může je **orchestrovat**.'),
],
'15 - MCP, skills, plugins a connectors.md':[
('### Local vs. remote server', '### Lokální vs. vzdálený server'),
('interní simulation service', 'interní simulační služba'),
],
'17 - Jak postavit jednoduchého agenta.md':[
('cloud i local models', 'cloudové i lokální modely'),
('sám spustí chybějící simulation', 'sám spustí chybějící simulaci'),
],
'22 - AI pro technické a inženýrské úlohy.md':[
('přesný measurement output', 'přesný výstup měření'),
('To je obecně rozumná engineering knowledge.', 'To je obecně rozumný inženýrský princip.'),
('Člověk zůstává ownerem engineering rozhodnutí.', 'Člověk nadále rozhoduje o zásadních inženýrských otázkách.'),
('AI spouští read-only / sandbox simulations', 'AI spouští read-only / sandbox simulace'),
('**AI je silný technický asistent pro dokumenty, datasheety, specifications a scripting.**', '**AI je silný technický asistent pro dokumenty, datasheety, specifikace a skriptování.**'),
('**Simulation je ideální zdroj zpětné vazby pro agentní smyčku.**', '**Simulace je ideální zdroj zpětné vazby pro agentní smyčku.**'),
('**LLM nemusí být nejlepší numerický optimizer; může orchestravat specializovaný optimalizační algoritmus.**', '**LLM nemusí být nejlepší numerický optimalizátor; může orchestrovat specializovaný optimalizační algoritmus.**'),
('**Autonomii lze přidávat po stupních a člověk zůstává decision makerem pro zásadní trade-offy.**', '**Autonomii lze přidávat po stupních a člověk zůstává tím, kdo rozhoduje o zásadních trade-offech.**'),
],
'23 - Případová studie - AI-assisted analog IC design.md':[
('## 23.6 Characterization data', '## 23.6 Charakterizační data'),
('Změní se tools a data source.', 'Změní se nástroje a zdroj dat.'),
('characterization data', 'charakterizační data'),
('můžeme vytvořit první candidate sizing.', 'můžeme vytvořit první kandidátní sizing.'),
('To je vysoká úroveň engineering rozhodnutí.', 'To je inženýrské rozhodnutí na vysoké úrovni.'),
('### Device sizing', '### Sizing tranzistorů'),
('## 23.8 SPICE / Spectre simulation', '## 23.8 SPICE / Spectre simulace'),
('příkazové nuance simulatoru', 'příkazové nuance simulátoru'),
('### LLM není jediný optimizer', '### LLM není jediný optimalizátor'),
('Bayesian optimizer', 'bayesovský optimalizátor'),
('## 23.13 Human designer jako decision maker', '## 23.13 Designer jako ten, kdo rozhoduje'),
('200 simulation runs', '200 simulačních běhů'),
('### Simulation execution', '### Spouštění simulací'),
('### Production write bez approval', '### Zápis do produkce bez schválení'),
('Nemění released design.', 'Nemění schválený návrh.'),
('Agent může generovat candidates na vlastní branch/workspace.', 'Agent může generovat kandidátní změny ve vlastní branch/workspace.'),
('**Knowledge base má dodávat prior knowledge, ne nekriticky kopírovat staré sizing.**', '**Knowledge base má dodávat předchozí znalosti, ne nekriticky kopírovat starý sizing.**'),
('**gm/ID vytváří užitečnou strukturovanou mezivrstvu mezi design intent a device sizing.**', '**gm/ID vytváří užitečnou strukturovanou mezivrstvu mezi návrhovým záměrem a sizingem tranzistorů.**'),
('**Characterization data musí pocházet ze skutečného PDK modelu a simulatoru.**', '**Charakterizační data musí pocházet ze skutečného PDK modelu a simulátoru.**'),
('**Pro první pilot je rozumné fixovat topologii a automatizovat sizing, simulation a verifikace.**', '**Pro první pilot je rozumné fixovat topologii a automatizovat sizing, simulaci a verifikaci.**'),
('**Human designer zůstává decision makerem pro topologii a zásadní trade-offy.**', '**Designer zůstává tím, kdo rozhoduje o topologii a zásadních trade-offech.**'),
],
'30 - Evaluace.md':[
('- ze simulatoru,', '- ze simulátoru,'),
],
'35 - Můj minimální AI stack.md':[
('obyčejný local index', 'obyčejný lokální index'),
('**Ollama je jednoduchá výchozí local vrstva; llama.cpp přidává kontrolu a vLLM serverový throughput.**', '**Ollama je jednoduchá výchozí lokální vrstva; llama.cpp přidává kontrolu a vLLM serverový throughput.**'),
],
'appendices/D - Hardware sizing.md':[
('Potřebuji interaktivní local AI?', 'Potřebuji interaktivní lokální AI?'),
],
'25 - Proč nestačí „máme ChatGPT“.md':[
('local domain expertise', 'lokální doménová expertiza'),
],
'32 - Kam se AI posouvá.md':[
('local AI\nedge AI\nprivate AI\nspecialized models', 'lokální AI\nedge AI\nprivátní AI\nspecializované modely'),
('- extraction,\n- classification,\n- function calling,\n- local coding,\n- routing,', '- extrakce,\n- klasifikace,\n- volání funkcí,\n- lokální coding,\n- směrování,'),
('small local model\n→ 80 % jednoduchých kroků\n\nlarge local/server model\n→ harder internal tasks\n\nfrontier cloud\n→ exceptional reasoning', 'malý lokální model\n→ 80 % jednoduchých kroků\n\nvětší lokální/serverový model\n→ náročnější interní úlohy\n\nfrontier cloud\n→ výjimečně náročné reasoning úlohy'),
('local memory\n+\nlocal processing\n+\nselective cloud reasoning', 'lokální paměť\n+\nlokální zpracování\n+\nselektivní cloudové reasoning'),
],
'33 - Co jsem se zatím naučil.md':[
('## 33.6 Cloud vs. local — jak se změnil můj pohled', '## 33.6 Cloud vs. lokální AI — jak se změnil můj pohled'),
('local where it makes sense\ncloud where it adds real value\npolicy decides what can go where', 'lokálně tam, kde to dává smysl\ncloud tam, kde přidává skutečnou hodnotu\npolicy rozhoduje, co smí kam'),
],
'36 - Deset praktických projektů od začátečníka k agentnímu systému.md':[
('knowledge base\n↓\nlocal model\n↓', 'knowledge base\n↓\nlokální model\n↓'),
('| 4 | local inference | výkon a falešná očekávání |', '| 4 | lokální inference | výkon a falešná očekávání |'),
],
}
for rel,pairs in R.items():
    for old,new in pairs: replace(CZ/rel,old,new,1)

replace(CZ/'22 - AI pro technické a inženýrské úlohy.md','pattern použitelný daleko za electronics.','vzor použitelný daleko za elektronikou.',1)
replace(CZ/'22 - AI pro technické a inženýrské úlohy.md','bias point,','pracovní bod,',1)
replace(CZ/'22 - AI pro technické a inženýrské úlohy.md','parasitics,','parazitní prvky,',1)
replace(CZ/'22 - AI pro technické a inženýrské úlohy.md','topology,','topologii,',1)
replace(CZ/'22 - AI pro technické a inženýrské úlohy.md','corners.','corner podmínkách.',1)

extra_pairs={
CZ/'07 - Cloud vs. on-prem vs. hybrid.md':[
('„trochu horší cloud a trochu horší local“','„trochu horší cloud a trochu horší lokální provoz“'),
('local nebo cloud','lokální model nebo cloud'),
],
CZ/'22 - AI pro technické a inženýrské úlohy.md':[
('- pracovní bod,','- pracovním bodu,'),('- parazitní prvky,','- parazitních prvcích,'),('- corner podmínkách.','- corner podmínkách.'),
('„Splní tento circuit stability přes všechny PVT?“','„Splní tento obvod požadavky na stabilitu přes všechny PVT?“'),
('**AI může navrhovat hypotézy. Simulator rozhoduje o tom, co daný model obvodu skutečně predikuje.**','**AI může navrhovat hypotézy. Simulátor rozhoduje o tom, co daný model obvodu skutečně predikuje.**'),
('A měření následně rozhoduje o skutečném siliconu.','A měření následně rozhoduje o skutečném čipu.'),
('definici engineering agenta.','definici inženýrského agenta.'),('označit uncertainty,','označit nejistotu,'),
('## Stupně engineering autonomie','## Stupně inženýrské autonomie'),('AI generuje scripts a analysis','AI generuje skripty a analýzy'),
('AI navrhuje další experiments podle výsledků','AI navrhuje další experimenty podle výsledků'),
('AI optimalizuje v omezeném design space','AI optimalizuje v omezeném návrhovém prostoru'),
('**Engineering kombinuje nestrukturované znalosti s velmi kvalitními deterministickými nástroji.**','**Inženýrská práce kombinuje nestrukturované znalosti s velmi kvalitními deterministickými nástroji.**'),
('**Engineering agent je nejlépe chápaný jako orchestrátor dokumentů, výpočtů, simulátorů a verifikace.**','**Inženýrský agent je nejlépe chápaný jako orchestrátor dokumentů, výpočtů, simulátorů a verifikace.**'),
],
CZ/'23 - Případová studie - AI-assisted analog IC design.md':[
('Agent má engineering language, ve kterém může pracovat.','Agent má inženýrský jazyk, ve kterém může pracovat.'),
('mezi design knowledge, daty technologie a automatizací.','mezi návrhovými znalostmi, daty technologie a automatizací.'),
('Pak agent může udělat query:','Pak agent může položit dotaz:'),('interní knowledge','interní znalosti'),
('### Topology selection','### Volba topologie'),('- currents,','- proudy,'),('- compensation.','- kompenzace.'),
('Může mít tools:','Může mít nástroje:'),('Uvnitř tool layer může být:','Uvnitř vrstvy nástrojů může být:'),
('- netlist generator,','- generátor netlistu,'),('- Virtuoso automation.','- automatizace Virtuoso.'),
('MCP/API wrapper vytvoří stabilní interface.','MCP/API wrapper vytvoří stabilní rozhraní.'),('- raw waveforms,','- nezpracované průběhy,'),('- logs,','- logy,'),('- measurements.','- měření.'),
('- trade-off mezi area a robustness,','- trade-off mezi plochou a robustností,'),('- rozhodnutí, zda změnit architecture,','- rozhodnutí, zda změnit architekturu,'),
('- interpretace neobvyklého failure,','- interpretace neobvyklého selhání,'),('- risk acceptance.','- přijetí rizika.'),
('nad kvalitně připravenými evidence.','nad kvalitně připravenými podklady.'),('### Knowledge retrieval','### Vyhledání znalostí'),
('### Characterization queries','### Dotazy nad charakterizačními daty'),('### Sizing calculations','### Výpočty sizingu'),
('### Netlist / testbench generation','### Generování netlistu / testbenche'),('### Measurement extraction','### Extrakce měření'),
('### Report generation','### Generování reportu'),('### Iterace v omezeném design space','### Iterace v omezeném návrhovém prostoru'),
('### Neomezené topology generation','### Neomezené generování topologií'),('Search space je obrovský','Prostor možností je obrovský'),
('system-level dopad.','dopad na úrovni systému.'),('AI intuition není sign-off.','Intuice AI není podklad pro sign-off.'),
('### Fáze 3 — sandbox design changes','### Fáze 3 — změny návrhu v sandboxu'),('### Fáze 4 — designer-approved optimization','### Fáze 4 — optimalizace schvalovaná designerem'),
('validovaných requirements.','validovaných požadavků.'),
],
}
for p,pairs in extra_pairs.items():
    for old,new in pairs: replace(p,old,new,1)

cz_manuscript=[CZ/'00 - Uvod - Jak cist tuto knihu.md'] + sorted([p for p in CZ.glob('[0-9][0-9] - *.md') if p.name not in {'00 - INDEX.md','00 - Uvod - Jak cist tuto knihu.md'}]) + sorted((CZ/'appendices').glob('*.md'))
for p in cz_manuscript:
    s=p.read_text(encoding='utf-8'); orig=s
    s=s.replace('status: final-draft','status: release-candidate',1).replace('updated: 2026-08-07','updated: 2026-08-08',1)
    if s!=orig: p.write_text(s,encoding='utf-8')
for p in list(CZ.glob('*.md'))+list((CZ/'appendices').glob('*.md')):
    s=p.read_text(encoding='utf-8'); orig=s
    s=s.replace('snapshot: "2026-08-07"','snapshot: "2026-08-08"').replace('Snapshot k 7. 8. 2026','Snapshot k 8. 8. 2026').replace('k 7. 8. 2026','k 8. 8. 2026')
    if s!=orig: p.write_text(s,encoding='utf-8')
replace(CZ/'00 - INDEX.md','date: 2026-08-07','date: 2026-08-08',1)
replace(CZ/'BIBLIOGRAPHY.md','## Snapshot modelů — 7. 8. 2026','## Snapshot modelů — 8. 8. 2026',1)
replace(CZ/'08 - Jak provozovat LLM lokálně.md','Další část knihy se přesune od infrastruktury k člověku:\n\n> **Jak vlastně modelu zadat práci tak, aby dostal správný cíl, kontext a omezení?**','Další část knihy se přesune od infrastruktury k člověku: **Jak vlastně modelu zadat práci tak, aby dostal správný cíl, kontext a omezení?**',1)
replace(CZ/'22 - AI pro technické a inženýrské úlohy.md','V další kapitole tento obecný princip převedeme na konkrétní případovou studii:\n\n> **AI-assisted analog IC design.**','V další kapitole tento obecný princip převedeme na konkrétní případovou studii: **AI-assisted analog IC design.**',1)

replace(EN/'13 - The Second Brain.md','The next step is what makes this knowledge operational. A model can read and write text. But what happens when we give it a calculator, a database, a simulator, a shell, or an API?\n\nThat is **tool use**.','The next step is what makes this knowledge operational. A model can read and write text. But what happens when we give it a calculator, a database, a simulator, a shell, or an API? **That is tool use.**',1)
replace(EN/'25 - Why We Have ChatGPT Is Not an AI Strategy.md','The next question is therefore foundational:\n\n> **Is the organization — and its data — ready for AI at all?**','The next question is therefore foundational: **Is the organization — and its data — ready for AI at all?**',1)
FINAL_SUB='How AI Actually Works — From LLMs and RAG to Tools, Agents, Evals, and Reliable Systems'
OLD_SUB='How AI Actually Works — and How to Build Reliable Systems with Models, Data, Tools, and Verification'
for rel in ['README.md','STYLE_GUIDE.md','ENGLISH_EDITION_NOTES.md']: replace(EN/rel,OLD_SUB,FINAL_SUB,1)
replace(EN/'ENGLISH_EDITION_NOTES.md','Working title:','Final title:',1)
replace(EN/'ENGLISH_EDITION_NOTES.md','Working subtitle:','Final subtitle:',1)
replace(EN/'ENGLISH_EDITION_NOTES.md','The English edition inherits the Czech master’s factual snapshot date of **August 7, 2026**','The English edition uses a factual snapshot date of **August 8, 2026**',1)
replace(EN/'STYLE_GUIDE.md','`Snapshot: August 7, 2026.`','`Snapshot: August 8, 2026.`',1)
eng_manuscript=[EN/'00 - Introduction - How to Read This Book.md'] + sorted([p for p in EN.glob('[0-9][0-9] - *.md') if p.name not in {'00 - INDEX.md','00 - Introduction - How to Read This Book.md'}]) + sorted((EN/'appendices').glob('*.md'))
for p in eng_manuscript:
    s=p.read_text(encoding='utf-8'); orig=s
    s=s.replace('status: international-draft','status: release-candidate',1).replace('updated: 2026-08-07','updated: 2026-08-08',1).replace('snapshot: "2026-08-07"','snapshot: "2026-08-08"').replace('August 7, 2026','August 8, 2026')
    if s!=orig: p.write_text(s,encoding='utf-8')
for p in [EN/'README.md',EN/'BIBLIOGRAPHY.md']:
    s=p.read_text(encoding='utf-8'); p.write_text(s.replace('August 7, 2026','August 8, 2026'),encoding='utf-8')
replace(EN/'00 - INDEX.md','status: international-draft','status: release-candidate',1)
replace(EN/'00 - INDEX.md','International English edition — v0.8-eng','International English release candidate — v0.8-eng',1)
replace(EN/'README.md','**International English edition — v0.8-eng**','**International English release candidate — v0.8-eng**',1)

allcz='\n'.join(p.read_text(encoding='utf-8') for p in cz_manuscript)
for bad in ['orchestravat','simulatoru','decision makerem','candidate sizing','Characterization data musí','Simulation je ideální','numerický optimizer']:
    if bad in allcz: raise SystemExit(f'Czech blocker remains: {bad}')
allen='\n'.join(p.read_text(encoding='utf-8') for p in eng_manuscript)
if 'status: international-draft' in allen or 'August 7, 2026' in allen: raise SystemExit('English metadata blocker remains')
print(f'Final bilingual editorial corrections applied: {len(changes)} exact replacements')
