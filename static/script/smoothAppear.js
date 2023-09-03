let blocks = document.querySelectorAll(".information_block");

function scrollAppear() {
  blocks.forEach(function (block) {
    var blockPosition = block.getBoundingClientRect().top;
    var screenPosition = window.innerHeight;

    if (blockPosition < screenPosition) {
      block.classList.add("information_block-appear");
    }
  });
}

window.addEventListener("scroll", scrollAppear);
