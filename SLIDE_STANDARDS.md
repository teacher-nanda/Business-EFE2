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

/* Selected (correct word chosen) */
background:#EEF7F0; color:#1A5C2A; border-color:#1A7A4A;

/* Faded (not chosen) */
background:#f5f5f5; color:#bbb; border-color:#e0e0e0;
text-decoration:line-through; opacity:0.6;
```

**Pick interaction (`hwXXPick`):**
1. Reset both buttons to default
2. Set clicked button → selected style (green)
3. Set other button → faded + line-through

**Check behaviour (`checkHWXX`) — smarter than the lesson slide:**
- **Correct answer**: leave as-is (already green — no change needed). Count score.
- **Wrong answer**: turn selected button **red** (`background:#FCEEED; color:#C4614A; border-color:#C4614A`). Reset the **other** button to **default** (neutral, clickable) so student can switch without resetting.
- **Unanswered**: leave as-is (don't touch).
- Do NOT reset all items to neutral before checking — only modify wrong ones.

**Why this matters:** student sees exactly which items are wrong (red) and can click the correct word immediately to fix them, without needing to hit Reset first.

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

## Language

### Spelling — American English only
**All text in every slide must use American English spelling.** This is non-negotiable and applies to every edit, rewrite, or new section.

- When rewriting or restructuring existing content, **preserve the original spelling exactly** — do not alter words that were already correct.
- Never introduce British spellings (e.g. favourite → favorite, colour → color, travelling → traveling, organise → organize, etc.).
- After any edit that touches article or exercise text, mentally verify no British spellings were introduced.

---

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
