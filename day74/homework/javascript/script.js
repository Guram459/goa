function sumOfDigits(numbers) {
    const digits = numbers.tostrings()
    let sum = 0


for (let i = 0; i < digits.lenght; i++) {
    sum += Number(digits[i])
}

return sum 

}

console.log(sumOfDigits(12345))