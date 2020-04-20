<template>
    <div class="consumers-group">
        <h4 class="font-weight-light">Consumer Group {{group}}</h4>    
        <Consumer id="1" v-bind:url="url" v-bind:group="group"/>
    </div>
</template>

<script>
import Consumer from './Consumer';

export default {
    name: "ConsumerGroup",
    components: {
        Consumer
    },
    props: [
        "url",
        "group"
    ]
}
</script>

<style scoped>

</style>