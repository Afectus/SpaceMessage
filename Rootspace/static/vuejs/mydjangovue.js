Vue.config.delimiters = ["[[","]]"]

var demo = new Vue({
    el: '#app',
    data: {
        'messages': [],
        counter:0,
    },
    methods: {
        addMessage: function () {
            var newMessage = {
                title: this.titleinput.trim(),
                text: this.textinupt.trim()
            };

            this.$http.post('http://127.0.0.1:8000/api/v1/get_messages/false/', newMessage);
        },
        removeMessage: function (index) {
            this.$http.delete('http://127.0.0.1:8000/api/v1/get_messages/all/'.concat(this.messages[index].id));
            this.messages.splice(index, 1);
        },
        changeStatus: function (index) {
            var newMessagee = {
                title: this.messages[index].title,
                text: this.messages[index].text,
                status:true
            };
            this.$http.post('http://127.0.0.1:8000/api/v1/get_messages/true/', newMessagee);
            this.$http.delete('http://127.0.0.1:8000/api/v1/get_messages/all/'.concat(this.messages[index].id));
            this.messages.splice(index, 1);
        },
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_messages/all/').then(function (response) {
                emulateJSON: true
                this.messages = response.data;
            },
            function (response) {
                console.log(response);
            });
        }
});