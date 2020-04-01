<template>
    <div class="consumer">
        <h3>I am consumer #{{id}}</h3>
        <p>My latest message is: {{latestMessage}}</p>
    </div>
</template>

<script>
// import axios from 'axios';
// import VueSocketIO from 'vue-socket.io'

export default {
    name: "consumer",
    props: [
        "id",
        "url",
        "group"
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
            console.log('updating consumer')
            this.$socket.emit('message', {'message': 'hi'})
        }
    },
    sockets: {
        connect: function() {
            console.log(`websocket connected for consumer ${this.id}`)
            // send the id of the consumer to create to the backend
            var data = { 
                'message': `consumer${this.id}`,
                'group': this.group
            }
            this.$socket.emit('createConsumer', data)
            var createEventName = `createConsumer${this.id}`
            // subscribe to the creation event for this consumer
            this.sockets.subscribe(createEventName, function(data) {
                console.log(`consumer ${this.id} created!: ${JSON.stringify(data)}`)
                const eventName = data['message']
                // subscribe to updates from this consumer
                this.sockets.subscribe(eventName, function(consumerData) {
                    console.log(`got data from consumer: ${consumerData}`)
                    this.latestMessage = consumerData
                })
            });
        }
    },
    created: function() {
        console.log("consuming!")
        // this.updateConsumer();

        // setInterval(function () {
        //     this.updateConsumer();
        // }.bind(this), 5000)
    }
}
</script>