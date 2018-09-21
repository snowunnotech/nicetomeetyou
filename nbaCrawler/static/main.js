var url = 'http://127.0.0.1:8000/api/nbaCrawler/'
// var btn = document.getElementById("btn")

// btn.addEventListener("click", function() {
//     var req = new XMLHttpRequest();
//     req.open("GET", url + this.id + '/');
//     req.onload = function() {
//         var data = JSON.parse(req.responseText);
//         console.log(data)
//     }

//     req.send();
// })

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
        htmlString += "<tr><th><img src=" + data[i].post_image_url + "></th>";
        htmlString += "<th>" + data[i].post_title + "</th>";
        var d = new Date(data[i].post_date)

        var time = d.getFullYear() + "-" + ("0" + (d.getMonth()+1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) 
                        + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2);

        htmlString += "<th>" + time + "</th>";
        htmlString += "<th><a href=" + data[i].post_url + ">Link</a></th>"
        htmlString += "<th><button class='btn' id=" + data[i].pk + "> " + "Content </button></th></tr>"
    }

    container.insertAdjacentHTML('beforeend', htmlString);
}

