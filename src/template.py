# template.py — page chrome: CSS, JS, lesson/print/index templates
import html, json

CSS = r"""
:root{--ink:#1F2630;--paper:#FAFAF7;--pcb:#1E6E52;--pcbd:#145039;--gold:#C8902A;--blue:#2457C5;--amber:#E8A317;--red:#C0392B;--grey:#6F7681;--mid:#C9CED6;--light:#EEF0F2;
--seg-start:#8A9099;--seg-learn:#2457C5;--seg-do:#1E6E52;--seg-check:#C8902A;--seg-pack:#6F7681;--radius:10px;
--font:"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;--mono:Consolas,"DejaVu Sans Mono",Menlo,monospace}
*{box-sizing:border-box}html{scroll-padding-top:120px}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font);font-size:16px;line-height:1.5}
a{color:var(--blue)}
.strip{position:sticky;top:0;z-index:20;background:var(--ink);color:#fff;padding:12px 24px 10px;box-shadow:0 2px 8px rgba(0,0,0,.25)}
.strip-top{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap}
.strip .course{font-weight:700;letter-spacing:.3px;color:#CFEFD9}
.strip .where{font-family:var(--mono);color:#FFD166;font-size:14px}
.strip h1{font-size:20px;margin:0;font-weight:700;flex:1 1 300px}
.strip .clock{font-family:var(--mono);font-size:22px;font-weight:700;min-width:5.2em;text-align:right}
.strip .clock.warn{color:#FFD166}.strip .clock.over{color:#FF8A80}
.strip button{background:#2E9E5B;color:#fff;border:0;border-radius:6px;padding:6px 12px;font:inherit;font-weight:700;cursor:pointer}
.strip button:focus-visible,button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #FFD166;outline-offset:2px}
.timeline{display:flex;gap:4px;margin-top:10px;height:30px}
.timeline .seg{position:relative;border-radius:6px;overflow:hidden;background:rgba(255,255,255,.12);color:#fff;font-size:12.5px;display:flex;align-items:center;padding:0 8px;white-space:nowrap}
.timeline .seg .fill{position:absolute;inset:0;width:0;background:var(--c);opacity:.85;transition:width 1s linear}
.timeline .seg span{position:relative;z-index:1;font-weight:600}
.timeline .seg.now{box-shadow:inset 0 0 0 2px #FFD166}
.wrap{max-width:1180px;margin:0 auto;padding:22px 24px 60px;display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:28px}
main{min-width:0;max-width:820px}
.outcomes{background:#fff;border:1px solid var(--mid);border-left:6px solid var(--pcb);border-radius:var(--radius);padding:14px 18px;margin:0 0 20px}
.outcomes h2{margin:0 0 6px;font-size:15px;color:var(--pcb)}
.outcomes ol{margin:0;padding-left:20px}
section.block{margin:26px 0 0}
section.block>h2{display:flex;align-items:center;gap:10px;font-size:18px;margin:0 0 10px;padding-bottom:6px;border-bottom:2px solid var(--c)}
section.block>h2 .min{font-family:var(--mono);font-size:13px;color:#fff;background:var(--c);border-radius:999px;padding:2px 10px}
section.block>h2 .who{font-size:12.5px;color:var(--grey);font-weight:400;margin-left:auto}
.steps{list-style:none;margin:0;padding:0;counter-reset:s}
.steps li{position:relative;padding:8px 44px 8px 52px;margin:6px 0;background:#fff;border:1px solid var(--mid);border-radius:8px}
.steps li::before{counter-increment:s;content:counter(s);position:absolute;left:12px;top:9px;width:26px;height:26px;border-radius:50%;background:var(--c);color:#fff;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center}
.steps li label{display:block;cursor:pointer}
.steps li input{position:absolute;right:12px;top:12px;width:18px;height:18px;accent-color:var(--pcb)}
.steps li.done{background:#F1F8F4;border-color:#BFE3CC}
.steps li.done label{color:var(--grey);text-decoration:line-through}
.steps li .note{display:block;font-size:13.5px;color:var(--grey);margin-top:2px}
.plain{margin:0;padding-left:20px}.plain li{margin:4px 0}
.learn p{margin:10px 0}
.callout{border-radius:8px;padding:12px 14px 12px 18px;margin:14px 0;background:#FFF8E6;border:1px solid #F3D48A;position:relative}
.callout.danger{background:#FDECEA;border-color:#F1B2AC}
.callout::before{content:"";position:absolute;left:0;top:0;bottom:0;width:8px;border-radius:8px 0 0 8px;background:repeating-linear-gradient(135deg,#1F2630 0 8px,#E8A317 8px 16px)}
.callout.danger::before{background:repeating-linear-gradient(135deg,#1F2630 0 8px,#C0392B 8px 16px)}
.callout strong{display:block;margin-bottom:2px}
.fig{width:100%;height:auto;display:block;background:#fff;border:1px solid var(--mid);border-radius:var(--radius);margin:12px 0}
.figcap{font-size:13.5px;color:var(--grey);margin:-6px 0 14px}
figure{margin:0}
code,kbd{font-family:var(--mono);font-size:.92em;background:#EEF0F2;padding:1px 5px;border-radius:4px}
pre{background:#1F2630;color:#E8ECF1;padding:12px 14px;border-radius:8px;overflow:auto;font-family:var(--mono);font-size:13.5px;line-height:1.45}
pre code{background:none;padding:0;color:inherit}
.quiz .q{background:#fff;border:1px solid var(--mid);border-radius:8px;padding:12px 14px;margin:10px 0}
.quiz .q p{margin:0 0 8px;font-weight:600}
.quiz .opt{display:block;margin:4px 0;padding:6px 10px;border:1px solid var(--mid);border-radius:6px;cursor:pointer;background:#FAFAF7}
.quiz .opt:hover{border-color:var(--blue)}
.quiz .opt.right{background:#E6F4EA;border-color:#2E9E5B;font-weight:600}
.quiz .opt.wrong{background:#FDECEA;border-color:#C0392B}
.quiz .why{display:none;margin-top:8px;font-size:14px;color:var(--pcb)}
.quiz .q.answered .why{display:block}
aside{position:sticky;top:110px;align-self:start}
.bench{background:#fff;border:1px solid var(--mid);border-radius:var(--radius);padding:14px 16px;margin-bottom:14px}
.bench h3{margin:0 0 8px;font-size:14px;color:var(--grey);font-weight:600}
.bench ul{margin:0;padding-left:18px;font-size:14.5px}
.bench li{margin:3px 0}
.pdfbtn{display:flex;align-items:center;gap:10px;width:100%;background:var(--ink);color:#fff;border:0;border-radius:8px;padding:12px 14px;font:inherit;font-weight:700;cursor:pointer;text-align:left}
.pdfbtn:hover{background:#2B333E}
.pdfbtn small{font-weight:400;color:#CFEFD9;display:block}
.dl{font-size:13px;margin:6px 0 0;text-align:center}
.vocab dt{font-weight:700;margin-top:6px}.vocab dd{margin:0 0 4px;font-size:14px;color:#3A4350}
footer{max-width:1180px;margin:0 auto;padding:0 24px 40px;font-size:13px;color:var(--grey);display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
footer a{color:var(--grey)}
.roles{display:flex;gap:10px;margin:10px 0 0;font-size:13.5px;flex-wrap:wrap}
.roles span{background:var(--light);border-radius:6px;padding:4px 10px}
.pb{background:#fff;border:1px solid var(--mid);border-radius:var(--radius);padding:14px;margin:12px 0}
.pb-grid{display:grid;grid-template-columns:1fr 240px;gap:16px;align-items:center}
.pb-list label{display:flex;align-items:center;gap:8px;margin:5px 0;font-size:14.5px}.pb-list label b{margin-left:auto;font-family:var(--mono);font-weight:600}
.pb-list select{font:inherit;padding:3px 6px;margin-left:auto}
.pb-verdict{text-align:center;font-weight:700;margin:4px 0 0}
.ledsim{background:#fff;border:1px solid var(--mid);border-radius:var(--radius);padding:14px;margin:12px 0}
.ledsim-row{display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.ledsim-btn{width:120px;height:120px;border-radius:50%;background:#2B333E;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:#CFEFD9;font-size:11px}
.ledsim-led{width:28px;height:28px;border-radius:50%;background:#555;box-shadow:0 0 0 3px #1F2630;transition:background .08s}
.ledsim-led.amber{background:#F2A900;box-shadow:0 0 14px #F2A900,0 0 0 3px #1F2630}.ledsim-led.white{background:#fff;box-shadow:0 0 14px #fff,0 0 0 3px #1F2630}
.ledsim-ctl label{display:block;margin-bottom:8px}.ledsim-ctl select,.ledsim-ctl button{font:inherit;padding:5px 9px;margin-right:6px}
.ledsim-read{font-family:var(--mono);font-weight:600;margin:8px 0 0;color:var(--pcb)}
.ledsim-note{font-size:13.5px;color:var(--grey);margin:10px 0 0}
.crimp{background:#fff;border:1px solid var(--mid);border-radius:var(--radius);padding:12px;margin:12px 0}
.crimp-tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.crimp-tabs button{font:inherit;font-size:14px;padding:6px 10px;border:1px solid var(--mid);background:#FAFAF7;border-radius:6px;cursor:pointer}
.crimp-tabs button.on{background:var(--pcb);color:#fff;border-color:var(--pcb)}
.crimp-p{display:grid;grid-template-columns:360px 1fr;gap:16px;align-items:center}.crimp-p[hidden]{display:none}.crimp-p .fig{margin:0}.crimp-p p{margin:0;font-size:15px}
.tester{background:#fff;border:1px solid var(--mid);border-radius:var(--radius);padding:14px;margin:12px 0}
.tester-ctl{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:12px}.tester-ctl select,.tester-ctl button{font:inherit;padding:5px 9px}
.tester-units{display:flex;gap:24px;flex-wrap:wrap}
.tester-unit{background:#2B333E;border-radius:10px;padding:12px 14px;color:#CFEFD9;min-width:300px}
.tester-name{font-weight:700;margin-bottom:8px}
.leds{display:flex;gap:8px}.led{display:flex;flex-direction:column;align-items:center;font-size:11px;gap:4px}
.led i{width:18px;height:18px;border-radius:50%;background:#444;display:block}
.led.on i{background:#2E9E5B;box-shadow:0 0 10px #2E9E5B}.led.bad i{background:#C0392B;box-shadow:0 0 10px #C0392B}
.tester-read{font-weight:600;margin:12px 0 0;color:var(--ink)}
.ipb{background:#fff;border:1px solid var(--mid);border-radius:var(--radius);padding:14px;margin:12px 0}
.ipb-row{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:10px}.ipb-row input{font:inherit;font-family:var(--mono);padding:4px 6px;width:11em}
.ipb-bits{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:6px 0;font-family:var(--mono);font-size:13px}
.ipb-bits .oct{display:flex;gap:2px;align-items:center}.ipb-bits .oct b{width:3em;text-align:right;margin-right:6px;font-weight:600}
.ipb-bits .bit{width:16px;height:22px;display:flex;align-items:center;justify-content:center;border-radius:3px;background:#EEF0F2}
.ipb-bits .bit.one{background:var(--blue);color:#fff}.ipb-mask .bit.one{background:var(--gold)}
.ipb-bits .bit.net{outline:2px solid var(--gold)}
.ipb-read{font-weight:600;margin:10px 0 0}
.term{background:#1F2630;border-radius:8px;overflow:hidden;margin:12px 0;font-family:var(--mono);font-size:13.5px}
.term-bar{background:#2B333E;color:#CFEFD9;padding:5px 12px;font-size:12px}
.term-body{padding:10px 14px;color:#E8ECF1;min-height:80px}
.term .tl{white-space:pre;opacity:0;animation:tl .3s forwards}
@keyframes tl{to{opacity:1}}
.rubric{border-collapse:collapse;width:100%;font-size:13px;margin:10px 0}.rubric th,.rubric td{border:1px solid var(--mid);padding:6px 8px;vertical-align:top;text-align:left}.rubric th{background:var(--light)}
table.plain{border-collapse:collapse;width:100%;font-size:14px;margin:10px 0}table.plain th,table.plain td{border:1px solid var(--mid);padding:6px 8px;vertical-align:top;text-align:left}table.plain th{background:var(--light)}
@media (max-width:900px){.wrap{grid-template-columns:1fr}aside{position:static}.pb-grid,.crimp-p{grid-template-columns:1fr}.strip h1{font-size:17px}}
@media (prefers-reduced-motion:reduce){*{animation-duration:.001s!important;animation-iteration-count:1!important}}
@media print{.strip,aside,.pdfbtn,.dl{display:none}.wrap{display:block}}
"""

