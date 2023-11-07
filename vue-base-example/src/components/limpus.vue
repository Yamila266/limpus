<template>
    <div class="container">
        <label class="categoria">Marca</label><select v-model="brand">
            <option value="Poett">Poett</option>
            <option value="Ayudin">Ayudin</option>
            <option value="Magistral">Magistral</option>
            <option value="Ala">Ala</option>
            <option value="Otra">Agregar Marca</option>
        </select>
        <input v-if="brand === 'Otra'" v-model="customBrand" placeholder="Nombre de la marca" />
        <label class="categoria">Modelo</label><input v-model="model">
        <label class="categoria">Precio</label><input v-model="price">
        <label class="categoria">Stock</label><input v-model="stock">
        <button @click="agregarItem()">Agregar</button>
        <table>
            <tr>
                <th>Id</th>
                <th>Marca</th>
                <th>Modelo</th>
                <th>Precio</th>
                <th>stock</th>
            </tr>
            <tr v-for="item in items" :key="item.id">
                <td>{{ item.id }}</td>
                <td>{{ item.brand }}</td>
                <td>{{ item.model }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.stock }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'



export default {
    name: 'APITest',
    data: function(){
        return {
            items: [],
            brand: '',
            model: '',
            price: '',
            stock: '',
            customBrand: ''
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
        },
        agregarItem(){
            axios.post('http://localhost:8000/products/', {
                model: this.model,
                brand: this.brand,
                stock: this.stock,
                price: this.price
            })
            .then(response => {
                console.log(response)
                this.cargarDatos()
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
        this.cargarDatos()
    }
}


</script>
<style>
    body {
        background-image: url('./imagenes/images.jpeg');
        background-size: cover; /* Ajusta la imagen al tamaño de la ventana del navegador */
        background-repeat: no-repeat; /* Evita la repetición de la imagen */
    }
    .container {
        background-color: #E7E6E1; /* Color de fondo para el componente */
        padding: 20px;
    }

    .categoria {
        font-weight: bold;
        margin-right: 10px;
        color: #F2A154;

    }
    
    input {
        margin-bottom: 10px;
        padding: 5px;
        width: 200px;
    }

    button {
        margin-top: 10px;
        padding: 10px 20px;
        background-color: #254145;
        color: #E7E6E1;
        border: none;
        cursor: pointer;
    }

    button:hover {
        background-color: #314E52;
    }

    table {
        background-color: #E7E6E1;
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }

    table, th, td {
        border: 1px solid #ddd;
        text-align: left;
    }

    th, td {
        padding: 10px;
        background-color: #F7F6E7;
    }

    tr:nth-child(even) {
        background-color: #F7F6E7;
    }
</style>