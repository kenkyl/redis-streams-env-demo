<template>
    <div class="dashboard-container">
        <h2 class="font-weight-light">Dashboard Container!</h2>    
        <v-container
            class="fill-height"
            fluid
        >
            <v-row
            align="center"
            justify="center"
            >
                <v-col class="shrink">
                    <!-- display -->
                    <TemperatureDisplay v-bind:tempValue="tempValue" />
                </v-col>
                <v-divider class="mx-4" dark vertical></v-divider>
                <v-col class="shrink">
                    <!-- stats -->
                </v-col>
                <v-divider class="mx-4" dark vertical></v-divider>
                <v-col class="shrink">
                    <!-- history -->
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import TemperatureDisplay from './TemperatureDisplay'

export default {
    name: "DashboardContainer",
    props: [
        "tempValue"
    ],
    components: {
        TemperatureDisplay
    }
}
</script>

<style scoped>

</style>