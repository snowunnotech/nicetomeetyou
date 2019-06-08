$(document).ready(function() {
  $.ajax({
    url: "http://127.0.0.1:8000/api/news/",
    dataType: "json",
    success: function(data) {
      var i, html;
      console.log(data);
      for (i = 0; i < data.length; i++) {
        html = '<div class="box"><a href="https://youtu.be/s6zR2T9vn2c" class="image fit"><img src="images/pic01.jpg" alt="" /></a><div class="inner">';
        html += '<h3>' + data[i]["title"] + '</h3>';
        html += '<p>'+ data[i]["created_at"] + '</p><a href="'
        html += 'http://127.0.0.1:8000/api/news/' + data[i]['id']
        html += '" class="button fit">Read</a></div>';
        $(".thumbnails").append(html);
      }
    }
  });
});
