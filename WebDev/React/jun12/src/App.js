import About from './About.js';
import Adfar from './Adfar.js';

var name = "Adfar"
var surname = "Rashid"
function App() {
  return (
    <div>
      <header>
        <h1>Subhadeep Mandal</h1>
        <About fname={name}/>
        <About fname="Ritik"/>
        <Adfar fname={name} lname={surname} />
      </header>
      {header}
    </div>
  );
}

const header = (
  <header>
        <h1>This is header</h1>
      </header>
);

export default App;
