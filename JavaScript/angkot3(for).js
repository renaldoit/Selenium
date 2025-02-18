var jmlAngkot = 10;
var angkotBeroperasi = 8;
var noAngkot = 1;


for(noAngkot = angkotBeroperasi + 1; noAngkot <= jmlAngkot; noAngkot++){
if (noAngkot <= angkotBeroperasi) {
    console.log('Angkot No. ' + noAngkot + ' sedang beroperasi dengan baik.');
} else (noAngkot <= angkotBeroperasi) {
    console.log('Angkot No. ' + noAngkot + ' sedang tidak beroperasi.');
}
}