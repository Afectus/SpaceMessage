Vue.config.delimiters = ["[[","]]"]

var demo = new Vue({
    el: '#addMessage',
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

            this.$http.post('http://127.0.0.1:8000/api/v1/get_messages/all/', newMessage);
        },

    },

});



var demo = new Vue({
    el: '#getAllMessage',
    data: {
        'messages': [],
        counter:0,
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
        },
    methods: {
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
});

var demo = new Vue({
    el: '#getFalseMessage',
    data: {
        'messages': [],
        counter:0,
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_messages/false/').then(function (response) {
                emulateJSON: true
                this.messages = response.data;
            },
            function (response) {
                console.log(response);
            });
        },
    methods: {
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
});

var demo = new Vue({
    el: '#getTrueMessage',
    data: {
        'messages': [],
        counter:0,
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_messages/true/').then(function (response) {
                emulateJSON: true
                this.messages = response.data;
            },
            function (response) {
                console.log(response);
            });
        },
    methods: {
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
    
});   

var demo = new Vue({
    el: '#addToken',
    data: {
        'tokenz': [],
        counter:0,
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_token/all/').then(function (response) {
                emulateJSON: true
                this.tokenz = response.data;
            },
            function (response) {
            });
        },
    methods: {
        addToken: function () {
            this.$http.post('http://127.0.0.1:8000/api/v1/get_token/all/');
        },

    },

});

 
var demo = new Vue({
    el: '#getFalseToken',
    data: {
        'tokenz': [],
        counter:0,
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_token/false/').then(function (response) {
                emulateJSON: true
                this.tokenz = response.data;
            },
            
            function (response) {

            });
        },
    methods: {
            removeMessage: function (index) {
            this.$http.delete('http://127.0.0.1:8000/api/v1/get_token/all/'.concat(this.messages[index].id));
            this.messages.splice(index, 1);
        },
            activedToken: function (index) {
            	var newToken = {
                    tokens: this.tokenz[index].tokens,
                    status:true
            };
            this.$http.post('http://127.0.0.1:8000/api/v1/get_token/all/', newToken);
            this.$http.delete('http://127.0.0.1:8000/api/v1/get_token/all/'.concat(this.tokenz[index].id));
            this.messages.splice(index, 1);
        },
    },
});
   
var demo = new Vue({
    el: '#getTrueToken',
    data: {
        'tokenz': [],
        counter:0,
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_token/true/').then(function (response) {
                emulateJSON: true
                this.tokenz = response.data;
            },
            
            function (response) {

            });
        },

});

