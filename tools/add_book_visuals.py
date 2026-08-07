from __future__ import annotations
from pathlib import Path
import html, math, re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'book'
ASSETS = BOOK / 'assets' / 'diagrams'
ASSETS.mkdir(parents=True, exist_ok=True)
W=1200; BG='#0b1220'; CARD='#111c30'; TEXT='#eef6ff'; MUTED='#a9bbcf'; ACC='#45c7ff'; PUR='#8b7cff'; GRN='#63d7a5'; YEL='#ffca6a'; RED='#ff7a8a'; LINE='#5e7188'
COLORS=[ACC,PUR,GRN,YEL]

def e(s): return html.escape(str(s), quote=True)
def txt(x,y,s,size=18,color=TEXT,weight=400,anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{e(s)}</text>'
def rect(x,y,w,h,title,body='',color=ACC):
    out=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{CARD}" stroke="{color}" stroke-width="2"/>',txt(x+w/2,y+36,title,21,TEXT,700)]
    if body:
        lines=body if isinstance(body,list) else [body]
        yy=y+66
        for line in lines: out.append(txt(x+w/2,yy,line,15,MUTED)); yy+=22
    return ''.join(out)
def arrow(x1,y1,x2,y2,label=''):
    s=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LINE}" stroke-width="3" marker-end="url(#arrow)"/>'
    return s+(txt((x1+x2)/2,(y1+y2)/2-10,label,13,MUTED) if label else '')
def wrap(title,subtitle,body,h=600):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="title desc"><title id="title">{e(title)}</title><desc id="desc">{e(subtitle)}</desc><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{LINE}"/></marker></defs><rect width="{W}" height="{h}" rx="28" fill="{BG}"/><text x="60" y="64" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="34" font-weight="700" fill="{TEXT}">{e(title)}</text><text x="60" y="96" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="18" fill="{MUTED}">{e(subtitle)}</text>{body}</svg>'''

def render(spec):
    kind=spec['kind']; title=spec['title']; sub=spec['subtitle']; data=spec['data']; footer=spec.get('footer','')
    if kind=='flow':
        n=len(data); margin=65; gap=26; bw=(W-2*margin-gap*(n-1))/n; y=185; bh=145; body=[]
        for i,node in enumerate(data):
            name=node[0]; lines=list(node[1:]); x=margin+i*(bw+gap); body.append(rect(x,y,bw,bh,name,lines,COLORS[i%4]))
            if i<n-1: body.append(arrow(x+bw+4,y+bh/2,x+bw+gap-4,y+bh/2))
        if footer: body.append(txt(W/2,505,footer,17,MUTED,500))
        return wrap(title,sub,''.join(body),560)
    if kind=='layers':
        x=170; w=860; y=145; lh=66; gap=10; body=[]
        for i,(name,desc) in enumerate(data):
            yy=y+i*(lh+gap); body.append(f'<rect x="{x}" y="{yy}" width="{w}" height="{lh}" rx="15" fill="{CARD}" stroke="{COLORS[i%4]}" stroke-width="2"/>'); body.append(txt(x+26,yy+28,name,19,TEXT,700,'start')); body.append(txt(x+26,yy+51,desc,14,MUTED,400,'start'))
        return wrap(title,sub,''.join(body),max(610,y+len(data)*(lh+gap)+45))
    if kind in ('hub','loop'):
        cx,cy=600,365; r=215; body=[]; center=spec.get('center','Cíl'); body.append(f'<circle cx="{cx}" cy="{cy}" r="82" fill="{CARD}" stroke="{ACC}" stroke-width="3"/>'); body.append(txt(cx,cy+7,center,23,TEXT,700)); pts=[]
        for i,name in enumerate(data):
            a=-math.pi/2+2*math.pi*i/len(data); x=cx+r*math.cos(a); y=cy+r*math.sin(a); pts.append((x,y,a)); body.append(rect(x-82,y-39,164,78,name,'',COLORS[i%4]));
            if kind=='hub': body.append(arrow(cx+78*math.cos(a),cy+78*math.sin(a),x-80*math.cos(a),y-38*math.sin(a)))
        if kind=='loop':
            for i,(x1,y1,a1) in enumerate(pts):
                x2,y2,_=pts[(i+1)%len(pts)]; a=math.atan2(y2-y1,x2-x1); body.append(arrow(x1+84*math.cos(a),y1+42*math.sin(a),x2-84*math.cos(a),y2-42*math.sin(a)))
        return wrap(title,sub,''.join(body),670)
    if kind=='matrix':
        x0,y0=230,510; x1,y1=1030,160; mx=(x0+x1)/2; my=(y0+y1)/2; body=[]
        body += [f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{LINE}" stroke-width="3" marker-end="url(#arrow)"/>',f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{LINE}" stroke-width="3" marker-end="url(#arrow)"/>',f'<line x1="{mx}" y1="{y1}" x2="{mx}" y2="{y0}" stroke="{LINE}" stroke-dasharray="8 8"/>',f'<line x1="{x0}" y1="{my}" x2="{x1}" y2="{my}" stroke="{LINE}" stroke-dasharray="8 8"/>']
        body += [txt(x0,y0+40,'nižší složitost',15,MUTED,500,'start'),txt(x1,y0+40,'vyšší složitost',15,MUTED,500,'end'),txt(x0-18,y0,'nižší hodnota',15,MUTED,500,'end'),txt(x0-18,y1+10,'vyšší hodnota',15,MUTED,500,'end')]
        pos=[(830,420),(430,420),(430,245),(830,245)]
        for i,(name,desc) in enumerate(data): body.append(rect(pos[i][0]-150,pos[i][1]-55,300,110,name,desc,COLORS[i%4]))
        return wrap(title,sub,''.join(body),650)
    if kind=='timeline':
        y=350; x0=85; x1=1115; step=(x1-x0)/(len(data)-1); body=[f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="4"/>']
        for i,(year,name,desc) in enumerate(data):
            x=x0+i*step; up=i%2==0; yy=185 if up else 420; color=ACC if i<len(data)-3 else GRN; body += [f'<circle cx="{x}" cy="{y}" r="11" fill="{color}"/>',f'<line x1="{x}" y1="{y}" x2="{x}" y2="{yy+54 if up else yy}" stroke="{LINE}" stroke-width="2"/>',txt(x,yy,year,18,color,700),txt(x,yy+25,name,16,TEXT,700),txt(x,yy+47,desc,12,MUTED)]
        return wrap(title,sub,''.join(body),610)
    raise ValueError(kind)

D={
'01-history-timeline.svg':dict(kind='timeline',title='Od výpočtu k agentním systémům',subtitle='Historie AI je skládání algoritmů, dat, výkonu a nástrojů.',data=[('1936','Turing','obecný výpočet'),('1956','Dartmouth','pojem AI'),('1986','Backprop','neuronové sítě'),('2012','AlexNet','deep learning'),('2017','Transformer','základ LLM'),('2022','ChatGPT','masový trh'),('2025','Reasoning + tools','praktičtí agenti'),('2026','Agentní systémy','model jako část systému')]),
'02-ai-taxonomy.svg':dict(kind='layers',title='AI → ML → Deep Learning → Generative AI → LLM',subtitle='LLM je typ modelu; agentní systém je nadstavba kolem modelu.',data=[('Artificial Intelligence','nejširší množina inteligentních systémů'),('Machine Learning','učení vzorů z dat'),('Deep Learning','vícevrstvé neuronové sítě'),('Generative AI','generování nového obsahu'),('Foundation Models / LLM','obecné modely adaptovatelné na mnoho úloh')]),
'03-model-vs-database.svg':dict(kind='flow',title='LLM není databáze odpovědí',subtitle='Trénink mění parametry; přesné dokumenty musí dodat search, RAG nebo nástroj.',data=[('Trénovací data','texty a kód'),('Učení','vztahy a vzory'),('Parametry','komprimovaná reprezentace'),('LLM','generuje další token')]),
'03-embeddings.svg':dict(kind='flow',title='Embedding: význam převedený na čísla',subtitle='Vektorová reprezentace umožňuje výpočet významové podobnosti.',data=[('Text / token','„tranzistor“'),('Embedding','[0.13, −0.42, …]'),('Vektorový prostor','relativní poloha'),('Podobné pojmy','MOSFET, gate…')]),
'03-token-generation-loop.svg':dict(kind='flow',title='Jak LLM generuje odpověď',subtitle='Odpověď vzniká opakovaným odhadem dalšího tokenu.',data=[('Prompt','dosavadní kontext'),('Transformer','výpočet'),('Pravděpodobnosti','kandidátní tokeny'),('Sampling','výběr tokenu'),('Nový kontext','prompt + token')],footer='Smyčka pokračuje do konce odpovědi nebo limitu.'),
'03-enter-to-answer.svg':dict(kind='flow',title='Od Enteru po odpověď',subtitle='Zjednodušená inferenční cesta.',data=[('Kontext','system + user + historie'),('Tokenizace','text → tokeny'),('Model','Transformer vrstvy'),('Decoding','výběr tokenu'),('Stream','tokeny uživateli')]),
'07-cloud-onprem-hybrid.svg':dict(kind='flow',title='Cloud vs. on-prem vs. hybrid',subtitle='Úlohu směrujeme podle dat, výkonu, ceny a provozního rizika.',data=[('Cloud','frontier modely','rychlá škála'),('Hybrid','citlivé lokálně','cloud selektivně'),('On-prem','kontrola dat','vlastní provoz')]),
'08-local-memory-stack.svg':dict(kind='layers',title='Kde se spotřebuje paměť lokálního LLM',subtitle='Modelové váhy jsou jen část celkové paměťové potřeby.',data=[('Aplikace / UI','chat a agent framework'),('Inference runtime','Ollama / llama.cpp / vLLM'),('KV cache + context','roste s délkou kontextu'),('Modelové váhy','FP16 / INT8 / INT4'),('VRAM / unified memory','typický limit'),('CPU RAM + storage','offload a data')]),
'09-prompt-anatomy.svg':dict(kind='layers',title='Prompt jako specifikace úlohy',subtitle='Silný prompt je strukturovaný kontext, ne magická formulka.',data=[('Cíl','co má být výsledkem'),('Kontext','co model potřebuje vědět'),('Omezení','co musí a nesmí'),('Příklady','vzor správného řešení'),('Výstupní formát','text / tabulka / JSON'),('Iterace','zpětná vazba')]),
'10-context-stack.svg':dict(kind='layers',title='Context engineering: co model skutečně vidí',subtitle='Kvalita odpovědi závisí na správném kontextu právě teď.',data=[('System instructions','pravidla aplikace'),('User intent','aktuální zadání'),('Relevantní historie','jen užitečné části'),('Retrieved knowledge','RAG / files / web'),('Tool results','API / Python / simulátor'),('Working memory','stav a mezivýsledky')]),
'11-external-data-bridge.svg':dict(kind='flow',title='Jak dostat moje data k modelu',subtitle='Soukromé a aktuální informace musí být do kontextu přivedeny externí vrstvou.',data=[('Moje data','PDF / e-mail / DB'),('Access layer','search / RAG / MCP'),('Relevantní kontext','jen potřebný výřez'),('LLM','interpretace'),('Odpověď','ideálně s citací')]),
'12-rag-pipeline.svg':dict(kind='flow',title='RAG: od dokumentu k odpovědi se zdrojem',subtitle='Retrieval odděluje vyhledání relevantních dat od generování odpovědi.',data=[('Dokumenty','parse + chunking'),('Index','embeddings + metadata'),('Dotaz','semantic / hybrid search'),('Rerank','nejlepší části'),('LLM','odpověď + citace')],footer='RAG model nepřeučuje; při dotazu mu dodá správný kontext.'),
'13-second-brain.svg':dict(kind='hub',title='Druhý mozek s AI',subtitle='AI je navigátor nad znalostní bází, ne náhrada samotných znalostí.',center='Knowledge base',data=['Poznámky','Dokumenty','E-maily','Meetingy','Web','Knihy']),
'14-tool-use.svg':dict(kind='flow',title='Tool use: LLM přestává jen psát',subtitle='Model zvolí nástroj, obdrží výsledek a pokračuje s novým kontextem.',data=[('Uživatel','cíl'),('LLM','volba nástroje'),('Tool call','funkce + argumenty'),('Nástroj','DB / web / API'),('LLM','interpretace')]),
'15-mcp-architecture.svg':dict(kind='flow',title='MCP jako standardizované rozhraní',subtitle='MCP odděluje AI aplikaci od konkrétních integrací.',data=[('AI host','chat / IDE / agent'),('MCP client','sjednocené volání'),('MCP server','tools + resources'),('Nativní API','autentizace + logika'),('Reálný systém','files / DB / Git / CAD')]),
'16-agent-anatomy.svg':dict(kind='layers',title='Anatomie AI agenta',subtitle='Agent je software kolem LLM: cíl, stav, nástroje, kontroly a smyčka.',data=[('Cíl / instrukce','co má systém dokončit'),('LLM / reasoning','volba dalšího kroku'),('Nástroje','akce v okolním světě'),('Stav / memory','co se už stalo'),('Kontroly','verify + human approval'),('Smyčka','opakování do stop podmínky')]),
'17-agent-loop.svg':dict(kind='loop',title='Agentní smyčka',subtitle='Každý krok může změnit další rozhodnutí.',center='Cíl',data=['Observe','Reason','Plan','Act','Verify']),
'18-build-agent.svg':dict(kind='flow',title='Jak stavět agenta bez zbytečné autonomie',subtitle='Začněte deterministickou kostrou a autonomii přidávejte až po měření.',data=[('Use-case','jedna přesná úloha'),('Tools + data','jen nutná práva'),('Checks','validace'),('Human gate','rizikové akce'),('Autonomie','až po evals')]),
'19-multi-agent.svg':dict(kind='hub',title='Multi-agentní systém',subtitle='Více agentů dává smysl jen s jasně oddělenými rolemi.',center='Orchestrator',data=['Planner','Researcher','Coder','Reviewer','Executor','Critic']),
'20-orchestration.svg':dict(kind='flow',title='Orchestrace agentních systémů',subtitle='Workflow drží stav, retry a checkpointy; LLM rozhoduje jen tam, kde přidává hodnotu.',data=[('Input','event / request'),('State','checkpoint'),('Agent step','LLM + tools'),('Control','retry / timeout'),('Output','result')]),
'21-coding-agent.svg':dict(kind='loop',title='Coding agent jako vývojová smyčka',subtitle='Síla vzniká propojením modelu s codebase, testy a Gitem.',center='Úkol',data=['Read code','Plan','Edit','Run tests','Review diff','Commit']),
'22-document-pipeline.svg':dict(kind='flow',title='AI nad heterogenními dokumenty',subtitle='Nejtěžší část bývá kvalitní převod, metadata, oprávnění a citace.',data=[('PDF / Word / Excel','PPT / logs'),('Normalizace','parse / OCR'),('Metadata + chunks','struktura'),('Search / RAG','retrieval + rerank'),('LLM','odpověď + zdroje')]),
'23-engineering-loop.svg':dict(kind='loop',title='AI + deterministický engineering tool',subtitle='LLM navrhuje další krok; simulátor nebo solver rozhoduje fyziku.',center='Požadavky',data=['Specifikace','Návrh','Simulace','Extrakce','Porovnání']),
'24-analog-ic-loop.svg':dict(kind='loop',title='AI-assisted analog IC design',subtitle='Znalosti, gm/ID, simulátor a rozhodnutí návrháře v jedné smyčce.',center='Designer',data=['Spec','gm/ID sizing','SPICE / Spectre','Extract metrics','Optimize']),
'25-security-boundaries.svg':dict(kind='flow',title='Bezpečnostní hranice agentního systému',subtitle='Nedůvěryhodná data, model a nástroje musí oddělovat oprávnění a kontroly.',data=[('Nedůvěryhodný vstup','web / mail / docs'),('Policy boundary','sanitace'),('LLM / agent','tool selection'),('Permissions','least privilege'),('Nástroj','read / write / external')]),
'26-ai-capability-stack.svg':dict(kind='layers',title='„Máme ChatGPT“ není AI capability',subtitle='Firemní hodnota vzniká propojením modelu s procesy, daty, nástroji a lidmi.',data=[('Business proces','co chceme zlepšit'),('Workflow / agent','řízení kroků'),('Tools + integrations','API a aplikace'),('Knowledge + data','správný kontext'),('Model layer','cloud / local / routing'),('Governance + evals','bezpečnost a kvalita'),('Lidé','kompetence a ownership')]),
'27-ai-readiness.svg':dict(kind='layers',title='AI readiness není jen technika',subtitle='Proces, data, bezpečnost, měření a lidé musí být připraveni společně.',data=[('Proces','jasný průběh a owner'),('Data','dostupnost a kvalita'),('Knowledge','co je dokumentováno'),('Security','citlivost a práva'),('Measurement','baseline a metriky'),('People','uživatelé a odpovědnost')]),
'28-usecase-matrix.svg':dict(kind='matrix',title='Výběr AI use-case',subtitle='Preferujeme vysokou hodnotu a rozumnou technickou / provozní složitost.',data=[('Strategic bet','vysoká hodnota, vysoká složitost'),('Nízká priorita','malá hodnota i složitost'),('Quick win','vysoká hodnota, nízká složitost'),('Pozor','složité, ale malý přínos')]),
'29-pilot-scale.svg':dict(kind='flow',title='Pilot → důkaz → škálování',subtitle='AI projekt má projít měřitelnými branami.',data=[('Baseline','čas / kvalita / cena'),('Pilot','omezený use-case'),('Evidence','evals + users'),('Go / no-go','rozhodnutí'),('Scale','industrializace')]),
'30-adoption-loop.svg':dict(kind='loop',title='Adopce jako učící se smyčka',subtitle='Technologie sama nestačí; lidé musí vidět užitek a sdílet výsledky.',center='Use-case',data=['Experiment','Měřit','Sdílet','Trénovat','Standardizovat']),
'31-evaluation-stack.svg':dict(kind='layers',title='Evaluace od komponenty k business výsledku',subtitle='Jedna hezká odpověď není důkaz kvality systému.',data=[('Business metric','čas / náklady / chybovost'),('End-to-end task','splnil reálný úkol?'),('Agent / workflow','správné kroky a recovery'),('RAG / retrieval','našel správné zdroje?'),('Model','kvalita odpovědi'),('Regression set','golden questions v čase')]),
'32-ai-tco.svg':dict(kind='layers',title='TCO AI řešení',subtitle='Cena tokenů nebo GPU je jen jedna vrstva celkových nákladů.',data=[('Cena chyby','dopad špatného výsledku'),('Lidé a provoz','monitoring a support'),('Integrace','vývoj a údržba'),('Inference','API tokeny / GPU'),('Hardware / cloud','CAPEX / OPEX'),('Security + compliance','audit a governance')]),
'35-learning-roadmap.svg':dict(kind='flow',title='Roadmapa učení: od modelu k produkci',subtitle='Další kroky dávají smysl v pořadí, ve kterém na sebe navazují.',data=[('Local stack','model + runtime'),('RAG','vlastní data'),('Tools','reálné akce'),('Agent','spolehlivá smyčka'),('Multi-agent','jen kde dává smysl'),('Production','evals + observability')]),
'36-minimal-ai-stack.svg':dict(kind='hub',title='Můj minimální AI stack',subtitle='Minimum není jeden chatbot, ale malá sada vrstev pro model, data, nástroje a měření.',center='AI workspace',data=['Frontier LLM','Local LLM','Search + RAG','Git + files','Automation','Monitoring']),
'37-project-ladder.svg':dict(kind='flow',title='10 projektů: cesta k agentnímu systému',subtitle='Každý projekt přidává jednu schopnost a zároveň nové riziko.',data=[('1–2','chat nad dokumenty'),('3–4','knowledge + local'),('5–6','RAG + tool'),('7–8','filesystem + coding'),('9–10','workflow + multi-agent')])
}

P=[
('01 - ','# 1.','01-history-timeline.svg','Časová osa vývoje AI','Zlomové body od obecného výpočtu po agentní systémy.',0),('02 - ','# 2.','02-ai-taxonomy.svg','Vztah AI, ML, deep learningu, generativní AI a LLM','Pojmy tvoří vrstvy; agentní systém je nadstavba kolem modelu.',0),
('03 - ','## 3.1','03-model-vs-database.svg','LLM není databáze','Modelové parametry nejsou knihovna dokumentů.',1),('03 - ','## 3.4','03-embeddings.svg','Princip embeddings','Embedding převádí text do číselné reprezentace.',1),('03 - ','## 3.7','03-token-generation-loop.svg','Autoregresivní generování tokenů','LLM skládá odpověď token po tokenu.',1),('03 - ','## 3.18','03-enter-to-answer.svg','Od Enteru po odpověď','Zjednodušená inferenční cesta od kontextu k odpovědi.',1),
('07 - ','# 7.','07-cloud-onprem-hybrid.svg','Cloud, hybrid a on-prem','Rozdělení úloh podle dat, výkonu, ceny a provozní odpovědnosti.',0),('08 - ','# 8.','08-local-memory-stack.svg','Paměťové vrstvy lokálního LLM','VRAM není jen velikost modelových vah.',0),('09 - ','# 9.','09-prompt-anatomy.svg','Anatomie kvalitního promptu','Prompt jako strukturovaná specifikace úlohy.',0),('10 - ','# 10.','10-context-stack.svg','Vrstvy kontextu','Co model při řešení úlohy skutečně vidí.',0),('11 - ','# 11.','11-external-data-bridge.svg','Připojení modelu k vlastním datům','Soukromá a aktuální data musí být do kontextu přivedena externí vrstvou.',0),('12 - ','# 12.','12-rag-pipeline.svg','RAG pipeline','Od dokumentů přes retrieval až k odpovědi s citacemi.',0),('13 - ','# 13.','13-second-brain.svg','Architektura druhého mozku','AI jako navigátor nad znalostní bází.',0),('14 - ','# 14.','14-tool-use.svg','Tool use','Model zvolí nástroj, obdrží výsledek a pokračuje.',0),('15 - ','# 15.','15-mcp-architecture.svg','MCP architektura','Standardizované propojení AI aplikace s nástroji a zdroji.',0),('16 - ','# 16.','16-agent-anatomy.svg','Anatomie AI agenta','Agent je software kolem LLM: cíl, stav, nástroje, kontroly a smyčka.',0),('17 - ','# 17.','17-agent-loop.svg','Agentní smyčka','Observe → reason → plan → act → verify.',0),('18 - ','# 18.','18-build-agent.svg','Postup stavby jednoduchého agenta','Autonomii přidávat až po validaci a měření.',0),('19 - ','# 19.','19-multi-agent.svg','Multi-agentní systém','Orchestrátor koordinuje specialisty s jasnými rolemi.',0),('20 - ','# 20.','20-orchestration.svg','Orchestrace agentního systému','State, retry, checkpointy a agentní kroky v jednom workflow.',0),('21 - ','# 21.','21-coding-agent.svg','Coding agent loop','Čtení kódu, editace, testy, review diffu a commit.',0),('22 - ','# 22.','22-document-pipeline.svg','Pipeline nad firemními dokumenty','Heterogenní soubory se musí normalizovat, indexovat a citovat.',0),('23 - ','# 23.','23-engineering-loop.svg','AI a deterministické engineering nástroje','LLM orchestruje; specializovaný nástroj rozhoduje fyziku.',0),('24 - ','# 24.','24-analog-ic-loop.svg','AI-assisted analog IC design loop','Specifikace → gm/ID → simulace → extrakce → optimalizace.',0),('25 - ','# 25.','25-security-boundaries.svg','Bezpečnostní hranice agentního systému','Data, LLM a nástroje musí oddělovat oprávnění a kontroly.',0),('26 - ','# 26.','26-ai-capability-stack.svg','Firemní AI capability stack','Chatbot je jen jedna vrstva celého pracovního systému.',0),('27 - ','# 27.','27-ai-readiness.svg','Vrstvy AI readiness','Proces, data, security, measurement a lidé musí být připraveni společně.',0),('28 - ','# 28.','28-usecase-matrix.svg','Matice AI use-case','Hodnota versus složitost rozlišuje quick wins a strategic bets.',0),('29 - ','# 29.','29-pilot-scale.svg','Pilot až škálování','Každá fáze má vlastní měřitelnou bránu.',0),('30 - ','# 30.','30-adoption-loop.svg','Smyčka adopce AI','Experiment, měření, sdílení, trénink a standardizace.',0),('31 - ','# 31.','31-evaluation-stack.svg','Evaluační stack','Od regresních testů až po business metriku.',0),('32 - ','# 32.','32-ai-tco.svg','TCO AI řešení','Tokeny a GPU jsou jen část celkových nákladů.',0),('35 - ','# 35.','35-learning-roadmap.svg','Roadmapa dalšího učení','Lokální stack → RAG → tools → agent → production.',0),('36 - ','# 36.','36-minimal-ai-stack.svg','Minimální AI stack','Modely, data, nástroje, Git, automatizace a monitoring.',0),('37 - ','# 37.','37-project-ladder.svg','Deset projektů od začátečníka k agentům','Postupné přidávání schopností i rizik.',0)]

def locate(prefix):
    m=sorted(BOOK.glob(prefix+'*.md')); return m[0] if m else None

def block(svg,alt,caption):
    return f'<!-- visual:{svg} -->\n\n![{alt}](assets/diagrams/{svg})\n\n*Obrázek: {caption}*\n'

def apply(content,anchor,b,replace_ascii):
    marker=b.splitlines()[0]
    if marker in content: return content,False,'already-present'
    lines=content.splitlines(keepends=True); idx=next((i for i,l in enumerate(lines) if l.strip().startswith(anchor)),None)
    if idx is None: return content,False,'anchor-not-found'
    if replace_ascii:
        for j in range(idx+1,min(len(lines),idx+80)):
            if j>idx+2 and re.match(r'^##\s',lines[j]): break
            if lines[j].strip() in ('```text','```ascii'):
                k=j+1
                while k<min(len(lines),idx+80) and lines[k].strip()!='```': k+=1
                if k<len(lines):
                    raw=''.join(lines[j+1:k])
                    if any(t in raw for t in ('↓','↑','→','←','┌','└','│','─','=>','->')):
                        lines[j:k+1]=['\n'+b+'\n']; return ''.join(lines),True,'replaced-ascii'
    lines.insert(idx+1,'\n'+b+'\n'); return ''.join(lines),True,'inserted'

def ascii_hits(content):
    out=[]; lines=content.splitlines(); i=0
    while i<len(lines):
        if lines[i].strip() in ('```text','```ascii'):
            s=i; i+=1; buf=[]
            while i<len(lines) and lines[i].strip()!='```': buf.append(lines[i]); i+=1
            raw='\n'.join(buf)
            if any(t in raw for t in ('↓','↑','→','←','┌','└','│','─','=>','->')): out.append((s+1,next((x.strip() for x in buf if x.strip()),'')[:90]))
        i+=1
    return out

def main():
    for name,spec in D.items(): (ASSETS/name).write_text(render(spec),encoding='utf-8')
    results=[]
    for prefix,anchor,svg,alt,caption,repl in P:
        path=locate(prefix)
        if not path: results.append((prefix,svg,'file-not-found')); continue
        old=path.read_text(encoding='utf-8'); new,changed,status=apply(old,anchor,block(svg,alt,caption),bool(repl))
        if changed: path.write_text(new,encoding='utf-8')
        results.append((path.name,svg,status))
    chapters=sorted(p for p in BOOK.glob('*.md') if re.match(r'^\d{2} - ',p.name)); total=0
    report=['# Visual audit knihy','', '> Automaticky vytvořeno skriptem `tools/add_book_visuals.py`.','',f'- Projito kapitol: **{len(chapters)}**',f'- Vytvořeno SVG diagramů: **{len(D)}**',f'- Naplánováno vložení vizuálů: **{len(P)}**','','## Vložené / kontrolované vizuály','']
    report += [f'- `{f}` → `{s}` — {st}' for f,s,st in results]
    report += ['','## Zbývající textové bloky, které vypadají jako ASCII diagram','', 'Nejsou automaticky odstraněny bez jistoty, že nejde o užitečný příklad, výpočet nebo ukázku tokenizace.','']
    for path in chapters:
        hits=ascii_hits(path.read_text(encoding='utf-8'))
        if hits:
            total+=len(hits); report += [f'### {path.name}']+[f'- řádek ~{line}: `{first or "(prázdný začátek)"}`' for line,first in hits]+['']
    report.insert(7,f'- Zbývající podezřelé ASCII diagramy: **{total}**')
    (BOOK/'VISUAL_AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    print(f'visuals={len(D)} placements={len(P)} remaining_ascii={total}')
if __name__=='__main__': main()
