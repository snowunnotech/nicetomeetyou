"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        news : []
    },
    mounted() {
        var self = this;
        var url = new URL(window.location.href);
        var pk = url.searchParams.get("pk");
        var endpoint = '/api/news/' + pk;
        $.ajax({
            url: endpoint,
            method: 'GET',
            success: function (data) {
                self.news = data;
            },
            error: function (error) {
                console.log(error)
            }
        });
    }
});
