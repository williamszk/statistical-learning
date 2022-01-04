// The event listener will listen to some event like a click
// this is different from a program running from top to bottom

var numDrumButtons = document.querySelectorAll(".drum").length;

for (var i = 0; i < numDrumButtons; i++) {
  document.querySelectorAll(".drum")[i].addEventListener("click", function() {
    this.style.color = "white";
  });
}

// var audio = new Audio("sounds/crash.mp3");
// audio.play();