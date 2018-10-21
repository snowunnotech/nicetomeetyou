
$(function(){
        
	$("#tabpage").dataTable({
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
    	
});