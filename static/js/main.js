var url = "/news/?format=json"

$.ajax({
    method:'GET',
    url: url,
    success:function(data){
        console.log(data)
        console.log("success")
        $(function() {
            $.each(data, function(i, item) {
                var $tr = $('<tr >').append(
                    $('<td>').append(
                        $('<h6 id='+item.news_id+'>').text(item.title)
                    ).append(
                        $('<p>').text(item.introduction)
                    )              
                ).append($('<td>').append(
                    $('<button id='+item.news_id+' onClick="btnclick(this.id)">').text("內文")
                    )).appendTo('#news_table');

            });
        });
    },
    error:function(data){
        console.log("error")
    }
})

// $("button").click(function() {
//     alert(this.id); // or alert($(this).attr('id'));
// });



function btnclick(clicked) { 
    // <span class="close">&times;</span>
    $(".content").remove();
    var $span = $('<span class="close content" >').text("X").appendTo('#content_text');
    var url = "/content/"+clicked+"/id/?format=json"
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    span.onclick = function() {
        modal.style.display = "none";
    }

    
    $.ajax({
        method:'GET',
        url: url,
        success:function(data){
            modal.style.display = "block";
            var $h2 = $('<h2 class="content">').text(data.content_title).appendTo('#content_text');
            var $p = $('<a class="content" href='+data.content_url+'>').text('資料來源: 聯合新聞網-NBA').appendTo('#content_text');
            var $p = $('<p class="content datetime">').text(data.news_date).appendTo('#content_text');
            var $p = $('<p class="content content_text">').text(data.content_text).appendTo('#content_text');
            var $p = $('<p class="content bye">').text("@@非商業用途,僅使用測試@@").appendTo('#content_text');
        },
        error:function(data){
            console.log("error")
        }
    })
}  

$('#content_text').on('hidden', function(){
    $(this).data('modal', null);
});
