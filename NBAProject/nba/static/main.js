var url = "http://" + window.location.host + "/api/news/"
var allData = ""

$.ajax({
	method: "GET",
	url: url,
	success: function(data){
		allData = data
		renderHTML(data);
		console.log(data)
		console.log("success")
	},
	error: function(error_data){
		console.log("error")
	}
})

function showText(i){
	sourceHtml = "<a class='lead-small' href='" + allData[i].web_link + "'>查看更多</a>";
	$("#list-container > div").hide();
	$("#news-text"+i).html(allData[i].content + sourceHtml);
	$("#news-text"+i).show();
}

function renderHTML(data){
	var container = document.getElementById("list-container")
	var htmlStr = "";
	for (i=0;i<data.length;i++){
		htmlStr += "<button id='list-btn' onClick='showText(" + i + ")' type='button' class='list-group-item'>" + 
					"<div class='date lead-small'>發佈時間： " + data[i].publishedtime + "</div>" +
					"<div class='lead-max'>" + (i+1) + ". " + data[i].title + "</div></button>" + 
					"<div id='news-text" + i + "' class='list-group-item lead-mid' style='display:none'></div>"
	}
	container.insertAdjacentHTML('beforeend', htmlStr)
}

