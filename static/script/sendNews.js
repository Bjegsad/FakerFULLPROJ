let form = document.querySelector("form");
let result = document.querySelector(".result");
let result_text = document.querySelector(".result_text");
let result_icon = document.querySelector(".result_icon");
var loader = document.getElementById("loader");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  result.style.display = "flex";
  form.style.display = "none";
  loader.style.display = "block";

  const formData = new FormData(form);

  fetch("/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      let res_text;
      if (data["label"] == true) {
        res_text = `Ваша новость достоверна с вероятностью ${data["score"]}`;
        result_icon.classList.remove("result_icon-false", "result_icon-error");
        result_icon.classList.add("result_icon-true");
      } else {
        res_text = `Ваша новость не достоверна с вероятностью ${data["score"]}`;
        result_icon.classList.remove("result_icon-true", "result_icon-error");
        result_icon.classList.add("result_icon-false");
      }
      loader.style.display = "none";
      result_icon.style.display = "block";
      result_text.innerHTML = res_text;
    })
    .catch((error) => {
      // Обработка ошибок
      result_icon.classList.remove("result_icon-false", "result_icon-true");
      result_icon.classList.add("result_icon-error");
      loader.style.display = "none";
      result_icon.style.display = "block";
      result_text.innerHTML = "Возникла Ошибка! Попробуйте еще раз";
    });
});
