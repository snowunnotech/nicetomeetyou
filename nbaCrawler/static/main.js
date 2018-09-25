var url = 'http://127.0.0.1:8000/api/nbaCrawler/'
var dataLength = 0

$(document).ready(function(){
    $firstload = loadPost();

    if($firstload) {
        setInterval('loadPost()', 10000);
    }


})

function loadPost() {
    $.ajax({
        method: 'GET',
        url: url,
        success: function(data) {
            renderHTML(data);
            console.log("Success")
        },
        error: function(error_data) {
            console.log("Error")
        }
    })

    return true
}


function renderHTML(data) {
    var container = document.getElementById("container")
    var htmlString = ""

    if (data.length > dataLength) {
        
        console.log('Add New Post.')

        for (i = 0; i < data.length - dataLength; i++) {
            htmlString += "<tr><th><img src=" + data[i].post_image_url + " width='220px'></th>";
            htmlString += "<th>" + data[i].post_title + "</th>";
            var d = new Date(data[i].post_date)
    
            var time = d.getFullYear() + "-" + ("0" + (d.getMonth()+1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) 
                            + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2);
    
            htmlString += "<th>" + time + "</th>";
            htmlString += "<th><a href=" + data[i].post_url + ">Link</a></th>"
            htmlString += "<th><input type='button' id='btn' onclick='loadContent(" + data[i].pk + ")' value='Content' /></th></tr>"
    
        }

        container.insertAdjacentHTML('afterbegin', htmlString);
    }

    dataLength = data.length

}

function loadContent(post_id) {
    $.ajax({
        method: 'GET',
        url: url + post_id + '/',
        success: function(data) {
            renderHTML(data)
            console.log("Success")
        },
        error: function(error_data) {
            console.log("Error")
        }
    })

    function renderHTML(data) {
        
        var container = document.getElementById("content")
        var htmlString = ""

        htmlString += "<dialog open id='content_dialog'><div><button onclick='closeDialog()' style='align: left' class='btn'>X</button><br>"
        htmlString += "<img src=" + data.post_image_url + " width='500px'>";
        htmlString += "<div style='text-align: left; max-height: 400px; overflow:auto;'>" + data.post_content + "</div></div></dialog>"

        container.insertAdjacentHTML('beforeend', htmlString);   
    }
}

function closeDialog() {
    var dialog = document.getElementById("content_dialog");
    dialog.close(); 
    dialog.remove();
}
