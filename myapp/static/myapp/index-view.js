// image interaction with user.
let image = document.querySelector("img");
image.addEventListener("mouseenter", (event) => {
  image.style.width = "240px";
  image.style.height = "216px";
  image.style.boxShadow = "3px 5px 5px goldenrod";
  image.style.border = "3px solid blue";
});
image.addEventListener("mouseleave", (event) => {
  image.style.width = "200px";
  image.style.height = "180px";
  image.style.boxShadow = "3px 5px 5px #555";
  image.style.border = "0";
});

// psuedo button insteraction with user.
let buttons = document.querySelectorAll("div.bta"); // they are psuedo buttons, though.
for (let i = 0; i < buttons.length; ++i) {
  buttons[i].addEventListener("mouseenter", (event) => {
    buttons[i].style.height = "50px";
    buttons[i].style.width = "200px";
    buttons[i].style.border = "3px solid red";
    buttons[i].style.boxShadow = "3px 5px 5px goldenrod";
  });
  buttons[i].addEventListener("mouseleave", (event) => {
    buttons[i].style.height = "40px";
    buttons[i].style.width = "160px";
    buttons[i].style.border = "0";
    buttons[i].style.boxShadow = "3px 5px 5px #555";
  });
}
