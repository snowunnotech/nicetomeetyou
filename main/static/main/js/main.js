$(document).ready(function() {
    // AJAX when the title of news is clicked.
    $('a.link-ajax').on('click', function(event) {
        event.preventDefault();
        var actionEndpoint = $(this).attr('href');
        var id= $(this).attr('id');

        $.ajax({
            url: actionEndpoint,
            method: 'GET',
            success: function(data) {
                // Clear the home page and add detail information of news.
                var text1 = "<h3>" + data.title + "</h3><br><br>"
                var text2 = "<p>" + data.content + "</p>"
                var text3 = "<p>原文網址：<a target='_blank' rel='noopener noreferrer' href='"
                            + data.url + "'>" + data.url + "</a></p>"
                var btn = "<a class='mt-10 ml-auto btn btn-primary' href='/'>回到新聞列表</a>"
                $('.detail').append(text1, text2, text3, btn);
                $('.cards').remove();
            },
            error: function(errorData) {
                console.log('error')
            }
        })
    })
})
