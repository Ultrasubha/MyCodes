let p = new Promise((resolve, reject) => {
  val = 2 + 2;
  if (val === 5) {
    resolve("Life Bindas!");
  } else {
    reject("Full loss hain bhai");
  }
});

p.then((msg) => {
  console.log(`Dekh Bhai - ${msg}`);
}).catch((msg) => {
  console.error(`Ab kya kare - ${msg}`);
});
