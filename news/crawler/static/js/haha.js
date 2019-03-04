$(document).ready(function () {
  $.ajax({
      url: "http://localhost:8000/newsapi",
      dataType: "json",
      success: function (data) {
          $.each(data, function (index, element) {
              $('.news').append(
              $('<li>', { html:'<u>'+ element.title +'</u>' +'<p>'+ element.content+'</p>'}),
          )});
          }
      })
});


$(".newslist").click(function () {
  $.ajax({
    url: "http://localhost:8000/newsapi",
    dataType: "json",
    success: function (data) {
        $.each(data, function (index, element) {
              if(element.id==26){
                alert('5');
              }
            });
          }
      })
});