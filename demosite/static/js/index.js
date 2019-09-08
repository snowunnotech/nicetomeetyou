var Index = function () {

    var init = function () {
        initPagination();
    }

    var initPagination = function () {
        var pagecontainer = $('#pagination-container');
        var dataContainer = $('.data-container');
        pagecontainer.pagination({
            dataSource: globalVariables.newsListUrl,
            locator: '',
            pageSize: 20,
            showNavigator: true,
            className: 'paginationjs-theme-blue paginationjs-big',
            ajax: {
                beforeSend: function() {
                    dataContainer.html('Loading...');
                }
            },
            callback: function (data, pagination) {
                // template method of yourself
                var html = simpleTemplating(data);
                dataContainer.html(html);
            },
            afterPaging  : function () {
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
