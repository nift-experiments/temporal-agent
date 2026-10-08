// Local deployment contract harness; no remote network calls.
const http=require('node:http'),fs=require('node:fs'),path=require('node:path');
const publication=path.resolve(process.argv[2]),port=Number(process.argv[3]||4390);
const site=path.resolve(__dirname,'../build-work'),config=require(path.join(site,'vercel.json'));
const redirects=require(path.join(site,'bin/redirect-utils'));
const compiled=redirects.compileRedirects(config.redirects);
const types={'.html':'text/html; charset=utf-8','.md':'text/markdown; charset=utf-8','.txt':'text/plain; charset=utf-8','.js':'application/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.woff2':'font/woff2','.woff':'font/woff','.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.ico':'image/x-icon','.xml':'application/xml'};
http.createServer((request,response)=>{
 const url=new URL(request.url,'http://127.0.0.1:'+port); let pathname=decodeURIComponent(url.pathname);
 if(pathname.length>1 && pathname.endsWith('/')){response.writeHead(308,{Location:pathname.replace(/\/+$/,'')+url.search});return response.end();}
 const hit=redirects.findRedirect(pathname,compiled);
 if(hit){response.writeHead(hit.rule.permanent?308:307,{Location:redirects.substitute(hit.rule.destination,hit.params)+url.search});return response.end();}
 if(request.headers.accept?.includes('text/markdown') && !pathname.startsWith('/assets/') && !pathname.startsWith('/img/') && !pathname.endsWith('.md')) pathname=(pathname==='/'?'/index':pathname)+'.md';
 const resolved=path.resolve(publication,'.'+pathname); if(resolved!==publication && !resolved.startsWith(publication+path.sep)){response.writeHead(403);return response.end();}
 let file=resolved; if(fs.existsSync(file)&&fs.statSync(file).isDirectory()) file=path.join(file,'index.html');
 if(!fs.existsSync(file)&&!path.extname(file)&&fs.existsSync(path.join(file,'index.html'))) file=path.join(file,'index.html');
 if(!fs.existsSync(file)){
  if(pathname.endsWith('.md')){
   const moved=redirects.markdownRedirect(pathname,compiled); if(moved){response.writeHead(moved.status,{Location:moved.location});return response.end();}
   response.writeHead(404,{'Content-Type':types['.md'],'Vary':'Accept, Accept-Encoding'});return response.end('# Page not found\n\nThis URL does not match a page in the Temporal documentation.\n\n## Where to look next\n\n- [Documentation index](https://docs.temporal.io/llms.txt)\n- [Documentation sitemap](https://docs.temporal.io/sitemap.xml)\n- [Temporal documentation home](https://docs.temporal.io/)\n');
  }
  file=path.join(publication,'404.html'); response.statusCode=404;if(!fs.existsSync(file))return response.end('Not found');
 }
 const extension=path.extname(file); response.setHeader('Content-Type',types[extension]||'application/octet-stream');
 response.setHeader('Vary','Accept, Accept-Encoding');
 if(extension==='.md') response.setHeader('X-Robots-Tag','noindex');
 fs.createReadStream(file).on('error',()=>{response.statusCode=404;response.end('Not found');}).pipe(response);
}).listen(port,'127.0.0.1',()=>console.log('Local frozen reference http://127.0.0.1:'+port));
