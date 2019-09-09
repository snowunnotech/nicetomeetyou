var Index = function () {

    var init = function () {
        initPagination();
    }

    var initPagination = function () {
        var pagecontainer = $('#pagination-container');
        var dataContainer = $('.data-container');
        pagecontainer.pagination({
            dataSource: function (done) {
                $.ajax({
                    type: 'GET',
                    url: globalVariables.newsListUrl,
                    success: function(response) {
                        done(response);
                    }
                });
            },
            locator: 'title',
            pageSize: 20,
            totalNumberLocator: function (response) {
                // you can return totalNumber by analyzing response content
                return response.length;
            },
            className: 'paginationjs-theme-blue paginationjs-big',
            ajax: {
                beforeSend: function () {
                    dataContainer.html('Loading...');
                }
            },
            callback: function (data, pagination) {
                // template method of yourself
                var html = simpleTemplating(data);
                dataContainer.html(html);
            },
            afterPaging: function () {
                $('div.data-container ul li a')[0].click();
            }
        })
    }

    function simpleTemplating(data) {
        var html = '<ul>';
        $.each(data, function (index, item) {
            html += '<li><a href="#" onclick="javascript:LoadContent(' + item['uid'] + ');">' + item['title'] + '</a></li>';
        });
        html += '</ul>';
        return html;
    }

    return {
        init: init
    };

};
