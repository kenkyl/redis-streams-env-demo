<template>
  <v-app >
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>{{title}}</v-toolbar-title>
      <img class="app-bar-image" src="../assets/redissquarelogo.png" />
    </v-app-bar>

    <v-content>
      <div class="home">
        <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
        <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
        <ContentLayout />
        <!-- <ProducersPanel />
        <ConsumersPanel /> -->
      </div>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  // @ is an alias to /src
  
  import ContentLayout from '../components/ContentLayout'
  export default {
    props: {
      source: String,
      title: String
    },

    components: {
      ContentLayout
    },

    data: () => ({
      drawer: null,
    }),

    created () {
      this.$vuetify.theme.dark = true
    },
  }
</script>

<style scoped>
  .app-bar-image {
    height: 80%;
    position: absolute;
    right: 2%;
  }

</style>
