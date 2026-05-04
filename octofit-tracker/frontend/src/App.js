import { useEffect, useState } from 'react';
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';
import brandImage from './assets/octofitapp-small.png';
import './App.css';

const API_BASE_URL =
  process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

function Home() {
  const [apiMessage, setApiMessage] = useState('Checking backend API...');

  useEffect(() => {
    const controller = new AbortController();

    async function checkApi() {
      try {
        const response = await fetch(`${API_BASE_URL}/api/`, {
          signal: controller.signal,
        });
        if (!response.ok) {
          throw new Error('API request failed');
        }

        const data = await response.json();
        setApiMessage(data.message || 'API is online.');
      } catch (error) {
        setApiMessage('Backend API unavailable. Start Django on port 8000.');
      }
    }

    checkApi();

    return () => controller.abort();
  }, []);

  return (
    <main className="home-page">
      <section className="hero-card">
        <img src={brandImage} className="hero-image" alt="OctoFit Tracker" />
        <h1>OctoFit Tracker</h1>
        <p className="tagline">
          Train smarter with activity tracking, teams, and competitive
          leaderboards.
        </p>
        <p className="api-status">{apiMessage}</p>
      </section>
    </main>
  );
}

function Placeholder({ title, text }) {
  return (
    <main className="home-page">
      <section className="hero-card">
        <h1>{title}</h1>
        <p className="tagline">{text}</p>
      </section>
    </main>
  );
}

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header className="top-nav">
          <div className="nav-brand">OctoFit</div>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/activities">Activities</Link>
            <Link to="/teams">Teams</Link>
            <Link to="/leaderboard">Leaderboard</Link>
          </nav>
        </header>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/activities"
            element={
              <Placeholder
                title="Activity Logging"
                text="Track workouts and monitor progress over time."
              />
            }
          />
          <Route
            path="/teams"
            element={
              <Placeholder
                title="Team Management"
                text="Create teams and organize group fitness challenges."
              />
            }
          />
          <Route
            path="/leaderboard"
            element={
              <Placeholder
                title="Competitive Leaderboard"
                text="Compare progress and climb the rankings."
              />
            }
          />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
