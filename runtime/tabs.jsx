import React from 'react';
import Tabs from '@theme-original/Tabs';
export default function TabGroup(props){const values=React.Children.toArray(props.children).map(child=>child.props?.value);return <span style={{display:'contents'}} data-temporal-tab-group={props.groupId||undefined} data-temporal-tab-values={JSON.stringify(values)}><Tabs {...props}/></span>;}
