import React from 'react';
import {createRoot} from 'react-dom/client';
import './index.css';
import App from './App';
import * as neo4j from  'neo4j-driver';

const driver = neo4j.driver('bolt://10.4.2.7:7687', neo4j.auth.basic('neo4j','password'))

const rootElement = 
document.getElementById('root');
const root = createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App driver={driver}/>
  </React.StrictMode>);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
