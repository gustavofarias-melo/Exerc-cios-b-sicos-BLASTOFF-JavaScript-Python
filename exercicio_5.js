let num1 = 3, num2 = 12;

if (num1 % num2 == 0 || num2 % num1 == 0){
    return console.log(`${num1} e ${num2} são multiplos.`)
} 
else {
    return console.log(`${num1} e ${num2} NÃO são multiplos.`)
}