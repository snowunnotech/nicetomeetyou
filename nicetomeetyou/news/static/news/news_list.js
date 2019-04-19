$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/news/api/news",
		success: function (data){
            data.forEach(function(ele){
                $("#news_list").append("<div id='" + ele.number + "'></div>");
//                $("#"+ ele.number).append("<div><a class='id'  disabled>" + ele.id + "</a></div>")
                $("#"+ ele.number).append("<div><img src='" + ele.image + "'height='200' width='300'></div>");
                $("#"+ ele.number).append("<div><a class='title' href='http://127.0.0.1:8000/news/news/" + ele.id + "'>" + ele.title + "</a></div>");
                $("#"+ ele.number).append("<div><a class='published'>" + ele.published_date + "</a></div>");
                $("#"+ ele.number).append("<br>");
            })
		},
		error: function (e){
            console.log(e);
		}
    })
})