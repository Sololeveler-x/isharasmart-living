(function(){"use strict";function initRiVaPhotoHouse(section){if(!section||section.dataset.rivaPhInit==="true"){return}
section.dataset.rivaPhInit="true";var house=section.querySelector(".riva-ph-house");var statusEl=section.querySelector("#riva-ph-status-text");var micBtn=section.querySelector("#riva-ph-mic");var voiceEl=section.querySelector("#riva-ph-voice-line");if(!house){return}
var reduceMotion=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;if(!reduceMotion){section.classList.add("riva-anim")}
var IMG_W=1536,IMG_H=1024;var WINDOWS=[{x0:345,x1:757,y0:522,y1:817},{x0:355,x1:636,y0:241,y1:423},{x0:788,x1:947,y0:243,y1:405}];var WIN_NAME=["Hallroom","Bedroom","Kitchen"];function groupIdx(t){return t==="all"?[0,1,2]:[t]}
function grpWord(t){return t==="all"?"All":WIN_NAME[t]}
function grpFromIdx(idx){return idx.length===3?"All":WIN_NAME[idx[0]]}
function roomTargets(t){if(/bed\s*room/.test(t)){return[1]}
if(/kitchen/.test(t)){return[2]}
if(/hall|living|lounge|down/.test(t)){return[0]}
return[0,1,2]}
var FRAME_BASE="./img/";var FRAMES={day:{on:"Smart-Home-–-Day-Curtains-Open-Lights-On.webp",cool:"Smart-Home-–-Day-Cool-White-Lights.webp",off:"Smart-Home-–-Day-Curtains-Open-Lights-Off.webp",closed:"Smart-Home-–-Day-Curtains-Closed-Lights-Off-1.webp"},night:{on:"Smart-Home-–-Night-Curtains-Open-Lights-On.webp",cool:"Smart-Home-–-Night-Cool-White-Lights.webp",off:"Smart-Home-–-Night-Curtains-Open-Lights-Off.webp",closed:"Smart-Home-–-Night-Curtains-Closed-Lights-Off.webp"}};var SIZES="(max-width:880px) 92vw, 56vw";function frameURL(name){return encodeURI(FRAME_BASE+name)}
function frameSrcset(name){var stem=name.replace(/\.webp$/,"");return frameURL(stem+"-768x512.webp")+" 768w, "+frameURL(stem+"-1024x683.webp")+" 1024w, "+frameURL(name)+" 1500w"}
function frameSrc(name){return frameURL(name.replace(/\.webp$/,"")+"-1024x683.webp")}
var FIRST={day:{on:!0,off:!0}};var LAYER_SPECS=[{role:"base",frame:"off"},{role:"ext",frame:"on"},{role:"extCool",frame:"cool"}];WINDOWS.forEach(function(w,wi){LAYER_SPECS.push({role:"openOff",win:wi,frame:"off"});LAYER_SPECS.push({role:"openOn",win:wi,frame:"on"});LAYER_SPECS.push({role:"openCool",win:wi,frame:"cool"});LAYER_SPECS.push({role:"bandL",win:wi,frame:"closed"});LAYER_SPECS.push({role:"bandR",win:wi,frame:"closed"})});var layers={day:{},night:{}};var deferred=[];function layerKey(sp){return sp.role+(sp.win==null?"":sp.win)}
function setImg(im,name){im.sizes=SIZES;im.srcset=frameSrcset(name);im.src=frameSrc(name)}
function buildTheme(theme){if(layers[theme].built){return}
var host=section.querySelector(theme==="day"?".riva-ph-day":".riva-ph-night");if(!host){return}
LAYER_SPECS.forEach(function(sp){var d=document.createElement("div");d.className="riva-ph-layer";var im=document.createElement("img");im.alt="";im.setAttribute("aria-hidden","true");im.decoding="async";im.className="skip-lazy";im.setAttribute("data-no-lazy","1");var name=FRAMES[theme][sp.frame];if(FIRST[theme]&&FIRST[theme][sp.frame]){setImg(im,name)}else{im._rivaFrame=name;deferred.push(im)}
d.appendChild(im);host.appendChild(d);layers[theme][layerKey(sp)]=d});layers[theme].built=!0}
buildTheme("day");var restLoaded=!1;function loadRest(){if(restLoaded){return}
restLoaded=!0;buildTheme("night");onFrameLoad();deferred.forEach(function(im){im.addEventListener("load",onFrameLoad,{once:!0});setImg(im,im._rivaFrame)})}["pointerdown","touchstart","keydown","focusin"].forEach(function(ev){section.addEventListener(ev,loadRest,{once:!0,passive:!0})});function onIntentMove(e){if(!e.movementX&&!e.movementY){return}
section.removeEventListener("pointermove",onIntentMove);loadRest()}
section.addEventListener("pointermove",onIntentMove,{passive:!0});function afterLoad(){var go=function(){setTimeout(loadRest,8000)};if(document.readyState==="complete"){go()}else{window.addEventListener("load",go,{once:!0})}}
afterLoad();function clamp01(v){return v<0?0:(v>100?100:v)}
function insetPct(t,r,b,l){return"inset("+clamp01(t).toFixed(2)+"% "+clamp01(r).toFixed(2)+"% "+clamp01(b).toFixed(2)+"% "+clamp01(l).toFixed(2)+"%)"}
function eLevel(i){return state.lights[i].on?state.lights[i].bright/100:0}
function eOut(){return state.outside.on?state.outside.bright/100:0}
function tLevel(i){return(state.lights[i].temp||0)/100}
function tOut(){return(state.outside.temp||0)/100}
function updatePhoto(){var r=house.getBoundingClientRect();var cw=r.width,ch=r.height;if(!cw||!ch){return}
var scale=Math.max(cw/IMG_W,ch/IMG_H);var ox=(cw-IMG_W*scale)/2,oy=(ch-IMG_H*scale)/2;var fx=function(nx){return(ox+nx*scale)/cw*100};var fy=function(ny){return(oy+ny*scale)/ch*100};var oL=eOut(),oTemp=tOut();["day","night"].forEach(function(theme){var L=layers[theme];if(L.ext){L.ext.style.opacity=oL*(1-oTemp)}
if(L.extCool){L.extCool.style.opacity=oL*oTemp}
WINDOWS.forEach(function(w,wi){var e=eLevel(wi),tp=tLevel(wi);var closed=1-(state.curtains[wi]/100);var mid=(w.x0+w.x1)/2,half=(mid-w.x0)*closed;var Ty=fy(w.y0),By=fy(w.y1);var xL=fx(w.x0),xLm=fx(w.x0+half),xRm=fx(w.x1-half),xR=fx(w.x1);var openClip=insetPct(Ty,100-xRm,100-By,xLm);var lClip=insetPct(Ty,100-xLm,100-By,xL);var rClip=insetPct(Ty,100-xR,100-By,xRm);if(L["openOff"+wi]){L["openOff"+wi].style.clipPath=openClip;L["openOff"+wi].style.opacity=1}
if(L["openOn"+wi]){L["openOn"+wi].style.clipPath=openClip;L["openOn"+wi].style.opacity=e*(1-tp)}
if(L["openCool"+wi]){L["openCool"+wi].style.clipPath=openClip;L["openCool"+wi].style.opacity=e*tp}
if(L["bandL"+wi]){L["bandL"+wi].style.clipPath=lClip;L["bandL"+wi].style.opacity=1}
if(L["bandR"+wi]){L["bandR"+wi].style.clipPath=rClip;L["bandR"+wi].style.opacity=1}})});var nightGlow=state.night?1:0;for(var i=0;i<3;i++){var closedFrac=1-(state.curtains[i]/100);section.style.setProperty("--glow"+i,(eLevel(i)*closedFrac*0.9*nightGlow*(1-tLevel(i))).toFixed(3))}}
var state={night:!1,lights:[{on:!0,bright:75,temp:0},{on:!0,bright:75,temp:0},{on:!0,bright:75,temp:0}],outside:{on:!0,bright:100,temp:0},curtains:[100,100,100],lightTarget:"all",curtainTarget:"all",lock:!0,camera:!0,speaker:!1,sensor:!1};function lightUnits(t){if(t==="all"){return[0,1,2,"out"]}
if(t==="outside"){return["out"]}
return[t]}
function unitLit(u){return u==="out"?eOut()>0:litAt(u)}
function unitBright(u){return u==="out"?state.outside.bright:state.lights[u].bright}
function unitTemp(u){return(u==="out"?state.outside.temp:state.lights[u].temp)||0}
function unitObj(u){return u==="out"?state.outside:state.lights[u]}
function tempWord(v){return v<34?"Warm":(v<67?"Neutral":"Cool")}
function lightWord(t){return t==="all"?"All":t==="outside"?"Outside":WIN_NAME[t]}
function setText(k,t){var n=section.querySelector('[data-state="'+k+'"]');if(n){n.textContent=t}}
function setSwitch(k,on){var b=section.querySelector('[data-toggle="'+k+'"]');if(b){b.setAttribute("aria-checked",on?"true":"false")}
var r=section.querySelector('[data-row="'+k+'"]');if(r){r.classList.toggle("is-off",!on)}}
function setSlider(k,v){var w=section.querySelector('[data-slider="'+k+'"]');if(!w){return}
w.querySelector("input").value=v;w.style.setProperty("--fill",v+"%")}
function say(m){if(statusEl){statusEl.textContent=m}}
function litAt(i){return state.lights[i].on&&state.lights[i].bright>0}
function avg(arr){return Math.round(arr.reduce(function(a,c){return a+c},0)/arr.length)}
function uniform(arr){return arr.every(function(v){return v===arr[0]})}
function render(){section.style.setProperty("--night",state.night?1:0);updatePhoto();house.classList.toggle("is-unlocked",!state.lock);house.classList.toggle("cam-on",state.camera);house.classList.toggle("spk-on",state.speaker);house.classList.toggle("sense-on",state.sensor);var lu=lightUnits(state.lightTarget);var lOn=lu.map(unitLit);var allLit=lOn.every(Boolean),anyLit=lOn.some(Boolean);var lBr=lu.map(unitBright);var lTp=lu.map(unitTemp);var tVal=uniform(lTp)?lTp[0]:avg(lTp);setSwitch("lights",allLit);setSlider("lights",uniform(lBr)?lBr[0]:avg(lBr));setSlider("lighttemp",tVal);setText("lights",allLit?(uniform(lBr)?"On · "+lBr[0]+"%":"On"):(anyLit?"Mixed":"Off"));var ci=groupIdx(state.curtainTarget);var cVals=ci.map(function(i){return state.curtains[i]});var allOpen=cVals.every(function(v){return v>0});setSwitch("curtains",allOpen);setSlider("curtains",uniform(cVals)?cVals[0]:avg(cVals));setText("curtains",!uniform(cVals)?"Mixed":cVals[0]===0?"Closed":cVals[0]===100?"Open":cVals[0]+"% open");section.querySelectorAll('[data-groups="lights"] button').forEach(function(bn){bn.classList.toggle("is-on",bn.dataset.group===String(state.lightTarget))});section.querySelectorAll('[data-groups="curtains"] button').forEach(function(bn){bn.classList.toggle("is-on",bn.dataset.group===String(state.curtainTarget))});setSwitch("lock",state.lock);setSwitch("camera",state.camera);setSwitch("speaker",state.speaker);setSwitch("sensor",state.sensor);setText("lock",state.lock?"Locked":"Unlocked");setText("camera",state.camera?"Recording":"Off");setText("speaker",state.speaker?"Playing":"Off");setText("sensor",state.sensor?"Armed":"Disarmed");section.querySelectorAll(".riva-ph-seg button").forEach(function(b2){b2.classList.toggle("is-on",(b2.dataset.time==="night")===state.night)})}
var SPEAK={lights:function(){var lu=lightUnits(state.lightTarget);return lightWord(state.lightTarget)+(lu.some(unitLit)?" lights on":" lights off")},curtains:function(){var ci=groupIdx(state.curtainTarget);var open=ci.some(function(i){return state.curtains[i]>0});return grpWord(state.curtainTarget)+(open?" curtains opening":" curtains closing")},lock:function(){return state.lock?"Front door locked":"Front door unlocked"},camera:function(){return state.camera?"Camera recording":"Camera off"},speaker:function(){return state.speaker?"Music playing":"Music stopped"},sensor:function(){return state.sensor?"Motion sensor armed":"Motion sensor off"}};section.querySelectorAll("[data-toggle]").forEach(function(btn){btn.addEventListener("click",function(){var k=btn.dataset.toggle;if(k==="curtains"){var ci=groupIdx(state.curtainTarget);var anyOpen=ci.some(function(i){return state.curtains[i]>0});ci.forEach(function(i){state.curtains[i]=anyOpen?0:100})}else if(k==="lights"){var lu=lightUnits(state.lightTarget);var anyOn=lu.some(unitLit);lu.forEach(function(u){var o=unitObj(u);if(anyOn){o.on=!1}else{o.on=!0;if(o.bright===0){o.bright=75}}})}else{state[k]=!state[k]}
render();say(SPEAK[k]())})});section.querySelectorAll("[data-slider] input").forEach(function(input){var k=input.closest("[data-slider]").dataset.slider;input.addEventListener("input",function(){var v=parseInt(input.value,10);if(k==="lights"){var lu=lightUnits(state.lightTarget);lu.forEach(function(u){var o=unitObj(u);o.bright=v;o.on=!0});say(lightWord(state.lightTarget)+(v===0?" lights off":" lights at "+v+"%"))}else if(k==="lighttemp"){var luT=lightUnits(state.lightTarget);luT.forEach(function(u){var o=unitObj(u);o.temp=v;o.on=!0});say(lightWord(state.lightTarget)+" lights — "+tempWord(v).toLowerCase()+" white")}else{var ci=groupIdx(state.curtainTarget);ci.forEach(function(i){state.curtains[i]=v});say(grpWord(state.curtainTarget)+" curtains "+(v===0?"closed":v===100?"open":v+"% open"))}
render()})});section.querySelectorAll("[data-groups] button").forEach(function(btn){btn.addEventListener("click",function(){var which=btn.closest("[data-groups]").dataset.groups;var g=btn.dataset.group;var val=(g==="all"||g==="outside")?g:parseInt(g,10);if(which==="lights"){state.lightTarget=val}else{state.curtainTarget=val}
render()})});section.querySelectorAll("[data-time]").forEach(function(btn){btn.addEventListener("click",function(){state.night=(btn.dataset.time==="night");render();say(state.night?"Evening":"Daytime")})});var SCENES={morning:{night:!1,lights:!1,brightness:60,temp:70,curtains:100,outside:!1,lock:!0,camera:!0,speaker:!0,sensor:!1,label:"Good morning — curtains open, music on"},movie:{night:!0,lights:!0,brightness:15,temp:0,curtains:0,outside:!1,lock:!0,camera:!0,speaker:!0,sensor:!1,label:"Movie night — curtains closed, warm lights at 15%"},away:{night:!1,lights:!1,brightness:75,temp:0,curtains:0,outside:!0,lock:!0,camera:!0,speaker:!1,sensor:!0,label:"Away — locked, sensor armed, outside lights on"},goodnight:{night:!0,lights:!1,brightness:60,temp:0,curtains:0,outside:!0,lock:!0,camera:!0,speaker:!1,sensor:!0,label:"Good night — locked up, outside lights on, sensor armed"}};function applyScene(name){var s=SCENES[name];if(!s){return null}
for(var i=0;i<3;i++){state.lights[i]={on:s.lights,bright:s.brightness,temp:s.temp||0};state.curtains[i]=s.curtains}
state.outside={on:s.outside,bright:100,temp:s.temp||0};state.night=s.night;state.lock=s.lock;state.camera=s.camera;state.speaker=s.speaker;state.sensor=s.sensor;render();say(s.label);return s.label}
section.querySelectorAll("[data-scene]").forEach(function(btn){btn.addEventListener("click",function(){applyScene(btn.dataset.scene)})});function speakBack(text){try{if(!window.speechSynthesis){return}
var u=new SpeechSynthesisUtterance(text);u.rate=1.02;window.speechSynthesis.cancel();window.speechSynthesis.speak(u)}catch(e){}}
function num(t){var m=t.match(/(\d{1,3})\s*(?:%|percent)?/);return m?Math.max(0,Math.min(100,parseInt(m[1],10))):null}
function handleCommand(raw){var t=(raw||"").toLowerCase().trim();if(!t){return null}
t=t.replace(/\b(hey|ok|okay)?\s*(ishara|shara|riva|reva|rita|viva|river)\s*(smart)?\b/g,' ').trim();
if(/good\s*night|goodnight|bed\s*time/.test(t)){return applyScene("goodnight")}
if(/good\s*morning|morning\s*scene/.test(t)){return applyScene("morning")}
if(/movie|cinema|film/.test(t)){return applyScene("movie")}
if(/away|leaving|going out|i'?m out/.test(t)){return applyScene("away")}
var on=/\b(on|open|start|play|arm|resume|unlock)\b/.test(t);var off=/\b(off|close|shut|stop|pause|disarm|lock|draw)\b/.test(t);if(/curtain|blind|drape/.test(t)){var cIdx=roomTargets(t);var n=num(t);cIdx.forEach(function(i){if(n!==null&&/percent|%/.test(t)){state.curtains[i]=n}else if(/close|shut|draw/.test(t)){state.curtains[i]=0}else if(/open/.test(t)){state.curtains[i]=100}else{state.curtains[i]=state.curtains[i]>0?0:100}});render();var anyOpen=cIdx.some(function(i){return state.curtains[i]>0});var m1=grpFromIdx(cIdx)+" curtains "+(anyOpen?"opening":"closing");say(m1);return m1}
if(/light|lamp|bright|dim|warm|cool|cold|white/.test(t)){var units=/outside|exterior|garden|porch|roof|facade|driveway/.test(t)?["out"]:roomTargets(t);var n2=num(t);var wantWarm=/\bwarm\b/.test(t);var wantCool=/\bcool\b|\bcold\b/.test(t);if(wantWarm||wantCool){var tp=wantCool?100:0;units.forEach(function(u){var L=unitObj(u);L.temp=tp;L.on=!0;if(L.bright===0){L.bright=75}});render();var labelT=(units.length===1&&units[0]==="out")?"Outside":grpFromIdx(units);var mT=labelT+" lights — "+(wantCool?"cool":"warm")+" white";say(mT);return mT}
units.forEach(function(u){var L=unitObj(u);if(n2!==null&&/percent|%|to \d/.test(t)){L.bright=n2;L.on=!0}else if(/dim/.test(t)){L.bright=Math.max(0,L.bright-30);L.on=!0}else if(/bright/.test(t)){L.bright=Math.min(100,L.bright+30);L.on=!0}else if(off){L.on=!1}else if(on){L.on=!0;if(L.bright===0){L.bright=75}}else{L.on=!L.on;if(L.on&&L.bright===0){L.bright=75}}});render();var anyLit=units.some(unitLit);var label=(units.length===1&&units[0]==="out")?"Outside":grpFromIdx(units);var m2=label+" lights "+(anyLit?"on":"off");say(m2);return m2}
if(/door|lock/.test(t)){state.lock=/unlock|open/.test(t)?!1:(/lock|shut|close/.test(t)?!0:!state.lock);render();var m3=state.lock?"Front door locked":"Front door unlocked";say(m3);return m3}
if(/camera|cctv|recording/.test(t)){state.camera=off?!1:(on?!0:!state.camera);render();var m4=state.camera?"Camera recording":"Camera off";say(m4);return m4}
if(/music|speaker|song|sonos|play/.test(t)){state.speaker=/stop|off|pause/.test(t)?!1:(/play|on|start/.test(t)?!0:!state.speaker);render();var m5=state.speaker?"Music playing":"Music stopped";say(m5);return m5}
if(/sensor|motion|alarm|security/.test(t)){state.sensor=/disarm|off|stop/.test(t)?!1:(/arm|on|start/.test(t)?!0:!state.sensor);render();var m6=state.sensor?"Motion sensor armed":"Motion sensor off";say(m6);return m6}
if(/night|evening|dark/.test(t)){state.night=!0;render();say("Evening");return"Evening"}
if(/day|morning|light out/.test(t)){state.night=!1;render();say("Daytime");return"Daytime"}
return null}
function runPhrase(text,spoken){if(voiceEl){voiceEl.textContent="“"+text+"”"}
var reply=handleCommand(text);setTimeout(function(){if(!voiceEl){return}
if(reply){voiceEl.innerHTML="“"+text+"” &nbsp;<em>→ "+reply+"</em>";if(spoken){speakBack(reply)}}else{voiceEl.innerHTML="<em>Sorry, I did not catch that. Try one of these:</em>"}},260)}
section.querySelectorAll("[data-say]").forEach(function(b){b.addEventListener("click",function(){runPhrase(b.dataset.say,!1)})});var SR=window.SpeechRecognition||window.webkitSpeechRecognition;var LISTEN_MS=8000;var MAX_RESTART=6;var recog=null;var listening=!1;var windowOpen=!1;var gotFinal=!1;var restarts=0;var stopTimer=null;var tickTimer=null;function paintListening(secondsLeft){if(!voiceEl){return}
voiceEl.innerHTML="<em>Listening… "+secondsLeft+"s</em>"}
function clearTimers(){clearTimeout(stopTimer);stopTimer=null;clearInterval(tickTimer);tickTimer=null}
function endWindow(message){windowOpen=!1;clearTimers();if(recog){try{recog.stop()}catch(e){}}
listening=!1;section.classList.remove("is-listening");if(message&&voiceEl&&!gotFinal){voiceEl.innerHTML="<em>"+message+"</em>"}}
function startRecogniser(){recog=new SR();recog.lang="en-IN";recog.continuous=!0;recog.interimResults=!0;recog.maxAlternatives=1;recog.onstart=function(){listening=!0;section.classList.add("is-listening")};recog.onresult=function(ev){var txt="",isFinal=!1;for(var i=ev.resultIndex;i<ev.results.length;i++){txt+=ev.results[i][0].transcript;if(ev.results[i].isFinal){isFinal=!0}}
txt=txt.trim();if(!txt){return}
if(voiceEl){voiceEl.textContent="“"+txt+"”"}
if(isFinal){gotFinal=!0;endWindow(null);runPhrase(txt,!0)}};recog.onerror=function(ev){if(ev.error==="no-speech"||ev.error==="aborted"){return}
if(ev.error==="not-allowed"||ev.error==="service-not-allowed"){endWindow("Microphone blocked — tap a phrase instead.");return}
endWindow("Speech service unavailable — tap a phrase instead.")};recog.onend=function(){listening=!1;if(windowOpen&&!gotFinal&&restarts<MAX_RESTART){restarts++;setTimeout(function(){if(!windowOpen||gotFinal){return}
try{recog.start()}catch(e){}},150);return}
section.classList.remove("is-listening")};try{recog.start()}catch(e){endWindow("Could not start the microphone — tap a phrase instead.")}}
if(micBtn){micBtn.addEventListener("click",function(){if(!SR){if(voiceEl){voiceEl.innerHTML="<em>This browser has no speech recognition — "+"tap one of the phrases instead.</em>"}
return}
if(windowOpen){endWindow("Stopped listening — tap a phrase, or try again.");return}
gotFinal=!1;restarts=0;windowOpen=!0;section.classList.add("is-listening");var left=Math.round(LISTEN_MS/1000);paintListening(left);tickTimer=setInterval(function(){left-=1;if(left>0&&windowOpen&&!gotFinal){paintListening(left)}},1000);stopTimer=setTimeout(function(){endWindow("Nothing heard — try again, or tap a phrase.")},LISTEN_MS);startRecogniser()})}
render();var resizeRaf=null;function onResize(){if(resizeRaf){return}
resizeRaf=requestAnimationFrame(function(){resizeRaf=null;house.classList.add("riva-no-anim");updatePhoto();requestAnimationFrame(function(){house.classList.remove("riva-no-anim")})})}
if("ResizeObserver" in window){new ResizeObserver(onResize).observe(house)}else{window.addEventListener("resize",onResize)}
var frameRaf=null;function onFrameLoad(){if(frameRaf){return}
frameRaf=requestAnimationFrame(function(){frameRaf=null;house.classList.add("riva-no-anim");updatePhoto();requestAnimationFrame(function(){house.classList.remove("riva-no-anim")})})}
section.querySelectorAll(".riva-ph-layer img").forEach(function(im){if(!im.getAttribute("src")||im.complete){return}
im.addEventListener("load",onFrameLoad,{once:!0})})}
function initAll(){document.querySelectorAll(".riva-ph-section").forEach(function(s){initRiVaPhotoHouse(s)})}
if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",initAll)}else{initAll()}
if(window.jQuery){window.jQuery(window).on("elementor/frontend/init",function(){setTimeout(initAll,200)})}})()