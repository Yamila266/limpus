<template>
    <div>
        <h1 class="titulo">Ejercicio 2</h1>
        <h2 class="subtitulo">Calculadora</h2>
        <input v-model="num1"/><br>
        <input v-model="num2"/><br>
        /* eslint-disable */
        <select v-model="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multip">Multiplicación</option>
            <option value="div">División</option>
        </select>
        <button v-on:click="calcular()">Calcular</button>
    <div class="mensaje  resultado">El resultado es: {{resultado}}</div>
    </div>
</template>
<style scoped>
    .mensaje{
        text-align: center;
        border-radius: 10px;
        margin: 10px 0;
        padding: 10px;
    }

    .resultado{
        border: 1px solid green;
        background-color: lightgreen;
        color: green;
    }
</style>

<script>
/* eslint-disable */
    export default {
        name: 'Ejercicio2',
        data: function () {
            return {
                num1: 0,
                num2: 0,
                resultado: undefined,
                operacion: ""
            }
        },
        methods: {
            calcular: function () {
                // creamos nuevas variables (locales) y las usamos
                // para guardar la entrada del usuario convertida a float
                var num1_parsed = parseFloat(this.num1)
                var num2_parsed = parseFloat(this.num2)
  
                // si ambos valores son válidos usamos el valor
                // de operation para saber cuál calculo hacer
                // y guardamos el valor en la variable resultado
                if(this.operacion == "suma"){
                    this.resultado = num1_parsed + num2_parsed;
                }else if(this.operacion == "resta"){
                    this.resultado = num1_parsed - num2_parsed;
                }else if(this.operacion == "multip"){
                    this.resultado = num1_parsed * num2_parsed;
                }else if(this.operacion == "div"){
                    this.resultado = num1_parsed / num2_parsed;
                }
            }
        }
    }
</script>