JS = r"""
(function(){
const L=document.body.dataset.lesson;
const segs=[...document.querySelectorAll('.timeline .seg')];const total=segs.reduce((a,s)=>a+ +s.dataset.min,0);
let t0=null,timer=null;const clock=document.querySelector('.clock');const btn=document.querySelector('[data-start]');
function paint(){const el=(Date.now()-t0)/60000;let acc=0;segs.forEach(s=>{const m=+s.dataset.min;const f=Math.max(0,Math.min(1,(el-acc)/m));s.querySelector('.fill').style.width=(f*100)+'%';s.classList.toggle('now',el>=acc&&el<acc+m);acc+=m});
 const rem=total*60-(Date.now()-t0)/1000;const a=Math.abs(rem);clock.textContent=(rem<0?'-':'')+String(Math.floor(a/60)).padStart(2,'0')+':'+String(Math.floor(a%60)).padStart(2,'0');clock.classList.toggle('warn',rem<300&&rem>=0);clock.classList.toggle('over',rem<0);}
if(btn){btn.addEventListener('click',()=>{if(timer){clearInterval(timer);timer=null;t0=null;btn.textContent='Start lesson timer';segs.forEach(s=>{s.querySelector('.fill').style.width='0';s.classList.remove('now')});clock.textContent=String(total).padStart(2,'0')+':00';clock.className='clock';return}t0=Date.now();btn.textContent='Reset';paint();timer=setInterval(paint,1000)});}
const key='rebuildlab:'+L;let saved={};try{saved=JSON.parse(localStorage.getItem(key)||'{}')}catch(e){}
document.querySelectorAll('.steps input[type=checkbox]').forEach((c,i)=>{c.checked=!!saved[i];c.closest('li').classList.toggle('done',c.checked);c.addEventListener('change',()=>{c.closest('li').classList.toggle('done',c.checked);saved[i]=c.checked;try{localStorage.setItem(key,JSON.stringify(saved))}catch(e){}})});
document.querySelectorAll('.quiz .q').forEach(q=>{const ans=+q.dataset.a;q.querySelectorAll('.opt').forEach((o,i)=>{const pick=()=>{if(q.classList.contains('answered'))return;q.classList.add('answered');o.classList.add(i===ans?'right':'wrong');q.querySelectorAll('.opt')[ans].classList.add('right')};o.addEventListener('click',pick);o.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick()}})})});
const pdfB64=document.getElementById('pdfdata');
function pdfBlob(){const bin=atob(pdfB64.textContent.trim());const u=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)u[i]=bin.charCodeAt(i);return new Blob([u],{type:'application/pdf'})}
const pb=document.querySelector('.pdfbtn');if(pb&&pdfB64){pb.addEventListener('click',()=>{const url=URL.createObjectURL(pdfBlob());const w=window.open(url,'_blank');if(!w)location.href=url});
 const dl=document.querySelector('[data-dl]');if(dl){dl.addEventListener('click',e=>{e.preventDefault();const url=URL.createObjectURL(pdfBlob());const a=document.createElement('a');a.href=url;a.download=dl.dataset.dl;document.body.appendChild(a);a.click();a.remove()})}}
const PARTS=window.PARTS||{};document.querySelectorAll('svg.anatomy').forEach(sv=>{const cap=document.createElement('p');cap.className='figcap';cap.textContent='Click any part to read what it does.';sv.after(cap);sv.querySelectorAll('.part').forEach(p=>p.addEventListener('click',()=>{const d=PARTS[p.dataset.part];if(d){cap.innerHTML='<b>'+d[0]+'</b> — '+d[1]}sv.querySelectorAll('.part').forEach(x=>x.classList.remove('hl'));p.classList.add('hl')}))});
document.querySelectorAll('[data-visual=power_budget]').forEach(w=>{const arc=w.querySelector('.pb-arc'),tot=w.querySelector('.pb-total'),v=w.querySelector('.pb-verdict');
 function calc(){let s=0;w.querySelectorAll('input[data-w]').forEach(c=>{if(c.checked)s+=+c.dataset.w});s+=+w.querySelector('[data-gpu]').value;const psu=+w.querySelector('[data-psu]').value;const need=Math.round(s*1.3);tot.textContent=need+' W';const f=Math.min(1,need/psu);arc.style.strokeDashoffset=283-283*f;arc.style.stroke=f<.7?'#2E9E5B':f<.9?'#E8A317':'#C0392B';
 v.textContent=f<.7?'Comfortable on a '+psu+' W unit':f<.9?'Tight: it will run but near the limit on '+psu+' W':'Over budget for '+psu+' W: pick a bigger PSU or smaller GPU';v.style.color=f<.7?'#1E6E52':f<.9?'#B07A00':'#C0392B'}
 w.querySelectorAll('input,select').forEach(e=>e.addEventListener('change',calc));calc()});
document.querySelectorAll('[data-visual=dell_led]').forEach(w=>{const led=w.querySelector('.ledsim-led'),sel=w.querySelector('[data-code]'),read=w.querySelector('.ledsim-read');let run=0;
 function blink(n,cb){let i=0;(function step(){if(i>=n)return cb();led.classList.add('amber');setTimeout(()=>{led.classList.remove('amber');i++;setTimeout(step,250)},250)})()}
 w.querySelector('[data-play]').addEventListener('click',()=>{const id=++run;const [a,b]=sel.value.split(',').map(Number);read.textContent='Watch and count…';(function loop(){if(id!==run)return;blink(a,()=>setTimeout(()=>blink(b,()=>{read.textContent=sel.value+' → '+sel.options[sel.selectedIndex].text.split('— ')[1];setTimeout(loop,2000)}),800))})()});
 w.querySelector('[data-beep]').addEventListener('click',()=>{try{const ac=new (window.AudioContext||window.webkitAudioContext)();let t=ac.currentTime+.1;[1,3,2].forEach(g=>{for(let i=0;i<g;i++){const o=ac.createOscillator(),ga=ac.createGain();o.type='square';o.frequency.value=880;ga.gain.value=.08;o.connect(ga).connect(ac.destination);o.start(t);o.stop(t+.25);t+=.4}t+=.6});read.textContent='1-3-2 = memory failure (reseat / swap the RAM)'}catch(e){read.textContent='Audio not available in this browser'}});});
document.querySelectorAll('[data-visual=crimp]').forEach(w=>{w.querySelectorAll('[data-step]').forEach(b=>b.addEventListener('click',()=>{w.querySelectorAll('[data-step]').forEach(x=>x.classList.remove('on'));b.classList.add('on');w.querySelectorAll('.crimp-p').forEach(p=>p.hidden=p.dataset.p!==b.dataset.step)}))});
document.querySelectorAll('[data-visual=tester]').forEach(w=>{const units=w.querySelectorAll('.tester-unit'),read=w.querySelector('.tester-read');const MAP={good:{map:[1,2,3,4,5,6,7,8],bad:[],txt:'Pass: lights 1→8 in order on both units. Straight-through, all pairs correct.'},open:{map:[1,2,3,0,5,6,7,8],bad:[],txt:'Fail: light 4 never comes on at the remote end. A wire is not reaching its pin (open). Re-terminate the end you suspect.'},cross:{map:[1,3,2,4,5,6,7,8],bad:[2,3],txt:'Fail: master lights 2 then 3 but the remote lights 3 then 2. Miswire. Re-do the colour order on one plug.'},split:{map:[1,2,5,4,3,6,7,8],bad:[3,5],txt:'Fail-ish: a cheap tester may say PASS, but the pairs are split (3 and 5 swapped). It will link, then drop out at speed. Cut it off.'},short:{map:[1,1,3,4,5,6,7,8],bad:[1,2],txt:'Fail: two lights come on at once. Bare copper is touching inside the plug (short). Cut it off and strip again.'}};
 w.querySelector('[data-run]').addEventListener('click',()=>{const m=MAP[w.querySelector('[data-mode]').value];units.forEach(u=>u.querySelectorAll('.led').forEach(l=>l.className='led'));read.textContent='Testing…';let i=0;(function step(){if(i>=8){read.textContent=m.txt;return}units[0].querySelector('[data-led="'+(i+1)+'"]').classList.add('on');const r=m.map[i];if(r){const el=units[1].querySelector('[data-led="'+r+'"]');el.classList.add(m.bad.includes(i+1)?'bad':'on')}i++;setTimeout(step,450)})()})});
document.querySelectorAll('[data-visual=ipbits]').forEach(w=>{const ia=w.querySelector('[data-ipa]'),ib=w.querySelector('[data-ipb]'),ic=w.querySelector('[data-cidr]'),ba=w.querySelector('[data-bitsa]'),bb=w.querySelector('[data-bitsb]'),bm=w.querySelector('[data-bitsm]'),rd=w.querySelector('.ipb-read');
 function parse(s){const p=s.trim().split('.');if(p.length!==4)return null;const n=p.map(x=>/^\d+$/.test(x)?+x:-1);return n.some(x=>x<0||x>255)?null:n}
 function row(el,octs,cidr,label){el.innerHTML='';octs.forEach((o,k)=>{const d=document.createElement('div');d.className='oct';d.innerHTML='<b>'+o+'</b>'+[...Array(8)].map((_,i)=>{const bit=(o>>(7-i))&1;const idx=k*8+i;return '<span class="bit '+(bit?'one':'')+(idx<cidr?' net':'')+'">'+bit+'</span>'}).join('');el.appendChild(d)});const l=document.createElement('div');l.style.gridColumn='1/-1';l.style.color='#6F7681';l.textContent=label;el.prepend(l)}
 function calc(){const a=parse(ia.value),b=parse(ib.value),c=Math.max(8,Math.min(30,+ic.value||24));if(!a||!b){rd.textContent='Type a valid address like 192.168.10.11';return}
  const mask=[0,1,2,3].map(k=>{const bits=Math.max(0,Math.min(8,c-k*8));return bits?(0xFF<<(8-bits))&0xFF:0});row(ba,a,c,'Address A');row(bb,b,c,'Address B');row(bm,mask,c,'Mask /'+c+' = '+mask.join('.'));
  const na=a.map((o,k)=>o&mask[k]),nb=b.map((o,k)=>o&mask[k]);const same=na.join('.')===nb.join('.');rd.innerHTML='Network of A: <code>'+na.join('.')+'</code> &nbsp; Network of B: <code>'+nb.join('.')+'</code> &nbsp; → '+(same?'<span style="color:#1E6E52">same network: they can talk directly through the switch</span>':'<span style="color:#C0392B">different networks: they need a router between them</span>');}
 [ia,ib,ic].forEach(e=>e.addEventListener('input',calc));calc()});
})();
"""

