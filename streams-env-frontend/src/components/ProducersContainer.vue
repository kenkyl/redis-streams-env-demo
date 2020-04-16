<template>
    <div>
        <h2 class="font-weight-light	">Producers Container!</h2> 
        <Producer id="1" url="http://localhost:5000"/>
    </div>
</template>

<script>
import Producer from './Producer'

export default {
    name: "ProducersContainer",
    components: {
        Producer
    }
    
}
</script>

<style scoped>

</style>