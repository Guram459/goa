const html = document.querySelector('html');
const button = document.getElementById('dark-mode');

button.addEventListener('click', function () {
    html.classList.toggle('dark');
});

