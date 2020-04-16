<template>
    <v-card
        class="mx-auto"
        max-width="300"
        tile
    >
        <v-list>
            <v-subheader>{{title}} LOG</v-subheader>
            <v-list-item-group v-model="item" color="primary">
                <v-list-item
                v-for="(item, i) in items"
                :key="i"
                >
                <v-list-item-content>
                    <v-list-item-title v-text="item"></v-list-item-title>
                </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-list>
    </v-card>
</template>

<script>

export default {
    name: "Log",
    props: [
        "title",
        "maxLength",
        "logChannel"
    ],
    data() {
        return {
            item: 1,
            items: [
                
            ]
        }
    },
    methods: {
        addToList: function(newItem) {
            console.log(`adding ${newItem} to the list`)
            if (this.items.length == this.maxLength) {
                this.items.shift();
            }
            this.items.push(newItem);
            
        }
    },
    created: function() {
       this.$on(this.logChannel, this.addToList)
       console.log(`listenting on ${this.logChannel}`)
    }
}
</script>