PRINT_CSS = r"""
@page{size:A4;margin:16mm 15mm 18mm 15mm}
body{font-family:"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;font-size:11pt;color:#1F2630;line-height:1.4;margin:0}
.ph{display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px solid #1E6E52;padding-bottom:6px;margin-bottom:10px}
.ph .c{font-weight:700;color:#1E6E52}.ph .w{font-family:Consolas,"DejaVu Sans Mono",monospace;color:#6F7681}
h1{font-size:19pt;margin:4px 0 2px}h2{font-size:12.5pt;margin:14px 0 6px;padding-bottom:3px;border-bottom:1.5px solid #C9CED6;color:#1F2630}
.name{display:flex;gap:30px;font-size:10pt;color:#6F7681;margin:0 0 10px}.name span{border-bottom:1px solid #1F2630;min-width:200px;display:inline-block}
ol,ul{margin:4px 0;padding-left:20px}li{margin:3px 0}
.chk{list-style:none;padding-left:0}.chk li{padding-left:24px;position:relative}.chk li::before{content:"";position:absolute;left:2px;top:4px;width:12px;height:12px;border:1.5px solid #1F2630;border-radius:2px}
.fig{width:100%;height:auto;border:1px solid #C9CED6;border-radius:6px;margin:6px 0;page-break-inside:avoid}
.callout{border:1.5px solid #E8A317;border-left:8px solid #E8A317;border-radius:4px;padding:6px 10px;margin:8px 0;background:#FFF8E6;font-size:10.5pt}
.callout.danger{border-color:#C0392B;background:#FDECEA}
.callout strong{display:block;margin-bottom:1px}
.lines{margin:4px 0 10px}.lines div{border-bottom:1px solid #9AA3AE;height:22px}
.q{page-break-inside:avoid;margin:8px 0}
code{font-family:Consolas,"DejaVu Sans Mono",monospace;background:#EEF0F2;padding:0 3px;border-radius:3px;font-size:10pt}
pre{background:#EEF0F2;padding:8px 10px;border-radius:4px;font-family:Consolas,"DejaVu Sans Mono",monospace;font-size:9.5pt;white-space:pre-wrap}
pre code{background:none;padding:0}
.vocab{columns:2;font-size:10pt}.vocab div{break-inside:avoid;margin-bottom:3px}
.exit{border:1.5px dashed #1E6E52;padding:8px 10px;margin-top:10px;border-radius:4px}
*{animation:none!important}
.pb,.ledsim,.tester,.ipb,.crimp-tabs,.figcap{display:none}
.crimp-p{display:grid;grid-template-columns:1fr 1fr;gap:10px;align-items:center;page-break-inside:avoid}.crimp-p[hidden]{display:grid}
.term{background:#EEF0F2;border-radius:4px;font-family:Consolas,"DejaVu Sans Mono",monospace;font-size:9.5pt;padding:6px 10px}.term-bar{font-weight:700;color:#6F7681;font-size:9pt}.term .tl{white-space:pre}
.rubric{border-collapse:collapse;width:100%;font-size:9.5pt}.rubric th,.rubric td{border:1px solid #C9CED6;padding:4px 6px;vertical-align:top}
table.plain{border-collapse:collapse;width:100%;font-size:10pt}table.plain th,table.plain td{border:1px solid #C9CED6;padding:4px 6px;vertical-align:top;text-align:left}
.foot{font-size:8.5pt;color:#8A9099;display:flex;justify-content:space-between;margin-top:14px;border-top:1px solid #C9CED6;padding-top:4px}
"""

