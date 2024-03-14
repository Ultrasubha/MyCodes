function delay(n, callBack) {
  setTimeout(() => {
    if(n%2){
        callBack(new Error("Go away odd numbers"),23.5)
    }else{
        callBack(null, 3.414);
    }
  }, n * 1000);
}

delay(3, (err, data) => {
  if (err) {
    console.error("Error : ", err);
  } else {
    console.log("The data is ", data);
  }
});
