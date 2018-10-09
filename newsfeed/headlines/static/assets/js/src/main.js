/* Formatted-String */ 
String.format = function() {
    // The string containing the format items (e.g. "{0}")
    // will and always has to be the first argument.
    var theString = arguments[0];
    
    // start with the second argument (i = 1)
    for (var i = 1; i < arguments.length; i++) {
        // "gm" = RegEx options for Global search (more than one instance)
        // and for Multiline search
        var regEx = new RegExp("\\{" + (i - 1) + "\\}", "gm");
        theString = theString.replace(regEx, arguments[i]);
    }
    return theString;
}

$(document).ready(function(){
    $firstload = ajaxLoadPost();
    if($firstload) {
        setInterval('ajaxLoadPost()', 10000);
    }
 })

function renderPost(data){
    var container = document.getElementById("container-row")
    var postTemplate = "<div class=\"col-md-4\"><div class=\"card mb-4 box-shadow\"><img class=\"card-img-top\" src={0}><div class=\"card-body\"><p class=\"card-text\">{1}</p><div class=\"d-flex justify-content-between align-items-center\"><div class=\"btn-group\"><button type=\"button\" class=\"btn btn-sm btn-outline-secondary\">View</button></div><small class=\"text-muted\">{2}</small></div></div></div></div>"
    
    for(var i=0; i<data.length; ++i){
        var img_url = data[i].img_url;
        var post_title = data[i].post_title
        var post_date = new Date(data[i].post_date);

        var posts = String.format(postTemplate, img_url, post_title, post_date.toLocaleString())
        container.insertAdjacentHTML('beforeend', posts);
    }

    // DEBUG PRINT
    console.log(data)
}

function ajaxLoadPost(){
    $.ajax({  
      url: '/api/headlines/',  
      type: 'GET',
      success: renderPost,  
      dataType: "json"  
    });  

    //return true;
}