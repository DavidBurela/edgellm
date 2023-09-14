import ReactDOM from 'react-dom';
import { FluentProvider, teamsDarkTheme } from '@fluentui/react-components';

import App from './App';
import "./index.css";

ReactDOM.render(
  <FluentProvider theme={teamsDarkTheme}>
    <App />
  </FluentProvider>,
  document.getElementById('root'),
);