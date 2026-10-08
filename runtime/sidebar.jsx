import React from 'react';import Items from '@theme/DocSidebarItems';import navigation from '@temporal/navigation';
export default function Sidebar({sidebarKey,path}){return <ul className="theme-doc-sidebar-menu menu__list"><Items items={navigation[sidebarKey]||[]} activePath={path} level={1}/></ul>;}
