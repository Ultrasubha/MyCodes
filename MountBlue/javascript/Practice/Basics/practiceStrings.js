/* Learn String Methods */

// Modifications

/*
toUpperCase
toLowerCase
trim
trimEnd
trimStart
concat
padEnd
padStart
*/

s = " HeLlo ".trimStart();
s += "wO rLd ".trimEnd();
upper = s.toUpperCase();
lower = upper.toLowerCase();
s = s.concat(" Subho");
padStart = s.padStart(20, "#");
padEnd = s.padEnd(20, "@");
padded = padStart + padEnd;

//Same as python

/*
repeat
replace
slice
split
substring
charCodeAt
*/

s = "subho_deep"
repeatedTwice = s.repeat(2)
replaced = s.replace("o","a")
replacedAll = s.replaceAll("ee", "i");
slice_n_Diced = s.slice(0,5)
splitted = s.split("_")
subStr = s.substring(0,5)
charCodeAt3 = s.charCodeAt(3);


console.log(charCodeAt3);


// Booleans

/* 
endsWith
includes
indexOf
lastIndexOf 
*/

endWith = s.endsWith("bho");
include = s.includes("H");
index = s.indexOf("o");
lastIndex = s.lastIndexOf("O");



//Template literal
msg = "template literal";
template = `What is this ${msg} thingy?`;
