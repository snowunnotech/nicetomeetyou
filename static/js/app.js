var app = angular.module('newsApp', []);

app.controller('newsController', function($scope, $http) {
    $http.get('/api/news/').then(function(response) {
        $scope.newsList = [];
        for (var i = 0; i < response.data.length; i++) {

            var news = {};
            news.newsTitle = response.data[i].title;
            news.newsDatetime = response.data[i].issued_date;
            news.id = response.data[i].id;
            $scope.newsList.push(news);
        }
    });
});

app.controller('newsDetailController', function($scope, $http, $location) {
    apitype = $location.absUrl().split("/")[3];
    tid = $location.absUrl().split("/")[4];
    url = '/api/' + apitype + '/' + tid + '/';

    $http.get(url).then(function(response) {
        if (response.data.length !== 0) {
            $scope.newsTitle = response.data.title;
            $scope.newsAuthor = response.data.author;
            $scope.newsContent = response.data.content;
            $scope.newsDatetime = response.data.issued_date;
        }
    });
});
