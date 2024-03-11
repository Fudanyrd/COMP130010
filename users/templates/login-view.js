// this script intends to further beautify this login page.
// for some reasons, using <script src="login-view.js"> won't work...
let inputs = document.querySelectorAll("input");
let lbs = document.querySelectorAll("label");

inputs[1].placeholder = " Username";
inputs[2].placeholder = " Password";
inputs[1].style.width = inputs[2].style.width = "500px";
inputs[1].style.height = inputs[2].style.height = "30px";
inputs[1].style.borderRadius = inputs[2].style.borderRadius = "5px";
inputs[1].style.margin = "20px 0 10px 0";
inputs[2].style.margin = "10px 0 20px 5px";
inputs[1].style.boxShadow = inputs[2].style.boxShadow = "3px 5px 5px grey";
inputs[1].style.border = inputs[2].style.border = "1px solid black";
// inputs[2].style.marginLeft = '5px';

// add listener for input fields.
inputs[1].addEventListener("mouseenter", (event) => {
  inputs[1].style.border = "4px solid blue";
  lbs[0].style.color = "goldenrod";
  lbs[0].style.fontSize = "20px";
});
inputs[1].addEventListener("mouseleave", (event) => {
  inputs[1].style.border = "1px solid black";
  lbs[0].style.color = "#333";
  lbs[0].style.fontSize = "15px";
});
inputs[2].addEventListener("mouseenter", (event) => {
  inputs[2].style.border = "4px solid blue";
  lbs[1].style.color = "goldenrod";
  lbs[1].style.fontSize = "20px";
});
inputs[2].addEventListener("mouseleave", (event) => {
  inputs[2].style.border = "1px solid black";
  lbs[1].style.color = "#333";
  lbs[1].style.fontSize = "15px";
});

button = document.querySelector("button");
button.addEventListener("mouseenter", (event) => {
  button.style.backgroundColor = "rgb(0, 64, 192)";
  button.style.width = "140px";
  button.style.height = "60px";
});
button.addEventListener("mouseleave", (event) => {
  button.style.backgroundColor = "#337ab7";
  button.style.width = "120px";
  button.style.height = "50px";
});
