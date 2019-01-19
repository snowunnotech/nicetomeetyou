  var NowID ="0"
  $(function() {
    
    GetNewsList();
    setInterval(function() { GetNewsList(); }, 60000);

  });

function Showyourself() {
    console.log('Hey!')
}

function GetNewsList() {
   
    $.ajax({
        type: 'Get',
        url: 'https://lanmor-py-demo-lanmorop01.c9users.io/api/news/',
        success: function(response) {
            //var obj = JSON.parse(response);
            //console.log(response.length);
            if(NowID!="0" && NowID!=response[0].id){
                alert("有新的新聞!")
            }
            NowID = response[0].id
            
             $("#newslist li").remove();
            
            for (var i = 0; i < response.length; i++) {
                let _time = moment(response[i].time).format('YYYY/MM/DD HH:mm');

                let url = "'" + response[i].news_url + "'"
                $("#newslist").append("<li><a href='#'" + "onclick='ShowNews(" + response[i].Serial + "," + response[i].group_id + ")'>" +
                    "<span class='tab'>" + _time + ' ' + response[i].title + '</span></a></li>');
            }
           console.log("List is Update,Lastest ID:" + NowID)
        },
        error: function(output) {
            alert("fail");
        }
    });

}

function ShowNews(Serial, group_id) {
    let FullUrl = 'https://nba.udn.com//nba/story/' + group_id.toString() + "/" + Serial.toString();
    console.log(FullUrl);
    let tmp = "<iframe width='100%' height='100%' src='" + FullUrl + "'></iframe>";
    document.getElementById("ShowNews").innerHTML = tmp;
    const videos = document.querySelectorAll('videos')

    function pauseVideo() {
        this.pause();
    }

    videos.forEach(video => video.addEventListener('click', pauseVideo));
}
