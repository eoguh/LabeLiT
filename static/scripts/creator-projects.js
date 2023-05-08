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
