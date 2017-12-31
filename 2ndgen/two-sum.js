'use strict'

var myMap = new Map();

var twoSum = (nums, target) => {
    for (var i=0; i < nums.length; i++) {
        myMap.set(nums[i], i);
    }

    for (var i=0; i< nums.length; i++) {
        var complement = target - nums[i];
        if (myMap.get(complement) && myMap.get(complement) != i) {
            return [i, myMap.get(complement)];
        }
    }
    throw 'Could not find two sum';
}

var list = [3, 2, 4];
var target = 6;
console.log(twoSum(list, target));