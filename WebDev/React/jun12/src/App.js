import About from './components/About.js';

var name = "Ichigo"
var surname = "Kurosaki"
var arr= ["Byakuya Kuchiki", "Toshiro Hitsugaya", "Gin Ichimaru", "Kenpachi Zaraki"]
var shinigami = {
  Alias : "Kisuke Urahara",
  Bankai : "Kanon Biraki Benihime Aratame",
  Gotei : 13,
  SoulReapers : ["Byakuya Kuchiki", "Toshiro Hitsugaya", "Gin Ichimaru", "Kenpachi Zaraki"]
}
function App() {
  return (
    <div>
      <header>
        <h1>Subhadeep Mandal</h1>
        {arr[0]}
        <About fname={name} lname={surname} and death={shinigami} />
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
