var domain = "https://boiling-citadel-11734.herokuapp.com/";
// var domain = "http://127.0.0.1:8000/"

$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: domain + "news/api/notice",
        success: function (data){
            console.log(data.status);
            if (data.status == true){
                $("#notice span").text("有最新消息！");
            } else {
                $("#notice span").text("尚無最新消息！");
            }
        },
		error: function (e){
            console.log(e);
		}

    })

    $.ajax({
        type: "GET",
        url: domain + "news/api/news",
		success: function (data){
            data.forEach(function(ele){
                $("#news_list").append("<div id='" + ele.number + "'></div>");
                $("#"+ ele.number).append("<div><img src='" + ele.image + "'height='200' width='300'></div>");
                $("#"+ ele.number).append("<div><a class='title' href='" + domain +"news/news/" + ele.id + "'>" + ele.title + "</a></div>");
                $("#"+ ele.number).append("<div><a class='published'>" + ele.published_date + "</a></div>");
                $("#"+ ele.number).append("<br>");
            })
		},
		error: function (e){
            console.log(e);
		}
    })
})