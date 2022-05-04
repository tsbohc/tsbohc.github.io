let posts = []

let input = document.getElementById('s');
let sections
let main

function init() {
  main = document.getElementsByTagName('main')[0];
  sections = main.getElementsByTagName('section');

  if (posts.length == 0) {
    console.log("init")
    var title, summary, tags;
    for (var i = 0; i < sections.length; i++) {
      title = sections[i].getElementsByTagName('a')[0].innerText.toLowerCase();
      summary = sections[i].getElementsByTagName('div')[0].innerText.toLowerCase();
      tags = sections[i].getElementsByTagName('span')[0].innerText.toLowerCase();
      posts.push(title + ' ' + summary + ' ' + tags);
    }
  }
}

function search() {
  init()
  let filter = input.value.toLowerCase();
  for (var i = 0; i < posts.length; i++) {
    if (posts[i].indexOf(filter) > -1) {
      sections[i].style.display = "";
    } else {
      sections[i].style.display = "none";
    }
  }
}

input.addEventListener('keyup', (event) => {
  if (location.pathname == '/') {
    search();
  } else if (event.key === 'Enter') {
    let url = new URL(location.origin);
    let params = new URLSearchParams(url.search);
    params.set('query', input.value.toLowerCase());
    window.location.href = '/?' + params.toString();
  }
});

const url = new URL(location);
const query = url.searchParams.get('query');

if (query) {
  input.value = query
  search();
}

// // javascript bad
//
// function wrapWords(str) {
//   return str.replace(/(?:\w|[-]\w)+/g, "<span class='tooltip' data-tooltip='$&'>$&</span>");
// }
//
// // lazy
//
// function wrapWords2(str) {
//   return str.replace(/(?:\w|[-]\w)+/g, "<span class='toki-pona-tooltip' data-tooltip='$&'>$&</span>");
// }
//
// let linjapona = document.getElementsByTagName('del');
//
// for (var i = 0; i < linjapona.length; i++) {
//   linjapona[i].innerHTML = wrapWords2(linjapona[i].innerText)
// }
//
// let tokipona = document.getElementsByClassName('toki-pona');
//
// for (var i = 0; i < tokipona.length; i++) {
//   tokipona[i].innerHTML = wrapWords2(tokipona[i].innerText)
// }
