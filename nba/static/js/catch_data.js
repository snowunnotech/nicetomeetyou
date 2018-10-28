$(function(){
       
    

    getdata();
    var a = '';
    
    function total(){
        return ID_A;
    }
   
    
    
   
    setInterval(function(){
        // a = ID_A;
        a = total();
        getdata();
        },10000);
 
    
    function getdata(){    
        $.ajax({
 
        // type:"HEAD",
            async:false,
            datatype:"json",
            beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
        },
            url:"http://127.0.0.1:8000/api/",
            success:function (data){
           
            ID_A = data.slice(-1)[0]["ID"];
            ID_N = (data.length)

            if (ID_N>a){
                alert("新資料來囉！！")
            }
            
            // console.log(ID_N)
            $('section').remove();
            for (var i = data.length-1; i>-1; i--){
                var nba_page_url = ("http://127.0.0.1:8000/fullnews/" +data[i]['ID']);
                // console.log(nba_page_url)
                if((data[i]['cotent'].length)>=50){
                   var fusion_cotent = data[i]['cotent'].slice(0,250)
                    } 
                
                

                $('.content_all').append($('<section></section>')
                .append($('<div></div>')
                .attr("class",'title_box')
                .append($('<div></div>')
                .attr("class",'title').text(data[i]['title']))
                .append($('<div></div>')
                .attr("class","time").text(data[i]['time'])))
                .append($("</br>"))
                .append($('<div></div>')
                .attr("class","content_box")
                .append($('<img></img>')
                .attr("class","content_img").attr("src",data[i]['img']))
                .append($('<div></div>')
                .attr("class","content").text(fusion_cotent)
                .append($('<a></a>')
                .attr("class","read_link").attr("href",nba_page_url)
                .text("....(繼續閱讀)")))))
                
            }
         
        },
            error:function(){
                console.log("error!!");
            }
        });
    }
    
});