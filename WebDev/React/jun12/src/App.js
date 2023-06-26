import About from './components/About.js';
import Mapping from './Mapping.js';
import Classbased from './components/Classbased.js';
import Functionstate from './components/Functionstate.js';
import FormUncontrolledclass from './components/FormUncontrolledclass.js';
import Formuncontrolledfunction from './components/Formuncontrolledfunction.js';
import Classcontrolled from './components/Classcontrolled.js';
import Functioncontrolled from './components/Functioncontrolled.js';
import Project1 from './components/Project1/Project1.js';
import LifeCycleMethods from './components/Project1/LifeCycleMethods.js';
import ShouldComponentUpdate from './components/Project1/ShouldComponentUpdate.js';
import ColorChange from './Assessment/ColorChange.js';
import FunctionEffect from './Assessment/FunctionEffect.js';
import UseReducer from './Assessment/UseReducer.js';
import Jokes from './Assessment/Jokes.js';

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
      {/*<header>
        <h1>Subhadeep Mandal</h1>
        <About fname={name} lname={surname} dost={friends} death={shinigami} />
      </header>
      {main}
      <Mapping />
      <Classbased name="Sosuke Aizen" arr={["Adfar",25,"React"]}/>
      <Functionstate />
      <FormUncontrolledclass/>
      <Formuncontrolledfunction/>
      <Classcontrolled />
      <Functioncontrolled />
      <Project1/>
      <LifeCycleMethods />
      <ShouldComponentUpdate />
      <ColorChange />
      <FunctionEffect />
      <UseReducer />*/}
      <Jokes />
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
