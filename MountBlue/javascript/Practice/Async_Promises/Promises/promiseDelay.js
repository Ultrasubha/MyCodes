function delay(time) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Promise resolved after ${time} milliseconds`);
      resolve("yes");
    }, time);
  });
}

delay(2000).then((msg) => {
  console.log(`${msg}Promise has been resolved!`);
});
