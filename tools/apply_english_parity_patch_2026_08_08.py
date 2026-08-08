from pathlib import Path

root = Path('book_final_eng')


def insert_before(path, marker, insertion, sentinel):
    p = root / path
    t = p.read_text(encoding='utf-8')
    if sentinel in t:
        return False
    if marker not in t:
        raise RuntimeError(f'marker not found in {path}')
    p.write_text(t.replace(marker, insertion + marker, 1), encoding='utf-8')
    return True


def replace_once(path, old, new, sentinel):
    p = root / path
    t = p.read_text(encoding='utf-8')
    if sentinel in t:
        return False
    if old not in t:
        raise RuntimeError(f'pattern not found in {path}')
    p.write_text(t.replace(old, new, 1), encoding='utf-8')
    return True

changed = []

if insert_before(
    '13 - The Second Brain.md',
    '---\n\n## Key Takeaways\n',
    '''---\n\n## 13.16 Prevent the Second Brain from Becoming a Digital Warehouse\n\nThe main enemy of a second brain is not too little data.\n\nIt is **too much unstructured data**.\n\nAutomation can make this worse. A system that saves every email, web page, transcript, screenshot, and document may become a technically perfect archive that is practically difficult to use.\n\nA useful architecture separates three layers:\n\n```text\nRAW ARCHIVE\n→ original transcripts, PDFs, email, web captures\n\nKNOWLEDGE\n→ validated notes, decisions, summaries, durable references\n\nWORKING\n→ current projects, open questions, tasks, active evidence\n```\n\nThe raw archive preserves history. The knowledge layer contains information that has been selected, structured, and given enough metadata to be reusable. The working layer contains what matters now.\n\nAI can help move information between these layers, but the promotion rules should remain explicit and human-governed. Otherwise automatic capture quietly turns into automatic clutter.\n\nA minimal second-brain architecture can therefore stay surprisingly simple:\n\n```text\n             SOURCES\n\nnotes | PDFs | email | transcripts | web\n                ↓\n        extraction / metadata\n                ↓\n          knowledge store\n          ┌─────┴─────┐\n          ↓           ↓\n     human view     AI index\n      Obsidian        RAG\n          ↓           ↓\n          └─────┬─────┘\n                ↓\n               AI\n                ↓\n       search / summary / agent\n```\n\nThe important property is architectural independence:\n\n> **The source knowledge is not trapped inside the model. The model is a work layer over it.**\n\n''',
    '## 13.16 Prevent the Second Brain from Becoming a Digital Warehouse'
): changed.append('13')

if insert_before(
    '15 - MCP, Skills, Plugins, and Connectors.md',
    '---\n\n## Key Takeaways\n',
    '''---\n\n## 15.14 A Constrained MCP Example: AI-Assisted Analog Design\n\nConsider an agent connected to an analog-design environment. Giving it an unrestricted shell would make the integration powerful, but it would also make the security boundary unnecessarily broad.\n\nA safer MCP server can expose only the operations the workflow actually needs:\n\n```text\nTOOLS\n\nrun_spectre_simulation(\n    testbench,\n    corner,\n    temperature\n)\n\nget_measurement(\n    run_id,\n    measurement\n)\n\nlist_available_testbenches()\n```\n\nThe agent cannot execute:\n\n```text\nrm -rf project/\n```\n\nbecause no such tool exists. Its action space is defined by the host, not by what the model can imagine.\n\nAbove those tools, a skill can encode the engineering procedure:\n\n```text\nSKILL: verify-LDO-design\n\n1. read the specification\n2. select the required testbenches\n3. run the required corners\n4. extract measurements\n5. compare results with the specification\n6. produce a verification report\n```\n\nThis separation is useful beyond analog design:\n\n- **MCP tools provide the hands.**\n- **The skill provides the workflow.**\n- **The LLM provides interpretation and bounded decision-making.**\n- **Host software defines permissions and the security boundary.**\n\nThe result is more useful than a generic shell and easier to audit.\n\n''',
    '## 15.14 A Constrained MCP Example: AI-Assisted Analog Design'
): changed.append('15')

