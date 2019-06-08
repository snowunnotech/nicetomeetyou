$(document).ready(function() {
  console.log($("#pk").text());
  $.ajax({
    url: "http://127.0.0.1:8000/api/news/" + $("#pk").text(),
    dataType: "json",
    success: function(data) {
      var i, html;
      console.log(data);
      $("#title").append(data["title"]);
      $("#content").append(data["content"]);
      $("#created_at").append(data["created_at"]);
    }
  });
});
