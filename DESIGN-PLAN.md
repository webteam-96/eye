# Design plan — Dr. Anchal Gupta

**Superseded on 16 Sep 2026.** The Pass 1 plan (a Snellen-chart editorial direction) was built, reviewed and rejected by the client:

> "The current design doesn't match the reference sites and I'm not approving it. […] The references are the brief. Do not substitute your own direction."
> "make design like https://medic-128.webflow.io/ exact same only animation of electrocardiogram trace and other micro animation … https://25.saveachildsheart.org/"

The plan now is `REFERENCE-TEARDOWN.md`: a measured teardown of both references (container, grid, section padding at desktop and mobile, the full type scale in px, colour usage, section-by-section layout inventory, component anatomy, motion specs) and a mapping table of every section of the five pages against the Medic 128 section its layout copies. The rules in force:

1. **Medic 128 governs everything visible**: header, hero variants, buttons, cards, accordions, bands, forms, footer, inner-page templates, mobile stacking and alignment. If a choice in the reference looks like a generic default, it is built that way anyway.
2. **Save a Child's Heart governs motion only**: the EKG trace (drawn on load, under one word of each heading, scrubbed by scroll on the Expertise timeline), rise-and-fade reveals (`translateY(120px)→0`, 1200ms `cubic-bezier(0,0,0,1)` + opacity 1000ms, siblings staggered 300ms), marquee strips, card lift and 4-second image zoom on hover, the preloader that exits downwards after 1.2s.
3. **Only three things change from the reference**: the content (PRD, gaps marked `TODO:`), the palette (Medic teal → olive `#5E6A42`, navy → near-black `#383434`, pink → amber `#D99A2B` with ink text only, deep teal → moss `#3C4632`, pink wash → paper), and the photography.

The measured system lives in `assets/css/tokens.css`; the pass log is in `NOTES.md`.
