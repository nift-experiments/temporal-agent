import DesktopTOC from '@theme/TOC';
import Sidebar from './sidebar';
import IntegrationsGrid from '../islands-src/components/IntegrationsGrid';
import GuidesGrid from '../islands-src/components/GuidesGrid';
import TemporalLifecycleDemo from '../islands-src/components/Demos/TemporalLifecycle/TemporalLifecycleDemo';
import StandaloneActivityDemo from '../islands-src/components/Demos/StandaloneActivity/StandaloneActivityDemo';
import ServerlessWorkerDemo from '../islands-src/components/Demos/ServerlessWorker/ServerlessWorkerDemo';
import PriorityFairnessWalkthrough from '../islands-src/components/elements/PriorityFairnessWalkthrough';
import PriorityFairnessSimulator from '../islands-src/components/elements/PriorityFairnessSimulator';
import Video from '../islands-src/components/elements/Video/Video';
import ToolTipTerm from '../islands-src/components/ToolTipTerm/ToolTipTerm';
import ZoomableImage from '../islands-src/components/elements/Images/ZoomableImage';
import EnlargeImage from '../islands-src/components/elements/Images/EnlargeImage';
import CaptionedImage from '../islands-src/components/elements/Images/CaptionedImage';
import React from 'react';
import Retry from '@site/src/components/Demos/RetrySimulator/RetrySimulator';
import Mermaid from '@site/src/theme/Mermaid';
import LLMActions from '../islands-src/components/LLMActions/LLMActions';
import Search from '@site/src/theme/SearchBar';
import JsonTable from '../islands-src/components/elements/Tables/JsonTable';
import RetainedTOC from '@theme/TOCCollapsible';import mobileTOCStyles from '@docusaurus/theme-classic/lib/theme/DocItem/TOC/Mobile/styles.module.css';function TOC(props){return <RetainedTOC {...props} className={'theme-doc-toc-mobile '+mobileTOCStyles.tocMobile}/>;}
import {CodeControls} from './code-controls';
import AnnotatedCode from '../islands-src/components/elements/AnnotatedCode';
import {extractFenceText} from '../islands-src/components/utils/extractElementText';
function AnnotatedCodeComponent({code,...props}){return <AnnotatedCode {...props}><pre><code>{code}</code></pre></AnnotatedCode>;}
export const islandComponents={DesktopTOC,Sidebar,CaptionedImage,EnlargeImage,ZoomableImage,ToolTipTerm,Video,PriorityFairnessSimulator,PriorityFairnessWalkthrough,ServerlessWorkerDemo,StandaloneActivityDemo,TemporalLifecycleDemo,GuidesGrid,IntegrationsGrid,AnnotatedCode:AnnotatedCodeComponent,Retry,Mermaid,LLMActions,Search,JsonTable,TOC,CodeControls};
function wrap(name){const Component=islandComponents[name];return function Island(props){return <span style={{display:'contents'}} data-temporal-island={name} data-props={JSON.stringify(props)}><Component {...props}/></span>;};}
export const RetryIsland=wrap('Retry');
export const MermaidIsland=wrap('Mermaid');
export default wrap('LLMActions');

export const JsonTableIsland=wrap('JsonTable');

const AnnotatedIsland=wrap('AnnotatedCode');export function AnnotatedCodeIsland({children,...props}){return <AnnotatedIsland {...props} code={extractFenceText(children)}/>;}

export const CaptionedImageIsland=wrap('CaptionedImage');
export const EnlargeImageIsland=wrap('EnlargeImage');
export const ZoomableImageIsland=wrap('ZoomableImage');
export const ToolTipTermIsland=wrap('ToolTipTerm');
export const VideoIsland=wrap('Video');
export const PriorityFairnessSimulatorIsland=wrap('PriorityFairnessSimulator');
export const PriorityFairnessWalkthroughIsland=wrap('PriorityFairnessWalkthrough');
export const ServerlessWorkerDemoIsland=wrap('ServerlessWorkerDemo');
export const StandaloneActivityDemoIsland=wrap('StandaloneActivityDemo');
export const TemporalLifecycleDemoIsland=wrap('TemporalLifecycleDemo');
export const GuidesGridIsland=wrap('GuidesGrid');
export const IntegrationsGridIsland=wrap('IntegrationsGrid');

export const SidebarIsland=wrap('Sidebar');

export const TOCIsland=wrap('TOC');export const DesktopTOCIsland=wrap('DesktopTOC');
