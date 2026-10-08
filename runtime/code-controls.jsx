import React from 'react';
import {CodeBlockContextProvider,useCodeBlockContext,useCodeWordWrap} from '@docusaurus/theme-common/internal';
import Buttons from '@theme-original/CodeBlock/Buttons';
export function CodeControls({metadata,className,codeElement}){const wordWrap=useCodeWordWrap();wordWrap.codeBlockRef.current=codeElement;return <CodeBlockContextProvider metadata={metadata} wordWrap={wordWrap}><Buttons className={className}/></CodeBlockContextProvider>;}
export default function CodeControlIsland({className}){const {metadata}=useCodeBlockContext();return <span style={{display:'contents'}} data-temporal-island="CodeControls" data-props={JSON.stringify({metadata,className})}><Buttons className={className}/></span>;}
