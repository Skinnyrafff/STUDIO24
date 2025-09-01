import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ClientView from './views/ClientView';
import OwnerView from './views/OwnerView';
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          {/* Por ahora, la vista del dueño será la principal para el desarrollo */}
          <Route path="/" element={<OwnerView />} />
          <Route path="/client" element={<ClientView />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App
