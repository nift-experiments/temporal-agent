import React from 'react';
import {MDXProvider} from '@mdx-js/react';
import components from '@theme/MDXComponents';
import {MermaidIsland,DetailsIsland,MDXImageIsland} from './islands';
export default function MDXContent({children}){return <MDXProvider components={{...components,mermaid:MermaidIsland,details:DetailsIsland,img:MDXImageIsland}}>{children}</MDXProvider>;}
