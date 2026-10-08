// Corpus-driven frozen reference audit. Every nonlocal request is locally fulfilled/blocked.
const {chromium}=require('../build-work/node_modules/@playwright/test');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..'),base='http://127.0.0.1:4390';
const fixtures=JSON.parse(fs.readFileSync(path.join(root,'source-audit/parity-fixture-candidates.json')));
const label=process.argv[2]||'t2-browser-reference',out=path.join(root,'runs',label);
if(fs.existsSync(out))throw Error('Refuse overwrite audit');fs.mkdirSync(out,{recursive:true});
const record={scope:'Frozen upstream reference; deterministic local transports, no live remote/backend exercise',browser:'Playwright Chromium',states:[],externalAttempts:[],errors:[]};
const {install}=require('./local-transports.cjs');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
  for(const viewport of fixtures.viewports)for(const theme of fixtures.themes){
   const context=await browser.newContext({viewport:{width:viewport.width,height:viewport.height},colorScheme:theme==='dark'?'dark':'light',reducedMotion:'reduce'});await install(context,record,base);
   await context.addInitScript(theme=>{if(theme==='system')localStorage.removeItem('theme-014');else localStorage.setItem('theme-014',theme);},theme);
   const page=await context.newPage(); page.on('pageerror',error=>record.errors.push({viewport:viewport.name,theme,error:error.message}));
   for(const fixture of fixtures.fixtures){
    const response=await page.goto(base+fixture.route,{waitUntil:'networkidle'});await page.waitForTimeout(350);
    if(fixture.family==='home'){const reject=page.getByRole('button',{name:'Reject All',exact:true});if(await reject.count()){await reject.click();await page.waitForTimeout(200);}}
    const state=await page.evaluate(()=>({title:document.title,theme:document.documentElement.getAttribute('data-theme'),themeChoice:document.documentElement.getAttribute('data-theme-choice'),heading:document.querySelector('h1')?.textContent,mainText:document.querySelector('main')?.innerText||'',links:[...document.querySelectorAll('main a[href]')].map(a=>[a.textContent.trim(),a.getAttribute('href')]),tabs:[...document.querySelectorAll('[role=tab]')].map(a=>({text:a.textContent,selected:a.getAttribute('aria-selected')})),mermaidSvg:document.querySelectorAll('svg[id^=mermaid],svg[id^=mermaid-]').length,buttons:[...document.querySelectorAll('main button')].map(b=>({text:b.textContent.trim(),label:b.getAttribute('aria-label'),title:b.getAttribute('title')})),clientWidth:document.documentElement.clientWidth,scrollWidth:document.documentElement.scrollWidth,feedbackWidgets:document.querySelectorAll('feedback-button').length,feedbackButtons:[...document.querySelectorAll('feedback-button')].map(e=>({hydrated:!!e.shadowRoot,buttons:e.shadowRoot?[...e.shadowRoot.querySelectorAll('button')].map(b=>b.textContent.trim()):[]}))}));
    record.states.push({viewport:viewport.name,requestedTheme:theme,family:fixture.family,route:fixture.route,status:response.status(),...state});
    if(fixture.family==='home')await page.screenshot({path:path.join(out,viewport.name+'-'+theme+'-home.png')});
    fs.writeFileSync(path.join(out,'observations.json'),JSON.stringify(record,null,2)+'\n');
    console.log(viewport.name,theme,fixture.route,response.status(),state.theme,'tabs',state.tabs.length,'diagrams',state.mermaidSvg);
   }
   await context.close();
  }
 }finally{await browser.close();fs.writeFileSync(path.join(out,'observations.json'),JSON.stringify(record,null,2)+'\n');}
 console.log('Reference states',record.states.length,'remote attempts intercepted',record.externalAttempts.length,'page errors',record.errors.length);
})().catch(error=>{console.error(error);process.exitCode=1;});
