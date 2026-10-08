// Explicit maintained-HTML island refresh. No Markdown is read or compiled.
process.env.NODE_ENV='production';
const fs=require('fs'),path=require('path'),{spawnSync}=require('child_process'),c=require('cheerio'),root=path.resolve(__dirname,'..');
const index=process.argv.indexOf('--island'),name=index<0?null:process.argv[index+1];
if(!name)throw Error('--island is required');
if(!fs.existsSync(path.join(root,'html')))throw Error('Only the maintained-HTML project uses this workflow');
const entry="import React from 'react';import {renderToString} from 'react-dom/server';import {Context} from '@migration/context';import {islandComponents} from '@migration/islands';export function render(name,metadata,props){const Component=islandComponents[name];if(!Component)throw Error('Unknown retained island '+name);return renderToString(<Context metadata={metadata}><Component {...props}/></Context>);}";
fs.mkdirSync(path.join(root,'.cache'),{recursive:true});fs.writeFileSync(path.join(root,'.cache/maintenance-entry.jsx'),entry);
const child=spawnSync(process.execPath,['tools/bundle.cjs','--maintenance'],{cwd:root,stdio:'inherit'});if(child.status!==0)throw Error('Selective maintenance bundle failed');
const server=require(path.join(root,'.cache/bundle/maintenance/server.cjs'));
let roots=0,files=0;
for(const row of JSON.parse(fs.readFileSync(path.join(root,'models/routes.json')))){
 const file=path.join(root,row.body),old=fs.readFileSync(file,'utf8');
 if(!old.includes('data-temporal-island="'+name+'"'))continue;
 const $=c.load(old,null,false);let changed=false;
 $('[data-temporal-island]').filter((i,e)=>$(e).attr('data-temporal-island')===name).each((i,e)=>{const element=$(e),props=JSON.parse(element.attr('data-props')||'{}'),rendered=server.render(name,row.metadata,props);roots++;if(element.html()!==rendered){element.html(rendered);changed=true;}});
 if(changed){fs.writeFileSync(file,$.html());files++;}
}
console.log(JSON.stringify({island:name,roots,maintainedHtmlFilesUpdated:files,markdownProcessing:false,ordinaryBuild:false}));
