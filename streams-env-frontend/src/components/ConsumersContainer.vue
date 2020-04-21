<template>
    <div class="consumers-container">
        <h2 class="font-weight-light">Consumers Container!</h2>    
        <ConsumerGroup v-bind:url="url" group="1" v-on:update-temp="updateTemp"/>
    </div>
</template>

<script>
import ConsumerGroup from './ConsumerGroup';

export default {
    name: "ConsumersContainer",
    components: {
        ConsumerGroup
    },
    props: [
        "url"
    ],
    methods: {
        updateTemp(value) {
            this.$emit('update-temp', value)
        }
    }

    

}
</script>

<style scoped>

</style>