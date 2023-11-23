const app = document.getElementById("app");
let html = "";

const headings = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

for (const headingElement of headings) {
    const el = document.createElement(headingElement);
    el.innerText = 'Esto es una etiqueta de html ' + headingElement;

    app.appendChild(el);
}