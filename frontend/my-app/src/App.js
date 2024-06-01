import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import UploadPDFCard from './LandingPage/LandingPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<UploadPDFCard/>}/>
        <Route exact path="/analysis" element={<UploadPDFCard/>}/>
      </Routes>
    </Router>
    // <div className="App">
    //   <h1 className="text-3xl">
    //     <UploadPDFCard />
    //   </h1>
    // </div>
  );
}

export default App;
