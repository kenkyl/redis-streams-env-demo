<template>
    <div class="producer">
        <h3>I am producer #{{id}}</h3>
        <p>My latest message is: {{latestMessage}}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Producer",
    props: [
        "id",
        "url"
    ],
    data() {
        return {
            latestMessage: ''
        }
    },
    computed: {
        produceUrl: function() {
            return `${this.url}/producers`
            // return `${this.url}/producers/${this.id}`

        }
    },
    methods: {
        updateProducer: function() {
            var temp = Math.random() * 100;
            var payload = { "temp-sensor": temp }
            // POST request to backend to publish data from producer
            axios.post(this.produceUrl, payload)
                .then( res => {
                    console.log(`result: ${res}`)
                    this.latestMessage = JSON.stringify(payload)
                })
                .catch(err => console.error(err));
        }
    },
    created: function() {
        console.log("producing!")
        this.updateProducer();

        setInterval(function () {
            this.updateProducer();
        }.bind(this), 5000)
    }
}
</script>