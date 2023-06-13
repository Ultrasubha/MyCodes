import About from './components/About.js';

var name = "Ichigo"
var surname = "Kurosaki"
var friends= ["Uryu Ishida","Orihime Inoue","Yasutora Sado"]
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
        <About fname={name} lname={surname} dost={friends} death={shinigami} />
      </header>
      {main}
    </div>
  );
}

const myStyle = {
  color : 'red',
  backgroundColor:"pink"
}

const main = (
  <q style={myStyle}>Woah! This is boring</q>
);
export default App;
