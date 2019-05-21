$("#div_digg .action").click(function () {
    if ($(".info").attr("username")) {


        // 點讚或踩滅
        var is_up = $(this).hasClass("diggit");
        var article_id = $(".info").attr("article_id");

        $.ajax({
            url: "/blog/up_down/",
            type: "post",
            data: {
                is_up: is_up,
                article_id: article_id,
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) {



                if (data.state) {// 讚或者滅成功

                    if (is_up) {
                        var val = $("#digg_count").text();
                        val = parseInt(val) + 1;
                        $("#digg_count").text(val);
                    } else {
                        var val = $("#bury_count").text();
                        val = parseInt(val) + 1;
                        $("#bury_count").text(val);
                    }
                }
                else {    // 重複提交

                    if (data.first_action) {
                        $("#digg_tips").html("您已經推薦過！");
                    } else {
                        $("#digg_tips").html("您已經反對過！");
                    }

                    setTimeout(function () {
                        $("#digg_tips").html("")
                    }, 1000)

                }

            }
        })


    }
    else {
        location.href = "/login/"
    }


});