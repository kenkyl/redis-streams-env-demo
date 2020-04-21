<template>
    <v-container
        class="fill-height"
        fluid
    >
        <v-row
          align="center"
          justify="center"
        >
          <DashboardContainer v-bind:tempValue="tempValue"/>
        </v-row>
        <v-divider class="mx-4" dark></v-divider>
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="shrink">
              <!-- <ProducerComponent title="Producer!" message="Producing Environmental Data..."/> -->
              <ProducersContainer />
          </v-col>
          <v-divider class="mx-4" dark vertical></v-divider>
          <v-col class="shrink">
              <!-- <ConsumersPanel title="Consumers!"/> -->
              <ConsumersContainer v-on:update-temp="updateTemp"/>
          </v-col>
        </v-row>
      </v-container>
</template>

<script>
import ProducersContainer from './ProducersContainer';
import ConsumersContainer from './ConsumersContainer';
import DashboardContainer from './DashboardContainer';

export default {
    name: "ContentLayout",
    props: [
        "title",
    ],
    components: {
        ProducersContainer,
        ConsumersContainer,
        DashboardContainer
    }, 
    data: function() {
        return {
            tempValue: 0
        }
    },
    methods: {
      updateTemp(value) {
        this.tempValue = value;
      }
    }
}
</script>