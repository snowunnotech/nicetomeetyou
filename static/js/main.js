var url ='http://127.0.0.1:8000/api/aritcles/';

// 設定自動傳request的時間，此處單位為毫秒
setInterval(function(){
	$.ajax({
		method: 'GET',
		url : 'http://127.0.0.1:8000/home/'
	})
	.done(function(){
		$.ajax({
		method: 'GET',
		url : url,
		success: function(data){
			console.log(data)
			console.log("success")
		},
		error: function(error_data){
			console.log("error")
		}
	})
	.done(function(data){
			renderhtml(data);
		});
	})
},100000);


// 抓取API資料
$(document).ready(function(){
	$.ajax({
		method: 'GET',
		url : url,
		success: function(data){
			console.log(data)
			console.log("success")
		},
		error: function(error_data){
			console.log("error")
		}
	})
	.done(function(data){
			renderhtml(data);
		});
})

// 將資料加到HTML上
function renderhtml(data){
	var container = document.getElementById("ourcontainer")
	// 清掉舊有的news
	$(" .card-body").empty(); 
	for (i=0; i < data.length; i++){
		content = "";
		content += 	"<a href= " + data[i].detail +"</a>"+
					"<img src =" + data[i].img + "</>" +"<br>"+
					"<b>" + data[i].time + "</b>"+ "<br>"+
					"<h3>" + data[i].title + "</h3>" + 
					"<p>" +data[i].text + "</p>" + 
					"<br>"
					;		
		$(" .card-body").append(content);
	}
}

