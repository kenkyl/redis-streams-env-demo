<template>
    <v-container
        class="fill-height"
        fluid
    >
        <v-row
          align="center"
          justify="center"
        >
          <DashboardContainer />
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
              <ConsumersContainer />
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

        }
    }
}
</script>