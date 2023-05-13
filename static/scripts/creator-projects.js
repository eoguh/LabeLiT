
//This block of code brings a popup to create a new project

const newProject = document.getElementById('new-project')
popUp = document.getElementById('popup')

popUpExit = document.getElementById('popup-exit')

body = document.getElementsByTagName('body');

newProject.addEventListener('click', () => {
document.getElementById("myNav").style.width = "100%";
})

popUpExit.addEventListener('click', () => {
document.getElementById("myNav").style.width = "0%";
});

//End of create new project popup

//This code creates a popup to edit project name
const newProjectNameForm = document.getElementById("edit-project-name-form");

function editProjectName() {
    
    newProjectNameForm.style.display = "flex";
};

function closeEditNameForm() {
    newProjectNameForm.style.display = "none";
};

function updateProjectName() {
    var newProjectName = document.getElementById("input-new-project-name");
    var oldProjectName = document.getElementById("project-name");

    // Update the project name with the new input value
    oldProjectName.textContent = newProjectName.value;
};

//This code creates a popup to edit the list of labels

const editLabelBox = document.getElementById("label-list-dialog");

function editLabels() {

    editLabelBox.style.opacity = "100%";
    editLabelBox.style.zIndex = "999";
};


// Function to add a label
//Get the list of labels from localStorage or create an empty array if it doesn't exist
var labelList = JSON.parse(localStorage.getItem("labelList")) || [];

// Function to save the list of labels to localStorage
function saveLabelList() {
  localStorage.setItem("labelList", JSON.stringify(labelList));
}

// Function to create a new label item
function createLabelItem(labelText) {
  var newLabelItem = document.createElement("li");
  var deleteIcon = document.createElement("i");
  var space = document.createTextNode("\u00A0");
  var newLabelContent = document.createTextNode(labelText);

  deleteIcon.className = "fa fa-close";
  deleteIcon.addEventListener("click", function() {
    var index = labelList.indexOf(labelText);
    if (index > -1) {
      labelList.splice(index, 1);
      saveLabelList();
    }
    this.parentNode.remove();
  });

  newLabelItem.appendChild(deleteIcon);
  newLabelItem.appendChild(space);
  newLabelItem.appendChild(newLabelContent);
  return newLabelItem;
}

// Function to add a new label to the list
function addLabel() {
  var inputLabel = document.getElementById("input-label");
  var newLabel = inputLabel.value.trim();

  if (newLabel) {
    var labelListElement = document.getElementById("listOfLabels");
    var newLabelItem = createLabelItem(newLabel);

    labelListElement.appendChild(newLabelItem);
    labelList.push(newLabel);
    saveLabelList();
    inputLabel.value = "";
  }
}

// Function to load the list of labels from localStorage
function loadLabelList() {
  var labelListElement = document.getElementById("listOfLabels");

  for (var i = 0; i < labelList.length; i++) {
    var newLabelItem = createLabelItem(labelList[i]);
    labelListElement.appendChild(newLabelItem);
  }
}

function closeAddLabel() {
  var inputLabel = document.getElementById("input-label");
  inputLabel.value = "";
}

loadLabelList();

function closeAddLabel() {
  editLabelBox.style.zIndex = "-1";
  editLabelBox.style.opacity = "0";
  
}
