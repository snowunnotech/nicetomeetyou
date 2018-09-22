var url = 'http://127.0.0.1:8000/api/nbaCrawler/'

$.ajax({
    method: 'GET',
    url: url,
    success: function(data) {
        console.log(data)
        renderHTML(data);
        console.log("Success")
    },
    error: function(error_data) {
        console.log("Error")
    }
})



function renderHTML(data) {
    var container = document.getElementById("container")
    var htmlString = ""

    for (i = 0; i < data.length; i++) {
        htmlString += "<tr><th><img src=" + data[i].post_image_url + " width='220px'></th>";
        htmlString += "<th>" + data[i].post_title + "</th>";
        var d = new Date(data[i].post_date)

        var time = d.getFullYear() + "-" + ("0" + (d.getMonth()+1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) 
                        + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2);

        htmlString += "<th>" + time + "</th>";
        htmlString += "<th><a href=" + data[i].post_url + ">Link</a></th>"
        htmlString += "<th><input type='button' id='btn' onclick='loadContent(" + data[i].pk + ")' value='Content' /></th></tr>"
        // htmlString += "<th><input type='button' id='btn' id=" + data[i].pk + "/></th></tr>"
    }

    container.insertAdjacentHTML('beforeend', htmlString);
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

        htmlString += "<dialog open id='content_dialog'><div style='width: 80%'><button onclick='closeDialog()' style='align: left' class='btn'>X</button><br>"
        htmlString += "<img src=" + data.post_image_url + " width='500'>";
        htmlString += "<div style='text-align: left;'>" + data.post_content + "</div></div></dialog>"

        container.insertAdjacentHTML('beforeend', htmlString);   
    }
}

function closeDialog() {
    var dialog = document.getElementById("content_dialog");
    dialog.close(); 
    dialog.remove();
}