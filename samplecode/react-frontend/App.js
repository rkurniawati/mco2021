import './App.css';
import {useState, useEffect} from 'react'

function App() {
  const [message, setMessage] = useState('Original message')  
  useEffect(() => {
    const fetchMessage = async () => {
      const result = await fetch(
          '/message');
      const fetchedMessage = await result.text()
      setMessage(fetchedMessage);

    }
    fetchMessage();
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>
          {message}
        </p>
      </header>
    </div>
  );
}

export default App;