SEG = [("start", "Start", "--seg-start"), ("learn", "Learn", "--seg-learn"), ("do", "Do", "--seg-do"), ("check", "Check", "--seg-check"), ("pack", "Pack down", "--seg-pack")]

def esc(s): return html.escape(str(s), quote=False)

def steps_html(items):
    out = ['<ol class="steps">']
    for s in items:
        note = ""
        if isinstance(s, (tuple, list)): s, note = s
        out.append(f'<li><label><input type="checkbox" aria-label="done">{s}{f"<span class=note>{note}</span>" if note else ""}</label></li>')
    out.append("</ol>")
    return "".join(out)

def plain_list(items):
    return '<ul class="plain">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def callouts_html(items):
    return "".join(f'<div class="callout {kind}"><strong>{title}</strong>{body}</div>' for kind, title, body in items)

def quiz_html(qs):
    out = ['<div class="quiz">']
    for q in qs:
        opts = "".join(f'<span class="opt" role="button" tabindex="0">{o}</span>' for o in q["o"])
        out.append(f'<div class="q" data-a="{q["a"]}"><p>{q["q"]}</p>{opts}<div class="why">{q["why"]}</div></div>')
    out.append("</div>")
    return "".join(out)

def fill_figs(html_text, figs):
    for i, f in enumerate(figs):
        html_text = html_text.replace("{F%d}" % i, f'<figure>{f}</figure>')
    return html_text

