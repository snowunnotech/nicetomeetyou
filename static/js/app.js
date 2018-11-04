$(document).ready(function() {
    $('#dailyTable').DataTable( {
        serverSide: true,
        dom:'lBrtip',
        ajax: {
            type: "post",
            url: 'http://127.0.0.1:8000/get_news_for_table_data/'
        },
        columns: [
             {
                 data: 'title',
                 sortable: false,
                 render: function(data, type, JsonResultRow, meta) {
                     var id = JsonResultRow['id'];
                     return '<a href="/get_news/id='+id+'">' + data+ '</a>'; }
              },
             {data: 'author', sortable: false},
             {data: 'org_news_date', sortable: false},
        ],
        oLanguage: {
            sSearch: "搜索",
            sLengthMenu: "每頁顯示 _MENU_ 條紀錄",
            sZeroRecords: "抱歉， 每有找到",
            sInfo: "從 _START_ 到 _END_ /共 _TOTAL_ 條數據",
            sInfoEmpty: "沒有數據",
            sInfoFiltered: "(從 _MAX_ 條數據中檢索)",
            oPaginate: {
                sFirst: "第一頁",
                sPrevious: "前一頁",
                sNext: "下一頁",
                sLast: "尾頁"
            },
            sProcessing: "正在加載數據......"}
    });
});
/*
$(document).ready(function() {
	$('#dailyTable').DataTable({
        processing: true,
        serverSide: true,
        ajax: {
            url: "http://127.0.0.1:8000/get_news_for_table_data/",
            type: "post",
            dataType: "json",
            success: function (json) {
                console.log(json)
            },
            error: function () {
                $("#dailyTable").css("display", "none");
            }
        },

});
*/
// https://datatables.net/examples/ajax/objects.html
// https://dotblogs.com.tw/shadow/2018/04/03/033936