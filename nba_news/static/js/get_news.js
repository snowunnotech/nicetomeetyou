function get_news(article_id)
{
	$.ajax({
        type: 'GET',
        url: 'nba_news/' + article_id,
        success: function(response) 
	{
	   var added_html = "<h1>" + response.title + "</h1> "
			+ response.published_time + "<br>"
			+ " <img src=" + response.image_url
			+ "width='500' height='250'>" + "<br>"
			+ response.content + "<br><br>";
	   $("#article_content").empty();
	   $("#article_content").append(added_html);
	}});
}

function check_news_list()
{
	var article_num_in_web = $(".article").length;
	$.ajax({
        type: 'GET',
        url: 'all_nba_news/' + article_num_in_web,
        success: function(response) 
	{
	    response.forEach(function(news){
		var added_html = "<div class=article id=" + news.article_id
			+ "><a href='#' onclick='get_news(" + news.article_id
			+ ")'; h1>" + news.title + "</a>"
			+ " <img src=" + news.image_url
			+ " width='100' height='50'>" + news.published_time
		  	+"<br></div><br><br><br>"
	        $("#news_list").prepend(added_html);
	   });
	}});
	
}
