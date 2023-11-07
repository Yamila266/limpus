<template>
  <div id="app">
    <label> Seleccionar ejercicio </label>
    <select v-model="Ejercicio">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
      <option value="7">7</option>
      <option value="Limpus">Limpus</option>
    </select>
  <div v-if="Ejercicio==1">
    <Ejercicio_1/>
  </div>
  <div v-if="Ejercicio==2">
    <Ejercicio_2/>
  </div>
  <div v-if="Ejercicio==3">
    <Ejercicio_3/>
  </div>
  <div v-if="Ejercicio==4">
    <Ejercicio_4/>
  </div>
  <div v-if="Ejercicio==5">
    <Ejercicio_5/>
  </div>
  <div v-if="Ejercicio==6">
    <Ejercicio_6/>
  </div>
  <div v-if="Ejercicio==7">
    <Ejercicio_7/>
  </div>
  <div v-if="Ejercicio=='Limpus'">
    <Limpus/>
  </div>
  </div>
</template>

/* eslint-disable */

<script>
  import Ejercicio_1 from './components/ejercicio_1.vue'
  import Ejercicio_2 from './components/ejercicio_2.vue'
  import Ejercicio_3 from './components/ejercicio_3.vue'
  import Ejercicio_4 from './components/Ejercicio4.vue'
  import Ejercicio_5 from './components/Ejercicio5.vue'
  import Ejercicio_6 from './components/Ejercicio6.vue'
  import Ejercicio_7 from './components/Ejercicio7.vue'
  import Limpus from './components/limpus.vue'
  import axios from 'axios'
  export default {
    name: 'App',
    components: {
      Limpus,
      Ejercicio_3,
      Ejercicio_4,
      Ejercicio_5,
      Ejercicio_6,
      Ejercicio_7,
      Ejercicio_2,
      Ejercicio_1
    },
    data: function(){
      return {
        Ejercicio: undefined,
      }
    },
  
    methods: {
      cargarDatos (){
        axios.get('http://localhost:8000/products/')
        .then(response => {
            this.items = response.data
            console.log(response.data)
        })
        .catch(error => {
            console.log(error)
        })
      }
    },
  }
</script>

<style>

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    background-color: #f0f0f0; 
    padding: 20px; 
    
  }

</style>









