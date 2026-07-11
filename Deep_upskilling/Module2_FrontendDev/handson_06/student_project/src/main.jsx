import React from "react";
import ReactDOM from "react-dom/client";
import "./App.css";
import EnrollmentProvider from "./context/EnrollmentContext";
import { Provider } from "react-redux";
import { store } from "./store/store";
import { BrowserRouter } from "react-router-dom";

import App from "./App";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <Provider store={store}>

    <BrowserRouter>
      <EnrollmentProvider>
        <App />
      </EnrollmentProvider>
    </BrowserRouter>

  </Provider>



);