function bubbleSort(models) {
  var name1, name2;
  var len = models.length;
  var isSwapped = false;

  for (name1 = 0; name1 < len; name1++) {
    isSwapped = false;

    for (name2 = 0; name2 < len - name1 - 1; name2++) {
      if (models[name2] > models[name2 + 1]) {
        var temp = models[name2];
        models[name2] = models[name2 + 1];
        models[name2 + 1] = temp;
        isSwapped = true;
      }
    }
    // IF no two elements were swapped
    // by inner loop, then break
    if (!isSwapped) {
      break;
    }
  }
}
module.exports.bubbleSort = bubbleSort;