const {parse} = require("csv-parse")
const fs = require("fs")

const parser = parse({column:true},(err,dt)=>{
    if(err){
        
    }
    for(item of dt){
        console.log(item);
    }
})

fs.createReadStream("data.csv").pipe(parser)