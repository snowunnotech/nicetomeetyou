// select html element
var newsContainer = document.getElementById("news-list");

// ajax magic 
$(document).ready(function(){
    var dataId = [];

    // start crawling
    $("#start-crawl").click(function(){
        $("#start-crawl").attr("disabled", true)
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is working...');
        $.ajax({
            url: '/crawl/',
            type: 'POST',
            data: {
                'url': "https://nba.udn.com/nba/index?gr=www",
            },
            success: crawlSuccess,
            error: crawlFail,
        })
        
    });

    // read and show api
    $("#show").click(function(){
        $.getJSON("api/News/?format=json", function(data, status){
            if(dataId.length == 0){
                $.each(data, function(index, ele){
                    dataId.push(ele.id);
                });
                renderHTML(data)
            } else{
                var counter = 0;
                $.each(data, function(index, ele){
                    if(dataId.includes(ele.id)){
                        // console.log("dataId contains " + ele.id);
                    } else{
                        // console.log("dataId does not contain  " + ele.id);
                        counter++;
                    }
                });
                $('#progress').attr("class", "alert alert-secondary");
                $('#progress').html(counter + " new news available.");
                setTimeout(function(){
                    $('#progress').empty();
                    $('#progress').removeClass();
                },2000);
            }
        });
    });
});

// render REST api data into HTML
function renderHTML(apidata){
    var html = "";
    var apidatalength = apidata.length; // reverse randering
    for (i = 0; i < apidatalength; i++){
        html += "<div class='content-section'>";
        html += "<h2><a href=" + apidata[apidatalength-i-1].link_url + ">" + apidata[apidatalength-i-1].title + "</a></h2>";
        html += "<img src=" + apidata[apidatalength-i-1].img_url + ">";
        html += "</div>";
    }
    newsContainer.insertAdjacentHTML('beforeend', html);
}

function checkCrawlStatus(taskId, uniqueId){
    $.ajax({
        url: '/crawl/?task_id='+taskId+'&unique_id='+uniqueId+'/',
        type: 'GET',
        success: showCrawledData,
        error: showCrawledDataFail,
    })
}

function crawlSuccess(data){
    taskId = data.task_id;
    uniqueId = data.unique_id;
    statusInterval = setInterval(function() {checkCrawlStatus(taskId, uniqueId);}, 5000);
}

function crawlFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showCrawledData(data){
    if (data.status){
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is ' + data.status + ' ... ' + 'After crawling, the results are returned');
    }else{
        clearInterval(statusInterval);
        $('#progress').attr("class", "alert alert-primary");
        $('#progress').html('crawling is finished!');
        $("#start-crawl").attr("disabled", false);
        setTimeout(function(){
            $('#progress').empty();
            $('#progress').removeClass();
        },2000);
    }
}

function showCrawledDataFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}
