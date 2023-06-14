import React from 'react';
import './App.css';
import {ForceGraph3D} from 'react-force-graph';

// Usage: <CypherViz driver={driver}/>

class CypherViz extends React.Component {

    constructor({driver}) {
      super();
      this.driver = driver;
      this.state = { 
        query: `
        MATCH (g_a: GENE)-[r:SL]->(g_b: GENE) 
        RETURN g_a.hgnc_id as source, labels(g_a) as labels_a, g_b.hgnc_id as target, labels(g_b) as labels_b LIMIT 3
        `,
        data : {nodes:[{name:"HGNC:100", label:"GENE"}, {name:"DB0009", label:"COMPOUND"}],links: [{source:"HGNC:100", target:"DB0009"}]} }
    }

    handleChange = (event) => {
      this.setState({query:event.target.value})
    }
    loadData = async () => {
      let session = await this.driver.session({database:"iokgdata7"});
      let res = await session.run(this.state.query);
      session.close();

      console.log(res);

      let all_nodes = new Set();
      let links = res.records.map(r => {
        let source = r.get("source");
        let target = r.get("target");
        let labels_a = r.get("labels_a");
        let labels_b = r.get("labels_b");
        all_nodes.add({source, labels_a});
        all_nodes.add({target, labels_b});
        return {source, target}});

      const nodes = [];

      for (const element of all_nodes) {
        let name, label;
        if (element.source) {
          name = element.source;
          label = element.labels_a[0];
        } else if (element.target) {
          name = element.target;
          label = element.labels_b[0];
        }
        if (name && label) {
          const index = nodes.findIndex(el => el.name === name && el.label === label);
          if (index === -1) {
            nodes.push({name, label});
          }
        }
      }
      this.setState({ data : {nodes, links}});
    }

    render() {
      return (
        <div class="fullscreen">
          <textarea class = "textfield" value={this.state.query} onChange={this.handleChange}/>
          <button class= "main-button" onClick={this.loadData}>Reload</button>
          <ForceGraph3D class="content" graphData={this.state.data} nodeId="name" 
                    linkCurvature={0.2} nodeAutoColorBy="label" />
        </div>
      );  
    }
  }
  
  export default CypherViz