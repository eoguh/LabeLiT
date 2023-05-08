var totalImages = document.getElementById("total-images");

var labeledImages = document.getElementById("labeled-images");

if (totalImages.textContent === labeledImages.textContent) {
  labeledImages.style.color = totalImages.style.color;
}


const newAnnotator = document.getElementById('new-annotator')
popUp = document.getElementById('popup')

popUpExit = document.getElementById('popup-exit')

body = document.getElementsByTagName('body');

newAnnotator.addEventListener('click', () => {
document.getElementById("myNav").style.width = "100%";
})

popUpExit.addEventListener('click', () => {
document.getElementById("myNav").style.width = "0%";
});
