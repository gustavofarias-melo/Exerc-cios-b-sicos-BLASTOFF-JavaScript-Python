let num = 12;

numPrimo(num);

function numPrimo(num) {
  for (let i = 2; i < num; i++) {
    if (num % 2 === 0) {
      return console.log(num + " NÃO é um número primo");
    } else {
      return console.log(num + " é um número primo");
    }
  }
}
