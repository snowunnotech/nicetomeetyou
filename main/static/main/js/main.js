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
                var title = "<h3>" + data.title + "</h3><br><br>"
                var content = "<p>" + data.content + "</p>"
                var url = "<p>原文網址：<a target='_blank' rel='noopener noreferrer' href='"
                            + data.url + "'>" + data.url + "</a></p>"
                var btn = "<div class='col-12 my-3'><a class='btn btn-primary' href='/'>回到新聞列表</a></div>"
                // Print Photos
                var i;
                var images = "<br>";
                for (i = 0; i < data.photo.length; i++) {
                    images += "<img class='mt-3' src='" + data.photo[i].src + "' alt='" + data.photo[i].alt
                    + "'><div class='col-12 mb-3'><p>" + data.photo[i].description + "</p></div>";
                }
                $('.detail').append(btn, title, content, url, images);
                $('.cards').remove();
            },
            error: function(errorData) {
                console.log('error')
            }
        })
    })
})