if insert_before(
    '18 - Multi-Agent Systems.md',
    '---\n\n## Key Takeaways\n',
    '''---\n\n## 18.16 Engineering Example: An Analog Block\n\nA plausible multi-agent architecture for analog design might look like this:\n\n```text\n                  ORCHESTRATOR\n                        │\n          ┌─────────────┼─────────────┐\n          ↓             ↓             ↓\n   KNOWLEDGE AGENT   DESIGN AGENT   SIM AGENT\n   specs + prior art  sizing         Spectre\n          │             │             │\n          └─────────────┼─────────────┘\n                        ↓\n                    REVIEWER\n                        ↓\n                 HUMAN DESIGNER\n```\n\nThe diagram is attractive. That does not mean it should be the starting architecture.\n\nI would first build one closed loop:\n\n```text\nspecification → simulation → evaluation\n```\n\nOnly after that loop works would I split it. Perhaps retrieval and design reasoning pollute each other's context. Perhaps simulation can run independently in parallel. Perhaps the reviewer needs different permissions or a different model. Those are real reasons to introduce additional agents.\n\n> **A multi-agent system should evolve from a working single-agent workflow, not substitute for designing one.**\n\nThat rule prevents a common failure mode: adding organizational complexity before the underlying task is understood.\n\n''',
    '## 18.16 Engineering Example: An Analog Block'
): changed.append('18')

if insert_before(
    '24 - AI Security.md',
    '### A minimal AI system card\n',
    '''### AI literacy is an operating capability, not one-off training\n\nSafe operation depends on users understanding a small set of practical truths:\n\n- the model can hallucinate;\n- a model and a tool are different security objects;\n- sensitive data needs explicit handling rules;\n- some outputs require independent verification;\n- an agent must have a defined action boundary.\n\nThis is not generic “AI awareness.” It is an operating capability closer to security awareness: people need enough understanding to recognize when the system has moved outside its safe envelope.\n\nThat capability also has to evolve. A team that was trained on chat-only assistants may still be unprepared for agents with file, database, or production-system access.\n\n''',
    '### AI literacy is an operating capability, not one-off training'
): changed.append('24')

if insert_before(
    '33 - What I Have Learned So Far.md',
    '---\n\n## Key Takeaways\n',
    '''---\n\n## 33.11 What I Would Do Differently\n\nIf I were starting again, I would spend less time searching for the “best” model and start building small end-to-end experiments earlier.\n\nSomething like:\n\n```text\n1. one document\n2. one local model\n3. one tool\n4. one RAG pipeline\n5. one agent\n6. one real workflow\n```\n\nFor every step I would record:\n\n```text\nwhat worked\nwhat failed\nwhy\n```\n\nI would also separate failure classes much earlier:\n\n```text\nMODEL PROBLEM\nvs.\nCONTEXT PROBLEM\nvs.\nTOOL PROBLEM\nvs.\nDATA PROBLEM\nvs.\nVERIFICATION PROBLEM\n```\n\nWithout this separation, it is very easy to keep changing models while never fixing the real bottleneck.\n\nMost importantly, I would focus earlier on the **closed loop**. Not merely:\n\n```text\nAI proposes something\n```\n\nbut:\n\n```text\nAI proposes\n→ a tool executes\n→ the system measures\n→ the result is verified\n```\n\nThat is where the technology becomes most interesting to me: not when the model sounds intelligent, but when the system can connect reasoning to evidence and measurable outcomes.\n\n## 33.12 Seven Rules I Would Put on Page One\n\nIf I had to restart with seven rules in front of me, they would be these:\n\n1. **Do not start by choosing the best model. Define the task precisely first.**\n2. **When the result is poor, identify whether the failure is in the model, data, context, tool, permissions, state, or verifier.**\n3. **Verify externally whenever you can.** A test, simulator, database, or deterministic rule is stronger evidence than confident prose.\n4. **Build small end-to-end experiments.** One working closed loop teaches more than ten disconnected chatbot demos.\n5. **A smaller model inside a well-designed workflow can be more valuable than a frontier model without the right context and tools.**\n6. **Add autonomy only after you have evals, limits, and a reliable way to stop or escalate the system.**\n7. **Invest in data, integrations, and evals so the model can be replaced tomorrow.** Those assets are more durable than today's benchmark winner.\n\nIf I compress my current view into one sentence, it is still this:\n\n> **The most important skill is not choosing the smartest model. It is giving the model the right context and tools at the right moment — and reliably verifying what comes out.**\n\nThat is not a final answer about AI. It is a working compass. Models, prices, frameworks, and interfaces will keep changing. The stable questions are: **What is the goal? What evidence is needed? What should the model decide? What should a tool do? What are the permission boundaries? And how will we know the result is correct?**\n\nOnce those questions are explicit, AI stops being a magic box and becomes engineering material.\n\n''',
    '## 33.11 What I Would Do Differently'
): changed.append('33')

