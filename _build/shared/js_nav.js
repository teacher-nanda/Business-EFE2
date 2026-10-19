var slides = Array.from(document.querySelectorAll('.slide'));
var current = 0;
var notesStoreKey = 'befeNotes::' + document.title;
var notesData = {};
try { var _savedNotes = JSON.parse(localStorage.getItem(notesStoreKey)); if (_savedNotes) Object.assign(notesData, _savedNotes); } catch(e) {}
var notesOpen = false;

if (slides.length !== slideIds.length || slides.length !== slideLabels.length) {
  console.warn('Slide count mismatch:', slides.length, 'slides,', slideIds.length, 'IDs,', slideLabels.length, 'labels');
}

var dotsWrap = document.getElementById('dots');
slides.forEach(function(s, i){
  var d = document.createElement('div');
  d.className = 'dot' + (i === 0 ? ' active' : '');
  d.onclick = function(){ goTo(i); };
  dotsWrap.appendChild(d);
});

function goTo(n){
  if (n < 0 || n >= slides.length) return;
  saveNotes();
  slides[current].classList.remove('active');
  current = n;
  slides[current].classList.add('active');
  document.querySelectorAll('.dot').forEach(function(d,i){ d.classList.toggle('active', i===current); });
  document.getElementById('counter').textContent = (current+1)+'/'+slides.length;
  document.getElementById('prevBtn').disabled = current===0;
  document.getElementById('nextBtn').disabled = current===slides.length-1;
  document.getElementById('homeBtn').style.display = current===0 ? 'none' : 'flex';
  var panel = document.getElementById('notesPanel');
  if (current === 0) { if (notesOpen) panel.classList.add('cover'); }
  else { panel.classList.remove('cover'); }
  loadNotes(current);
}
function goToId(id){ var i = slideIds.indexOf(id); if (i>-1) goTo(i); }

document.addEventListener('keydown', function(e){
  var tag = document.activeElement.tagName;
  if (tag === 'INPUT' || tag === 'TEXTAREA' || document.activeElement.contentEditable === 'true') return;
  if (e.key === 'ArrowRight') goTo(current+1);
  if (e.key === 'ArrowLeft') goTo(current-1);
});

