const btn = document.querySelector("button");
btn,addEventListener("click", () => {
    console.log("arrow >>>>> gurami")
});

const body = document.getElementById("body")
console.log(body)

function bgchange(){
    body.style.background = "red"
}

function myName() {
    return " gurami "
}

console.log(myName());
const myArrowName = () => " arrow => gurami V1";
const myArrowName1 = (name) => (
    "arrow => gurami V2"
);

const myArrowName2 = () => {
    let name = "gurami";
    return (
        "arrow => gurami V3"
    )
}

console.log(myArrowName())
console.log(myArrowName1())
console.log(myArrowName2())