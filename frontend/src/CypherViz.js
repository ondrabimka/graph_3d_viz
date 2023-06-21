import React from 'react';
import './App.css';
import React, { useEffect, useState } from "react";
import {ForceGraph3D} from 'react-force-graph';

// Usage: <CypherViz driver={driver}/>

class CypherViz extends React.Component {

  constructor({driver}) {
    super();
    this.driver = driver;
    this.state = {
      query: `MATCH n RETURN n LIMIT 25`,
      data : {nodes:[{name:"HGNC:100", label:"GENE"}, {name:"DB0009", label:"COMPOUND"}],links: [{source:"HGNC:100", target:"DB0009"}]} }
  }

  handleChange = (event) => {
    this.setState({query:event.target.value})
  }

  loadData = async () => {
    const response = await fetch('http://localhost:5000/cypher', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({query:this.state.query}),
    });
    console.log(response);
    const body = await response.json();
    console.log(body);
    setText(body);
    this.setState({data:body});
  }

  render() {
    return (
      <div class="fullscreen">
        <textarea class = "textfield" value={this.state.query} onChange={this.handleChange}/>
        <button class= "main-button" onClick={this.loadData}>Reload</button>
        <ForceGraph3D class="content" graphData={this.state.data} nodeId="name"
                  linkCurvature={0.2} nodeAutoColorBy="label" />
        <t1>Current data: {this.state.data}</t1>
      </div>
    );
  }
}

export default CypherViz;
