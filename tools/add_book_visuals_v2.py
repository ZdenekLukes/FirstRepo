from add_book_visuals import D, P, main

D.update({
'04-llm-strengths-limits.svg':dict(
    kind='layers',
    title='Kde je LLM silný — a kde potřebuje oporu',
    subtitle='Jazykový model je výborný interpret a generátor; přesnost často dodává externí nástroj.',
    data=[
        ('Silná stránka: transformace','shrnutí, přepis, překlad, strukturování'),
        ('Silná stránka: extrakce','hledání a třídění informací v dodaném kontextu'),
        ('Silná stránka: tvorba','text, kód, návrhy a varianty řešení'),
        ('Ověřovat: fakta a reasoning','sebevědomý výstup nemusí být správný'),
        ('Připojit nástroj: aktuální svět','web, databáze, API a firemní systémy'),
        ('Připojit nástroj: přesnost','kalkulačka, Python, testy, simulátor')
    ]
),
'05-model-map.svg':dict(
    kind='hub',
    title='Mapa AI modelů podle úlohy',
    subtitle='Neexistuje jeden nejlepší model; vybíráme podle modality, schopnosti a provozního režimu.',
    center='Use-case',
    data=['General LLM','Reasoning','Coding','Vision','Speech','Embeddings']
),
'06-model-selection.svg':dict(
    kind='flow',
    title='Jak vybrat model pro reálnou úlohu',
    subtitle='Benchmark je jen jeden vstup; rozhoduje vlastní test nad skutečným workflow.',
    data=[
        ('Use-case','reálná úloha'),
        ('Test set','vlastní příklady'),
        ('Kvalita','správnost + robustnost'),
        ('Provoz','latence + cena'),
        ('Constraints','privacy + licence')
    ],
    footer='Vyber model, který nejlépe splní celý soubor požadavků — ne ten s nejvyšším jedním benchmarkem.'
),
'12-model-rag-agent.svg':dict(
    kind='flow',
    title='Model vs. RAG vs. Agent',
    subtitle='Nejsou to tři konkurenční věci. Každá další vrstva přidává systému novou schopnost.',
    data=[
        ('Model','generuje a interpretuje'),
        ('+ RAG','dohledá vlastní znalosti'),
        ('+ Tools','umí provést akci'),
        ('+ Agent loop','volí další krok'),
        ('AI systém','data + tools + controls')
    ]
)
})

P.extend([
('04 - ','# 4.','04-llm-strengths-limits.svg','Silné stránky a limity LLM','LLM je silný v práci s jazykem; přesná nebo aktuální data často dodává nástroj.',0),
('05 - ','# 5.','05-model-map.svg','Mapa AI modelů podle úlohy','Model vybíráme podle konkrétního use-case, ne podle jediné univerzální tabulky.',0),
('06 - ','# 6.','06-model-selection.svg','Jak vybrat model','Vlastní test set propojuje kvalitu modelu s provozními omezeními.',0),
('12 - ','## 12.2','12-model-rag-agent.svg','Model vs. RAG vs. Agent','Model generuje, RAG přidává znalosti a agent přidává akce a opakovanou smyčku.',0)
])

if __name__ == '__main__':
    main()
