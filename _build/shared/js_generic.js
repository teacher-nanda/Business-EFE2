/* ===================== NOTES ===================== */

/* -- DRAGGABLE NOTES PANEL -------------------- */
(function(){
  var panel = document.getElementById('notesPanel');
  if (!panel) return;
  var handle = document.getElementById('notesDragHandle') || panel.querySelector('.notes-header') || document.getElementById('notesToolbar');
  if (!handle) return;
  handle.style.touchAction = 'none';
  var dragging = false, startX, startY, startLeft, startTop;
  function onDown(e){
    if (e.target.closest('button')) return;
    dragging = true;
    panel.classList.add('dragging');
    panel.classList.remove('cover');
    var rect = panel.getBoundingClientRect();
    panel.style.left = rect.left + 'px';
    panel.style.top = rect.top + 'px';
    panel.style.right = 'auto';
    panel.style.bottom = 'auto';
    panel.style.transform = 'none';
    startX = e.clientX; startY = e.clientY;
    startLeft = rect.left; startTop = rect.top;
    e.preventDefault();
    document.addEventListener('pointermove', onMove);
    document.addEventListener('pointerup', onUp);
  }
  function onMove(e){
    if (!dragging) return;
    var dx = e.clientX - startX, dy = e.clientY - startY;
    var newLeft = startLeft + dx, newTop = startTop + dy;
    var maxLeft = window.innerWidth - panel.offsetWidth - 4;
    var maxTop = window.innerHeight - 40;
    newLeft = Math.max(4, Math.min(newLeft, maxLeft));
    newTop = Math.max(4, Math.min(newTop, maxTop));
    panel.style.left = newLeft + 'px';
    panel.style.top = newTop + 'px';
  }
  function onUp(){
    dragging = false;
    panel.classList.remove('dragging');
    document.removeEventListener('pointermove', onMove);
    document.removeEventListener('pointerup', onUp);
  }
  handle.addEventListener('pointerdown', onDown);
})();

