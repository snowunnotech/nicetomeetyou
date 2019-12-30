all_news= document.querySelector('.all_news')
xhr = new XMLHttpRequest()
all_news.addEventListener('click',function(e){
    if (e.target.classList.contains('news_ajax')){
        alink = e.target.previousElementSibling['href']
        title = e.target.previousElementSibling.innerText
        content_node = e.target.parentNode.nextElementSibling
        // xhr open傳網址過去
        // xhr.open("GET",`./getnews_detail/${alink}`)
        xhr.open("POST","./getnews_detail")
        xhr.setRequestHeader("Content-type","application/json;charset=utf-8");
        const data = JSON.stringify({
            'href': alink,
            'title':title
        })
        xhr.send(data); // 3. 送出
        xhr.onload = function(){
            const res_data = JSON.parse(xhr.responseText);
            // 放到顯示畫面上
            display_info(content_node, res_data);
            if (content_node.classList.contains('news_hidden')){
                e.target.value = "Ajax拿取資料";
            }else{
                e.target.value = "隱藏內文";
            }
        }
    }
})
function display_info(node, res_data){
    node.innerText = res_data.content;
    node.classList.toggle("news_detailbox");
    node.classList.toggle("news_hidden");
}