const users = {
    "John": {
        age: 24,
        desgination: "Senior Golang Developer",
        interests: ["Chess, Reading Comics, Playing Video Games"],
        qualification: "Masters",
        nationality: "Greenland"
    },
    "Ron": {
        age: 19,
        desgination: "Intern - Golang",
        interests: ["Video Games"],
        qualification: "Bachelor",
        nationality: "UK"
    },
    "Wanda": {
        age: 24,
        desgination: "Intern - Javascript",
        interests: ["Piano"],
        qualification: "Bachaelor",
        nationality: "Germany"
    },
    "Rob": {
        age: 34,
        desgination: "Senior Javascript Developer",
        interest: ["Walking his dog, Cooking"],
        qualification: "Masters",
        nationality: "USA"
    },
    "Pike": {
        age: 23,
        desgination: "Python Developer",
        interests: ["Listing Songs, Watching Movies"],
        qualification: "Bachaelor's Degree",
        nationality: "Germany"
    }
}

//Q1 Find all users who are interested in playing video games.
// Q2 Find all users staying in Germany.
names = Object.keys(users)

function videoGamesInterest(names,users){
    let pass = false;
    for(i=0; i<names.length; i++){
        pass = false;
        if(users[names[i]].hasOwnProperty("interests")){
            plays = Object.values(users)[i].interests.join("").split(", ")
            if(plays.includes("Video Games")){
                pass = true
            }else{
                for(j=0;j<plays.length;j++){
                    if(plays[j].includes("Video Games")){
                        pass = true
                    }
                }
            }
        }else{
            plays = Object.values(users)[i].interest.join("").split(", ")//.includes("Playing Video Games")
        }
        if(pass){
            console.log(names[i])
        }
    }
}

function hofVideoGamesInterest(names, users) {
    names.reduce((accumulator, name) => {
      let pass = false;
  
      if (users[name]?.interests) {
        const plays = users[name].interests.join("").split(", ");
        if (plays.includes("Video Games") || plays.some(play => play.includes("Video Games"))) {
          pass = true;
        }
      } else if (users[name]?.interest) {
        const plays = users[name].interest.join("").split(", ");
        pass = plays.includes("Video Games") || plays.some(play => play.includes("Video Games"));
      }
  
      if (pass) {
        console.log(name);
      }
  
      return accumulator; // The accumulator is not used in this case
    }, null);
  }

console.log(hofVideoGamesInterest(names, users))