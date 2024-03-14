const me = "Subhadeep Mandal";

countCharNormal = function (me) {
  let occurence = {};
  for (i in me) {
    if (occurence.hasOwnProperty(me[i]) == false) {
      occurence[me[i]] = 1;
    } else {
      occurence[me[i]] += 1;
    }
  }
  return occurence;
};

const countChar = function(me) {
    return [...me].reduce((occurrence, char) => {
      occurrence[char] = (occurrence[char] || 0) + 1;
      return occurrence;
    }, {});
  };
console.log(countChar(me));
