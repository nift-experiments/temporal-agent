import React from 'react';
import {MemoryRouter,useHistory} from 'react-router-dom';
import {HelmetProvider} from 'react-helmet-async';
import {DocusaurusContextProvider} from '@docusaurus/core/lib/client/docusaurusContext';
import {BrowserContextProvider} from '@docusaurus/core/lib/client/browserContext';
import {ColorModeProvider,ScrollControllerProvider} from '@docusaurus/theme-common/internal';
import {DocsPreferredVersionContextProvider,DocProvider} from '@docusaurus/plugin-content-docs/client';
function NavigationBridge(){const history=useHistory();React.useEffect(()=>history.listen((location,action)=>{const target=location.pathname+location.search+location.hash;if(location.pathname===window.location.pathname){window.history[action==='PUSH'?'pushState':'replaceState'](null,'',target);}else window.location.assign(target);}),[history]);return null;}
export function Context({metadata,frontMatter={},contentTitle,children}){return <HelmetProvider><MemoryRouter initialEntries={[typeof window==='undefined'?metadata.permalink:window.location.pathname+window.location.search+window.location.hash]}><NavigationBridge/><DocusaurusContextProvider><DocsPreferredVersionContextProvider><BrowserContextProvider><ColorModeProvider><ScrollControllerProvider><DocProvider content={{metadata,frontMatter,assets:{},contentTitle,toc:[]}}>{children}</DocProvider></ScrollControllerProvider></ColorModeProvider></BrowserContextProvider></DocsPreferredVersionContextProvider></DocusaurusContextProvider></MemoryRouter></HelmetProvider>;}
