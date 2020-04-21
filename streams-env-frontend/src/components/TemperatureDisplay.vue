<template>
    <v-card
        class="mx-auto"
        max-width="344"
        outlined
    >
    <v-card-title>
        {{title}}
    </v-card-title>
    <v-card-text>
        Current Temperature:
        <span>{{tempValue}}</span>
        <br/>
        Updated By:
        <span class="font-weight-light">{{tempConsumer}}</span>
    </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: "TemperatureDisplay",
    props: [
        "tempValue",
        "tempConsumer"
    ],
    data: function() {
        return {
            title: "Current Temperature"
        }
    }
}
</script>

<style scoped>

</style>