let navboxes = document.querySelectorAll("div.navbox");
for (let i = 0; i < navboxes.length; ++i) {
  navboxes[i].style.color = "#333";
}
for (let i = 1; i < navboxes.length; ++i) {
  navboxes[i].addEventListener("mouseenter", (event) => {
    navboxes[i].style.fontSize = "30px";
    navboxes[i].style.color = "blue";
    navboxes[i].style.marginTop = "5px";
    navboxes[i].style.marginBottom = "5px";
  });
  navboxes[i].addEventListener("mouseleave", (event) => {
    navboxes[i].style.fontSize = "18px";
    navboxes[i].style.color = "#333";
    navboxes[i].style.marginTop = "15px";
    navboxes[i].style.marginBottom = "10px";
  });
}
