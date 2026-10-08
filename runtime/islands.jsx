import React from 'react';
import Retry from '@site/src/components/Demos/RetrySimulator/RetrySimulator';
import Mermaid from '@site/src/theme/Mermaid';
import LLMActions from '../islands-src/components/LLMActions/LLMActions';
import Search from '@site/src/theme/SearchBar';
import JsonTable from '../islands-src/components/elements/Tables/JsonTable';
import TOC from '@theme/TOCCollapsible';
import {CodeControls} from './code-controls';
import AnnotatedCode from '../islands-src/components/elements/AnnotatedCode';
import {extractFenceText} from '../islands-src/components/utils/extractElementText';
function AnnotatedCodeComponent({code,...props}){return <AnnotatedCode {...props}><pre><code>{code}</code></pre></AnnotatedCode>;}
export const islandComponents={AnnotatedCode:AnnotatedCodeComponent,Retry,Mermaid,LLMActions,Search,JsonTable,TOC,CodeControls};
function wrap(name){const Component=islandComponents[name];return function Island(props){return <span style={{display:'contents'}} data-temporal-island={name} data-props={JSON.stringify(props)}><Component {...props}/></span>;};}
export const RetryIsland=wrap('Retry');
export const MermaidIsland=wrap('Mermaid');
export default wrap('LLMActions');

export const JsonTableIsland=wrap('JsonTable');

const AnnotatedIsland=wrap('AnnotatedCode');export function AnnotatedCodeIsland({children,...props}){return <AnnotatedIsland {...props} code={extractFenceText(children)}/>;}
