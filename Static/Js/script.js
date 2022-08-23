setTimeout(() => {
  if (document.querySelector("#Remove").innerText === null) {
  } else {
    document.querySelector("#Remove").innerText = "";
  }
}, 3000);

function Changetheme() {
  document.querySelector(".Body").style.backgroundColor = "#292929";
  document.querySelector(".Footer").style.backgroundColor = "#292929";
  document.querySelector(".Container").style.color = "White";
}

function Transform() {
  document.querySelector(".Over").classList.toggle("Completedtask");
}

document.getElementById("Password").addEventListener("change", myFunction);

function myFunction() {
  var x = document.getElementById("Password").value;
  if (x.length == 0) {
    document.getElementById("weak").innerText = "";
    document.getElementById("strong").innerText = "";
    document.getElementById("medium").innerText = "";
  } else if (x.length < 5) {
    document.getElementById("weak").innerText = "Your password is too weak 😒";
    document.getElementById("strong").innerText = "";
    document.getElementById("medium").innerText = "";
  } else if (x.length <= 9) {
    document.getElementById("weak").innerText = "";
    document.getElementById("medium").innerText = "Your password ok 😐";
    document.getElementById("strong").innerText = "";
  } else {
    document.getElementById("weak").innerText = "";
    document.getElementById("medium").innerText = "";
    document.getElementById("strong").innerText = "Your password is strong 🙂";
  }
}
