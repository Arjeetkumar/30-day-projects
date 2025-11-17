let expressionDiv = document.getElementById("expression");
let resultDiv = document.getElementById("result");

let current = "";
let prev = "";
let op = null;

function update() {
    expressionDiv.textContent = prev + " " + (op || "") + " " + current;
    resultDiv.textContent = current || "0";
}

function appendNumber(num) {
    if (num === "." && current.includes(".")) return;
    current += num;
    update();
}

function chooseOp(operation) {
    if (current === "") return;
    if (prev !== "") compute();
    op = operation;
    prev = current;
    current = "";
    update();
}

function compute() {
    let a = parseFloat(prev);
    let b = parseFloat(current);
    let res = 0;

    if (op === "/" && b === 0) {
        alert("Cannot divide by zero");
        clearAll();
        return;
    }

    switch(op){
        case "+": res = a + b; break;
        case "-": res = a - b; break;
        case "*": res = a * b; break;
        case "/": res = a / b; break;
    }

    current = String(res);
    prev = "";
    op = null;
    update();
}

function clearAll() {
    current = "";
    prev = "";
    op = null;
    update();
}

function backspace() {
    current = current.slice(0, -1);
    update();
}

function toggleNegative() {
    current = current.startsWith("-") ? current.slice(1) : "-" + current;
    update();
}

document.querySelectorAll("[data-num]").forEach(btn =>
    btn.onclick = () => appendNumber(btn.dataset.num)
);

document.querySelectorAll("[data-op]").forEach(btn =>
    btn.onclick = () => chooseOp(btn.dataset.op)
);

document.querySelector("[data-action='equal']").onclick = compute;
document.querySelector("[data-action='clear']").onclick = clearAll;
document.querySelector("[data-action='back']").onclick = backspace;
document.querySelector("[data-action='negative']").onclick = toggleNegative;

// Keyboard support
document.addEventListener("keydown", e => {
    if (!isNaN(e.key)) appendNumber(e.key);
    if (["+", "-", "*", "/"].includes(e.key)) chooseOp(e.key);
    if (e.key === "Enter") compute();
    if (e.key === "Escape") clearAll();
    if (e.key === "Backspace") backspace();
    if (e.key === ".") appendNumber(".");
});
