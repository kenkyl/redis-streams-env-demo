<template>
    <div class="producers-panel">
        <h2>This is the producers panel!</h2>
        <Producer id="1" url="http://localhost:5000"/>
    </div>
</template>

<script>

import Producer from './Producer'

export default {
    name: "ProducersPanel",
    components: {
        Producer
    }
}
</script>

<style scoped>

</style>