// Content-verified transient caches. --force always recomputes independently.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),root=path.resolve(__dirname,'..');
const hash=exports.hash=value=>crypto.createHash('sha256').update(value).digest('hex');
exports.signature=value=>hash(JSON.stringify(value));
exports.walk=function walk(dir){if(!fs.existsSync(dir))return [];return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);};
exports.inputs=files=>hash(Buffer.concat([...new Set(files)].sort().map(file=>Buffer.concat([Buffer.from(path.relative(root,file)+'\0'),fs.readFileSync(file),Buffer.from('\0')]))));
const location=(stage,key)=>path.join(root,'.cache/stage-records',stage,Buffer.from(key).toString('base64url')+'.json');
exports.read=function(stage,key,input,force){if(force)return null;const record=location(stage,key);if(!fs.existsSync(record))return null;let value;try{value=JSON.parse(fs.readFileSync(record));}catch(error){if(error instanceof SyntaxError)return null;throw error;}if(value.input!==input)return null;for(const [file,digest] of Object.entries(value.products)){const target=path.join(root,file);if(!fs.existsSync(target)||hash(fs.readFileSync(target))!==digest)return null;}return value;};
exports.write=function(stage,key,input,files,data){const file=location(stage,key);fs.mkdirSync(path.dirname(file),{recursive:true});const value=JSON.stringify({input,products:Object.fromEntries(files.map(file=>[path.relative(root,file),hash(fs.readFileSync(file))])),data});if(!fs.existsSync(file)||fs.readFileSync(file,'utf8')!==value){const temporary=file+'.tmp-'+process.pid;fs.writeFileSync(temporary,value);fs.renameSync(temporary,file);}};
