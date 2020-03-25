<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <ProducersPanel />
    <ConsumersPanel />
  </div>
</template>

<script>
// @ is an alias to /src
import ProducersPanel from '../components/ProducersPanel'
import ConsumersPanel from '../components/ConsumersPanel'

export default {
  name: 'Home',
  components: {
    ProducersPanel,
    ConsumersPanel
  }
}
</script>
