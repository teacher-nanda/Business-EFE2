# Business EFE — Slide Standards

This file is the single source of truth for all design and UX decisions across Business EFE lessons. Update it whenever a new standard is established.

---

## Layout

### Columns — Example placement and split

#### When N (exercises) is EVEN
- **Example spans the full width** — placed in a dedicated `<div id="hwXX-example">` above the `.two-col` grid, NOT inside a column.
- Exercises split **equally**: N/2 left, N/2 right → `i < N/2`.
- In HTML: add `<div id="hwXX-example"></div>` between the instruction `<p>` and `<div class="two-col">`.
- In JS: `exEl.innerHTML=''` on build/reset; append example to `exEl`, not to `left`.
  - N=8 → 4 left + 4 right, example full-width above
  - N=10 → 5 left + 5 right, example full-width above

#### When N (exercises) is ODD
- **Example goes in the LEFT column**, at the top (as a block inside `hw43-left` / similar).
- Formula: `split_index = floor(N/2)` → left gets `floor(N/2)` exercises, right gets `ceil(N/2)`.
- Counting total visible blocks per column: left = Example + floor(N/2), right = ceil(N/2). For odd N the total blocks difference is 1 (left heavier), which is acceptable.
  - N=5 → `i < 2` → left: Example+2 (3 blocks), right: 3 (3 blocks) — equal total ✓
  - N=11 → `i < 5` → left: Example+5 (6 blocks), right: 6 (6 blocks) — equal total ✓

### Slide title position — never override
Every content slide's `.content` div uses the standard, unmodified layout: `padding:16px 36px 20px;overflow-y:auto;max-height:calc(100vh - 118px);` with the `<h2>` as the first element inside it. **Never add `display:flex`, `flex-direction:column`, `justify-content:center`, or any other rule that vertically centers or repositions content** — even for image-only or short slides. Every slide's title must land in the exact same position as every other slide. If a slide looks sparse, that's fine; do not "fix" it by centering — that breaks visual consistency across the deck.

### Never use `placeholder="..."` on inputs — and never fake one with static text either
**No `<input>` in any exercise may have a `placeholder` attribute — ever, in any lesson, in any course.** Leave the input empty by default; do not hint the expected format or answer via placeholder text (e.g. no `placeholder="do/does"`, no `placeholder="?"`, no `placeholder="…"`). This is a permanent, non-negotiable rule. (The notes panel's `data-placeholder` on `#notesTA`, a `contenteditable` div and not a form input, is the one exception — it is UI chrome, not an exercise.)
- **This rule is not limited to the literal `placeholder=` attribute.** Any clickable blank built as a `<span>`/`<div>` (used by click-to-place word-bank and fill-gap exercises instead of a real `<input>`) must default to **empty text content**, not a filler character like `?`, `…`, or `___`. A blank showing "?" by default is a placeholder in every way that matters even though it isn't the HTML attribute — it visually hints "type/pick something here" the same way a real placeholder does, and it's wrong for the same reason. Give the blank a `min-height` in its CSS (e.g. `min-height:1.3em`) so it doesn't visually collapse while empty, rather than filling it with a character. Found and fixed real violations in Business-EFE1 Lesson 4 (`s14`, `hw58`), the shared `wbBuild` reference implementation itself (`Business-EFE2/Lesson_01_Introductions.html`), and Business-HR Lesson 2 (`twd1`–`twd6`) — check every clickable blank in a lesson whenever you touch it, the same as matching exercises and word-bank order.

### Matching exercises — right-column order must follow the book, never "solved" order
When an exercise matches beginnings/questions to endings/answers (whether built with the `qamBuild` module or a bespoke render function — see below), the right-hand column **must display answers in the exact order the book prints them** — which is deliberately scrambled and independent of the left column's numbering. Never let the right column default to "solved order" (answer for item 1 first, item 2 second, etc.) — that silently gives away the pairing and doesn't match the source. This has been the single most repeated mistake in this project; it is not optional and there is no acceptable exception.
- `qamBuild(exId, qContainerId, aContainerId, pairs, resultId, exampleQ, exampleA, answerOrder)` — the `answerOrder` param is an array of `pairs` indices (0-based) giving the exact top-to-bottom print order of the right column; use `-1` at the position where the example's own answer is printed (the example's answer is often interleaved partway down the list, not always at the top).
- **Bespoke/hand-rolled matching renderers (not using `qamBuild`) must implement the exact same rule.** Several lessons (e.g. Business-EFE1 Lesson 4's `renderS12`/`renderHW55`) predate `qamBuild` and render their own right column by looping over the data array directly (`data.forEach(function(item, i){...})`), which produces "solved order" by construction. When you find one of these, add an explicit order array (e.g. `s12AnswerOrder = [0,2,4,1,3]`) and loop over that array instead of the raw data array for the right/answer column only — the left/question column keeps looping over the raw array in book order. Do not assume a matching exercise is safe just because it doesn't call `qamBuild`.
- **The example's own answer is part of the right column's print order — it is not automatically first.** The left column's example question genuinely is printed first in the book (that's why it's fine to always pin it at the top of the question column), but its matching answer is usually scrambled in *with* the real answers on the right, often several rows down — e.g. the book prints "It's across from the meeting room." (the example's answer) as the *3rd* row of six, not the 1st. A real bug shipped in Lesson 4's `renderS12`/`renderHW55`: the example's struck-through answer chip was hardcoded to render before the loop (visually pinned to the top of the right column, aligned with the example question), which is wrong whenever the book's own layout doesn't put it there. Fix: render the example's answer chip *inside* the same loop/order array as the real answers, at its correct index (an `s12ExampleAfter`/`hw55ExampleAfter`-style counter that inserts it after N real chips have been rendered) — never as a separately-pinned element unless you've confirmed the book itself prints it first.
- **Once a matching is scored/checked, real matched items show a "↳ [answer text]" completion line beneath the question/situation half. The static Example row must show this same completion line too, styled consistently (same "↳" prefix), not just the bare unmatched question/statement.** A real bug shipped in Lesson 4's `renderS12`/`renderHW55`: every real matched pair displayed its completion once matched, but the static Example box never did, making it visually inconsistent and looking like a leftover unmatched item. Fix: hardcode the Example's own answer as a `↳ ...` line directly in the Example box's static markup (it's always known in advance, no matching interaction needed for it).
- Determine the order by reading the actual book page (render it as an image and view it — see "Verifying against the book" below) and noting which row each ending appears in, then mapping each row back to its data index.
- The left column always stays in the book's own left-column order (this is the natural 1..N numbering) — only the right column needs the explicit order override.
- This rule applies to every course (EFE1, EFE2, and Business-HR) and every lesson, not just the one it was first caught in. **Whenever you touch a lesson for any reason, check every matching exercise in that file against the book before moving on — don't wait to be told about a specific slide.**