function toggleNotes(){
  notesOpen = !notesOpen;
  var panel = document.getElementById('notesPanel');
  panel.classList.toggle('open', notesOpen);
  if (current === 0) panel.classList.toggle('cover', notesOpen);
  document.getElementById('notesBtn').textContent = notesOpen ? '✕ Close' : '📝 Notes';
  /* reset position on close */
  if (!notesOpen) { panel.style.left=''; panel.style.top=''; panel.style.right=''; panel.style.bottom=''; panel.style.transform=''; }
}
function notesFormat(cmd){
  document.getElementById('notesTA').focus();
  document.execCommand(cmd, false, null);
  saveNotes();
}
function notesHilite(color){
  var ta = document.getElementById('notesTA');
  ta.focus();
  var sel = window.getSelection();
  if (!sel || !sel.rangeCount || sel.getRangeAt(0).collapsed) return;
  document.execCommand('styleWithCSS', false, true);
  if (color !== 'remove'){
    var cur = document.queryCommandValue('backColor');
    var hex = color.replace('#','');
    var r = parseInt(hex.substr(0,2),16), g = parseInt(hex.substr(2,2),16), b = parseInt(hex.substr(4,2),16);
    if (cur === 'rgb('+r+', '+g+', '+b+')' || cur === 'rgb('+r+','+g+','+b+')') { color = 'remove'; }
  }
  if (color === 'remove'){
    document.execCommand('hiliteColor', false, 'transparent');
    Array.from(ta.querySelectorAll('[style*="background"]')).forEach(function(el){
      var c = el.style.backgroundColor;
      if (c === 'transparent' || c === 'rgba(0, 0, 0, 0)' || c === ''){
        var p = el.parentNode;
        if (!p) return;
        while (el.firstChild) p.insertBefore(el.firstChild, el);
        p.removeChild(el);
      }
    });
  } else {
    document.execCommand('hiliteColor', false, color);
  }
  saveNotes();
}
function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; }
function loadNotes(idx){ document.getElementById('notesTA').innerHTML = notesData[idx] || ''; }
function clearAllNotes(){
  if(!confirm('Delete all notes for this lesson? This cannot be undone.')) return;
  Object.keys(notesData).forEach(function(k){ delete notesData[k]; });
  var ta = document.getElementById('notesTA');
  if (ta) ta.innerHTML = '';
  try{ if (typeof notesStoreKey !== 'undefined') localStorage.removeItem(notesStoreKey); }catch(e){}
}
function savePDF(){
  saveNotes();
  var hasNotes = Object.keys(notesData).some(function(k){ return notesData[k] && notesData[k].replace(/<[^>]*>/g,'').trim(); });
  if (!hasNotes){ alert('No notes to save yet!'); return; }
  var win = window.open('', '_blank');
  var cards = '';
  slideIds.forEach(function(sid, idx){
    var note = notesData[idx] || '';
    if (!note.replace(/<[^>]*>/g,'').trim()) return;
    cards += '<div class="card"><div class="card-header">Slide '+(idx+1)+' &mdash; '+slideLabels[idx]+'</div><div class="card-body">'+note+'</div></div>';
  });
  win.document.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Notes – AEF4 4B</title><style>'+
    'body{font-family:"Segoe UI",system-ui,sans-serif;max-width:800px;margin:0 auto;padding:32px 24px;color:#1C2B3A}'+
    '.header{border-bottom:2px solid #0B1929;padding-bottom:8px;margin-bottom:4px}'+
    '.header h1{font-size:1.4rem;margin:0 0 6px;color:#0B1929}.header .lesson-link{font-size:1.05rem;color:#1C2B3A}.header a{color:#1B6E96}'+
    '.date{font-size:.85rem;color:#666;margin:10px 0 24px}'+
    '.card{border:1px solid #DDD;border-radius:8px;margin-bottom:16px;overflow:hidden;}'+
    '.card-header{background:#0B1929;color:#fff;padding:8px 14px;font-weight:700;font-size:.88rem;break-after:avoid-page;page-break-after:avoid;}'+
    '.card-body{orphans:3;widows:3;}'+
    '.card-body{padding:12px 16px;font-size:.95rem;line-height:1.7}'+
    'mark{background:#FFE066;color:#1a1a1a;padding:0 2px}'+
    '[style*="background-color"]{color:#1a1a1a!important}'+
    '.card-body,.card-body *{color:#1a1a1a!important}'+
    '*{print-color-adjust:exact;-webkit-print-color-adjust:exact}'+
    '@media print{@page{margin:1.5cm}body{padding:0}button{display:none}}'+
  '</style></head><body>'+
  '<div class="header"><h1>AEF4 4B – A Risky Business</h1><div class="lesson-link">📝 Here you can see our Notes from Class.</div><div class="lesson-link" style="margin-top:4px;">You can also access <a href="https://teacher-nanda.github.io/AEF-Courses/AEF4-4B/index.html" target="_blank">this link</a> to review the lesson material and do your optional Homework activities.</div></div>'+
  '<p class="date">'+new Date().toLocaleDateString('en-US',{weekday:'long',year:'numeric',month:'long',day:'numeric'})+'</p>'+
  cards+'</body></html>');
  win.document.close();
  setTimeout(function(){ win.print(); }, 400);
}