p = root / '36 - Ten Projects from Beginner to Agentic Systems.md'
t = p.read_text(encoding='utf-8')
if '## Recommended Difficulty Progression' not in t:
    replacements = [
        ('''Desired output:\n\n```text\nparameter | rev B | rev C | change | source\n```\n\nRequire conflict marking when sources disagree. Manually verify a random sample.\n''', '''Desired output:\n\n```text\nparameter | rev B | rev C | change | source\n```\n\nA useful procedure is deliberately boring:\n\n1. define the output schema before asking the model to compare anything;\n2. identify every document and revision explicitly;\n3. generate the structured table;\n4. manually verify a random sample of rows;\n5. require the system to mark conflicts instead of silently choosing one source.\n\nRequire conflict marking when sources disagree. Manually verify a random sample.\n'''),
        ('''If the system cannot distinguish current authoritative information from history, it is not ready to become agent memory.\n\n---\n\n## Project 4 — Run a Local LLM\n''', '''If the system cannot distinguish current authoritative information from history, it is not ready to become agent memory.\n\nTest it with questions whose answers changed over time. A good result should retrieve not only the latest answer, but also the date, source, status, and the older decision it replaced. This turns “search my notes” into a test of real knowledge management.\n\n---\n\n## Project 4 — Run a Local LLM\n'''),
        ('''Start small — perhaps 20–50 documents — and create 30 golden questions with known authoritative sources.\n\nMeasure retrieval **before** generation:\n''', '''Start small — perhaps 20–50 documents — and create 30 golden questions with known authoritative sources.\n\nUse this order:\n\n1. ingest and parse the corpus;\n2. create chunks and metadata;\n3. build the index;\n4. label the authoritative source for every golden question;\n5. measure retrieval without an LLM;\n6. only then add answer generation.\n\nMeasure retrieval **before** generation:\n'''),
        ('''If multi-agent does not create measurable value, the simpler system wins.\n\n---\n\n## Document Every Project\n''', '''If multi-agent does not create measurable value, the simpler system wins.\n\n### Human approval\n\nUntil reliability and risk evidence justify otherwise, require explicit approval for actions that:\n\n- modify production data;\n- publish an official result;\n- send external communication;\n- trigger a financially significant action;\n- trigger a technically consequential or hard-to-reverse action.\n\nThe approval boundary should be defined by consequence, not by whether the action happens to be initiated by one agent or five.\n\n---\n\n## Document Every Project\n'''),
        ('''---\n\n## When AI Fails: Debug the Layer That Failed\n''', '''---\n\n## Recommended Difficulty Progression\n\n| Project | New capability | Typical risk |\n|---|---|---|\n| 1 | context grounding | answering outside the source |\n| 2 | provenance | mixing documents or revisions |\n| 3 | knowledge management | stale or superseded information |\n| 4 | local inference | performance and false expectations |\n| 5 | retrieval | bad chunks, missed evidence, injection |\n| 6 | tool use | incorrect tool call or arguments |\n| 7 | agent loop | permissions that are too broad |\n| 8 | coding agent | unintended change or regression |\n| 9 | enterprise workflow | data, identity, auditability |\n| 10 | orchestration | complexity without measurable value |\n\nThe progression is intentional. Each project adds one new failure surface while keeping the previous layers visible enough to debug.\n\n---\n\n## When AI Fails: Debug the Layer That Failed\n''')
    ]
    for old, new in replacements:
        if old not in t:
            raise RuntimeError('chapter 36 patch marker not found')
        t = t.replace(old, new, 1)
    p.write_text(t, encoding='utf-8')
    changed.append('36')

print('Parity patch applied to chapters:', ', '.join(changed) if changed else 'already applied')
