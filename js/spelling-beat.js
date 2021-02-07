'use strict';


function findWords(letters) {
    // regex: /^[abcdefg]*a[abcdefg]*$/
    let regex = new RegExp('^[' + letters + ']*' + letters[0] + '[' + letters + ']*$');
    return words.filter(word => word.match(regex));
}

let filterPangrams = word => (new Set(word.split('')).size == 7);

function solve() {
    let letters = document.getElementById("letters").value.toLowerCase();
    var words = findWords(letters);
    // sort with pangrams first
    words.sort((a,b) => {
        let aIsPangram = new Set(a.split('')).size == 7;
        let bIsPangram = new Set(b.split('')).size == 7;

        return aIsPangram !== bIsPangram ? bIsPangram - aIsPangram : a.localeCompare(b);
    });

    let pangrams = new Set(words.filter(filterPangrams));

    var wordsList = document.createElement("ul");
    for (const word of words) {
        var item = document.createElement("li");
        item.textContent = word;
        if (pangrams.has(word)) {
            item.setAttribute("class", "pangram");
        }
        wordsList.appendChild(item);
    }
    let wordsDiv = document.getElementById("words");
    wordsDiv.innerHTML = "";
    wordsDiv.appendChild(wordsList);
    window.location.hash = '#' + letters.toUpperCase();
}

window.onload = function() {
    if (window.location.hash && window.location.hash.length == 8) {
        document.getElementById("letters").value = window.location.hash.substring(1);
        solve();
    }
};