/* ===================== GENERIC: TYPED GAP-FILL ===================== */
function norm(s){ return (s||'').toString().trim().toLowerCase().replace(/[.,!?;:'’]+$/,'').replace(/\s+/g,' '); }
function checkSlide(sid){
  var box = document.getElementById(sid);
  var inputs = box.querySelectorAll('.ans-input');
  inputs.forEach(function(inp){
    var val = norm(inp.value);
    if (!val) { inp.classList.remove('correct','wrong'); inp.classList.add('empty-warn'); return; }
    inp.classList.remove('empty-warn');
    var ans = norm(inp.dataset.ans);
    var alts = (inp.dataset.alt || '').split('|').map(norm).filter(Boolean);
    if (val === ans || alts.indexOf(val) > -1) { inp.classList.add('correct'); inp.classList.remove('wrong'); }
    else { inp.classList.add('wrong'); inp.classList.remove('correct'); }
  });
}
function resetSlide(sid){
  var box = document.getElementById(sid);
  box.querySelectorAll('.ans-input').forEach(function(inp){ inp.value=''; inp.classList.remove('correct','wrong','empty-warn'); });
}

/* ===================== GENERIC: CIRCLE MC ===================== */
function circPick(btn){
  var group = btn.dataset.group;
  var box = btn.closest('.slide');
  var wasPicked = btn.classList.contains('picked');
  box.querySelectorAll('.circ-opt[data-group="'+group+'"]').forEach(function(b){ b.classList.remove('picked'); });
  if (!wasPicked) btn.classList.add('picked');
}
function circScope(sid){
  var el = document.getElementById(sid);
  if (!el) return null;
  if (el.querySelector('.circ-opt[data-group]')) return el;   /* scope to this exercise */
  return el.closest('.slide') || el;                           /* legacy fallback */
}
function checkCircSlide(sid){
  var box = circScope(sid);
  var groups = {};
  box.querySelectorAll('.circ-opt[data-group][data-correct]').forEach(function(b){ groups[b.dataset.group] = groups[b.dataset.group] || []; groups[b.dataset.group].push(b); });
  Object.keys(groups).forEach(function(g){
    var picked = groups[g].find(function(b){ return b.classList.contains('picked'); });
    groups[g].forEach(function(b){ b.classList.remove('correct','wrong'); });
    if (!picked) return;
    if (picked.dataset.correct === picked.textContent.trim()) picked.classList.add('correct');
    else picked.classList.add('wrong');
  });
}
function resetCircSlide(sid){
  var box = circScope(sid);
  box.querySelectorAll('.circ-opt[data-group]').forEach(function(b){ b.classList.remove('picked','correct','wrong'); });
}

/* ===================== GENERIC: COLOUR-PAIR MATCH ===================== */
var matchColours = ['c0','c1','c2','c3','c4','c5','c6','c7'];
var matchPending = {};
function matchPick(el){
  var wrap = el.closest('.match-wrap');
  var wid = wrap.id;
  if (el._linked){
    var partner = el._linked;
    matchColours.forEach(function(c){ el.classList.remove(c); partner.classList.remove(c); });
    el.classList.remove('correctpair','wrongpair','picking');
    partner.classList.remove('correctpair','wrongpair','picking');
    el._linked = null; partner._linked = null;
    delete el.dataset.colour; delete partner.dataset.colour;
    if (matchPending[wid] === el) matchPending[wid] = null;
    return;
  }
  var pending = matchPending[wid];
  if (pending && pending !== el && pending.dataset.side !== el.dataset.side){
    var used = Array.from(wrap.querySelectorAll('.match-item')).map(function(x){ return x.dataset.colour; }).filter(Boolean);
    var next = matchColours.find(function(c){ return used.indexOf(c) === -1; }) || matchColours[Math.floor(used.length/2) % matchColours.length];
    pending.classList.remove('picking');
    pending.classList.add(next); el.classList.add(next);
    pending.dataset.colour = next; el.dataset.colour = next;
    pending._linked = el; el._linked = pending;
    matchPending[wid] = null;
    return;
  }
  if (pending === el){
    pending.classList.remove('picking');
    matchPending[wid] = null;
    return;
  }
  if (pending) pending.classList.remove('picking');
  el.classList.add('picking');
  matchPending[wid] = el;
}
function checkMatchSlide(id){
  var wrap = document.getElementById(id);
  wrap.querySelectorAll('.match-item[data-side="left"]').forEach(function(l){
    l.classList.remove('correctpair','wrongpair');
    if (l._linked) l._linked.classList.remove('correctpair','wrongpair');
    if (!l._linked) return;
    var r = l._linked;
    if (r.dataset.pair === l.dataset.pair){ l.classList.add('correctpair'); r.classList.add('correctpair'); }
    else { l.classList.add('wrongpair'); r.classList.add('wrongpair'); }
  });
}
function resetMatchSlide(id){
  var wrap = document.getElementById(id);
  wrap.querySelectorAll('.match-item').forEach(function(el){
    matchColours.forEach(function(c){ el.classList.remove(c); });
    el.classList.remove('correctpair','wrongpair','picking');
    el._linked = null;
    delete el.dataset.colour;
  });
  matchPending[id] = null;
}

/* ===================== GENERIC: CLASSIFY / SORT ===================== */
var classifySelected = {};
function classifyPick(chip){
  if (chip.classList.contains('used')) return;
  var bank = chip.closest('[id$="-bank"]') || chip.parentElement;
  bank.querySelectorAll('.classify-chip').forEach(function(c){ c.classList.remove('selected'); });
  chip.classList.add('selected');
  classifySelected[bank.id] = chip;
}
function classifyTarget(col){
  var colsEl = col.closest('[id$="-cols"]');
  var bankId = colsEl ? colsEl.id.replace(/-cols$/, '-bank') : null;
  var chip = bankId ? classifySelected[bankId] : null;
  if (!chip) return;
  var tag = document.createElement('span');
  tag.className = 'placed';
  tag.textContent = chip.textContent;
  tag.dataset.ans = chip.dataset.ans;
  tag.dataset.chipRef = '1';
  tag.onclick = function(e){ e.stopPropagation(); tag.remove(); chip.classList.remove('used'); };
  col.appendChild(tag);
  chip.classList.add('used'); chip.classList.remove('selected');
  delete classifySelected[bankId];
}
function checkClassifySlide(prefix){
  var cols = document.getElementById(prefix+'-cols');
  cols.querySelectorAll('.classify-col').forEach(function(col){
    col.querySelectorAll('.placed').forEach(function(tag){
      tag.classList.remove('correct','wrong');
      if (tag.dataset.ans === col.dataset.target) tag.classList.add('correct');
      else tag.classList.add('wrong');
    });
  });
}
function resetClassifySlide(prefix){
  var bank = document.getElementById(prefix+'-bank');
  var cols = document.getElementById(prefix+'-cols');
  cols.querySelectorAll('.placed').forEach(function(tag){ tag.remove(); });
  bank.querySelectorAll('.classify-chip').forEach(function(c){ c.classList.remove('used','selected'); });
  classifySelected = {};
}

/* ===================== GENERIC: WORD BANK FILL ===================== */
var wbSelected = {};
function wbPick(tile){
  if (tile.classList.contains('used')) return;
  var bank = tile.parentElement;
  bank.querySelectorAll('.wb-tile').forEach(function(t){ t.classList.remove('selected'); });
  tile.classList.add('selected');
  wbSelected[closestSlideId(tile)] = tile;
}
function closestSlideId(el){ return el.closest('.slide').id; }
function wbPlace(blank){
  var sid = closestSlideId(blank);
  if (blank.classList.contains('filled')) {
    var tile = blank._tileRef;
    if (tile) tile.classList.remove('used');
    blank.textContent = '______';
    blank.classList.remove('filled','correct','wrong');
    blank._tileRef = null;
    return;
  }
  var tile = wbSelected[sid];
  if (!tile) return;
  blank.textContent = tile.dataset.val;
  blank.classList.add('filled');
  blank._tileRef = tile;
  tile.classList.add('used'); tile.classList.remove('selected');
  delete wbSelected[sid];
}
function checkWbSlide(sid){
  var box = document.getElementById(sid);
  box.querySelectorAll('.wb-blank').forEach(function(b){
    b.classList.remove('correct','wrong');
    if (!b.classList.contains('filled')) return;
    if (norm(b.textContent) === norm(b.dataset.ans)) b.classList.add('correct');
    else b.classList.add('wrong');
  });
}
function resetWbSlide(sid){
  var box = document.getElementById(sid);
  var slideEl = box.closest('.slide') || box;
  box.querySelectorAll('.wb-blank').forEach(function(b){ b.textContent='______'; b.classList.remove('filled','correct','wrong'); b._tileRef=null; });
  slideEl.querySelectorAll('.wb-tile').forEach(function(t){ t.classList.remove('used','selected'); });
  wbSelected = {};
}

/* ===================== GENERIC: TICK / CHECKBOX ===================== */
function toggleTick(el){
  el.classList.toggle('picked');
}
function checkTickSlide(sid, correctVals){
  var box = document.getElementById(sid);
  box.querySelectorAll('.tick-item').forEach(function(item){
    var val = item.dataset.val;
    var isCorrect = correctVals.indexOf(val) > -1;
    item.classList.remove('correct','wrong','missed');
    if (item.classList.contains('picked') && isCorrect) item.classList.add('correct');
    else if (item.classList.contains('picked') && !isCorrect) item.classList.add('wrong');
    else if (!item.classList.contains('picked') && isCorrect) item.classList.add('missed');
  });
}
function resetTickSlide(sid){
  var box = document.getElementById(sid);
  box.querySelectorAll('.tick-item').forEach(function(item){ item.classList.remove('picked','correct','wrong','missed'); });
}

/* ===================== SUGGESTED ANSWER / ANSWER KEY TOGGLE ===================== */
function toggleSuggested(id){
  var box = document.getElementById(id);
  box.classList.toggle('show');
}

/* ===================== SHARED NO-REPEAT SHUFFLE BAG ===================== */
var shuffleBags = {}, shuffleLast = {};
function shuffleArray(arr){
  var a = arr.slice();
  for (var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; }
  return a;
}
function nextNoRepeat(key, size){
  if (!shuffleBags[key] || shuffleBags[key].length === 0){
    var idxs = []; for (var k=0;k<size;k++) idxs.push(k);
    var bag = shuffleArray(idxs);
    if (size > 1 && shuffleLast[key] !== undefined && bag[bag.length-1] === shuffleLast[key]){
      var swapWith = Math.floor(Math.random()*(bag.length-1));
      var tmp = bag[bag.length-1]; bag[bag.length-1] = bag[swapWith]; bag[swapWith] = tmp;
    }
    shuffleBags[key] = bag;
  }
  var n = shuffleBags[key].pop();
  shuffleLast[key] = n;
  return n;
}
