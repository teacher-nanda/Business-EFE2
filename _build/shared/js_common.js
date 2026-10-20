/* ===================== PRINT LESSON ===================== */
function printAll(){
  saveNotes();
  var injected = [];
  slides.forEach(function(slide, i){
    if (i === 0){
      var linkEl = document.createElement('div');
      linkEl.className = 'lesson-link-print';
      linkEl.innerHTML = '<span class="lp-title">__LESSON_NAME__</span>' +
        '<span class="lp-sub">📝 Here you can see our Notes from Class.</span>' +
        '<span class="lp-sub" style="margin-top:6px;">You can also access <a href="__URL__" target="_blank">this link</a> to review the lesson material and do your optional Homework activities.</span>';
      slide.insertBefore(linkEl, slide.firstChild);
      injected.push(linkEl);
    }
    var n = notesData[i] || '';
    if (n.replace(/<[^>]*>/g,'').trim()){
      var notesEl = document.createElement('div');
      notesEl.className = 'slide-notes-print';
      notesEl.innerHTML = '<div class="slide-notes-print-label">📝 Teacher Notes</div>' + n;
      slide.appendChild(notesEl);
      injected.push(notesEl);
    }
  });
  document.body.classList.add('print-all');
  window.print();
  setTimeout(function(){
    document.body.classList.remove('print-all');
    injected.forEach(function(el){ el.parentNode && el.parentNode.removeChild(el); });
  }, 1500);
}

/* ===================== UNSAVED-NOTES WARNING + PROGRESS BAR ===================== */
(function(){
  var notesUnsaved = false;
  document.addEventListener('input', function(e){ if (e.target && e.target.id === 'notesTA') notesUnsaved = true; });
  document.addEventListener('click', function(e){
    var t = e.target && e.target.closest ? e.target.closest('#dlNotesBtn') : null;
    if (t) setTimeout(function(){ notesUnsaved = false; }, 300);
  });
  window.addEventListener('beforeunload', function(e){
    if (notesUnsaved) { e.preventDefault(); e.returnValue = ''; return ''; }
  });
  var bar = document.getElementById('progBar'); var all = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  function upd(){ var i = all.findIndex(function(x){ return x.classList.contains('active'); }); if (i < 0) return; bar.style.width = ((i+1)/all.length*100) + '%'; }
  new MutationObserver(upd).observe(document.getElementById('deck'), {attributes:true, subtree:true, attributeFilter:['class']});
  upd();
})();

/* init */
document.getElementById('counter').textContent = '1/' + slides.length;
document.getElementById('prevBtn').disabled = true;
loadNotes(0);


