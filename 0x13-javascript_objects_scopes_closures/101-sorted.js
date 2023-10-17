#!/usr/bin/node
const { dict } = require('./101-data');

const totalList = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = Array.from(new Set(vals));
const newDict = {};

for (const val of valsUniq) {
  const list = totalList.filter(([_, v]) => v === val).map(([k, _]) => k).reverse();
  newDict[val] = list;
}

console.log(newDict);
