"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        news : []
    },
    mounted() {
        var self = this;
        var endpoint = '/api/news/';
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