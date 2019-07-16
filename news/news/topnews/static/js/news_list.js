// URL for data from database
var url = "http://127.0.0.1:8000/news/news/"

$(document).ready(function(){
    $.ajax({
        url: url,
        dataType: "json",
        success: function(data){
            // Insert data of ten top news
            for (i=0; i<10; i++){
                
                // Concatenate with "+" (easy but should be careful)
                $("#NewsList").append(
                    "<li class='list-group-item'>" +
                        "<a href='http://127.0.0.1:8000/news/" + data[i].id + "'>" +
                            "<h3>" + data[i].title + "</h3>" +
                        "</a>" +
                        "<img src='" + data[i].pre_img_link + "'>" +
                        "<p>" + data[i].preview + "</p>" +
                        "<p>" + data[i].time + "</p>" +
                    "</li>"
                );

            }
        }
    });
});