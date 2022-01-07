// alert("Hello...")

// document.querySelector("h1").innerHTML = "Good Bye :)";


function main() {
  // below are some examples of DOM manipulation

  getElementsByTagName() // return an array
  document.getElementsByTagName("li")[2].style.color = "purple"

  document.getElementsByClassName("btn");
  document.getElementsByClassName("btn")[0].style.color = "red";

  document.getElementById("list"); // singular, just one id per page

  document.querySelector("#list") // like in css, ids need to use #
  document.querySelector(".list") // for class we need .
  document.querySelector("li a") // hierarchical css
  document.querySelector("li.item") // combinate selectors

  // the querySelector just fetches the first match
  document.querySelectorAll("li.item") // this will bring an array


  document.querySelector("#list .item").style.color = "orange";
  document.querySelector("#list .item").getElementsByTagName("a")[0]
  document.querySelector("#list .item").getElementsByTagName("a")[0].style.color = "red"

  // text-decoration: none 

  document.querySelector("h1").style.color = "red";
  document.querySelector("h1").style.fontSize = "5rem";
  document.querySelector(".btn").style.visibility = "hidden";
  document.querySelector(".btn").style.backgroundColor = "yellow";

  document.querySelector("button").classList;
  // we can add new classes to a certain element
  document.querySelector("button").classList.add("invisible");
  // we can change the appearance of the page by adding new CSS classes
  document.querySelector("button").classList.remove("invisible");
  // toggle is used to add if the class is not there, or remove if the class is there
  document.querySelector("button").classList.toggle("invisible");
  // this is good for the separation of concerns

  document.querySelector("h1").classList.toggle("huge");
  document.getElementById("title").textContent = "Hi There!";
  document.getElementById("title").innerHTML
    // with innerHTML we have access to the html
    // and not only the text inside the tag
  document.getElementById("title").innerHTML = "<em>Good Bye :(</em>"

  // HTML attributes from specific tags
  document.querySelector("a");
  document.querySelector("a").attributes;
  document.querySelector("a").getAttribute("href");
  document.querySelector("a").setAttribute("href", "https://www.bing.com");
}