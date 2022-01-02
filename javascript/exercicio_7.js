let lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let numeros = [];

lista.forEach(function (numero) {
  if(numero === 0 ){
   
  }
    else if (numero % 2 == 0) {
    numeros.push(numero)
  }
});

console.log(numeros);
