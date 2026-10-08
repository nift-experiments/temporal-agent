const fs=require('node:fs'),path=require('node:path');const root=path.resolve(__dirname,'..');
const fonts=JSON.parse(fs.readFileSync(path.join(root,'remote-assets/fonts-manifest.json')));
const feedbackBase='https://cdn.jsdelivr.net/npm/pushfeedback@latest/dist/pushfeedback/';
async function install(context,record,base){
 await context.route('**/*',async route=>{
  const request=route.request(),url=new URL(request.url());
  if(url.origin===base && request.method()==='GET' && url.pathname!=='/comms')return route.continue();
  record.externalAttempts.push({url:request.url(),method:request.method(),resource:request.resourceType()});
  if(fonts[request.url()]){const value=fonts[request.url()];return route.fulfill({status:200,contentType:value.contentType,body:fs.readFileSync(path.join(root,'remote-assets',value.file))});}
  if(request.url().startsWith(feedbackBase)){
   const file=path.join(root,'remote-assets',path.basename(url.pathname));
   if(fs.existsSync(file))return route.fulfill({status:200,contentType:file.endsWith('.css')?'text/css':'application/javascript',body:fs.readFileSync(file)});
  }
  if(url.hostname==='widget.kapa.ai' && url.pathname==='/kapa-widget.bundle.js')return route.fulfill({status:200,contentType:'application/javascript',body:'window.__kapaFixtureCalls=[];window.Kapa={open:(options)=>window.__kapaFixtureCalls.push(options)};'});
  if(url.hostname==='app.pushfeedback.com' && url.pathname.startsWith('/api/v1/projects/'))return route.fulfill({json:{whitelabel:false,recaptcha_enabled:false,features:[]}});
  if(/algolia(?:net)?\.com$|algolia\.net$/.test(url.hostname) && url.pathname.includes('/queries')){
   const data=request.postDataJSON()||{}; const queries=data.requests||[{}];
   return route.fulfill({json:{results:queries.map(q=>{const query=typeof q.params==='string'?new URLSearchParams(q.params).get('query')||'':q.params?.query||q.query||'';const hits=/^workflows?$/i.test(query)?[{objectID:'fixture-python-workflows',type:'lvl1',hierarchy:{lvl0:'Developer Guides',lvl1:'Workflows - Python SDK'},content:'Deterministic fixture: start a Workflow with the Python SDK.',url:base+'/develop/python/workflows',url_without_anchor:base+'/develop/python/workflows',sdk_language:'python',_highlightResult:{hierarchy:{lvl0:{value:'Developer Guides',matchLevel:'none'},lvl1:{value:'Workflows - Python SDK',matchLevel:'full'}}},_snippetResult:{content:{value:'Deterministic fixture: start a Workflow with the Python SDK.',matchLevel:'none'}}}]:[];return {hits,nbHits:hits.length,page:0,nbPages:hits.length?1:0,hitsPerPage:20,processingTimeMS:0,query,params:'',facets:{sdk_language:{python:hits.length}},exhaustiveNbHits:true,exhaustiveFacetsCount:true};})}});
  }
  if(url.hostname==='consent.temporal.io')return route.fulfill({json:{country:'US',region:'CA',requiresConsent:true}});
  return route.fulfill({status:204,body:''});
 });
 await context.addInitScript(()=>{let seed=1701;Math.random=()=>((seed=(seed*1664525+1013904223)>>>0)/4294967296);});
}
module.exports={install};
