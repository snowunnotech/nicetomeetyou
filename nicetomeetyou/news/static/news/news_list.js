$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "https://boiling-citadel-11734.herokuapp.com/news/api/news",
		success: function (data){
            data.forEach(function(ele){
                $("#news_list").append("<div id='" + ele.number + "'></div>");
//                $("#"+ ele.number).append("<div><a class='id'  disabled>" + ele.id + "</a></div>")
                $("#"+ ele.number).append("<div><img src='" + ele.image + "'height='200' width='300'></div>");
                $("#"+ ele.number).append("<div><a class='title' href='https://boiling-citadel-11734.herokuapp.com/news/news/" + ele.id + "'>" + ele.title + "</a></div>");
                $("#"+ ele.number).append("<div><a class='published'>" + ele.published_date + "</a></div>");
                $("#"+ ele.number).append("<br>");
            })
		},
		error: function (e){
            console.log(e);
		}
    })
})