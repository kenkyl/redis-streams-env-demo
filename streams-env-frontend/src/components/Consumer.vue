<template>
    <div class="consumer">
        <h3>I am consumer #{{id}}</h3>
        <p>My latest message is: {{latestMessage}}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "consumer",
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
            return `${this.url}/consumers/${this.id}/last-message`
        }
    },
    methods: {
        updateConsumer: function() {
            // GET request to fetch latest consumer message
            axios.get(this.produceUrl)
                .then(res => {
                    console.log(`consumer result: ${res}`)
                    this.latestMessage = JSON.stringify(res)
                })
                .catch(err => console.error(err));
        }
    },
    created: function() {
        console.log("consuming!")
        this.updateConsumer();

        setInterval(function () {
            this.updateConsumer();
        }.bind(this), 1000)
    }
}
</script>