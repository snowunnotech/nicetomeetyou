
$(function(){
	
	/* ajax call */
	$.ajax({
		url: '/api/news/',
		type: 'GET',
		error: function(err) {
			//alert('Ajax request 發生錯誤');
			console.log(JSON.stringify(err));
		},
		success: function(response) {
			
			//console.log(JSON.stringify(result));
			$("#tabpage").dataTable({
				data: response,
				columns: [ 
					{ 
						data: 'imgsrc', 
						// transforming data, 
						//reference : https://datatables.net/manual/data/renderers
						render : function( data, type, row ){ return '<img src="' + data + '" width="292"/>'; }
					},
					{ data: 'title' },
					{ data: 'content' },
					{ data: 'time' },
					{ 
						data: 'id',
						render : function( data, type, row ){ return '<span style="color : red;" onclick="view(' + data + ');">檢視</span>'; }
					}
					],
				"sPaginationType":"full_numbers",
				"bPaginate":true,
				"bFilter":false,
				"bSort":false,
				"bAutoWidth":true,
				"bLengthChange": false,
				"bInfo":false,
				"iDisplayLength": 4,
				"oLanguage": {
					"sLengthMenu": "顯示 _MENU_ 筆記錄",
					"sZeroRecords": "無符合資料",
					"sInfo": "目前記錄：_START_ 至 _END_, 總筆數：_TOTAL_",
					"oPaginate":{
						"sNext": "&#10095;",
						"sLast": "",
						"sFirst":"",
						"sPrevious": "&#10094;",
					},
				}
			});
	 
		}
	});    	
});

//檢視詳細資料(遠端抓資料)
function view( id ){
	
	//ajax call
	$.ajax({
		
		url : '/api/news/' + id,
		type : 'GET',
		error: function(err) {
			//alert('Ajax request 發生錯誤');
			console.log(JSON.stringify(err));
		},
		success : function(response){
			
			//console.log(JSON.stringify(response));
			
			$('#title').text( response.title );
			
			$('#info').text( response.info );
			
			$('#imgsrc').attr( 'src', response.imgsrc );
			
			$('#content').text( response.content );
		}
	});
}