# Release Package Checklist — AI Book

Snapshot: **2026-08-08**

This checklist is the final gate between the current release-candidate manuscripts and a physical / commercial publication. It deliberately separates **content readiness**, **digital prepress readiness**, and **publisher/printer-specific production work**.

## Current release candidates

| Edition | Version | Content status | Digital PDF QA | Physical proof |
|---|---:|---|---|---|
| Czech — *AI od základů k agentním systémům* | 0.7 | content-locked release candidate | PASS | PENDING |
| English — *AI: From First Principles to Agentic Systems* | 0.8-eng | content-locked release candidate | PASS | PENDING |

Current trim used by the manuscript proofs: **170 × 240 mm**.

---

## 1. Content lock

- [x] Introduction present in both editions.
- [x] 36 numbered chapters in both editions.
- [x] 7 appendices in both editions.
- [x] Czech editorial QA passed.
- [x] English editorial QA passed.
- [x] CZ ↔ EN chapter content-parity audit completed.
- [x] English parity patch applied only where material gaps were identified.
- [ ] Re-run the fast-moving fact check immediately before publication, especially model names, product availability, regulations, pricing, and tooling snapshots.
- [ ] Freeze the final publication date and edition identifiers.

## 2. Figures and visual system

- [x] 43 figure references are present in each edition.
- [x] Screen and print SVG sets exist for the book diagrams.
- [x] Diagram text-overflow / box-fit issues were explicitly reviewed during the final visual pass.
- [x] Exact visually corrected SVG revisions are packaged into the PDFs currently linked from the root README.
- [x] All 43 figure pages in each GitHub-built PDF were reviewed digitally as contact sheets, with high-resolution spot checks of the previously most problematic diagrams.
- [ ] Inspect every figure again at final physical size, not only zoomed on screen.
- [ ] Check the thinnest strokes and pale gray text on the actual target paper / printer.
- [ ] Confirm that all captions remain comfortably readable in the physical proof.

## 3. Interior production file

- [x] Current manuscript proof uses 170 × 240 mm pages.
- [x] Page numbering, chapter starts, tables, code blocks, diagrams, and captions have undergone digital QA.
- [ ] Lock the target printer / platform before final production export.
- [ ] Confirm required bleed, safe margins, gutter, and binding allowance for that printer.
- [ ] Confirm PDF standard requested by the printer / platform.
- [ ] Verify font embedding with the final production PDF.
- [ ] Check image / vector handling after the printer's own preflight.
- [ ] Decide whether any intentionally blank pages are needed for recto chapter starts or signature layout.

## 4. Front matter and legal / bibliographic layer

- [ ] Final author display name.
- [ ] Title page.
- [ ] Copyright page.
- [ ] ISBN for each edition / format where applicable.
- [ ] Edition statement and publication year.
- [ ] Publisher / imprint or self-publishing identity.
- [ ] Tiráž / colophon for the Czech edition.
- [ ] Copyright / imprint equivalent for the English edition.
- [ ] Legal notices / trademark language where required.
- [ ] AI / technical-information disclaimer if desired.
- [ ] Credits for editing, design, diagrams, tooling, or external contributors if applicable.

## 5. Cover package

- [ ] Final front-cover concept.
- [ ] Back-cover copy.
- [ ] Author bio / photo if used.
- [ ] Barcode area if required.
- [ ] Final spine width calculated **only after** printer, paper stock, binding, and final page count are locked.
- [ ] Full wrap cover exported to the printer's exact template.
- [ ] Check crop marks / bleed rules according to the chosen printer; do not assume generic values.

## 6. Physical proof — mandatory final human gate

Order at least one physical proof of each materially different production format.

Check in normal reading conditions, not only under bright desk lighting:

- [ ] body-text size and line spacing feel comfortable after 20–30 minutes of reading;
- [ ] diagrams remain legible without magnification;
- [ ] smallest labels are readable;
- [ ] thin arrows / connector lines remain visible;
- [ ] pale gray text, captions, headers, and notes have enough contrast;
- [ ] tables are readable and do not look visually cramped;
- [ ] code blocks are readable and not too dense;
- [ ] gutter does not swallow text or diagrams;
- [ ] outer / top / bottom margins feel balanced;
- [ ] chapter-opening pages feel deliberate rather than accidentally sparse;
- [ ] no unexpected blank pages or orphan fragments;
- [ ] page numbers and running headers are correctly positioned;
- [ ] print alignment and trimming are consistent;
- [ ] binding opens comfortably enough for a technical book of this thickness.

Record every issue against the exact PDF page number. Make one controlled correction pass, rebuild, and re-proof only the affected risk areas.

## 7. Release artifacts

The final release package should contain, for each language edition:

- [ ] final print PDF;
- [ ] final cover PDF / artwork;
- [ ] source Markdown snapshot;
- [ ] exact diagram assets used in the build;
- [ ] bibliography / source snapshot;
- [ ] final QA reports;
- [ ] release notes;
- [ ] SHA-256 checksum of the publication PDF;
- [ ] Git commit SHA from which the publication package was built;
- [ ] ISBN / edition metadata;
- [ ] printer / platform production specification used for export.

## 8. Repository release hygiene

- [ ] Create a named Git tag for the publication candidate, for example `cz-v1.0-rc1` / `en-v1.0-rc1`, once the edition numbering is finalized.
- [ ] Do not move the release tag after a physical proof is approved; create a new RC instead.
- [ ] Ensure the PDF linked from the root README is byte-identical to the approved release artifact.
- [ ] Preserve previous release candidates rather than silently overwriting the historical record.
- [ ] Keep fast-moving fact snapshots date-stamped.

## 9. Final GO / NO-GO gate

Publication is **GO** only when all of the following are true:

1. content lock is still valid after the final fact check;
2. exact release PDF has passed mechanical / digital QA;
3. exact release PDF has passed the visual figure / page QA;
4. exact release PDF is the one stored in the release package and linked from GitHub;
5. printer-specific preflight passes;
6. a physical proof is approved;
7. cover / spine / ISBN / copyright / imprint data are final;
8. release commit + checksums are recorded.

> **The physical proof is the final authority for typography, contrast, line weight, gutter behavior, and real-world readability.**
