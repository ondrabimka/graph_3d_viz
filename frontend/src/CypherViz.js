import React from 'react';
import './App.css';
import {ForceGraph3D} from 'react-force-graph';

// Usage: <CypherViz driver={driver}/>

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

  handleChange = (event) => {
    this.setState({query:event.target.value})
  }

  loadData = async () => {
    const response = await fetch('http://0.0.0.0:8001/get_whole_graph');
    const body = await response.json();
    this.setState({data:body});
  }

  render() {
    return (
      <div class="fullscreen">
        {/* <textarea class = "textfield" value={this.state.query} onChange={this.handleChange}/>
        <button class= "main-button" onClick={this.loadData}>Reload</button> */}
        <ForceGraph3D class="content" graphData={this.state.data} nodeId="id"
                  linkCurvature={0.2} nodeAutoColorBy="label" />
      </div>
    );
  }
}

export default CypherViz;
