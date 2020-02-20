function muestramensaje(variable) {
    let dict = JSON.parse(variable);
    
    for(const key in dict) {
        console.log(key + ": " + dict[key]);
    }
    alert(dict.dato3);
}