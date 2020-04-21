<template>
    <div class="producer">
        <h3>I am producer #{{id}}</h3>

        <!-- TODO add produce button --> 

        <!-- <p>My latest message is: {{latestMessage}}</p> -->
        <Log title="Producer" v-bind:maxLength="3" v-bind:items="items"/>
        <!-- <v-list>
            <v-subheader>LOG</v-subheader>
            <v-list-item-group v-model="item" color="primary">
                <v-list-item
                v-for="(item, i) in items"
                :key="i"
                >
                <v-list-item-content>
                    <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-list> -->
    </div>
</template>

<script>
import axios from 'axios';
import Log from './Log';

export default {
    name: "Producer",
    props: [
        "id",
        "url"
    ],
    components: {
        Log
    },
    data() {
        return {
            latestMessage: '',
            items: [
            ],
            logLength: 5
        }
    },
    computed: {
        produceUrl: function() {
            return `${this.url}/producers`
            // return `${this.url}/producers/${this.id}`
        },
        logChannel: function() {
            return `producer-log-${this.id}`
        }
    },
    methods: {
        // TODO add button
        updateProducer: function() {
            var temp = Math.random() * 100;
            var payload = { "temp-sensor": temp }
            // POST request to backend to publish data from producer
            axios.post(this.produceUrl, payload)
                .then( res => {
                    //this.latestMessage = `Produced=> ${JSON.stringify(res.data)} => ${JSON.stringify(payload)}`
                    this.latestMessage = `Produced => ${JSON.stringify(payload)} => ${JSON.stringify(res.data)}`
                    
                    //console.log(`result: ${JSON.stringify(res)}`)
                    // update list!
                    //this.latestMessage = JSON.stringify(payload)
                    if (this.items.length == this.logLength) {
                        this.items.shift();
                    }
                    this.items.push(this.latestMessage);
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