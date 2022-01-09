// $("h1").css("color", "red");

// select h1 tag with .title as css class
// $("h1.title");

// selection one or many buttons with jQuery
// $("button");

$("h1").css("color");
// rgb(0, 0, 0)

$("h1").css("font-size");
// '32px'

// how to include a class into a tag
$("h1").addClass("big-title");
$("h1").removeClass("big-title");


// $("h1").addClass("big-title margin-50");

// see if an element has a particular class
$("h1").hasClass("margin-50"); // returns boolean


$("h1").text("New text: Bye");

// this will change all the buttons 
$("button").text("Don't click me!");

// this is equivalente to innerHTML from vanilla js
$("button").html("<em> This is italic </em>");


$("img").attr("src");
// drum.png

// set the value of the attribute
$("img").attr("src", "drum2.png");

$("a").attr("href", "http://www.yahoo.com");

// this is an event listener, if we click at the h1, then it will change
$("h1").click(function() {
  $("h1").css("color", "purple");
});

// an example of vanilla javascript
for (var i = 0; i < 5; i++) {
  document.querySelectorAll("button")[i].addEventListener("click", function() {
    document.querySelector("h1").style.color = "purple";
  })
}

// with jQuery it is much easier
$("button").click(function() {
  $("h1").css("color", "red");
});

// keypress event listener
$("input").keypress(function(event) {
  console.log(event.key);
});

// we can monitor if the user is typing any key while using the site
$(document).keypress(function(event) {
  console.log(event.key)
});

$(document).keypress(function(event) {
  $("h1").text(event.key);
});

$("h1").on("mouseover", function() {
  $("h1").css("color", "blue");
});

// how to add html elements?

$("h1").before("<button>New</button>"); // this one is added before, and outside the h1 tag
$("h1").after("<button>After button</button>")
$("h1").prepend("<button>Prepent button</button>") // this is added inside the h1 tag
$("h1").append("<button>Append button</button>")

// to remove all of the button elements 
// $("button").remove()

// when we click any button in the page 
// it will hide all h1
$("button").on("click", function() {
  $("h1").hide();
});

// the opposite effect is show()
$("h1").show()

// if we want the button to make appear and disapper we use toggle
$("button").on("click", function() {
  $("h1").toggle()
});

$("button").on("click", function() {
  $("h1").fadeOut();
  // fadeIn();
  // fadeToggle();
  // slideUp();
  // slideDown();
  // slideToggle();
});

$("button").on("click", function() {
  $("h1").animate({ oppasity: 0.5 });
  // $("h1").animate({margin: 20});
  // $("h1").animate({margin: "20%"});
  // $("h1").slideUp().slideDown().animate({opacity: 0.5});
});