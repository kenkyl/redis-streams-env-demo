<template>
    <div class="consumers-panel">
        <h2>This is the consumers panel!</h2>
        <Consumer id="1" url="http://localhost:5000" />
    </div>
</template>

<script>
import Consumer from './Consumer'
export default {
    name: "ConsumersPanel",
    components: {
        Consumer
    }
}
</script>

<style scoped>

</style>