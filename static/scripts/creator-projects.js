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
