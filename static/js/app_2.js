$( document ).ready(function() {
    renew_news_feeds();
});

$(function(){
　　t = setInterval("renew_news_feeds()", 1000 * 60);
});

function renew_news_feeds() {
    var chat_log = $("#chat-log");

    // 取得最新新聞的json
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/get_newsfeed/",
        dataType: "json",
        async: false,
        success: function(Jdata) {
            var datas = Jdata['data'];
            for(var i = 0; i < datas.length; i ++) {
                var title = datas[i]['title'];
                var org_news_date = datas[i]['org_news_date'];

                // 取得chat_log的值
                var chat_log_val = chat_log.val();

                chat_log.val(title + ' ' + org_news_date + '\n' + chat_log_val);
            }
        }
    });




}