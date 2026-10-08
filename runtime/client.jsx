import './static-controls';
import React from 'react';
import {hydrateRoot} from 'react-dom/client';
import {Context} from './context';
import {islandComponents} from './islands';
const metadata=JSON.parse(document.getElementById('temporal-page-data').textContent);
const mounted=new WeakSet();function mount(){for(const target of document.querySelectorAll('[data-temporal-island]')){if(mounted.has(target)||target.parentElement.closest('[data-temporal-island]'))continue;const Component=islandComponents[target.dataset.temporalIsland];if(!Component)throw Error('Unknown Temporal island '+target.dataset.temporalIsland);const props=JSON.parse(target.dataset.props);if(target.dataset.temporalIsland==='CodeControls')props.codeElement=target.parentElement.querySelector('pre');hydrateRoot(target,<Context metadata={metadata}><Component {...props}/></Context>);mounted.add(target);}}mount();window.addEventListener('resize',mount);