def lesson_page(L, pdf_b64, nav):
    segmins = [L["start"]["min"], L["learn"]["min"], L["do"]["min"], L["check"]["min"], L["pack"]["min"]]
    tl = "".join(f'<div class="seg" data-min="{m}" style="flex:{m};--c:var({v})"><div class="fill"></div><span>{n} {m}</span></div>' for (k, n, v), m in zip(SEG, segmins))
    outcomes = "".join(f"<li>{o}</li>" for o in L["outcomes"])
    kit = "".join(f"<li>{k}</li>" for k in L["kit"])
    vocab = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in L["vocab"])
    learn_body = fill_figs(L["learn"]["html"], L["learn"].get("figures", []))
    do_block = steps_html(L["do"]["steps"]) + L["do"].get("html", "")
    callouts = callouts_html(L.get("callouts", []))
    prev_l, next_l = nav
    total = sum(segmins)
    return f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ReBuild Lab W{L['week']} L{L['lnum']} — {esc(L['title'])}</title><style>{CSS}</style></head>
<body data-lesson="L{L['n']:02d}">
<header class="strip"><div class="strip-top"><span class="course">ReBuild Lab</span><span class="where">Week {L['week']} · Lesson {L['lnum']} · {L['n']} of 54</span><h1>{esc(L['title'])}</h1><span class="clock">{total:02d}:00</span><button type="button" data-start>Start lesson timer</button></div>
<div class="timeline">{tl}</div></header>
<div class="wrap"><main>
<div class="outcomes"><h2>By the end of this lesson you can</h2><ol>{outcomes}</ol>
<div class="roles"><span>Driver: hands on the hardware</span><span>Navigator: reads each step aloud, ticks it off, checks before power-on</span><span>Swap roles every lesson</span></div></div>
{callouts}
<section class="block" style="--c:var(--seg-start)"><h2><span class="min">{L['start']['min']} min</span>Start<span class="who">{esc(L['start'].get('who','whole class'))}</span></h2>{plain_list(L['start']['steps'])}</section>
<section class="block learn" style="--c:var(--seg-learn)"><h2><span class="min">{L['learn']['min']} min</span>Learn<span class="who">{esc(L['learn'].get('who','teacher explains, you follow on screen'))}</span></h2>{learn_body}</section>
<section class="block" style="--c:var(--seg-do)"><h2><span class="min">{L['do']['min']} min</span>Do<span class="who">{esc(L['do'].get('who','pairs at the bench'))}</span></h2>{do_block}</section>
<section class="block" style="--c:var(--seg-check)"><h2><span class="min">{L['check']['min']} min</span>Check<span class="who">answer on screen or on the worksheet</span></h2>{quiz_html(L['check']['quiz'])}</section>
<section class="block" style="--c:var(--seg-pack)"><h2><span class="min">{L['pack']['min']} min</span>Pack down</h2>{plain_list(L['pack']['steps'])}</section>
</main>
<aside>
<div class="bench"><button class="pdfbtn" type="button">Open the printable worksheet<small>PDF — opens in a new tab, then print</small></button><p class="dl"><a href="#" data-dl="{L['file'].replace('.html','.pdf')}">or download the PDF</a></p></div>
<div class="bench"><h3>On the bench</h3><ul>{kit}</ul></div>
<div class="bench"><h3>Words</h3><dl class="vocab">{vocab}</dl></div>
</aside></div>
<footer><span>ReBuild Lab · PC Building, Repair &amp; Maintenance · Year 9/10 · Plenty Valley Christian College</span><span>{f'<a href="{prev_l}">← previous</a>' if prev_l else ''} &nbsp; <a href="index.html">course map</a> &nbsp; {f'<a href="{next_l}">next →</a>' if next_l else ''}</span></footer>
<script id="pdfdata" type="application/pdf-base64">{pdf_b64}</script>
<script>window.PARTS={json.dumps(L.get('parts', {}))};</script>
<script>{JS}</script>
</body></html>"""

def print_page(L):
    figs = L["learn"].get("figures", [])
    fig_html = "".join(f'<figure>{f}</figure>' for f in figs[:2] if f.startswith("<svg"))
    do_steps = [s[0] if isinstance(s, (tuple, list)) else s for s in L["do"]["steps"]]
    do_list = '<ol class="chk">' + "".join(f"<li>{s}</li>" for s in do_steps) + "</ol>"
    qs = L["print"]["questions"]
    qhtml = "".join(f'<div class="q"><b>{i+1}.</b> {q[0]}<div class="lines">{"".join("<div></div>" for _ in range(q[1]))}</div></div>' for i, q in enumerate(qs))
    callouts = callouts_html(L.get("callouts", []))
    vocab = "".join(f"<div><b>{a}</b> — {b}</div>" for a, b in L["vocab"])
    return f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>{esc(L['title'])}</title><style>{PRINT_CSS}</style></head><body>
<div class="ph"><span class="c">ReBuild Lab · PC Building, Repair &amp; Maintenance</span><span class="w">Week {L['week']} · Lesson {L['lnum']} · {L['n']} of 54</span></div>
<h1>{esc(L['title'])}</h1>
<div class="name"><span>Name</span><span>Bench partner</span><span>Date</span></div>
<h2>By the end of this lesson you can</h2><ol>{"".join(f"<li>{o}</li>" for o in L['outcomes'])}</ol>
{callouts}
<h2>Key ideas</h2>{"".join(f"<p>{p}</p>" for p in L['print']['key_ideas'])}
{fig_html}
<h2>Do — tick each step</h2>{do_list}
{L['do'].get('print_html','')}
<h2>Worksheet</h2>{qhtml}
<div class="exit"><b>Exit ticket:</b> {L['print']['exit']}<div class="lines"><div></div><div></div></div></div>
<h2>Words</h2><div class="vocab">{vocab}</div>
<div class="foot"><span>ReBuild Lab · Lesson {L['n']} · {esc(L['title'])}</span><span>Plenty Valley Christian College · Digital Technologies</span></div>
</body></html>"""
