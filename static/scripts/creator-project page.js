const images = Array.from(document.querySelectorAll('#image-container img'));
const targetDiv = document.querySelector('#target-div');
const previousButton = document.querySelector('#previous-button');
const nextButton = document.querySelector('#next-button');
let currentIndex = -1;

function init() {
    const defaultImage = images[0];
    const clonedImage = defaultImage.cloneNode(true);
    targetDiv.appendChild(clonedImage);
    currentIndex = 0;
    updateCurrentImageName();
    toggleButtons();
  }


images.forEach(image => {
  image.addEventListener('click', function() {
    const clonedImage = image.cloneNode(true);
    const existingImage = targetDiv.querySelector('img');
    if (existingImage) {
      targetDiv.removeChild(existingImage);
    }
    targetDiv.appendChild(clonedImage);
    currentIndex = images.indexOf(image);
    updateCurrentImageName();
    toggleButtons();
  });
});

previousButton.addEventListener('click', function() {
  if (currentIndex > 0) {
    currentIndex--;
  } else {
    currentIndex = images.length - 1;
  }
  const existingImage = targetDiv.querySelector('img');
  if (existingImage) {
    targetDiv.removeChild(existingImage);
  }
  const previousImage = images[currentIndex];
  const clonedImage = previousImage.cloneNode(true);
  targetDiv.appendChild(clonedImage);
  updateCurrentImageName();
  toggleButtons();
});

nextButton.addEventListener('click', function() {
  if (currentIndex < images.length - 1) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  const existingImage = targetDiv.querySelector('img');
  if (existingImage) {
    targetDiv.removeChild(existingImage);
  }
  const nextImage = images[currentIndex];
  const clonedImage = nextImage.cloneNode(true);
  targetDiv.appendChild(clonedImage);
  updateCurrentImageName();
  toggleButtons();
});

const currentImageName = document.getElementById('current-image-name');

function updateCurrentImageName() {
    const currentImage = targetDiv.querySelector('img');
    if (currentImage) {
      const currentImageSrc = currentImage.getAttribute('src');
      const currentImageNameText = currentImageSrc.split('/').pop();
      currentImageName.textContent = currentImageNameText;
    }
  }

function toggleButtons() {
  if (currentIndex === 0) {
    previousButton.disabled = true;
  } else {
    previousButton.disabled = false;
  }
  if (currentIndex === images.length - 1) {
    nextButton.disabled = true;
  } else {
    nextButton.disabled = false;
  }
}

// Disable previous button initially
toggleButtons();

init();




// Get all the image elements in the div
const anotators = document.querySelectorAll('#anotators img');

// Add a click event listener to each image element
anotators.forEach(image => {
  image.addEventListener('click', (event) => {
    // Create a new div element to display the dialogue box
    const dialogBox = document.createElement('div');
    dialogBox.classList.add('dialog-box');

    // Set the dimensions of the dialogue box
    dialogBox.style.width = '300px';
    dialogBox.style.height = '300px';

    // Position the dialogue box close to the clicked image
    const imageOffset = image.getBoundingClientRect();
    dialogBox.style.top = imageOffset.top + 'px';
    dialogBox.style.left = imageOffset.right + 'px';

    // Add the dialogue box to the DOM
    document.body.appendChild(dialogBox);

    // Add a click event listener to the document object
    document.addEventListener('click', (event) => {
      // Remove the dialogue box if the click event was not on the dialogue box or the image
      if (!dialogBox.contains(event.target) && event.target !== image) {
        dialogBox.remove();
      }
    });
  });
});
