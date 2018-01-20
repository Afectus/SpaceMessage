Vue.config.delimiters = ["[[","]]"]

var demo = new Vue({
    el: '#app',
    data: {
        'apptitle': 'Django Vue.JS Job Board',
        'jobs': []
    },
    methods: {
        addJob: function () {
            var newJob = {
                title: this.title.trim(),
                text: this.text.trim()
            };

            this.$http.post('http://127.0.0.1:8000/api/v1/get_messages/', newJob);
        },
        removeJob: function (index) {
            this.$http.delete('http://127.0.0.1:8000/api/v1/get_messages/'.concat(this.jobs[index].id));
            this.jobs.splice(index, 1);
        }
    },
    ready: function()
        {
            this.$http.get('http://127.0.0.1:8000/api/v1/get_messages/').then(function (response) {
                this.jobs = response.data;
            },
            function (response) {
                console.log(response);
            });
        }
});