// tutorial notes based on:
// https://www.youtube.com/watch?v=Rs_rAxEsAvI&ab_channel=freeCodeCamp.org

const canvas = document.getElementById("my-canvas");
// make the canvas height variable depending on the size of the
// windows of the user
canvas.height = window.innerHeight;
canvas.width = 200;
// we fix the road width because we'll use more space later
// to show the neural network

// this is the drawing context
const ctx = canvas.getContext("2d");

// the Car class is defined in another file called car.js
// this file needs to be imported by the html
const car = new Car(100, 100, 30, 50);
car.draw(ctx);

// const car2 = new Car(20, 30, 30, 50);
// car2.draw(ctx);

