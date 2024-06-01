import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import UploadPDFCard from './LandingPage/LandingPage';
import AnalysisPage from './AnalysisPage/Analysispage';
import SignIn from './temp/temp';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<UploadPDFCard/>}/>
        <Route exact path="/analysis" element={<AnalysisPage/>}/>
        <Route exact path="/temp" element={<SignIn/>}/>
      </Routes>
    </Router>
  );
}

export default App;
