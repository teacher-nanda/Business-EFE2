# -*- coding: utf-8 -*-
"""If a worked example (.ex-given) sits directly above a .fixed-two-col, move it INTO the grid as item 1
and re-split all rows top-to-bottom then left-to-right (left = ceil(n/2))."""
import math
from bs4 import BeautifulSoup, Tag

def balance_slide(html):
    if 'ex-given' not in html or 'fixed-two-col' not in html:
        return html
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    for ex in soup.select('.ex-given'):
        gp = ex.parent.parent if ex.parent is not None else None
        if gp is not None and 'fixed-two-col' in (gp.get('class') or []):
            grid = gp
        else:
            grid = ex.find_next_sibling()
        while grid is not None and not isinstance(grid, Tag):
            grid = grid.find_next_sibling()
        if grid is not None and 'fixed-two-col' not in (grid.get('class') or []):
            sub = grid.find_all(recursive=False)
            if len(sub) == 1 and 'fixed-two-col' in (sub[0].get('class') or []):
                grid = sub[0]
        if grid is None or 'fixed-two-col' not in (grid.get('class') or []):
            continue
        cols = [c for c in grid.find_all(recursive=False) if c.name == 'div']
        if len(cols) != 2:
            continue
        rows = []
        for c in cols:
            rows += [ch for ch in c.find_all(recursive=False) if ch is not ex]
        n = len(rows)
        for c in cols:
            c.clear()
        # RULE: example + even rows -> example alone on top, rows split evenly in 2 columns
        #       example + odd rows  -> example joins column 1 (total is even, split evenly)
        if n % 2 == 0:
            if ex.parent is not None and ex.parent is not grid.parent:
                ex.extract(); grid.insert_before(ex)
            ex['style'] = (ex.get('style') or '') + ';max-width:calc(50% - 20px);box-sizing:border-box;'
            left = n // 2
            items = rows
        else:
            if ex.parent is not None: ex.extract()
            items = [ex] + rows
            left = (n + 1) // 2
        for i, it in enumerate(items):
            cols[0 if i < left else 1].append(it.extract() if it.parent else it)
        changed = True
    return str(soup) if changed else html

def balance_all(slides):
    return [(a, b, balance_slide(c)) for a, b, c in slides]

COLS = ('fixed-two-col','fixed-three-col','fixed-four-col','two-col-ex','two-col','match-wrap','classify-cols','sound-grid','verb-grid','two-profiles','art-two','quiz-two')
def _is_item(t):
    if not isinstance(t, Tag) or t.name != 'div' or 'ex-row' not in (t.get('class') or []): return False
    first = t.find(True)
    return first is not None and first.name == 'span' and any(c in (first.get('class') or []) for c in ('circ-num','example-badge'))

def columnize_slide(html, skip_ids=()):
    if 'ex-row' not in html: return html
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    for parent in soup.find_all(True):
        if any(set(a.get('class') or []) & set(COLS) for a in [parent] + list(parent.parents) if isinstance(a, Tag)):
            continue
        kids = [k for k in parent.children if isinstance(k, Tag)]
        i = 0
        while i < len(kids):
            if _is_item(kids[i]):
                j = i
                while j + 1 < len(kids) and _is_item(kids[j+1]): j += 1
                run = kids[i:j+1]
                if len(run) >= 4:
                    n = len(run); left = math.ceil(n/2)
                    g = soup.new_tag('div', **{'class': 'fixed-two-col', 'style': 'gap:0 40px;'})
                    c1 = soup.new_tag('div'); c2 = soup.new_tag('div')
                    g.append(c1); g.append(c2)
                    run[0].insert_before(g)
                    for k, it in enumerate(run):
                        (c1 if k < left else c2).append(it.extract())
                    changed = True
                i = j + 1
            else:
                i += 1
    return str(soup) if changed else html

def columnize_all(slides):
    return [(a, b, columnize_slide(c)) for a, b, c in slides]

def twocol_to_fixed(html):
    if 'two-col' not in html: return html
    soup = BeautifulSoup(html, 'html.parser'); changed = False
    for el in soup.select('div.two-col'):
        kids = [k for k in el.children if isinstance(k, Tag)]
        if len(kids) < 2: continue
        n = len(kids); left = math.ceil(n/2)
        c1 = soup.new_tag('div'); c2 = soup.new_tag('div')
        for k, it in enumerate(kids):
            (c1 if k < left else c2).append(it.extract())
        el.clear(); el.append(c1); el.append(c2)
        el['class'] = ['fixed-two-col']; el['style'] = (el.get('style') or '') + ';gap:0 40px;'
        changed = True
    return str(soup) if changed else html

def fix_all(slides):
    return [(a, b, balance_slide(columnize_slide(twocol_to_fixed(c)))) for a, b, c in slides]
