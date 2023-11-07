<template>
    <div>
        <h1>Lista de compras</h1>
        <p>Elemento</p>
        <input v-model="elemento" type="text">
        <p>Cantidad</p>
        <input v-model="cant" type="number">
        <button v-on:click="agregar()" :disabled="elemento=='' || isNaN(parseInt(cant)) || parseInt(cant) <= 0">Agregar</button> //sirve para que el botón solo se habilite cuando se cumplen las condiciones
        <div>
            <div v-if="lista.length===0" class = "listaVacia">La lista está vacía</div>
            <div v-else>
                <p class = "listaCompleta">Su lista es: </p>
                <ul class = "lista">
                    <li v-for="i in lista" :key="i.nombre">{{ i.nombre }} x {{ i.cantidad }}
                        <button v-on:click="eliminar(i.id)">Eliminar</button>
                    </li>
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
  name: 'Ejercicio6',
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
          id: this.uuidv4(),
          nombre: this.elemento,
          cantidad: quantity
        }
      }
      this.lista.push(nuevoElemento)
      this.elemento = ''
      this.cant = ''
    },
    uuidv4: function () {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        // eslint-disable-next-line eqeqeq, one-var
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8)
        return v.toString(16)
      })
    },
    eliminar: function (id) {
      this.lista = this.lista.filter((item) => item.id !== id)
    }
  }
}
</script>
