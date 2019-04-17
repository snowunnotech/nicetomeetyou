var btn = document.getElementById("btn");

var url = 'http://127.0.0.1:8000/getNews/';
var detailUrl ='http://127.0.0.1:8000/detail?article='
$("#btn").click(function () {
    $("#btn").attr('disabled',true);
    $.ajax({url,
    method: 'GET',
    dataType:'json',
    url:url,
    success:function (data) {
        console.log(data)
        console.log("success")
        renderHtml(data)
    },
    error:function (msg) {
        console.log(msg)
        console.log("error")
    }
})
})

function renderHtml(data) {
    var list = document.getElementById("list");
    var htmlString="";
    data["results"].forEach(function (element) {
        htmlString +="<a href="+detailUrl+element.article+"> 標題:"+element.title+"</a> <p>";
    })

    list.insertAdjacentHTML('beforeend',htmlString);
}