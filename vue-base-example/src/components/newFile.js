/* __placeholder__ */
/* eslint-disable */
export default (await import('vue')).defineComponent({
name: 'Ejercicio2',
data: function () {
return {
num1: 0,
num2: 0,
resultado: undefined,
operacion: ""
};
},
methods: {
calcular: function () {
// creamos nuevas variables (locales) y las usamos
// para guardar la entrada del usuario convertida a float
var num1_parsed = parseFloat(this.num1);
var num2_parsed = parseFloat(this.num2);

// si ambos valores son válidos usamos el valor
// de operation para saber cuál calculo hacer
// y guardamos el valor en la variable resultado
if (this.operacion == "suma") {
this.resultado = num1_parsed + num2_parsed;
} else if (this.operacion == "resta") {
this.resultado = num1_parsed - num2_parsed;
} else if (this.operacion == "multip") {
this.resultado = num1_parsed * num2_parsed;
} else if (this.operacion == "div") {
this.resultado = num1_parsed / num2_parsed;
}
}
}
});
