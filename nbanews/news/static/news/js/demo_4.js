
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
					{ data: 'time' }
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