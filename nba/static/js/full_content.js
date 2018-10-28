$(function(){
var nba_content_url = $(location).attr('pathname').split('/')

// console.log(nba_content_page_url)

 $.ajax({

// type:"HEAD",
 async:false,
 datatype:"json",
 beforeSend: function(xhr) {
 xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
},
 url:"http://127.0.0.1:8000/api/",
 success:function (data){
     for ( var i = 0; i < data.length; i++){
        if (data[i]["ID"] == nba_content_url[2]){
            var nba_content_url_home = "http://127.0.0.1:8000/news/"
            $(".title").text(data[i]["title"]);
            $(".time").text(data[i]["time"]);
            $(".pic").attr("src",data[i]["img"]);
            $(".content").text(data[i]["cotent"]);
            $("#back_home").attr("href",nba_content_url_home)
        }
    }
}
});
});