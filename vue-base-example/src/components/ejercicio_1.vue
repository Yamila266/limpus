
<template>
    <div>
        <h1 class="titulo">Ejercicio 1</h1>
        <h2 class="subtitulo">Saludar</h2>
        <label>Ingrese su nombre: </label>
        <input v-model="nombre">
        <p>Hola, {{ nombre }}!</p>
    </div>
</template>
<script>
    export default {
        name: 'Ejercicio_1',
        data: function () {
            return {
                nombre: undefined
            };
        }
    };
</script>
  