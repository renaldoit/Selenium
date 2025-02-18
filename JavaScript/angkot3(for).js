var jmlAngkot = 10;
var angkotBeroperasi = 8;
var noAngkot = 1;


for(noAngkot = angkotBeroperasi + 1; noAngkot <= jmlAngkot; noAngkot++) {
    console.log('Angkot No. ' + noAngkot + ' sedang tidak beroperasi.');
}else (noAngkot <= angkotBeroperasi && noAngkot !== 5) {
    console.log('Angkot No. ' + noAngkot + ' sedang beroperasi dengan baik.');
}