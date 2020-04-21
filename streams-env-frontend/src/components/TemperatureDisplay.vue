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
    </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: "TemperatureDisplay",
    props: [
        "tempValue"
    ],
    data: function() {
        return {
            title: "Temperature"
        }
    }
}
</script>

<style scoped>

</style>