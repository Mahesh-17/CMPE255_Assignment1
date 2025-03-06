import React from "react";
import "./App.css";

function App() {
  return (
    <div style={{ margin: "20px" }}>
      <h1>San Jose Crash Data Visualization</h1>

      <section style={{ marginBottom: "40px" }}>
        <h2>Streamlit Dashboard</h2>
        <iframe
          src="https://mkbip97kyau73agra4wtob.streamlit.app/?embed=true"
          width="100%"
          height="800"
          title="Streamlit Dashboard"
          style={{ border: "1px solid #ccc" }}
        ></iframe>
      </section>

      <section>
        <h2>Looker Studio Dashboard</h2>
        <iframe
          src="https://lookerstudio.google.com/embed/reporting/b908c1a1-c9a4-4760-9698-1459709da6c8/page/i3h4E"
          width="100%"
          height="800"
          title="Looker Studio Dashboard"
          style={{ border: "1px solid #ccc" }}
        ></iframe>
      </section>
    </div>
  );
}

export default App;
