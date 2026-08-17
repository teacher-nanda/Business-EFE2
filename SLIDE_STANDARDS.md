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

### Cross-out / "Select the Correct Option" exercises
When the book shows a "Cross Out the Incorrect Word" exercise, implement it as **Select the Correct Option** — same style as the in-lesson exercise (e.g. slide 6 / s7).

**Title (h2):** `HW X – Select the Correct Option` — plain `<h2>` with no inline style, matching the lesson slide.

**Instruction (`<p class="instruction">`, bold):**
> Click the correct word that fits the sentence — the other will be crossed out automatically.

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

```html
<div style="background:#FFF4EE; border-left:3px solid #C45020; border-radius:10px; padding:8px 14px; margin-bottom:12px; font-size:1.05rem;">
  <strong>Example:</strong> ...
</div>
```
- Font: always `1.05rem` minimum.
- Background: `#FFF4EE` (warm cream).
- Border: orange left border (`#C45020`).
- Label: `<strong>Example:</strong>` — always say "Example", never "a" or a number.

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
function woBuild(exId, containerId, items, resultId){
  woState[exId] = { items:items, containerId:containerId, resultId:resultId,
    bank: items.map(function(it){return it.words.slice();}),
    built: items.map(function(){return [];}), checked:false, ok:[] };
  woRender(exId);
}
function woRender(exId){ /* renders one .wo-row per item: a .wo-zone (built words, click to remove)
                             above a .wo-bank (remaining words, click to add) */ }
function woAdd(exId,i,wi){ /* move word from bank[i] to built[i] */ }
function woRemove(exId,i,wi){ /* move word from built[i] back to bank[i] */ }
function woCheck(exId){ /* compares norm(built[i].join(' ')) to norm(item.ans); colors each .wo-zone green/red */ }
function woReset(exId){ /* restores original scrambled bank, clears built + colors */ }
```

- `items` = `[{ words: ["scrambled","word","tokens"], ans: "The correct sentence." }, ...]`. Word tokens already carry their sentence-position punctuation (e.g. `"open?"`, `"Are"`) so `built.join(' ')` reproduces the answer string exactly when in the right order.
- One `woBuild(...)` call per exercise slide (in-lesson or homework) — call it from that exercise's own `buildXX()` wrapper so `checkXX()`/`resetXX()` can stay as the `onclick` targets already used elsewhere (`checkXX(){ woCheck('xx'); }`).
- CSS classes: `.wo-row` (card), `.wo-num`, `.wo-zone` (dashed drop target, `.wo-correct`/`.wo-wrong` after Check), `.wo-bank`, `.wo-chip` (`font-size:1.05rem` — never smaller, per the Typography rule).
- Include a static, non-interactive **Example** box above the exercise (same pattern as other exercise types) showing the scrambled words, an arrow, and the correct sentence — so students see the mechanic before attempting item 1.
- On Check: color each `.wo-zone` green (correct order) or red (wrong order) — do not reveal the correct order for wrong items, consistent with the "Do NOT reveal the correct answer" rule under Check/Correction Behaviour.

---

## Language

### Spelling — American English only
**All text in every slide must use American English spelling.** This is non-negotiable and applies to every edit, rewrite, or new section.

- When rewriting or restructuring existing content, **preserve the original spelling exactly** — do not alter words that were already correct.
- Never introduce British spellings (e.g. favourite → favorite, colour → color, travelling → traveling, organise → organize, etc.).
- After any edit that touches article or exercise text, mentally verify no British spellings were introduced.

---

*Last updated: 2026-08-17 (No Book References rule expanded — no meta/course framing, no fabricated Warm-Up quizzes, check precedent in existing lessons before building; no unit numbers, no book-section numbering in titles/labels; Word-Order/Sentence-Building Exercises pattern added — clickable word chips, not free typing, reference implementation in Lesson 4)*
*2026-08-14: Notes Panel — added mandatory paste-sanitizer to prevent invisible pasted text; always-visible #pdfBtn pattern, mandatory loadNotes()-on-navigation to prevent notes bleeding across slides, highlight-readability CSS fix, downloadNotes() spec*
