'use strict';

function mergeSort(arr, leftIndex, rightIndex) {
  if (rightIndex > leftIndex) {
    // console.log(arr);
    var middleIndex = (leftIndex + rightIndex) / 2;
    var middleIndex = Math.floor(middleIndex);

    mergeSort(arr, leftIndex, middleIndex);
    mergeSort(arr, middleIndex + 1, rightIndex);
    merge(arr, leftIndex, middleIndex, rightIndex);
  }
};

function merge(arr, l, m, r) {
  // given an array arr, there are known subarrays from l to m, to m+1 to r
  // iterate through subarrays, then take the lower value and replace original arr

  // number of sorted elements to merge
  var n1 = m - l + 1;
  var n2 = r - m;

  var L = [];
  var R = [];


  for (var i=0; i < n1; i++) {
    L.push(arr[l + i]);
  }

  for (var j=0; j < n2; j++) {
    if (arr[m + 1 + j]) {
      R.push(arr[m + 1 + j]);
    }
  }

  var i = 0;
  var j = 0;
  var k = l;
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i += 1;
    } else {
      if (R[j] !== undefined) {
        arr[k] = R[j];
      }
      j += 1;
    }
    k += 1;
  }

  while (i < n1) {
    arr[k] = L[i];
    i += 1;
    k += 1;
  }

  while (j < n2) {
    arr[k] = R[j];
    j += 1;
    k += 1;
  }
};


var test_arr = [38,27,43,3,9,82,10];
console.log(test_arr);
mergeSort(test_arr, 0, test_arr.length)
console.log(test_arr);