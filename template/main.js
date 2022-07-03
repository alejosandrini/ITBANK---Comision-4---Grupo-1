
let compra= document.querySelectorAll('#valorCompra');
let venta= document.querySelectorAll('#valorVenta');
let variacion= document.querySelectorAll('#variacion');
console.log(compra)

function imprimir(arr, data, atrib)
{
    let i = 0;
    for(let elem of arr)
    {
        elem.innerHTML= `$${data[i].casa[atrib]}`
        console.log( data[i].casa[atrib]);
        i++;
    }  
}

fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
  .then(response => response.json())
  .then(data => {
      
   imprimir(compra, data, 'compra');
    
   imprimir(venta, data, 'venta');

   

   let i = 0;
    for(let elem of variacion)
    {
        elem.innerHTML= `VARIACION ${data[i].casa.variacion} % `
        console.log(data[i].casa.variacion);
        i++;
    }  
   
      
  });



 