/* ===================== SAVE NOTES AS PDF (student-friendly cover) ===================== */
function savePDF(){
  saveNotes();
  var hasNotes = Object.keys(notesData).some(function(k){ return notesData[k] && notesData[k].replace(/<[^>]*>/g,'').trim(); });
  if (!hasNotes){ alert('No notes to save yet!'); return; }
  var LESSON = '__URL__', HW = LESSON + '#homework';
  var win = window.open('', '_blank');
  var cards = '';
  slideIds.forEach(function(sid, idx){
    var note = notesData[idx] || '';
    if (!note.replace(/<[^>]*>/g,'').trim()) return;
    cards += '<div class="card"><div class="card-header">Slide '+(idx+1)+' &mdash; '+slideLabels[idx]+'</div><div class="card-body">'+note+'</div></div>';
  });
  var css =
    'body{font-family:"DM Sans","Segoe UI",system-ui,sans-serif;max-width:820px;margin:0 auto;padding:0 0 32px;color:#1C2B3A;background:#fff}'+
    '.hero{background:linear-gradient(135deg,#2B1B5E 0%,#5A2E8C 55%,#FF6B5E 130%);color:#fff;border-radius:0 0 28px 28px;padding:34px 36px 30px;position:relative;overflow:hidden}'+
    '.hero:after{content:"";position:absolute;right:-40px;top:-40px;width:200px;height:200px;border-radius:50%;background:rgba(255,255,255,.08)}'+
    '.hero .kicker{font-size:.85rem;letter-spacing:.22em;text-transform:uppercase;color:#FFD84D;font-weight:800;margin:0 0 6px}'+
    '.hero h1{font-family:"DM Serif Display",Georgia,serif;font-size:2.3rem;line-height:1.1;margin:0 0 6px;font-weight:600}'+
    '.hero .sub{font-size:1.1rem;opacity:.92;margin:0}'+
    '.hero .date{display:inline-block;margin-top:14px;background:rgba(255,255,255,.16);border-radius:999px;padding:4px 14px;font-size:.9rem}'+
    '.how{margin:26px 28px 8px;background:#FFF8E1;border:3px solid #FFD84D;border-radius:22px;padding:20px 24px}'+
    '.how h2{font-family:"DM Serif Display",Georgia,serif;font-size:1.45rem;margin:0 0 14px;color:#2B1B5E}'+
    '.step{display:flex;gap:14px;align-items:flex-start;margin:0 0 14px}'+
    '.step .n{flex:none;width:34px;height:34px;border-radius:50%;background:#2B1B5E;color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:1.1rem}'+
    '.step p{margin:0;font-size:1.08rem;line-height:1.55}'+
    '.btns{display:flex;gap:14px;flex-wrap:wrap;margin:6px 0 6px 48px}'+
    '.bigbtn{display:inline-block;text-decoration:none;color:#fff!important;font-weight:800;font-size:1.2rem;padding:13px 26px;border-radius:999px;border:3px solid #2B1B5E;box-shadow:0 5px 0 #2B1B5E}'+
    '.bigbtn.lesson{background:#1F9D6B}.bigbtn.hw{background:#FF6B5E}'+
    '.link-note{margin:6px 0 0 48px;font-size:.88rem;color:#5b5b6b;word-break:break-all}'+
    '.tip{margin-top:12px;font-size:.95rem;color:#5b5b6b}'+
    '.notes-title{font-family:"DM Serif Display",Georgia,serif;font-size:1.5rem;color:#2B1B5E;margin:26px 28px 12px}'+
    '.card{border:1px solid #DDD;border-radius:12px;margin:0 28px 16px;overflow:hidden}'+
    '.card-header{background:#2B1B5E;color:#fff;padding:8px 14px;font-weight:700;font-size:.92rem;break-after:avoid-page;page-break-after:avoid}'+
    '.card-body{padding:12px 16px;font-size:1rem;line-height:1.7;orphans:3;widows:3}'+
    'mark{background:#FFE066;color:#1a1a1a;padding:0 2px}'+
    '[style*="background-color"]{color:#1a1a1a!important}'+
    '.card-body,.card-body *{color:#1a1a1a!important}'+
    '*{print-color-adjust:exact;-webkit-print-color-adjust:exact}'+
    '@media print{@page{margin:1.2cm}body{padding:0}.hero,.how{break-inside:avoid}}';
  var today = new Date().toLocaleDateString('en-US',{weekday:'long',year:'numeric',month:'long',day:'numeric'});
  var html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Notes – '+document.title+'</title>'+
    '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;700;800&display=swap" rel="stylesheet">'+
    '<style>'+css+'</style></head><body>'+
    '<div class="hero"><p class="kicker">Conversational English with teacher Nanda</p>'+
      '<h1>'+document.title.replace(' — ',' · ')+'</h1>'+
      '<p class="sub">📝 Your notes from class</p><span class="date">'+today+'</span></div>'+
    '<div class="how"><h2>👋 How to use this PDF</h2>'+
      '<div class="step"><div class="n">1</div><p><b>Read your notes</b> below. These are the notes we made together in class.</p></div>'+
      '<div class="step"><div class="n">2</div><p><b>Click &ldquo;Open the Lesson&rdquo;</b> to see the lesson content from class and do homework activities.</p></div>'+
      '<div class="btns"><a class="bigbtn lesson" href="'+LESSON+'" target="_blank">▶ Open the Lesson</a></div>'+
      '<p class="link-note">If the button does not open, copy this link: '+LESSON+'</p></div>'+
    '<h2 class="notes-title">📝 Notes from class</h2>'+cards+'</body></html>';
  win.document.write(html);
  win.document.close();
  setTimeout(function(){ win.print(); }, 700);
}
/* open the Homework directly from the PDF button */
if (location.hash === '#homework' && document.getElementById('hw-cover')) { goToId('hw-cover'); }

/* guided conversation (chat bubbles) */
function chatNext(sid){
  var c=document.getElementById(sid+'-chat'), btn=document.getElementById(sid+'-next'); if(!c) return;
  var bs=c.querySelectorAll('.b');
  for(var i=0;i<bs.length;i++){
    if(!bs[i].classList.contains('show')){
      bs[i].classList.add('show');
      btn.textContent = (i===bs.length-1) ? 'End of conversation' : (bs[i].classList.contains('them') ? 'Your turn ▸' : 'Continue ▸');
      if(i===bs.length-1) btn.disabled=true;
      c.scrollTop=c.scrollHeight;
      return;
    }
  }
}
function chatReset(sid){
  var c=document.getElementById(sid+'-chat'), btn=document.getElementById(sid+'-next'); if(!c) return;
  c.querySelectorAll('.b').forEach(function(b){b.classList.remove('show');});
  c.querySelectorAll('.ccq-answer').forEach(function(a){a.classList.remove('show');});
  c.scrollTop=0; btn.disabled=false; btn.textContent='Start the conversation';
}

/* copy the AI prompt */
function copyPrompt(sid){
  var el=document.getElementById(sid+'-text'); if(!el) return;
  var txt=el.textContent, btn=el.closest('.ai-prompt-wrap').querySelector('.ai-copy');
  function done(){ btn.textContent='Copied \u2713'; setTimeout(function(){btn.textContent='Copy prompt';},2000); }
  function fallback(){ var r=document.createRange(); r.selectNodeContents(el); var s=window.getSelection(); s.removeAllRanges(); s.addRange(r); try{document.execCommand('copy');}catch(e){} s.removeAllRanges(); done(); }
  if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(done,fallback); } else { fallback(); }
}