### Word-bank fill-in-the-gap exercises — click-based, bank before rows
When the book shows a "fill in the gaps using the words in the panel" exercise, implement it as **click a word chip, then click a blank to place it** — never a typed `<input>` with the word bank shown only as a passive reference list. This matches the book's own convention of visually crossing out a word once it's used (e.g. "must" struck through after the worked example).
- Shared module: `wbBuild(exId, rowsId, bankId, items, bankWords, resultId, exampleHtml, exampleId, usedWords)` / `wbSelectWord` / `wbClickBlank` / `wbCheck` / `wbReset` (reference implementation: `Business-EFE2/Lesson_01_Introductions.html`, slides `s5`/`hw1`). `items` = `[{pre, post, ans:[...]}]`; clicking a used chip again picks it back up (moves it, doesn't duplicate); `.wb-used` marks a placed word's chip as struck-through/disabled in the bank.
- If the static worked example (the orange "Example:" box) uses a word from the same panel — e.g. "must" in "You must be Joe Smith." — that word is still shown in the bank exactly as the book prints it: **struck through and non-clickable, never omitted**. Pass it via the `usedWords` array (e.g. `wbBuild(..., ['must'])`); never silently drop it from the bank just because the example already "used" it — the student should see the full panel exactly as the book does, including the crossed-out word. Never fake this with a `placeholder=` attribute or grayed-out static text pretending to be an input — it must be a real, visible, struck-through chip in the bank, consistent with the permanent placeholder ban above.
- **The bank's word ORDER must also match the book's own print order exactly, left-to-right then top-to-bottom (row-major), including the struck-out example word in its actual printed position** — this is not optional and is the same category of mistake as matching-exercise order. Do not alphabetize, do not group by answer, do not order by which blank they fill. If a word is used twice in the book's answers (e.g. "What" appearing for two different blanks), the book repeats that word chip twice in the bank at its two actual printed positions — reproduce the repeat, don't de-duplicate it. This rule applies to `wbBuild` AND to bespoke/hand-rolled word-bank implementations that predate it (e.g. Business-EFE1 Lesson 4's `s14`/`hw58`, which use their own click-to-place code, not `wbBuild`) — check every word-bank exercise in a lesson against the actual book image whenever you touch that lesson, the same way matching exercises must be checked.
- **The word-bank container must be positioned BEFORE the sentence-rows container in the HTML**, regardless of where the book physically places the panel on the page (the book often puts it below/after the sentences — that's a print-layout constraint, not a UX requirement; our slides always show the tools before the task).
- Do not add an instruction like "(some words may be used more than once)" unless you've confirmed against the book that words actually repeat — check the book's own word count against the blank count first (most of these panels are a 1:1 bijection, no repeats).
- Only use a typed `<input>` mechanic for gap-fills where the book itself doesn't supply a fixed word panel (i.e. genuinely open/typed answers).

### Short/key-word titles must not remove information — put it in the instruction
When a slide's `<h2>` is trimmed to short key words (per house style), any descriptive information that was dropped from the longer title must be preserved in the `<p class="instruction">` or `<p class="inst-light">` line directly below it. A student should never lose context because the title got shorter — the full picture must still be recoverable by reading the h2 + the instruction paragraph together. Before shipping a shortened title, check: does the instruction line still say what the exercise actually is (not just "click X"), ideally opening with the book's own exercise line?

### Verifying against the book — render pages as images, don't trust PDF text extraction alone
Course book and practice book PDFs often have exercises (matching panels, gap-fill panels, speech-bubble graphics) baked into images rather than selectable text — plain `fitz`/PDF text extraction silently returns nothing useful for these, which is how fabricated or misordered content slips in undetected. Before building or auditing any exercise:
1. Render the relevant page(s) to PNG (`page.get_pixmap(matrix=fitz.Matrix(2.5,2.5))`) and view them directly (via the Read tool) rather than relying on extracted text.
2. Cross-check every exercise's content, order, and correct answers against the book's own "Answers" section at the back of the book (also image-based — render and view it too) rather than inferring answers from context. This caught real bugs: a True/False/Not-Given exercise with 4 of 5 answers wrong, and a "rewrite the sentence" exercise whose model answers didn't match the book's own key.
3. Do this for BOTH the Course Book (in-lesson slides) and the Practice Book (homework slides) — they are different exercises on the same topic, not the same content reused.
4. **The book's own back-of-book "Answers" pages are the single source of truth for every answer key — always check them, for every exercise, not just ones flagged as wrong.** Never substitute your own reasoning about the passage/exercise text for the printed key, and never assume an answer is safe just because it was "reasoned out" carefully during an earlier fix — if a past fix changed an answer based on inference rather than the printed key, re-verify it against the key the next time the file is touched. If your inference and the printed key disagree, the printed key wins; go back and figure out why your reading was wrong, don't override the book.

**This step is mandatory, not optional, and cannot be skipped just because an exercise "looks right" or was built carefully.** 2026-08-31: an entire HW exercise's Example (question text AND correct answer) was fabricated from scratch instead of copied from the book, and went undetected for a full session because it was never checked against a rendered page image — the exercise's *items* were correct, which created false confidence that the *example* was too. Concretely, whenever building or revisiting ANY exercise slide (in-lesson or HW):
- Render and view the exact book page BEFORE writing or trusting any item text, including the Example — never write example sentences "from memory" or by analogy with the items.
- Transcribe the Example word-for-word from the image, including its correct answer, exactly like every other item — it is not exempt from verification just because it's usually simpler.
- When later asked to "audit" or "recheck" a slide, always re-render the page fresh and re-diff every item + the Example against it, rather than re-reading the existing code and reasoning about whether it seems plausible.

### HW Slide Structure
Every HW slide must have:
1. Banner: `📝 Homework` (no slide numbers, no pills)
2. `<h2>` title: e.g. `HW 1 – Countries & Continents` (`font-size:1.75rem; font-weight:800`)
3. `<p class="inst-light">` instruction immediately below the title
4. Content (exercise)
5. Check / Reset buttons (`btn-check` / `btn-reset`)
6. Result div

---

## Typography

### Minimum font size
**Never use a font size smaller than `1.05rem`** for any content text in a slide body.
- `1.05rem` = `.inst-light` baseline — this is the floor, not a target.
- Exception: decorative UI-only labels (e.g. banner nav pills, dot counters) may use smaller sizes.

### Classes
| Class | Size | Weight | Use |
|---|---|---|---|
| `.instruction` | `1.08rem` | `700` (bold) | Action prompts, task labels |
| `.inst-light` | `1.05rem` | `400` (normal) | Explanatory/grammar text |
| `h2` | `1.75–1.85rem` | `800` | Slide titles |
| `.ex-row` | `1.06rem` | — | Exercise item rows |
| `.ans-input` | `1.05rem` | `700` | Text input fields |

### Instructions
- `.instruction` (bold): for action labels like "Choose the correct word."
- `.inst-light` (normal): for grammar explanations. Only the specific word/form being taught goes in `<strong>`.
- Example: `<p class="inst-light">Use <strong>"from"</strong> or a nationality adjective.</p>`

### Line spacing between exercise rows/items — never tighter than 14–16px
Stacked exercise rows or items (TFNG rows, matching-exercise rows, cross-out rows, gap-fill rows, word-order rows, speak-cards, etc.) must have at least `14px`–`16px` of vertical space between them — either as `gap` on the flex container (`.col-section` and similar row-stack containers use `gap:16px`) or as `margin-bottom` on the row itself (e.g. `.tfng-row{margin-bottom:16px}`). `8px`–`10px` reads as visually cramped once rows have their own padding and border — this was audited and fixed across the file 2026-08-31 (previously many row stacks used `gap:6px`–`10px`). This does not apply to the small gaps *inside* a single row between inline elements (e.g. a word and its blank) — only to spacing *between* separate rows/items.

---

## Colours

### Semantic colour rules — strictly enforced
| Colour | Hex | Use ONLY for |
|---|---|---|
| Green | `#1A7A4A` / `#EEF7F0` | ✅ Correct answers (after Check) |
| Red | `#C4614A` / `#FCEEED` | ❌ Wrong answers (after Check) |
| Navy | `#1A5080` | Selected chips/buttons (active state) |
| Orange | `#C45020` | Example boxes, accent borders |
| Purple | `#7B2FBE` | "from + Country" in rewrite exercises |
| Blue-teal | `#0E5C7A` / `#8BB0D0` | Input underlines, neutral borders |

### DO NOT use green for:
- Default chip backgrounds
- Word bank backgrounds
- Any element that hasn't been checked yet

---

## Word Banks & Chips

### Default chip states
```
Free:     background:#EEF5FA; color:#1C2B3A; border:1.5px solid #C5A8E0; opacity:1
Selected: background:#1A5080; color:#fff;    border-color:#1A5080; transform:scale(1.05)
Used:     background:#f0eef8; color:#bbb;    border-color:#ddd; text-decoration:line-through; opacity:0.65
```

### Word bank container
```css
background: #F5F0FF;
border: 1px solid #C5A8E0;
border-radius: 10px;
padding: 14px 18px;
```

### Behaviour
- **Click free chip** → selects it (navy)
- **Click zone/box** → places chip; chip becomes "used" (strikethrough)
- **Click used chip** → picks it back up (removes from zone, reselects)
- **Click selected chip again** → deselects (returns to free)
- **Zone highlighting** → `border-color:#1A5080; background:#EEF5FA` (NOT green)
- Student can **always redo** — never lock chips after Check

### Pre-used ("struck") example words stay in their real book position
When a word is already spent on the exercise's own worked Example (shown struck-through/disabled in the bank, e.g. "must" or "do"), it must render **in its real printed position** within the bank — never pulled out and shown first. `wbBuild`'s `bankWords` argument must be the complete row-major book order including that word; `usedWords` only marks which entries render struck/disabled in place, it does not reorder anything. (Real bug, 2026-08-31: the old `wbBuild` always rendered `usedWords` first regardless of the book's actual panel order.)

### Long word-bank exercises need two columns and a sticky bank
Once a `wbBuild` exercise has enough rows that they might not all fit on one screen (roughly 6+ items — use judgment, a short 4-item list is fine as a single column), it needs both of the following, not just one:
- **Two-column split**: pass `splitIds:{leftId,rightId}` to `wbBuild`, `leftCount = Math.ceil(N/2)` — same convention as `xoBuild`'s cross-out module.
- **Sticky word bank**: `position:sticky;top:0` on the bank's wrapper (inside the slide's scrolling `.content` container) so the bank stays visible while the student scrolls through the rows below it. Without this, a long list scrolls the bank out of view and the student has no way to see which words are left.

---

## Check / Correction Behaviour

### Multiple choice (select one option)
- On Check: color the **selected button only** — green if correct, red if wrong.
- **Do NOT reveal the correct answer** by highlighting it.
- Student sees red → understands they were wrong → can try again after Reset.

### Sort / drag to zone
- On Check: color each placed chip green (correct zone) or red (wrong zone).
- Student can click a red chip to retrieve it and re-place it.

### Text inputs
- On Check: `border-bottom-color` → green (correct) or red (wrong).
- `color` → green or red to match.

### Text input sizing
- **All inputs in an exercise must be the same fixed width** — no `min-width`/`max-width`, use `width` only.
- Use `flex-shrink:0` so the input never gets squashed in a flex row.
- Also use `flex-shrink:0` on the question/error text span — **do NOT use `flex:1`** on it. `flex:1` grabs all remaining space and pushes the input to the next line.
- Size the input so that the entire row (number + question text + input) fits on one line for the majority of sentences. Accepting that the 1–2 longest sentences may wrap is fine.
  - Target: `width:220px` for exercises where question texts are typically 18–35 chars.
  - Students type into the input — text scrolls within it if the answer is long, which is acceptable.

### Cross-out / "Choose the Correct Word" exercises
When the book shows a "Cross Out the Incorrect Word" exercise, implement the interaction as a cross-out (click the correct word, the wrong one gets crossed out automatically) — but **never say "cross out" or "the other will be crossed out" to the student**. That's the app's own behavior, not an instruction the student needs to follow. Students are choosing/clicking the correct word; the crossing-out is just the visual feedback.

**Title (h2):** `Choose the Correct Word` (in-lesson slide) / `HW X – Choose the Correct Word` (homework) — plain `<h2>` with no inline style, matching the lesson slide.

**Instruction (`<p class="instruction">`, bold):**
> Click the correct word.

Do not add anything about crossing out, the other option, or automatic behavior — keep it to that one short sentence. (Rule added 2026-08-21 — previously this used a longer title/instruction that narrated the crossing-out mechanic; corrected after user feedback.)

**Visual style — buttons, not span chips:**
```css
/* Default state */
border:2px solid #BDD4F0; border-radius:8px; padding:4px 14px;
font-size:1.05rem; font-weight:700; background:#fff; color:#1C2B3A;

/* Selected (picked, not yet checked) — NEUTRAL BLUE, never green */
background:#EAF1FB; color:#1A4A8C; border-color:#1A4A8C;

/* Faded (not chosen) */
background:#f5f5f5; color:#bbb; border-color:#e0e0e0;
text-decoration:line-through; opacity:0.6;

/* Confirmed correct (Check pressed, answer was right) — ONLY applied by Check, never by Pick */
background:#EEF7F0; color:#1A5C2A; border-color:#1A7A4A;

/* Confirmed wrong (Check pressed, answer was wrong) */
background:#FCEEED; color:#C4614A; border-color:#C4614A;
```

**Pick interaction (`hwXXPick`):**
1. Reset both buttons to default
2. Set clicked button → selected style (**neutral blue** — this is a choice, not a verdict)
3. Set other button → faded + line-through

**Check behaviour (`checkHWXX`) — smarter than the lesson slide:**
- **Correct answer**: turn the selected button **green** (`background:#EEF7F0; color:#1A5C2A; border-color:#1A7A4A`) and reset the other button to default. Count score. Green is applied HERE, at Check time — never earlier.
- **Wrong answer**: turn selected button **red** (`background:#FCEEED; color:#C4614A; border-color:#C4614A`). Reset the **other** button to **default** (neutral, clickable) so student can switch without resetting.
- **Unanswered**: leave as-is (don't touch).

**Why this matters:** green is this project's universal signal for "confirmed correct after Check" (see the top-level Colours rule and every other exercise type — matching, TFNG, word bank, MC). If Pick paints a green "confirmed correct" color the instant a student clicks, before they've pressed Check, the color is lying — the student hasn't been told they're right yet, they've just made a choice. A real violation of exactly this kind shipped in Business-EFE2 Lesson 1's `xoPick` (color applied on click, matching this doc's own outdated pre-2026-08-27 example) and was caught by the user, not by this file, because this file itself documented the wrong behavior until 2026-08-27(q). Selection must always use the same neutral color used everywhere else in this project for "picked, not yet verified" (`#1A4A8C` blue, matching `.mc-sel`/`.tfng-btn.sel`), and green/red are reserved exclusively for post-Check feedback, with zero exceptions for this exercise type or any other.

---

## Audio

- Only add audio if the `.mp3` file **actually exists** in the folder.
- Pattern: `<audio controls style="flex:1;width:100%;accent-color:#14607A;"><source src="X.mp3" type="audio/mpeg"></audio>` inside a gradient container.
- Do not add audio placeholders (`audio-placeholder` divs) to HW slides unless confirmed.

---

## Example Boxes

**The Example must ALWAYS be built from the exact same markup/classes as a real exercise item of that exercise type — never a generic quote-style callout.** The only allowed difference between the Example and a real item is color/accent (typically the orange `#C45020` accent) and that it's non-interactive/pre-solved. This is not optional and applies to every exercise type, not just some:

- **Cross-out exercises** (reference: `s11`/`hw56` in `Lesson_04_The_Office_Asking_Questions.html`): the Example reuses the exact same button style (`s11Btn`/`hw56Btn`) as the real word-choice buttons, just recolored — correct option green (`#EEF7F0`/`#1A7A4A`), wrong option struck-through gray — with `pointer-events:none` since it's not clickable.
- **Match exercises** (`qamBuild`): the Example reuses the same card style as a real question card (`background:#F4F8FA` pattern), just with the orange border/label, per `exampleQ`/`exampleA`.
- **Mark-the-correct-sentence exercises** (`s13`/similar): the Example reuses the same option-card style, correct one green with a ✓, wrong one struck through gray.
- **Word-order / sentence-building exercises** (`wo*` module): the Example is a real `.wo-row` — same `.wo-num` (labelled `Ex.` instead of a number), same `.wo-zone`, same `.wo-chip` markup — with the words already placed in the correct order and recolored orange (`border-color:#C45020`, chip text `#C45020`). **Never** a plain `<div><strong>Example:</strong> scrambled words → answer</div>` callout — that breaks visual symmetry with the real rows in the same column and was a real bug caught in Lesson 4 slide 4 (fixed 2026-08-20).
- **Fill-in-the-gap / word-bank exercises** (`wbBuild`, `gfBuild`): the Example is a real sentence row (`ex-row`/blank+pre/post text), not a floating quote box, with the blank already filled in and recolored.
- The ONLY case where a plain quote-style callout (the box shown below) is acceptable is for exercise types that have no natural "row" or "card" unit of their own — e.g. a single free-standing explanatory example that isn't one of a repeated list of items.

```html
<!-- Only for exercise types with no per-item row/card structure of their own -->
<div style="background:#FFF4EE; border-left:3px solid #C45020; border-radius:10px; padding:8px 14px; margin-bottom:12px; font-size:1.05rem;">
  <strong>Example:</strong> ...
</div>
```
- Font: always `1.05rem` minimum.
- Background: `#FFF4EE` (warm cream).
- Border: orange left border (`#C45020`).
- Label: `<strong>Example:</strong>` — always say "Example", never "a" or a number (row-based examples use `Ex.` in the item-number slot instead, to fit the row's own numbering column).

### Symmetry with column split
Because the Example lives inside the left column (per the odd-N column-split rule), it must read as one row among equals, not a visually distinct callout — this is what keeps the left column looking symmetrical with the right column instead of top-heavy with a mismatched block before the real items start.

---

## Sentence Colouring (Rewrite Exercises)

For exercises that switch between "from + Country" and nationality adjective:
- **"from [Country]"** → `color:#7B2FBE` (purple), bold
- **Nationality adjective** → `color:#C45020` (orange), bold
- Rest of sentence → `color:#1C2B3A` (black), normal weight

---

## Banner Standard

```html
<div class="banner" style="background:[COLOR];color:#fff;">EMOJI Category</div>
```
- Format: `emoji + space + Category name` only.
- **No slide numbers**, no pills, no extra info in the banner.
- For HW slides: `📝 Homework`
- For Key Language: `🔑 Key Language`
- For Listening: `🎧 Listening`

---

## Slide IDs & Navigation

- `slideIds` and `slideLabels` arrays **must stay in sync** (same length, same order).
- When deleting a slide: remove from HTML, `slideIds`, and `slideLabels`, and renumber HW `<h2>` titles.
- `goToId(id)` uses `slideIds.indexOf(id)`.

---

## HW Slide Numbering

When slides are added or deleted, **renumber all HW `<h2>` titles** sequentially:
`HW 1 – Title`, `HW 2 – Title`, etc.

---

## Notes Panel — Required on Every Lesson

Every lesson file must ship with a fully-featured notes panel — not just the "📝 Notes" toggle and textarea. This is a checklist, not optional polish.

### Required pieces
1. **`#notesBtn`** — fixed top-right toggle button (`📝 Notes` / `✕ Close`).
2. **`#pdfBtn`** — fixed top-right button, positioned immediately to the left of `#notesBtn` (`right:140px`, same `top:14px`), **always visible** (not tucked inside the collapsible toolbar — students must be able to export notes without first opening the panel). Label `📄 PDF Notes`, `onclick="downloadNotes()"`. Style matches `#notesBtn` (same background color family, `border-radius:22px`, hover state). Must be added to the print-hide rule alongside `#nav,#notesBtn,#notesPanel,#homeBtn` so it doesn't appear in the printed PDF itself.
3. **`#notesPanel`** with **`#notesToolbar`** containing, in this order:
   - Bold (`notesFormat('bold')`) and Underline (`notesFormat('underline')`) buttons
   - A thin divider (`<span style="width:1px;background:rgba(255,255,255,.2);...">`)
   - Four highlight-color dots (`notesHilite('#FFE600')`, `'#AAFFC3'`, `'#FFB3C1'`, `'#BFE0FF'`)
   - Another divider
   - **`🗑 Clear all`** button (`clearAllNotes()`) — erases every saved note for the lesson, with a `confirm()` guard
   - Do **not** duplicate `📄 Save as PDF` inside the toolbar — that lives only in the always-visible `#pdfBtn` (see #2).
4. **`#notesTA`** — the contenteditable notes area, per-slide persistence via `localStorage` keyed as `notes_l<N>_<slideIndex>` (e.g. `notes_l6_3`).
5. **`#notesTA [style*="background-color"]{color:#1a1a1a!important;}`** in the CSS — without this, highlighted text inherits the panel's white font color and becomes unreadable against the light highlight colors. This one-line rule is mandatory whenever `#notesTA` has `color:#fff` (or any light color) as its base.
6. **Slide-navigation function must call `loadNotes()` for the new slide.** Whatever function changes the active slide (`goTo(n)` / `goToSlide(n)`) must, after updating the current-slide index, reload `#notesTA` for the new index — e.g. `if(notesOpen) loadNotes();` (localStorage-keyed variant) or `loadNotes(current);` (in-memory `notesData` variant). If this call is missing, the notes textarea keeps showing the *previous* slide's content while the student is actually on a new slide; anything they type then gets saved under the new slide's key on top of the old slide's text, so notes appear to "bleed" and accumulate across slides. This was a real bug found in Lessons 3/4/6/7 (fixed 2026-08-07) — do not regress it in new lessons.
7. **`#notesTA` must sanitize paste.** Add a `paste` event listener on `#notesTA` that calls `e.preventDefault()` and inserts only `event.clipboardData.getData('text/plain')` via `document.execCommand('insertText', false, text)` — never let pasted HTML through as-is. Pasted content (from Word, a webpage, a dark-mode app, etc.) can carry its own inline `background-color`/`color` styles. Combined with rule #5's blanket `color:#1a1a1a!important` override, a pasted dark background ends up with forced dark text on top of it — i.e. black-on-black, invisible — and the same risk exists in reverse for any future rule that assumes a fixed base color. Stripping paste to plain text guarantees the only `background-color` spans that can ever exist in a note are the ones created by the app's own `notesHilite()` (the four known light colors), which rule #5 is designed for. This was a real bug — a parent's exported PDF showed an unreadable line from pasted text (fixed 2026-08-14). Reference implementation:
   ```js
   (function(){var t=document.getElementById('notesTA');if(t)t.addEventListener('paste',function(e){e.preventDefault();var text=(e.clipboardData||window.clipboardData).getData('text/plain');document.execCommand('insertText',false,text);});})();
   ```

8. **The notes panel must be draggable.** Add a `.notes-drag-handle` bar (`id="notesDragHandle"`) as the first child of `#notesPanel`, above `#notesToolbar` (grip icon `⠿⠿` + `DRAG TO MOVE` label, styled to match the panel's dark toolbar color). Wire a small IIFE that listens for `mousedown`/`touchstart` on the handle, tracks `mousemove`/`touchmove`, and on drag sets `panel.style.left/top` (clamped to the viewport), clears `right`/`bottom`, and sets `transform:'none'` (required to override the `.cover` slide's `left:50%;transform:translateX(-50%)` centering). Disable `panel.style.transition` during the drag so the panel doesn't lag behind the cursor, and restore it on release. Persist the last position to `localStorage` under `'<lesson's existing notes-storage key>:pos'` (e.g. `notes_l6_pos`, or `NOTES_KEY + ':pos'` for lessons using the `NOTES_KEY` object pattern) and re-apply it on page load. This is required in every lesson across all three courses (Business-EFE1, Business-EFE2, Business-HR) — added 2026-08-21. Reference implementation: any lesson file in Business-HR, or `Lesson_04_The_Office_Asking_Questions.html` (Business-EFE1).

### `downloadNotes()` — required behavior
- Calls `saveNotes()` first to flush the current slide's in-progress edits to `localStorage`.
- Loops over `slideIds`, reading `localStorage.getItem('notes_l<N>_'+idx)` for each index, skipping empty ones.
- If nothing was written, `alert('No notes to save yet!')` and stop.
- Otherwise builds a standalone printable HTML document (own `<style>`, one `.card` per slide with notes, `.card-header` = `Slide N — label`, `.card-body` = the saved note HTML), opens it in a new tab, and calls `window.print()` after a short delay.
- The exported page's own CSS **must also include** `.card-body [style*="background-color"]{color:#1a1a1a!important}` — the highlight-readability fix applies to the printed/PDF output too, not just the live panel.
- Include a link back to the lesson's GitHub Pages URL (`https://teacher-nanda.github.io/Business-EFE1/<filename>.html`) near the top of the exported page.

Use `Lesson_03_Business_Around_the_World.html`'s `downloadNotes()`/`clearAllNotes()` as the reference implementation — copy and adapt the lesson number and `localStorage` prefix, don't rewrite from scratch.

---

## No Book References

**Never cite the course book or practice book in any student-facing text.** Titles are titles — nothing else.

- **No unit numbers.** Never write "Unit 7," "Units 9–10," etc. anywhere a student sees it — not on `index.html` lesson cards, not in slide titles, not in banners.
- **No book/exercise numbering.** Never prefix a slide `<h2>` with a section number like `6.1`, `9.2`, `10.4`. A title is just its name: `Key Language: Questions with "Do"`, not `6.4 Key Language: Simple Questions with "Do."`
  - Exception: `HW 1 – Title`, `HW 2 – Title`, etc. — this is the lesson's own homework numbering (see "HW Slide Numbering" above), not a book citation, and stays as-is.
- Applies to `slideLabels` entries too (used for the dot-nav tooltips) — labels should read the same as the on-slide title, with no numbering prefix.
- This was a real correction (2026-08-17): `index.html` had "Unit X" pills on every lesson card, and several lessons had book-numbered titles (`6.1`, `6.2`…) baked into both the `<h2>` and `slideLabels`. Both were removed. Do not reintroduce either pattern in new lessons.
- **No meta/course framing either.** Never write "Welcome to Level 2," "Welcome to the course," "in this unit you will learn," or anything that talks *about* the book, the level, or the course structure. The student should only ever see the language content itself — never be reminded there's a book behind it.
- **Do not invent Warm-Up content.** A Warm-Up slide is only allowed when it is directly grounded in real material — e.g. a photo-discussion prompt that mirrors the book's own opening image (see `Lesson_01_Meeting_New_Colleagues.html`), or a genuine review bridge that quizzes students on phrases actually taught in the *immediately preceding* lesson (see `Lesson_02_Everyday_Work_Activities.html`'s "Formal or Informal?" slide). Never fabricate a generic trivia quiz with made-up sentences just to have an opening slide — this was a real correction (2026-08-17, EFE2 Lesson 1: a fabricated "Welcome to Level 2!" quiz was removed). If there's nothing genuine to warm up with (e.g. the very first lesson of a course, or a book unit that opens straight into Key Language), skip the Warm-Up slide entirely and go straight from Cover into the first real content slide — this is exactly what `Lesson_03_Business_Around_the_World.html` and `Lesson_04_The_Office_Asking_Questions.html` do.
- **Before building a new lesson, check the equivalent slides in already-built lessons for the same course** (e.g. Lessons 1–4) to confirm the pattern being followed is real precedent, not an assumption.

---

## Personal Names in Examples

**Never use the teacher's real name (Nanda) inside example sentences, sample answers, dialogues, or any other student-facing exercise content.** Always use a made-up name instead (e.g. Alex, Jordan, Maria, Tom).

- The one and only exception is the cover slide's teacher byline ("with teacher Nanda") — that's real course branding, identical across every lesson in all three courses, and stays as-is.
- This was a real correction (2026-08-31): Business-EFE2 Lesson 1 had "I'm Nanda" baked into a grammar example sentence and into two guided-speaking sample answers. Fixed by swapping in made-up names (Alex, Jordan). Rule added per explicit request: "remove my name from the lessons, not from the cover, from examples and sentences in the lesson... use made-up names. This should be a rule."
- When auditing or building any lesson, check for the teacher's real name in body content the same way you'd check for any other content violation — it is not limited to the one instance reported.

---

## Word-Order / Sentence-Building Exercises

When the book has a "put the words in the correct order" or "rewrite the sentence" exercise, implement it as **clickable word-order**, not free typing. Students click words in the box in order to build the sentence; there is no keyboard input, so nothing needs to be written down in class.

**Why:** typing full sentences from scratch is slow in a live lesson; clicking pre-supplied word chips into place is fast and still tests word order/grammar.

### Reference implementation
A single generic module (`woBuild` / `woRender` / `woAdd` / `woRemove` / `woCheck` / `woReset`) drives every word-order exercise in a lesson — copy it from `Lesson_04_The_Office_Asking_Questions.html` rather than writing bespoke per-exercise JS:

```js
var woState = {};
function woBuild(exId, leftId, rightId, items, resultId, exampleHtml, exampleFullWidthId){
  var n = items.length, isOdd = n % 2 !== 0, leftCount = isOdd ? Math.floor(n/2) : n/2;
  woState[exId] = { items:items, leftId:leftId, rightId:rightId, resultId:resultId,
    exampleHtml: exampleHtml||null, exampleInColumn: isOdd, leftCount: leftCount,
    bank: items.map(function(it){return it.words.slice();}),
    built: items.map(function(){return [];}), checked:false, ok:[] };
  if(!isOdd && exampleFullWidthId && exampleHtml){
    var fw=document.getElementById(exampleFullWidthId); if(fw) fw.innerHTML=exampleHtml;
  }
  woRender(exId);
}
function woRender(exId){ /* splits items into left.slice(0,leftCount) / right.slice(leftCount) per the
                             Columns — Example placement and split rule; renders one .wo-row per item
                             (a .wo-zone of built words above a .wo-bank of remaining words) into the
                             matching column; ODD N prepends exampleHtml to the left column's innerHTML */ }
function woAdd(exId,i,wi){ /* move word from bank[i] to built[i] */ }
function woRemove(exId,i,wi){ /* move word from built[i] back to bank[i] */ }
function woCheck(exId){ /* compares norm(built[i].join(' ')) to norm(item.ans); colors each .wo-zone green/red */ }
function woReset(exId){ /* restores original scrambled bank, clears built + colors */ }
```

- `items` = `[{ words: ["scrambled","word","tokens"], ans: "The correct sentence." }, ...]`. Word tokens already carry their sentence-position punctuation (e.g. `"open?"`, `"Are"`) so `built.join(' ')` reproduces the answer string exactly when in the right order.
- **Word-order exercises are two-column exercises and MUST follow the exact same "Columns — Example placement and split" rule as every other exercise type** — this is not optional and not exercise-type-specific. HTML uses `<div class="two-col"><div class="col-section" id="xx-wo-left"></div><div class="col-section" id="xx-wo-right"></div></div>`, never a single full-width container.
  - **ODD N** (e.g. N=5, N=7): the Example box is passed as `exampleHtml` and is rendered as the first block inside the LEFT column (`woRender` prepends it) — never as a separate full-width div above the grid. `leftCount = floor(N/2)` real items go left (below the example), `ceil(N/2)` go right. N=5 → left: Example+2, right: 3. N=7 → left: Example+3, right: 4.
  - **EVEN N**: pass `exampleFullWidthId` pointing at a dedicated `<div id="xx-example">` placed above the `.two-col` grid; the example is NOT counted in either column. `N/2` items left, `N/2` right.
- One `woBuild(...)` call per exercise slide (in-lesson or homework) — call it from that exercise's own `buildXX()` wrapper so `checkXX()`/`resetXX()` can stay as the `onclick` targets already used elsewhere (`checkXX(){ woCheck('xx'); }`).
- CSS classes: `.wo-row` (card), `.wo-num`, `.wo-zone` (dashed drop target, `.wo-correct`/`.wo-wrong` after Check), `.wo-bank`, `.wo-chip` (`font-size:1.05rem` — never smaller, per the Typography rule).
- On Check: color each `.wo-zone` green (correct order) or red (wrong order) — do not reveal the correct order for wrong items, consistent with the "Do NOT reveal the correct answer" rule under Check/Correction Behaviour.

---

## Reading Passage + Comprehension Questions

When a slide pairs a printed reading passage (a magazine/article-style card) with comprehension questions beside it, use this exact two-column layout — do not build a fresh version per lesson.

**Why:** two real bugs kept recurring in this shape of exercise before this rule existed: (1) the passage card stretched to match the taller questions column, leaving ugly empty white space inside it, and (2) either the whole slide needed to scroll together (losing sight of the passage while reading later questions) or the passage itself got a scrollbar it didn't need because its text already fit.

### Reference implementation
Copy this structure from `Business-EFE2/Lesson_01_Introductions.html`'s "Making Connections" slide (`s7`):

```html
<div style="display:grid;grid-template-columns:1fr 1.1fr;gap:20px;align-items:start;">
  <div style="background:#F4F0E4;border-radius:12px;padding:16px 18px;color:#2A2010;">
    <div style="font-size:1.05rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#7A2A5A;">[Category]</div>
    <div style="font-size:1.3rem;font-weight:900;margin-top:4px;">[Headline]</div>
    <div style="font-size:1.06rem;font-weight:700;margin-bottom:10px;font-style:italic;">[Subtitle]</div>
    <div style="font-size:1.06rem;line-height:1.85;">[Passage text — never below 1.05rem, line-height never below 1.8]</div>
  </div>
  <div style="max-height:390px;overflow-y:auto;padding-right:6px;">
    <div id="xx-example"></div>
    <div id="xx-qs"></div>
  </div>
</div>
<div class="hw-btns" style="margin-top:14px;">
  <button class="btn-check" onclick="checkXX()">✓ Check Answers</button>
  <button class="btn-reset" onclick="resetXX()">↺ Reset</button>
</div>
<div id="xx-result" style="margin-top:10px;font-weight:700;font-size:1.05rem;"></div>
```

```css
.mc-question{margin-bottom:20px;}
.mc-q-text{font-size:1.05rem;font-weight:700;color:#0A2010;margin-bottom:9px;line-height:1.5;}
.mc-opts{display:flex;flex-direction:row;gap:10px;flex-wrap:wrap;}
.mc-opt{background:#F4F8FA;border:2px solid #dde;border-radius:8px;padding:7px 14px;font-size:1.05rem;color:#1C2B3A;cursor:pointer;display:flex;align-items:center;gap:6px;transition:all .15s;flex:0 0 auto;line-height:1.4;}
```

- **The passage card never gets `max-height`/`overflow-y` of its own.** Its box must size to fit its own text exactly — no fixed height, no scrollbar, unless the passage itself is genuinely too long to fit the slide (rare; check before assuming).
- **`align-items:start` on the grid is mandatory.** Without it, the shorter column (almost always the passage) stretches to match the taller one (almost always the questions + buttons), creating dead white space inside the passage card.
- **Only the questions column scrolls**, via its own `max-height:390px;overflow-y:auto` — this is what lets the student scroll through questions while the passage stays fully visible and readable beside it at all times, satisfying "we need to see both text and questions together."
- **Check/Reset buttons and the result line live outside the scrolling column**, full-width below the grid — never inside the scrollable box, so they stay visible without needing to scroll to reach them.
- **Passage text**: `font-size` never below `1.05rem` (`1.06rem` is the house value used everywhere this pattern appears), `line-height` never below `1.8` (`1.85` is the house value) — a magazine-card passage reads noticeably worse than an `.ex-row` or `.dlg-bubble` at the same line-height because it's a longer, denser block of prose, so it needs more breathing room, not less.
- **`.mc-question`/`.mc-opt` spacing**: `.mc-question{margin-bottom:20px}` between separate questions, `.mc-q-text{margin-bottom:9px;line-height:1.5}` between a question and its answer pills, `.mc-opt{padding:7px 14px;line-height:1.4}` inside each pill. The original 10px/5px/4px values looked cramped once real multi-line questions were tested — always test this component with real (not placeholder) question text before shipping, since short lorem-ipsum-style text hides cramped spacing that real content reveals.

---

## Language

### Spelling — American English only
**All text in every slide must use American English spelling.** This is non-negotiable and applies to every edit, rewrite, or new section.

- When rewriting or restructuring existing content, **preserve the original spelling exactly** — do not alter words that were already correct.
- Never introduce British spellings (e.g. favourite → favorite, colour → color, travelling → traveling, organise → organize, etc.).
- After any edit that touches article or exercise text, mentally verify no British spellings were introduced.

---

*Last updated: 2026-08-24 (o) (Clarified the "no fabricated Warm-Up" rule's scope after adding a warm-up to Business-EFE2 Lesson 1 — the very first lesson of its course, where the existing rule says to skip Warm-Up entirely. On reflection, and confirmed with the user, the rule was written to ban fabricated *facts/trivia* and course-framing meta-talk (the deleted "Welcome to Level 2!" quiz), not to ban every possible opening activity — a warm-up that activates real-world knowledge the student already has, directly anticipating what the lesson is about to teach (not reviewing a prior lesson, since none exists), is a different and legitimate case. Built `s1b` for EFE2 Lesson 1: a "What Would You Say?" 4-question multiple-choice mini-game (realistic everyday scenarios, 2 plausible responses each, reusing the exact `mc-question`/`mc-opt` module and scoring pattern from `s1b` in `Lesson_04_The_Office_Asking_Questions.html`) followed by a purple "💬 Talk About It" open-discussion box with 2 speaking prompts — same visual structure as the EFE1 reference, banner `🔥 Warm-Up` (`#B8860B`). Inserted as a new slide ID (`s1b`) between the cover and the first real content slide, in both `slideIds` and `slideLabels`, without renumbering any existing slide — the same non-destructive insertion pattern used for EFE1 Lesson 4's warm-up. Verified via jsdom: slideIds/slideLabels stay in sync (18 entries each), the quiz renders and scores correctly, and `goTo()` navigation through the new slide and into the next one both work cleanly. Updated rule: "skip Warm-Up on a course's first lesson" is not absolute — a warm-up is fine there too if it's a genuine knowledge-activation/lead-in tied to that lesson's own upcoming content, not a review bridge (impossible, nothing precedes it) and not invented trivia.)*
*Last updated: 2026-08-31 (u) (Two more real bugs found after the user checked the book's own back-of-book Answers pages directly and caught HW1's layout. (1) **`wbBuild`'s odd-N column split never followed the Columns rule's odd-N example placement** — it always rendered the example in a separate full-width container (only correct for EVEN N) regardless of how many items there were, so HW1 (N=9, odd) showed the example full-width above an unbalanced 5/4 split instead of living inside the left column with a balanced 5/5 split (example+4 left, 5 right), the way `rwBuild` already does correctly for odd N. Root-caused and fixed in `wbBuild` itself: it now branches on `items.length % 2`, mirroring `rwBuild`'s exact pattern — even N keeps the existing full-width-example/equal-split behavior, odd N prepends the example as a real row inside the left column and splits `floor(N/2)` left / `ceil(N/2)` right. Verified via jsdom: HW1 now renders 5/5 with the example as the left column's first child. Audited every other split exercise in the file for the same bug: `qamBuild` (s4, hw2) uses a fundamentally different two-column shape (all N items appear in BOTH the question and answer columns, not split in half) so the odd/even split rule doesn't apply to it; `xoBuild` (s10 N=4, hw5 N=10) and `rwBuild` (s9 N=4, hw4 N=12) are all even-N and already correct; HW1's `wbBuild` was the only affected call site in this file. (2) **HW3's TFNG item 5 answer was wrong**: previously keyed `"N"` (Not Given) based on a 2026-08-24 reasoning pass that decided the reading passage was merely silent on education — but the book's own back-of-book Answers page states the correct answer is `"F"` (False). Corrected to match the book's printed key. New rule, reinforcing (t): **the book's own back-of-book Answers page is the single source of truth for every answer key in this project — it overrides any inference drawn from re-reading the passage/exercise text.** If an inferred answer and the book's printed key ever disagree, the book's key wins; go back and re-examine the passage to understand why, but do not substitute judgment for the printed key. Cross-checked the rest of Unit 1's HW/lesson exercises against the book's Unit 1 Answers pages (1.1–1.8): HW1, HW4, HW5, `s8` (reading comprehension), and `s9` (rewrite) all matched exactly; `s4`/`s6` (audio-based matching/listening) have no printed textual answer key at 1.2 in this book (audio script only) and were previously verified directly against the book's exercise page instead.)*
*Last updated: 2026-08-31 (t) (Full book-accuracy audit of every HW slide in Business-EFE2 Lesson 1, per explicit request after the user caught HW3's Example not matching the book. Rendered and viewed all 4 relevant Practice Book pages (12–15) fresh, transcribed every item + example, and diffed against the live code. HW1 (page 12), HW2 (page 13 top), HW4 (page 14), and HW5 (page 15) all matched the book exactly, word-for-word, item-for-item — no changes needed. HW3 (page 13 bottom) had two real bugs: (1) its TFNG Example was completely fabricated — code had `"Meeting new people is an essential skill for a business professional."` → `"T"`, while the book's actual example is `"The author says that meeting people is easy."` → Not Given (`"N"`); (2) item 2's wording said "your recent experience" (singular) where the book prints "your recent experiences" (plural). Both fixed directly in `hw3Items`/`buildHW3()`. Also audited and fixed line spacing across every stacked exercise-row container in the file — `.tfng-row` (`margin-bottom:10px→16px`), `.col-section` (`gap:10px→16px`, affects `s9`/`s10`/`hw1`/`hw4`/`hw5`'s two-column rows), `#s5-rows` (`gap:8px→16px`), `#s4-qs`/`#s4-as` and `#hw2-qs`/`#hw2-as` (matching-exercise columns, `gap:8px→14px`) — 8–10px between padded/bordered rows read as visually cramped, a pattern that had crept in across nearly every exercise type in this file, not just the one reported. New standing rule added under Typography ("Line spacing between exercise rows/items — never tighter than 14–16px"). Also strengthened the "Verifying against the book" rule itself into an explicit, mandatory checklist (see that section) after concluding the HW3 Example bug went undetected specifically because a correct-looking exercise's Example was never independently checked against a rendered page image — correct items created false confidence that an untouched Example was correct too, when in fact examples must be verified with the exact same rigor as every other item, every time a slide is built OR revisited.)*
*Last updated: 2026-08-31 (s) (Three real HW-slide bugs found and fixed after an explicit audit request. (1) **`wbBuild`'s struck-out "used" word was always rendered FIRST in the bank, regardless of where the book actually prints it** — this broke the "word-bank order must match the book's row-major print order, including the struck-out example word in its real printed position" rule from 2026-08-21(b) whenever the used word wasn't the book's first panel word. Found in Business-EFE2 Lesson 1's HW1 (book panel order: pleasure, see, ~~do~~, told, met, must, think, meet, introduce, Nice — "do" is 3rd, but the old code always showed it 1st). Fixed at the root: `wbBuild` now takes the full row-major `bankWords` list (used word included, in its real position) and a separate `usedWords` set that just marks which of those words render struck/disabled IN PLACE, never reordering. Updated both existing callers (`s5`, `hw1`) to pass the complete book-order array. (2) **HW1's 9 fill-in-the-gap items were a single full-width column**, unlike every other exercise type in this lesson, which violates the Columns rule for any exercise long enough to need one — added two-column support to `wbBuild` itself (`splitIds:{leftId,rightId}` param, `leftCount=Math.ceil(N/2)` split, matching the same convention `xoBuild` already uses), wired HW1 to split 5/4 across `#hw1-left`/`#hw1-right`. `s5` (4 items, fits on one screen without scrolling) was deliberately left as a single column — the two-column requirement is about long lists needing to fit/scroll sanely, not a blanket rule for every `wbBuild` exercise regardless of length. (3) **HW1's word bank scrolled out of view** once the exercise had enough rows to require scrolling — with no dedicated Reading+Questions-style fix existing yet for a *word bank*, added `position:sticky;top:0` to HW1's bank wrapper so it stays visible at the top of the scrolling `.content` area while the student scrolls through all 9 items, mirroring the same sticky-header technique already applied to Business-HR Lesson 2's word bank. New rule: whenever a `wbBuild` exercise is long enough that its rows might not all fit on one screen, it needs BOTH the two-column split AND a sticky word bank — a long single-column list with a bank that scrolls away is broken twice, not once.)*
*Last updated: 2026-08-31 (r) (New standard added: "Personal Names in Examples" — never use the teacher's real name (Nanda) inside example sentences, sample answers, or dialogues; always use a made-up name, with the sole exception of the cover slide's "with teacher Nanda" byline. Fixed in Business-EFE2 Lesson 1: a grammar example ("Hi, I don't think we've met. I'm Nanda...") and two guided-speaking sample answers used the real name — swapped in made-up names (Alex, Jordan). Also, in the same lesson: rebuilt the warm-up slide's layout (removed 4 scenario speak-cards, replaced with a two-column layout — 2 discussion questions on the left, a context photo on the right); fixed a capitalization mismatch between two options in a "Choose the Correct Word" item ("Do you enjoy" was lowercase "do" while its pair "Are you enjoying" was capitalized — both button-style options in a two-choice exercise must match in capitalization even when one wouldn't be capitalized as running prose, since each option is read as its own standalone label); fixed the same exercise's layout — a 4-item cross-out exercise was split into two narrow columns via `.two-col`, causing longer sentences to wrap awkwardly mid-phrase, corrected to a single full-width stacked column; and widened the guided-speaking slide's 4 speak-cards from a single stacked column into a 2-column grid.)*
*Last updated: 2026-08-27 (q) (Fixed a real, widespread "green on click" bug the user caught on Business-EFE2 Lesson 1 slide 10 ("Choose the Correct Word"): `xoPick` painted the clicked option green (`#EEF7F0`/`#1A5C2A`/`#1A7A4A`, this project's universal "confirmed correct" color) the instant a student selected an option, before Check was ever pressed — the student hadn't been told they were right yet, they'd just made a choice, but the color said otherwise. Root-caused to the Check/Correction Behaviour standard itself: the "Cross-out / Choose the Correct Word" section's own reference code and its "Correct answer: leave as-is (already green — no change needed)" instruction were teaching this exact bug, so every lesson that copied this pattern inherited it. Fixed at every level: (1) rewrote the standard's reference CSS/interaction spec so Pick always applies a neutral blue (`#EAF1FB`/`#1A4A8C`), matching the same "picked, not yet verified" blue used everywhere else in this project (`.mc-sel`, `.tfng-btn.sel`), and Check is now the only place green is ever applied; (2) fixed Business-EFE2 Lesson 1's shared `xoPick`/`xoCheck` functions (used by both `s10` and `hw5`) to match; (3) audited every other "Pick"-named exercise function across all 6 live Business-EFE1 lesson files for the same class of bug (a lesson learned from this project's repeated "check every other instance of the same mistake, not just the one reported" rule) and found and fixed 9 more real instances of the identical bug: `s7Pick`/`hw45Pick` (Lesson 3), `s11Pick`/`hw56Pick` (Lesson 4), `s7Pick`/`hw63Pick` (Lesson 5), `crossPick` (Lesson 6, shared across `s6`/`s14`/`hw1` via its `prefix` parameter), `s8Pick`/`hw3Pick` (Lesson 7) — all changed from green-on-select to blue-on-select. Their corresponding Check functions (`checkHW45`, `checkS11`, `checkHW56`, `checkHW63`, `checkS7`-L5, `checkCrossOut`, `checkHW3`, `checkS8`) previously relied on the correct answer's button "already being green" from Pick and did nothing on a correct match (`if(ok){ score++; }` with no color change) — fixed all 8 to actively paint the selected button green at Check time, matching the pattern Lesson 3's `checkS7` already used correctly (it was the one exception that didn't have this bug, having been written to reset-then-recolor both buttons from scratch on every Check). Business-EFE1 Lesson 2 was audited and found already clean — it doesn't use this cross-out pattern at all. Verified via syntax scan (`new Function()`) on all 5 touched Business-EFE1 files plus Business-EFE2 Lesson 1, and a fresh grep across every `Pick`-named function in all 6 Business-EFE1 lesson files confirming zero remaining instances of the bug pattern. New rule: when this project's own standards file's reference code contains the bug, every lesson that followed it faithfully is equally wrong — fixing the one reported instance is not enough, the standards file itself must be corrected first, then treated as the audit checklist for finding every other copy.)*
*Last updated: 2026-08-27 (p) (New standard added: "Reading Passage + Comprehension Questions" — codified the two-column layout built and refined for Business-EFE2 Lesson 1's "Making Connections" slide (`s7`) into a reusable rule, after three rounds of user feedback on the same slide: first "improve the line spacing... fix the text box to fit the text... use a scrolling box so we can see both text and questions together," then "if the text already fits in the box, no need for scrolling bar then, only for the question half," then "the line spacing in the questions... cannot be so close together." Final settled pattern: `align-items:start` on the two-column grid so the passage card sizes to its own content instead of stretching to match the taller questions column; the passage card itself never gets its own `max-height`/scrollbar; only the questions column gets `max-height:390px;overflow-y:auto`, keeping both halves visible together while only the longer one scrolls; Check/Reset buttons and the result line moved outside the scrollable column so they're always visible; passage text set to `line-height:1.85` (was `1.6`, too tight for a dense prose block); `.mc-question`/`.mc-q-text`/`.mc-opt` spacing widened (`margin-bottom` 10px→20px between questions, 5px→9px between question and its option pills, `.mc-opt` padding 4px 12px→7px 14px) since the original values only looked fine with short placeholder text and fell apart with real multi-line questions. Also lightly rewrote `s8`'s six comprehension questions for clearer, more natural phrasing while keeping every answer anchored to the actual article text. New rule: this exact layout (grid + `align-items:start` + one-sided scroll box + externalized action buttons + the specific `.mc-question` spacing values) must be reused verbatim for every future reading-passage-plus-questions slide in any of the three courses — do not rebuild it from scratch per lesson, and do not let the passage card get a scrollbar "just in case" if its actual text already fits without one.)*
*Last updated: 2026-08-27 (o) (Font-size audit of Business-EFE2 Lesson 1 against the Typography floor of 1.05rem for content text, per explicit request ("audit font sizes... we are not following standards"). Extracted every distinct `font-size` declaration in the file and classified each by context. Found and fixed three real violations, all in reading-passage text students must read to answer comprehension questions — the same category of mistake as every other Example/content-text violation this project has caught, just applied to prose instead of exercise rows: (1) the `s7`/"Making Connections" reading-article card had its section kicker at `.75rem`, its italic subtitle at `.85rem`, and its body paragraph at `.88rem` — all well under the floor; (2) the `hw3`/"Meeting and Greeting" reading-article card (a near-duplicate layout) had the identical three violations; (3) the speaking-exercise sample-answer text (`.speak-ex`, shown/hidden via the "👁 Sample answer" toggle) was `1.02rem`, just under the floor. Bumped the kicker labels to `1.05rem`, the subtitles/body text/sample-answer text to `1.06rem` (matching the standard's own `.ex-row` reference value), leaving headline sizes (`1.3rem`) untouched since they were already compliant. Explicitly checked and left alone as legitimate exceptions: `#notesToolbar button` (`.85rem`) and `#notesBtn`/`#pdfBtn`/`#nav button`/`#counter`/`.banner-pill` (all UI chrome, not content, already covered by the existing decorative-label exception), the `.speak-toggle` button label (`.98rem`, a functional button matching the existing sub-1.05rem convention already used by `.btn-check`/`.btn-reset` at `1rem` elsewhere in this same file), the "↳ [answer]" completion-line sub-labels (`.9rem`, an established secondary-annotation pattern used consistently across every exercise type in this file), and the generated PDF-popup's own internal CSS (`.card-header`/`.lesson-url` at `.88rem`) since that's a separate printed export document, not the interactive slide body the Typography floor targets. Verified via a `new Function()` syntax scan on the extracted script block (clean) and a follow-up grep confirming zero remaining sub-1.05rem content-text matches. New rule: when auditing font sizes, a flat "everything under 1.05rem is a violation" grep produces false positives — the check must distinguish content text a student reads/answers from UI chrome (nav, buttons, toggles, counters, secondary answer-reveal annotations) and from non-slide artifacts like the PDF export's own stylesheet, using the same "is this something the student reads as lesson material" test already established for Example Boxes.)*
*Last updated: 2026-08-24 (n) (Per explicit request — "I want the exact same, even the button positions" — moved Business-HR's `#notesBtn`/`#pdfBtn` from their old position (bottom-right, inside a `#lesson-btns` flex wrapper with `.action-btn` styling, opening the panel upward from the bottom corner) to match Business-EFE1/EFE2 exactly: two standalone fixed-position pill buttons top-right (`#pdfBtn{top:14px;right:140px}`, `#notesBtn{top:14px;right:22px}`), same padding/border-radius/backdrop-blur, same z-index, same hover behavior — kept Business-HR's own navy accent (`rgba(26,46,74)`) rather than switching hue. `#notesPanel`'s base position moved from `bottom:110px;right:18px` to `top:54px;right:22px` to open directly under the relocated buttons, matching EFE1/EFE2's layout. The `#lesson-btns`/`.action-btn` wrapper and its CSS were removed entirely across all 16 files (two on-disk HTML variants existed — single-line and multi-line — both handled). Updated the print-hide rule in all 16 files (two different pre-existing forms of that rule also existed) to hide `#notesBtn`/`#pdfBtn` by ID instead of the now-removed `#lesson-btns` wrapper. `.top-home-strip` (the full-width navy "🏠 Home" bar) was left untouched — it's a separate, unrelated nav element, not part of the notes system. Verified via syntax scan (all 16 clean) and a jsdom drag-simulation confirming both buttons exist, the panel opens/drags/closes-and-resets correctly with the new position. New rule: "put exactly the same, even X" from the user should be read literally and checked against every structural difference (container wrapper, positioning scheme, print-hide selectors) — not just the parts that were the topic of the most recent conversation turn.)*
*Last updated: 2026-08-24 (m) (Fixed the `downloadNotes()` "lesson link" bug across all 8 EFE1/EFE2 files with `downloadNotes()`: the exported PDF's link back to the lesson was a HARDCODED literal string (`https://teacher-nanda.github.io/Business-EFE1/Lesson_04_...html`) baked in at build time — safe only as long as the filename never changes, and a real trap for exactly the kind of lesson-renumbering/renaming this project does regularly (e.g. the 2026-08-24 Lesson 6→5/7→6/8→7 renumber earlier this file). The user caught a live example: a Business-HR Lesson 2 PDF export linked to `github.io/BusinessEFE2/Lesson_02_...html` — wrong repo entirely, left over from whenever that file's `downloadNotes()` was originally copy-pasted from an EFE2 template. Business-HR's own `downloadNotes()` was already correct because it uses a DYNAMIC pattern (`window.location.pathname.split('/').pop()`) instead of a literal filename — ported that same pattern to all 7 Business-EFE1 lessons and Business-EFE2 Lesson 1, keeping each file's correct hardcoded REPO name (`Business-EFE1`/`Business-EFE2`, which doesn't change per-lesson) but deriving the FILENAME portion live from the browser's actual URL at export time. Verified via jsdom by mocking `window.location` to a different filename than what's on disk and confirming the generated link followed the mocked URL, not the old hardcoded string — this proves the fix is robust against future renames, not just correct for today's filenames. New rule: any generated link/URL that embeds "this file's own name" must derive the filename dynamically (`window.location.pathname.split('/').pop()`), never hardcode it — a hardcoded self-referential filename silently goes stale on the next rename and won't be caught by any syntax or build check, only by a human noticing a wrong link days or weeks later.)*
*Last updated: 2026-08-24 (l) (Full re-audit of Business-EFE2 Lesson 1 against every rule in this file, after the user caught the TFNG listening exercise's Example rendered as a plain yellow "note-callout" text box with an instruction sentence baked inside it ("Mark each statement below as...") — exactly the banned pattern under Example Boxes. Root-caused and fixed at the shared-module level, then re-audited every other exercise in the same file for the same class of bug. Found and fixed real violations:
  1. **`tfngBuild`** (shared True/False/Not-Given module, used by `s6` and `hw3`) had NO example-row support at all — fixed by adding an `exampleQ`/`exampleAns` param that renders a real `.tfng-row` (same markup as live items), non-interactive, orange-accented, labeled `Ex.`, with the correct button pre-highlighted green. Removed the old free-floating note-callout from `s6`'s HTML entirely — the instruction line already covers what the student needs to do. Wired `s6`'s real book example ("Jared has met Sasha before." → True) and gave `hw3` a text-verifiable example drawn from its own on-slide reading passage (`hw3` has no audio dependency — the full article is printed on the slide, so the example and all 6 items were checked directly against that text, not guessed).
  2. **`hw3` content-accuracy bug**: item 5 ("The author suggests talking about your education.") was keyed `ans:"F"` but the reading passage never mentions education at all — corrected to `"N"` (Not Given). Rule: False requires the text to actively contradict the statement; a topic the text is simply silent on is Not Given, not False.
  3. **`wbBuild`** (shared word-bank module, reference implementation, used by `s5`/`hw1`) dumped the Example's raw HTML string directly into its container with zero styling — no card, no border, no background, worse than even the quote-callout fallback. Fixed to wrap it in the same `.ex-row` markup as real rows (orange border-left, `Ex.` label) and recolored the highlighted answer word from green to the standard orange `#C45020` Example accent in both call sites.
  4. **`s8`'s reading-MC Example** (`Making Connections`) was a plain gray quote box showing only the correct answer struck through — rebuilt as a real `.mc-question`/`.mc-opt` block with all 3 of the book's actual options ("Networking" / "Sharing" / "Dividing"), correct one green with a ✓, matching the book's checkbox-style example exactly (verified against the rendered course book page).
  5. **`rwBuild`** (shared rewrite-the-sentence module, used by `s9` N=4 and `hw4` N=12, both EVEN) always pinned the Example inside the left column regardless of N's parity — violating the Columns rule, which requires EVEN-N examples to be full-width above the grid with an exactly-equal split. Added an `exampleFullWidthId` param + odd/even branching (mirroring `woBuild`'s existing pattern), added the missing `<div id="s9-example">`/`<div id="hw4-example">` containers, and verified via jsdom that both now split exactly 2/2 and 6/6 with the example rendered separately above.
  6. **`s9`/`hw5` Cross-out slides** still used the old banned title/instruction wording ("Cross Out the Incorrect Words" / "Cross out the incorrect words in each sentence, then say the sentences out loud. Click the correct word — the incorrect one will be crossed out automatically.") predating the 2026-08-21(a) rule — corrected to "Choose the Correct Word" / "Click the correct word." in both the HTML and `slideLabels`. Their Example boxes (hand-built, reusing the real `xoBtn` style) were already compliant and left as-is.
  Verified every fix via `node --check`-equivalent syntax scan plus a full jsdom page-load + build-function smoke test (zero runtime errors, correct child counts per column, correct example markup per exercise type). New rule: "the example must look exactly like a real, solved item — never a differently-styled callout, and never with instructions written inside it" is the single most-repeated Example Boxes violation in this project; when auditing one exercise for this bug, check literally every other exercise in the same file for the same shape of mistake, not just the exercise type that was reported.)*
*Last updated: 2026-08-24 (k) (Re-audited every matching exercise for the 2026-08-21(d) rule — "the static Example row must show its '↳ [answer]' completion line just like real matched items do once checked" — after the user caught a violation in Business-EFE2 Lesson 1 slide 3. Found and fixed the bug at its root: Business-EFE2 Lesson 1 uses a *shared, parameterized* matching module (`qamBuild`/`qamRender`, reused by both slide 3's "Introductions Practice" and HW2) whose example-rendering block never appended the `st.exampleA` completion line at all — fixed once in `qamRender`, which fixes both call sites (`buildS4` for slide 3, `buildHW2`). Following up, audited Business-EFE1 for the same class of bug and found three more real violations in Lesson 7 (Jobs & Choosing a Career) that predate the 2026-08-21(d) rule and were missed by that pass: `s5` (9.1 Guess the Job — example "I care for patients in a hospital, but I'm not a doctor." was missing "↳ nurse"), `hw1` (10.1 Match the Sentences — missing "↳ I like animals."), and `hw5` (9.2 Vocabulary matching — missing "↳ A long-term, salaried position"); all three already had the correct answer sitting in the crossed-out right-column example chip, just never echoed into the left-column Example box. Lessons 4 and 5 were re-checked and are already compliant. New rule: when a bug is reported in one lesson, check whether the underlying render function is a *shared* module reused across multiple exercises in that file (fix once, fixes all call sites) versus a bespoke per-exercise copy-paste (must be checked and fixed individually in every file/exercise it was copied into) — this bug turned out to be both: a shared-module miss in EFE2 L1, and a copy-paste miss in EFE1 L7.)*
*Last updated: 2026-08-24 (j) (Aligned Business-HR's notes-panel font, background, and box dimensions to match Business-EFE1/EFE2, per explicit request. Business-HR's notes panel is no longer white (that was a short-lived (f)/whitening attempt this same day) — it's now dark navy `rgba(26,46,74,.92)` across `#notesPanel`/`.notes-drag-handle`/`.notes-toolbar`/`#notesTA`, one consistent accent for all 16 lessons (unlike EFE1/EFE2 which use a unique accent per lesson — Business-HR doesn't have per-lesson theme colors elsewhere in its design, so a single navy tied to its existing `--navy` brand color was used instead of inventing 16 new hues). Box sizing now matches exactly: `#notesPanel{width:360px}`, `#notesTA{min-height:220px;max-height:260px}`. Font size reverted from the earlier `.85rem` back to `1rem` to match EFE1/EFE2, superseding that earlier request. Business-HR's own class names (`.notes-toolbar`, `.notes-tbtn`, `.notes-actions`, `.notes-clear-btn`) and its already-correct drag/zoom-compensation JS were left untouched — only CSS values changed, consistent with the (f)/(h) pattern of reskinning being a color/size change, not a mechanics change. Rule: color-scheme requests for this notes panel have gone back and forth multiple times this session — always treat the MOST RECENT explicit instruction as authoritative and check the changelog before assuming a settled state, since "same style" has been interpreted three different ways across (f), (h), and now (j).)*
*Last updated: 2026-08-24 (i) (Reverted (h)'s white notes background for Business-EFE1/EFE2 only, per explicit user pushback — "I hate the formatting... please go back to the previous dark formatting." Business-EFE1's 7 lessons and Business-EFE2 Lesson 1 are back to each lesson's own dark, glassmorphic accent color (recovered exact original RGB values from git history: L1 `rgba(10,40,54)`, L2 `rgba(5,30,10)`, L3 `rgba(30,10,3)`, L4 `rgba(10,20,32)`, L5 `rgba(20,10,3)`, L6 `rgba(10,20,10)`, L7 `rgba(20,15,5)`, EFE2-L1 `rgba(10,26,20)`), white text, `backdrop-filter:blur`. Business-HR's notes panel stays white/light per the user's separate, still-standing request — the two courses are intentionally different here now. Also fixed a real regression discovered while reverting: the (h) whitening script's `#notesTA\{[^}]*\}` regex wasn't anchored against the `.cover`-scoped override selector `#notesPanel.cover #notesTA{...}`, so it also matched and replaced that shorter override (originally just the two `min-height`/`max-height` calc lines) with the full generic block — restored to the correct minimal override in all 8 files. Rule: when writing a regex to target one CSS selector for a bulk find/replace, explicitly check for and exclude any *scoped/compound* selector that contains the target selector's ID/class as a substring (e.g. `#notesPanel.cover #notesTA` contains `#notesTA`) — a plain regex will silently over-match and corrupt the compound rule.)*
*Last updated: 2026-08-24 (h) (Notes-panel visual style clarified and standardized: the user's earlier "match EFE1/EFE2 style" request meant the *draggability mechanics*, not a dark color scheme — the dark navy/glassmorphic reskin from (f) was reverted. The notes writing area (`#notesTA`, plus its toolbar/`.notes-drag-handle` chrome) is now **white background with dark text** across all three courses — Business-HR (16 files), Business-EFE1 (7 files), and Business-EFE2 (Lesson 1) — instead of each lesson's own dark accent color (EFE1/EFE2 previously varied per lesson, e.g. navy, brown, green, per the lesson's theme color; Business-HR was briefly dark navy under (f)). Font size in `#notesTA` standardized to `1rem` everywhere (Business-HR was `14px`, now matches EFE1/EFE2's existing `1rem`). The `#notesBtn` toggle pill (the small "📝 Notes" chip in the corner) keeps its per-lesson accent color — only the open panel's writing surface went white. Rule: "match X's style" from the user should be interpreted narrowly around what they're actually praising (here: dragging, not color) — when in doubt after a visual change, confirm rather than assume the color scheme was part of the ask. Also: a plain white notes background is deliberately friendlier to the "PDF Notes" print export (per the (e) print-color-adjust fix) since there's no colored background to risk stripping during print.)*
*Last updated: 2026-08-24 (g) (Found and fixed the actual remaining cause of Business-HR's erratic notes-panel dragging, after the user reported it was still broken post-(f): the (d) zoom fix divided `clientX`/`clientY` by the zoom factor but left `panel.getBoundingClientRect()` values and `window.innerWidth`/`innerHeight` un-divided, silently mixing "real/post-zoom viewport pixels" with "CSS/pre-zoom pixels" in the same subtraction/comparison — `getBoundingClientRect()` always returns real rendered coordinates, while `style.left`/`offsetWidth`/`offsetHeight` live in the pre-zoom CSS space, so combining them without converting both to the same space produces a systematically wrong offset that compounds every `mousemove` and either drifts or launches the panel off-screen. Rewrote the drag math in all 16 Business-HR files to convert every quantity into one consistent space (CSS/pre-zoom, matching `style.left`/`offsetWidth`) before any arithmetic: `rect.left/Z` and `clientX/Z` in `onDown`/`onMove`, `window.innerWidth/Z` in `clampAndApply`'s bounds, and the saved position in `onUp` now stored pre-divided so `__notesPosRestore` doesn't need special-casing. Verified via jsdom that a simulated multi-step drag now clamps exactly at the computed max bound instead of overshooting. New rule: when converting between two coordinate spaces (e.g. zoomed vs unzoomed, or any transform-scaled context), audit every value on both sides of every arithmetic operation — a fix that only converts some of the operands is worse than no fix, since it still passes a superficial "does it move at all" check while remaining wrong under sustained dragging.)*
*Last updated: 2026-08-24 (f) (Ported Business-EFE1/EFE2's notes-panel visual style to all 16 Business-HR lessons, on request, after confirming Business-HR's drag JS was already correctly fixed by the (b)/(c)/(d) passes above — only the CSS chrome (`#notesPanel`, `.notes-drag-handle`, `.notes-toolbar`, `.notes-tbtn`, `#notesTA`, `.notes-actions`, `.notes-clear-btn`) was reskinned from Business-HR's light/bordered card look to the dark, glassmorphic, floating-pill look EFE1/EFE2 use — `rgba(15,28,46,.92)` background (kept in Business-HR's own navy hue rather than EFE1's literal color, for brand consistency), `backdrop-filter:blur`, borderless rounded panel, translucent drag-handle bar. Selectors/IDs and all JS wiring were left untouched — this was a pure visual reskin, not a mechanics change, since Business-HR's drag/zoom-compensation/restore-on-open logic already matched the fixed EFE1 pattern. Verified via `node --check`-equivalent syntax scan on all 16 files plus a jsdom drag simulation confirming the panel still opens, drags, and clamps correctly with the zoom-compensated math intact.)*
*Last updated: 2026-08-24 (e) (Fixed the "PDF Notes" export rendering with white/blank card headers: `downloadNotes()`'s generated print window only applied `-webkit-print-color-adjust:exact` to `body`, not universally — browsers default to stripping background colors when printing/saving as PDF to save ink, so `.card-header{background:#1A4A8C;color:#fff}` lost its dark-blue background during print while keeping its white text, leaving invisible white-on-white text. Fixed in all 8 files that have `downloadNotes()` (7 Business-EFE1 lessons + Business-EFE2 Lesson 1) by adding a universal `*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;color-adjust:exact!important;}` rule to the generated PDF window's stylesheet, applied unconditionally (not just inside `@media print`) since the popup window exists only to be printed. Rule: any generated print/PDF popup window's stylesheet needs the color-adjust override applied broadly (`*` selector, `!important`), not just on `body` — a colored header/background anywhere in the document is otherwise silently stripped by the browser's print engine, and this is easy to miss since it only shows up in the actual PDF output, not in the on-screen editor.)*
*Last updated: 2026-08-24 (d) (Root-caused why the draggable notes panel behaved erratically in Business-HR specifically but never in Business-EFE1/EFE2: every Business-HR lesson sets `body{...zoom:1.4;...}` (EFE1/EFE2 don't use CSS `zoom` at all), and CSS `zoom` on an ancestor is a well-known source of coordinate-space mismatches between `MouseEvent.clientX/clientY` and `getBoundingClientRect()`/`style.left` for `position:fixed` descendants — the drag math was combining values from two different scales, causing the panel to accelerate towards an edge and disappear during an active drag, not just on reopen. Fixed across all 16 Business-HR files by reading the actual computed `zoom` value at drag time (`getComputedStyle(document.body).zoom`) and dividing the raw `clientX`/`clientY` by it before using them in the offset/move math, in both `onDown` and `onMove`. This could not be visually verified in the build sandbox (no real browser/display available there — puppeteer's bundled Chromium can't be downloaded without internet access), so it needs to be confirmed by the user after deploying. New rule: before styling any lesson's `body` with a non-1 CSS `zoom` value, be aware it will affect the coordinate math of any `position:fixed` draggable/interactive element on that page — either compensate explicitly in the JS (as done here) or avoid non-standard `zoom` scaling in favor of `transform:scale()` on a wrapping content container that excludes fixed UI chrome like the notes panel.)*
*Last updated: 2026-08-24 (c) (Found and fixed a second real draggable-notes-panel bug, this time in the position-restore logic itself, across all 24 lesson files that have it (16 Business-HR + 7 Business-EFE1 + 1 Business-EFE2): the saved drag position was being re-applied via `clampAndApply()` at page-load time, while the panel is still closed/hidden — at that moment `panel.offsetWidth`/`offsetHeight` are 0 (Business-HR, which uses `display:none` when closed) or otherwise not the real open size, so the clamp bounds are wrong and a position saved from a wider window (or dragged near an edge) can render almost entirely off-screen the next time the panel opens, i.e. the notes box appears to "disappear." Fixed by no longer restoring the saved position at load time — instead the drag IIFE exposes `window.__notesPosRestore()`, and `toggleNotes()` calls it only at the moment the panel actually opens (`notesOpen`/`.open` class true), when the panel has its real rendered dimensions, so the clamp math is always correct for the current viewport. Also tightened the window-resize re-clamp handler to only fire while the panel is open, for the same reason. New rule: any saved UI position (drag position, scroll position, etc.) must only be read back and clamped once the element is actually visible/laid out with real dimensions — never while `display:none` or before it's been added to the open/visible state — verify with an actual jsdom simulation of open-then-check-position, not just a syntax check.)*
*Last updated: 2026-08-24 (b) (Found and fixed a real bug in all 16 Business-HR lessons: the draggable-notes-panel IIFE was a plain `(function(){...})();` placed in a `<script>` block that runs BEFORE `#notesPanel`'s HTML appears in the document (the panel markup was placed after the script tag), so `getElementById('notesPanel')`/`getElementById('notesDragHandle')` always returned null and the whole feature silently no-opped — the CSS and markup were correct, only the wiring was broken, so it looked "already done" in every earlier audit that just grepped for the presence of the drag-handle CSS/markup instead of confirming it actually initialized. Fixed by wrapping the IIFE in `window.addEventListener('DOMContentLoaded', function(){...});` in all 16 files, verified via jsdom that the panel now actually moves on a simulated drag. New rule: when auditing a script-driven feature across lessons, grepping for the presence of code is not sufficient — confirm the code actually runs against the DOM order it's rendered in, ideally with a script-based simulation, not just static text search.)*
*Last updated: 2026-08-24 (Renumbered Business-EFE1 lessons: "Exchanging Details" is now Lesson 5, "Skills & Experience" Lesson 6, "Jobs & Choosing a Career" Lesson 7 — closes the gap that had index.html jumping from Lesson 4 straight to Lesson 6. While rebuilding Lesson 5, re-audited it against the course book and found the exact "solved order" matching bug this file already warns about, undetected until now because these exercises predate the standard: `s10`/`hw65` (7.8/7.5 matching) rendered their right columns in raw data order instead of an `answerOrder` array — fixed with explicit order arrays and `exampleAfter`, same pattern as Lesson 4. Also fixed cross-out title/instruction naming on `s7`/`hw63` (still said "Select the Correct Option" / narrated the crossing-out mechanic — predates the 2026-08-21(a) rule), removed literal `placeholder="?"`/`placeholder="…"` attributes from several inputs (predates the 2026-08-21(c) placeholder-ban expansion), and added real Check/Reset scoring to the two listening-order exercises (`s6`/`hw62`) using the book's own answer key, since audio isn't available yet. Added a warm-up review slide to Lesson 4 (`s1b`, review of Lessons 1-3) to match the warm-up slide Lesson 5 already had — every lesson from 4 onward should open with one. Confirms the standing rule: reused/older lesson files must be re-audited against the current standards file whenever touched, not assumed compliant just because they predate a specific bug report.)*
*Last updated: 2026-08-21 (d) (Matching exercises: added rule that the static Example row must show its "↳ [answer]" completion line just like real matched items do once checked — fixed Lesson 4's `renderS12`/`renderHW55` which left the Example looking unmatched. Re-audited Lesson 4's HW slides against the book: HW1 was wrongly built as a click-to-reorder word puzzle when the book's own exercise is a statement-plus-write-in-the-question format (matching HW2's style) — rebuilt as typed-answer rows; HW2's per-column images were stretched into one distorted banner instead of one icon per row — cropped the source collage into individual per-row icons matching the book's actual layout; HW8/`hw58` was single-column and had its word-bank panel placed after the exercise rows, violating the existing bank-before-rows rule from 2026-08-19 — rebuilt to two columns with the bank moved above the rows, and fixed the same bank-after-rows violation in slide 14 (`s14`) in the same file. Audit turned up the same bank-after-rows violation in Business-EFE1 Lesson 3 (`hw32`) that has not yet been fixed — flag for follow-up.)*
*2026-08-21 (c) (Two more real bugs found and fixed in Lesson 4's matching exercises: the example's answer chip was hardcoded to always render first in the right column, when the book actually prints it further down (3rd of 6, 3rd of 9) — fixed `renderS12`/`renderHW55` to insert the example's answer at its correct position inside the ordered loop, not pinned above it; rule expanded to state explicitly that the example's answer position must also be verified against the book, it is not assumed to be first just because the example question is. Also expanded the placeholder ban: clickable blanks (`<span>`-based, used instead of a real `<input>`) defaulting to a filler character like "?" are a placeholder in effect even without the `placeholder=` attribute — fixed real violations in Lesson 4 (`s14`, `hw58`), the shared `wbBuild` reference implementation, and Business-HR Lesson 2.)*
*2026-08-21 (b) (Word-bank order rule added: the bank's word order must match the book's row-major print order exactly, including repeated words printed twice and the struck-out example word in its real printed position — not just "include the used word," its POSITION in the sequence matters too. Found and fixed real violations in Business-EFE1 Lesson 4's `s14` and `hw58` (both bespoke, pre-`wbBuild` implementations) where the bank order didn't match the book and the example's already-used word ("How") was missing from the bank entirely. This is the same class of repeated-order-mistake as matching exercises — extended the "audit every instance in the file, not just the one reported" requirement to word-bank exercises too.)*
*2026-08-21 (a) (Cross-out exercises renamed to "Choose the Correct Word" with a one-line instruction — never narrate the crossing-out mechanic to the student; matching-order rule strengthened to explicitly cover bespoke/hand-rolled renderers, not just `qamBuild`, after finding real violations in Lesson 4 slide 12 and HW4/hw55; found and fixed two more column-symmetry violations in the same file — slide 13 (odd N=5 using the even-N split formula) and HW6/hw57 (even N=8 with the Example wrongly placed inside the left column instead of full-width above) — a full re-audit of every two-column exercise in a lesson is required whenever any one of them is found to be wrong, not just the slide reported; added draggable notes panel requirement for every lesson in all three courses)*
*2026-08-20 (Example Boxes rule rewritten: the Example must always reuse the exact same row/card markup and classes as a real item of that exercise type, only recolored — never a generic quote-style callout — this applies to every exercise type including word-order; fixed a real violation in Lesson 4 slide 4 where the word-order Example broke column symmetry)*
*2026-08-19: Matching exercises must use explicit `answerOrder` to follow the book's printed right-column order, never "solved" order; word-bank fill-gap exercises must be click-based with the bank positioned before the sentence rows, reference module `wbBuild`; short/key-word titles must not drop info — it must reappear in the instruction line; added mandatory page-image + answer-key verification workflow since PDF text extraction misses image-based exercises*
*2026-08-17: Word-Order exercises now explicitly follow the odd/even column-split rule like every other exercise type, with example placement spec for both cases; added explicit "never override title position" rule and a permanent, non-negotiable ban on `placeholder=` attributes on any exercise input*
*2026-08-17 (earlier): No Book References rule expanded — no meta/course framing, no fabricated Warm-Up quizzes, check precedent in existing lessons before building; no unit numbers, no book-section numbering in titles/labels; Word-Order/Sentence-Building Exercises pattern added — clickable word chips, not free typing, reference implementation in Lesson 4*
*2026-08-14: Notes Panel — added mandatory paste-sanitizer to prevent invisible pasted text; always-visible #pdfBtn pattern, mandatory loadNotes()-on-navigation to prevent notes bleeding across slides, highlight-readability CSS fix, downloadNotes() spec*
