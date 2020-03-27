import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSocketIO from 'vue-socket.io'

Vue.config.productionTip = false

//const options = { path: '/test' }; //Options object to pass into SocketIO
 
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000/consumers'
    //options: options
  })
);
 

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
