getReverseColor = (color) => {
  switch (color) {
    case "white":
      return "black";
    case "":
    case "black":
      return "white";
    // red and its reverse
    case "red":
      return "rgb(255, 240, 64)";
    case "rgb(255, 240, 64)":
      return "red";
    // green and its reverse
    case "green":
      return "rgb(32, 255, 128)";
    case "rgb(32, 255, 128)":
      return "green";
    // blue and its reverse
    case "blue":
      return "rgb(64, 240, 255)";
    case "rgb(64, 240, 255)":
      return "blue";
  }
};

let ths = document.querySelectorAll("th");
let tds = document.querySelectorAll("td");
for (let i = 0; i < ths.length; ++i) {
  ths[i].style.textAlign = 'center';
}
for (let i = 0; i < tds.length; ++i) {
  tds[i].style.textAlign = 'center';
}
for (let i = 0; i < ths.length; ++i) {
  ths[i].style.padding = "5px 10px 5px 10px";
  ths[i].addEventListener("mouseenter", (event) => {
    ths[i].style.backgroundColor = "#333";
    ths[i].style.color = "white";
  });
  ths[i].addEventListener("mouseleave", (event) => {
    ths[i].style.backgroundColor = "white";
    ths[i].style.color = "black";
  });
}
for (let i = 0; i < tds.length; ++i) {
  tds[i].style.padding = "5px 10px 5px 10px";
  tds[i].style.textAlign = "center";
  tds[i].addEventListener("mouseenter", (event) => {
    tds[i].style.backgroundColor = "#333";
    tds[i].style.color = getReverseColor(tds[i].style.color);
  });
  tds[i].addEventListener("mouseleave", (event) => {
    tds[i].style.backgroundColor = "white";
    tds[i].style.color = getReverseColor(tds[i].style.color);
  });
}

let tdas = document.querySelectorAll("a.tda");
for (let i = 0; i < tdas.length; ++i) {
  tdas[i].addEventListener("mouseenter", (event) => {
    tdas[i].style.color = "rgb(64, 240, 255)";
  });
  tdas[i].addEventListener("mouseleave", (event) => {
    tdas[i].style.color = "blue";
  });
}
let container = document.querySelector("#tbcontainer");
container.addEventListener("mouseenter", (event) => {
  container.style.border = "2px solid rgb(32,128, 255)";
  container.style.boxShadow = "0 0 6px 4px rgb(32,64, 255)";
});
container.addEventListener("mouseleave", (event) => {
  container.style.border = "2px solid #555";
  container.style.boxShadow = "5px 3px 3px grey";
});
