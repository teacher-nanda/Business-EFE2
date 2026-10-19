/* ===================== AUDIO FILES (fill in when the files are available) ===================== */
var AUDIO = {
  'cb1.1':'', 'cb1.2':'', 'cb1.3':'', 'cb1.4':'../1_4.mp3', 'cb1.5':'', 'cb1.7':'', 'cb1.8':'',
  'pb1.1':'', 'pb1.2':'', 'pb1.4':'', 'pb1.5':''
};
document.querySelectorAll('audio[data-track]').forEach(function(a){
  var f = AUDIO[a.dataset.track];
  if (f) { a.src = f; var box = a.closest('.audio-box'); if (box) box.classList.remove('pending'); }
});

/* ===================== TYPED ANSWERS: forgiving comparison ===================== */
/* ignores capitals, punctuation, curly apostrophes and extra spaces (overrides the generic version) */
function norm(s){
  return (s||'').toString().toLowerCase()
    .replace(/[‘’ʼ`]/g, "'")
    .replace(/[.,!?;:"“”]/g, ' ')
    .replace(/\s+/g, ' ').trim();
}

/* ===================== WARM-UP: DELEGATE BADGE ===================== */
var BD = {name:'', role:'', company:'', ask:''};
function bdRender(){
  document.querySelectorAll('[data-bd]').forEach(function(n){
    var v = BD[n.dataset.bd];
    n.textContent = v || ' ';
  });
}
function bdUpdate(){
  ['name','role','company','ask'].forEach(function(k){
    var el = document.getElementById('bd-' + k);
    BD[k] = el ? el.value.trim() : '';
  });
  bdRender();
}

/* ===================== FREER PRACTICE: DELEGATE CARDS ===================== */
var DEAL = [
  {head:'Coffee break', title:'A face you think you know',
   lines:['You are Marta, a finance manager.', 'You see Daniel from HTB Engineering. You think you met him in Lisbon last year.'],
   goal:'Start the conversation. Then find out what he usually does and what he is working on at the moment.'},
  {head:'Registration desk', title:'A stranger in the queue',
   lines:['You are Priya from the design team.', 'Your teacher is a delegate you have never met.'],
   goal:'Introduce yourself. Find out what they are doing at the conference this week.'},
  {head:'First day at the office', title:'Someone you have heard about',
   lines:['Your manager, Carl, has told you a lot about Eric from the UK office.', 'Your teacher is Eric.'],
   goal:'Greet him and show that you have heard about him. Ask what he is working on at the moment.'},
  {head:'Corridor', title:'Two people who do not know each other',
   lines:['You know both Hayao (visiting from the Japanese office) and Tony (your new director of marketing).', 'Your teacher plays both of them.'],
   goal:'Introduce them to each other.'},
  {head:'Welcome reception', title:'A polite introduction',
   lines:['You know Victoria from Finance and Faisal, a new client.', 'You are not sure they have met. Your teacher plays both of them.'],
   goal:'Introduce them to each other, then respond politely when they greet you.'},
  {head:'Workshop', title:'The seat next to you',
   lines:['You are Jun from Sales.', 'Your teacher is Lena, a delegate sitting next to you.'],
   goal:'Introduce yourself. Ask if she is enjoying the workshop, and what she usually does at conferences.'},
  {head:'Client visit', title:'A client you have only emailed',
   lines:['You are Sofia, a project manager.', 'Your teacher is Mr. Brandt. You have exchanged emails, but never met.'],
   goal:'Meet him in person for the first time. Show that you have heard about him.'},
  {head:'Networking event', title:'A shy start',
   lines:['You are Omar, a young engineer. You feel a little shy.', 'Your teacher is a stranger standing alone.'],
   goal:'Start a conversation. Ask about their job and what they are doing at the moment.'},
  {head:'Lobby', title:'Have we met?',
   lines:['You think you met your teacher (Ms. Costa, from Marketing) at a conference in Dubai.'],
   goal:'Check whether you have met. Then say what you do.'},
  {head:'Team lunch', title:'A new colleague',
   lines:['Ana joins your team today. You want her to meet your teammate Ben.', 'Your teacher plays both Ana and Ben.'],
   goal:'Introduce them to each other. Make them feel welcome.'},
  {head:'Airport shuttle', title:'Going to the same place',
   lines:['You are sitting next to a stranger. You are both going to the same conference.', 'Your teacher is the stranger.'],
   goal:'Introduce yourself. Ask what they are doing at the conference.'},
  {head:'Conference dinner', title:'An old colleague',
   lines:['You are at dinner with your teacher, an old colleague you have not seen for years.'],
   goal:'Greet them. Ask what they are doing now, and what they usually do these days.'}
];
var dealCount = 0;
function dealNext(){
  var i = nextNoRepeat('deal', DEAL.length);
  var d = DEAL[i];
  var card = document.getElementById('deal-card');
  card.innerHTML = '<div class="dc-head">Delegate card · ' + d.head + '</div><div class="dc-body"><p class="dc-setting">' + d.title + '</p>' +
    d.lines.map(function(l){ return '<p class="dc-line">' + l + '</p>'; }).join('') +
    '<div class="dc-goal"><b>Your goal</b>' + d.goal + '</div></div>';
  card.classList.remove('flip'); void card.offsetWidth; card.classList.add('flip');
  dealCount++;
  document.getElementById('deal-count').textContent = 'Cards played: ' + dealCount;
}
function dealReset(){
  shuffleBags['deal'] = []; shuffleLast['deal'] = undefined; dealCount = 0;
  document.getElementById('deal-count').textContent = 'Cards played: 0';
  document.getElementById('deal-card').innerHTML = '<div class="dc-head">Delegate card</div><div class="dc-body"><p class="dc-setting">Ready?</p><p class="dc-line">Press <b>Deal a card</b> to see who you are, who you meet, and what you need to do.</p></div>';
}

/* ===================== REVIEW: CHECKLIST ===================== */
function ckToggle(btn){
  btn.classList.toggle('on');
  var all = document.querySelectorAll('#ck-list .check-item');
  var on = document.querySelectorAll('#ck-list .check-item.on');
  document.getElementById('ck-win').classList.toggle('show', all.length === on.length);
}

/* the badge on the review slide always mirrors what was typed in the warm-up */
document.addEventListener('click', function(){ bdRender(); });
bdRender();
