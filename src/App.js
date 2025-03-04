import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>San Jose Crash Data Visualization</h1>
        <nav>
          <a
            href="https://mkbip97kyau73agra4wtob.streamlit.app/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Streamlit App
          </a>
          <a
            href="https://lookerstudio.google.com/reporting/b908c1a1-c9a4-4760-9698-1459709da6c8/page/i3h4E"
            target="_blank"
            rel="noopener noreferrer"
          >
            Looker Studio Dashboard
          </a>
        </nav>
      </header>

      <section id="streamlit">
        <h2>Streamlit App</h2>
        <p>
          <a
            href="https://mkbip97kyau73agra4wtob.streamlit.app/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Click here to open Streamlit App
          </a>
        </p>
      </section>

      <section id="looker-studio">
        <h2>Looker Studio Dashboard</h2>
        <p>
          <a
            href="https://lookerstudio.google.com/reporting/b908c1a1-c9a4-4760-9698-1459709da6c8/page/i3h4E"
            target="_blank"
            rel="noopener noreferrer"
          >
            Click here to open Looker Studio Dashboard
          </a>
        </p>
      </section>
    </div>
  );
}

export default App;
