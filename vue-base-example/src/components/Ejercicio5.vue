<template>
    <div>
        <h1>Lista de compras</h1>
        <p>Elemento</p>
        <input v-model="elemento" type="text">
        <p>Cantidad</p>
        <input v-model="cant" type="number">
        <button v-on:click="agregar()">Agregar</button>
        <div>
            <div v-if="lista.length===0" class = "listaVacia">La lista está vacía</div>
            <div v-else>
                <p class = "listaCompleta">Su lista es: </p>
                <ul class = "lista">
                    <li v-for="i in lista" :key="i.nombre">{{ i.nombre }} x {{ i.cantidad }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
.lista {
    text-align: left;
}
.listaVacia {
    border: 1px solid red;
    background-color: lightcoral;
    color: red;
    text-align: center;
    border-radius: 10px;
    margin: 10px 0;
    padding: 10px;
}
.listaCompleta {
    text-decoration: underline;
}
</style>

<script>
export default {
  name: 'Ejercicio5',
  data: function () {
    return {
      lista: [],
      elemento: '',
      cant: 0
    }
  },
  methods: {
    agregar: function () {
      var quantity = parseInt(this.cant)
      if (this.elemento !== '' && !isNaN(quantity) && quantity > 0) {
        var nuevoElemento = {
          nombre: this.elemento,
          cantidad: quantity
        }
        this.lista.push(nuevoElemento)
        this.elemento = ''
        this.cant = ''
      }
    }
  }
}
</script>
