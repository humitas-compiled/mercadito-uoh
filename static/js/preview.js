const input = document.getElementById("select_images");
const preview = document.getElementById("image_preview");
const prevBtn = document.getElementById("prev_btn");
const nextBtn = document.getElementById("next_btn");

let currentIndex = 0;
let imageUrls = [];

input.addEventListener("change", (e) => {
  const files = Array.from(e.target.files);
  imageUrls = files.map(file => URL.createObjectURL(file));

  if (imageUrls.length > 0) {
    currentIndex = 0;
    preview.src = imageUrls[currentIndex];
    preview.style.display = "block";
    updateNavButtons();
  } else {
    preview.src = "";
    preview.style.display = "none";
    prevBtn.style.display = "none";
    nextBtn.style.display = "none";
  }
});

function updateNavButtons() {
  prevBtn.style.display = currentIndex > 0 ? "block" : "none";
  nextBtn.style.display = currentIndex < imageUrls.length - 1 ? "block" : "none";
}

prevBtn.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
    preview.src = imageUrls[currentIndex];
    updateNavButtons();
  }
});

nextBtn.addEventListener("click", () => {
  if (currentIndex < imageUrls.length - 1) {
    currentIndex++;
    preview.src = imageUrls[currentIndex];
    updateNavButtons();
  }
});