import React from 'react';
import './App.css';
import {ForceGraph3D} from 'react-force-graph';

class CypherViz extends React.Component {

  constructor() {
    super();
    this.state = {
      query: `MATCH n RETURN n LIMIT 25`,
      data: {nodes:[], links:[]}
    }
  }

  componentDidMount() {
    this.loadData();
  }

  loadData = async () => {
    const response = await fetch('http://localhost:8000/get_whole_graph');
    const body = await response.json();
    this.setState({data: body});
  }

  render() {
    return (
      <div class="fullscreen">
        <button class= "main-button" onClick={this.loadData}>Reload Graph</button>
        <ForceGraph3D class="content" graphData={this.state.data} nodeId="id"
                  linkCurvature={0.2} nodeAutoColorBy="label" />
      </div>
    );
  }
}

export default CypherViz;
