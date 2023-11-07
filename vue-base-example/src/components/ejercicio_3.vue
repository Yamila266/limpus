<template>
    <div>
        <h1 class="titulo">Ejercicio 3</h1>
        <h2 class="subtitulo">Validador</h2>
        <input v-model="num1"/><br>
        <input v-model="num2"/><br>
        <select v-model="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multip">Multiplicación</option>
            <option value="div">División</option>
        </select>
        <button v-on:click="calcular()">Calcular</button>
        <div>
            <div v-if="!num1_valid" class="mensaje error">El valor 1 es invalido</div>
            <div v-else-if="!num2_valid" class="mensaje error">El valor 2 es invalido</div>
            <div v-else class="mensaje  resultado">El resultado es: {{resultado}}</div>
        </div>
    </div>
</template>

<style scoped>
    .mensaje{
        text-align: center;
        border-radius: 10px;
        margin: 10px 0;
        padding: 10px;
    }
    .error{
        border: 1px solid red;
        background-color: lightcoral;
        color: red;
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
        name: 'Ejercicio3',
        data: function () {
            return {
                num1: 0,
                num2: 0,
                resultado: undefined,
                num1_valid: false,
                num2_valid: false,
                operacion: ""
            }
        },
        methods: {
            calcular: function () {
                // creamos nuevas variables (locales) y las usamos
                // para guardar la entrada del usuario convertida a float
                var num1_parsed = parseFloat(this.num1)
                var num2_parsed = parseFloat(this.num2)
  
                // guardamos estas variables para saber si los valores
                // son válidos y poder mostrar mensajes correspondientes en el template
                this.num1_valid = !isNaN(num1_parsed);
                this.num2_valid = !isNaN(num2_parsed);
  
                // si ambos valores son válidos usamos el valor
                // de operation para saber cuál calculo hacer
                // y guardamos el valor en la variable resultado
                if(this.num1_valid && this.num2_valid){
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
    }
</script>