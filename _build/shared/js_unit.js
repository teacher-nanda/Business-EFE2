function SS(t){ return String(t).replace(/([.?!])\s+(?=[A-Z])/g,'$1<br>'); }
/* ===================== TYPED ANSWERS: forgiving comparison ===================== */
/* ignores capitals, punctuation, curly apostrophes and extra spaces (overrides the generic version) */
function norm(s){
  return (s||'').toString().toLowerCase()
    .replace(/[‘’ʼ`]/g, "'")
    .replace(/[.,!?;:"“”]/g, ' ')
    .replace(/\s+/g, ' ').trim();
}


var dealCount = 0;
function dealNext(){
  var i = nextNoRepeat('deal', DEAL.length);
  var d = DEAL[i];
  var card = document.getElementById('deal-card');
  card.innerHTML = '<div class="dc-head">' + DEAL_LABEL + ' · ' + d.head + '</div><div class="dc-body"><p class="dc-setting">' + d.title + '</p>' +
    d.lines.map(function(l){ return '<p class="dc-line">' + SS(l) + '</p>'; }).join('') +
    '<div class="dc-goal"><b>Your goal</b>' + SS(d.goal) + '</div></div>';
  card.classList.remove('flip'); void card.offsetWidth; card.classList.add('flip');
  dealCount++;
  document.getElementById('deal-count').textContent = 'Cards played: ' + dealCount;
}
function dealReset(){
  shuffleBags['deal'] = []; shuffleLast['deal'] = undefined; dealCount = 0;
  document.getElementById('deal-count').textContent = 'Cards played: 0';
  document.getElementById('deal-card').innerHTML = '<div class="dc-head">' + DEAL_LABEL + '</div><div class="dc-body"><p class="dc-setting">Ready?</p><p class="dc-line">Press <b>Deal a card</b> to see the situation and what you need to do.</p></div>';
}


/* ===================== REVIEW: CHECKLIST ===================== */
function ckToggle(btn){
  btn.classList.toggle('on');
  var list = btn.closest('.check-list');
  var all = list.querySelectorAll('.check-item'), on = list.querySelectorAll('.check-item.on');
  var win = list.parentElement.querySelector('.win-banner');
  if (win) win.classList.toggle('show', all.length === on.length);
}


/* ===================== LIVE-BOUND WARM-UP FIELDS ===================== */
function liveUpdate(){
  document.querySelectorAll('[data-live]').forEach(function(inp){
    var k = inp.dataset.live;
    document.querySelectorAll('[data-bd="' + k + '"]').forEach(function(n){ n.textContent = inp.value.trim() || ' '; });
  });
}
document.addEventListener('input', function(e){ if (e.target && e.target.dataset && e.target.dataset.live) liveUpdate(); });
