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

    const currentImageNameForComment = document.getElementById ('current-image-name-for-comment');

    function updateCurrentImageName() {
        const currentImage = targetDiv.querySelector('img');
        if (currentImage) {
          const currentImageSrc = currentImage.getAttribute('src');
          const currentImageNameText = currentImageSrc.split('/').pop();
          currentImageName.textContent = currentImageNameText;
          
    
         currentImageNameForComment.textContent = currentImageNameText;
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

    const targetDiv2 = document.querySelector('#small-target-div');


    const currentImageToComment = targetDiv.querySelector('img');



    const commentBox = document.getElementById('comment-box-wrapper');

    const closeCommentBtn = document.getElementById('close-comment');

    function writeComment() {

      commentBox.style.opacity = "100%";
      commentBox.style.height = "400px"
      commentBox.style.zIndex = "999";
    };

    closeCommentBtn.addEventListener('click', function() {
      commentBox.style.opacity = "0";
      commentBox.style.height = "0"
      commentBox.style.zIndex = "-1";
    });


    