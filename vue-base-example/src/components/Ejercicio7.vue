<template>
    <div>
        <BotonContador label="Jamón y Queso" color="Red"/>
        <BotonContador label="Choclo" color="Yellow"/>
        <BotonContador label="Carne" color="Brown"/>
        <BotonContador label="Zapallo" color="Orange"/>
    </div>
</template>

<script>
import BotonContador from './BotonContador.vue'
export default {
  name: 'Ejercicio7',
  data: function () {
    return {}
  },
  methods: {},
  components: { BotonContador }
}
</script>
