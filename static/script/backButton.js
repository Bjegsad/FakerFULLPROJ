let btn = document.querySelector(".btn_back");
let resulta = document.querySelector(".result");
let forma = document.getElementById("check_news");
let result_icon_hide = document.querySelector(".result_icon");
let result_text_hide = document.querySelector(".result_text");

btn.addEventListener("click", back);

function back() {
  result_icon_hide.style.display = "none";
  result_text_hide.innerHTML = "";

  resulta.style.display = "none";
  forma.style.display = "flex";
}
