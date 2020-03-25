<template>
    <header class="header">
        <img id="logo-header" alt="Vue logo" src="../assets/redislabs.png">
        <h1>{{title}}</h1>
    </header>
</template>

<script>
export default {
    name: "Header",
    props: [
        "title"
    ]
}
</script>

<style scoped>
    .header {
        background: #333;
        color: #fff;
        text-align: center;
        padding: 10px;
    }

    .header a {
        color: #fff;
        padding-right: 5px;
        text-decoration: none;
    }

    #logo-header {
        float: left;
    }
</style>