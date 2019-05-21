// 提交評論
        // var pid = "";
        $('body').on('click','.comment_btn',function () {
            var $start = $(this);
            var article_id = $(".info").attr("article_id");
            var $input_tag = $start.prev().find('input');
            var content = $input_tag.val();
            if ($start.parent().parent().parent().hasClass('list-group-item')){
                var pid = $start.parent().parent().parent().attr('self_id');
                var fid = $start.parent().parent().attr('self_id');
            }else if($start.parent().parent().parent().attr('id')=== 'main_li' ||
                $start.parent().parent().parent().attr('id')=== 'Second_li'){
                var pid = $start.parent().parent().attr('self_id');
                var fid = $start.parent().parent().attr('self_id');
            }else{
                var pid = '';
                var fid = '';
            };

            $.ajax({
                url: "/blog/comment/",
                type: "post",
                data: {
                    article_id: article_id,
                    content: content,
                    pid: pid,
                    fid: fid,
                    csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                },
                success: function (data) {
                    // console.log(data);
                    var create_time = data.create_time;
                    var content = data.content;
                    var username = data.username;
                    var avatar = data.avatar;
                    var pid = data.pid;
                    var fid = data.fid;

                    // var comment_li = '<li class="list-group-item"><div><span style="color: gray">' + create_time + '</span> &nbsp;&nbsp; <a href=""><span>' + username + '</span></a></div> <div class="con"> <p> ' + content + ' </p> </div> </li>';
                    var comment_li = '<li class="list-group-item well"><div><a href="#"><img class="" src="/media/' +avatar+ '"style="width: 30px; height: 30px"></a><a><span style="font-size: 1.2em">&nbsp;&nbsp;'+ username +'</span></a><span class="pull-right" style="color:gray;">' +create_time+ '</span></div><div class="con"><p style="margin-left: 6%">' +content+ '</p></div></li>';


                    // if (pid && fid){
                    //     $start.parent().prev().after(comment_li);
                    // }else if(pid && !fid){
                    //     $start.parent().prev().after(comment_li);
                    if (pid){
                        $start.parent().prev().after(comment_li);
                    }else {
                        // $("#main_li").append(comment_li);
                        // var page = $start.parent().parent().prev().find("li").last().clone();
                        // $start.parent().parent().prev().find("li").last().remove();
                        // $start.parent().parent().prev().append(comment_li).append(page);
                        // if ($("#main_li").find("li").length !== 1){
                        $start.parent().parent().prev().find("li").last().before(comment_li).prev().attr("style","margin-bottom:0px");
                        // }else{
                        //    $("#main_li").append(comment_li);
                        // };

                        window.scrollTo(0,document.body.scrollHeight);
                    };

                    // // 清空文本框
                    $input_tag.val("");
                    $input_tag.attr('placeholder', "寫下你的評論。。。");

                }
            })


        });
