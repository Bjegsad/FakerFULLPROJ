const cursor = document.querySelector(".cursor");
const allItems = document.querySelectorAll(".btn, a, input, .slider");

document.addEventListener("mousemove", (e) => {
  let leftPosition = e.pageX - window.scrollX + 4;
  let topPosition = e.pageY - window.scrollY + 4;

  cursor.style.left = leftPosition + "px";
  cursor.style.top = topPosition + "px";
});

allItems.forEach((link) => {
  link.addEventListener("mouseenter", () => {
    cursor.classList.add("large");
  });
});

allItems.forEach((link) => {
  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("large");
  });
});
