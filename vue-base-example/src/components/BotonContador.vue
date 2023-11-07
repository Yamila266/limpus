<template>
  <div>
    <button v-on:click="increaseCounter()" v-bind:style="{'background-color': color }">{{ label }} ({{ count }})</button>
  </div>
</template>

<style scoped>
div button {
  border-radius: 10px;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid black;
}
</style>

<script>
export default {
  name: 'BotonContador',
  props: [
    'label',
    'color'
  ],
  data: function () {
    return {
      count: 0
    }
  },
  methods: {
    increaseCounter () {
      this.count = this.count + 1
    }
  }
}
</script>
