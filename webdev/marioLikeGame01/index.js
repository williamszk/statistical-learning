// I want to build this game using JavaScript vanilla
// I think that I need to use global variables to keep the state...
// Maybe with this exercise I'll be able to find out how to build a game without global variables

const numGroundTiles = 20;

function sleep(ms) {
  /*
  await sleep(700);
  */
  return new Promise(resolve => setTimeout(resolve, ms));
}

function includeMario() {
  let marioPlayer = '<div class="mario-div"><img src="images/mario1.png" alt="mario1" class="mario-img"></div>';
  document.querySelector("#mario-player").innerHTML = marioPlayer;
}

function createGround() {
  // let theTerrain = document.querySelector("#the-terrain").innerHTML;
  let theTerrain = '<div class="ground-terrain-div"><img src="images/groundTerrain01.png" alt="groundTerrain01" class="terrain-img"></div>';

  // document.querySelector("#the-terrain").querySelector(".ground-terrain-div").style;
  for (let i = 0; i < numGroundTiles; i++) {
    document.querySelector("#the-terrain").innerHTML += theTerrain;
  }
  let terrainArray = document.querySelector("#the-terrain").querySelectorAll(".ground-terrain-div");
  for (let i = 0; i < numGroundTiles; i++) {
    terrainArray[i].style.left = (39 * i) + "px";
  }
}


createGround();
includeMario();

// console.log(window.screen.width);
// console.log(window.screen.height);