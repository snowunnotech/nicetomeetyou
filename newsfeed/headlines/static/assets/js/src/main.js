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
    ajaxLoadPost();
 })

function renderPost(data){
    var container = document.getElementById("container-row")
    var postTemplate = "<div class=\"col-md-4\"><div class=\"card mb-4 box-shadow\"><img class=\"card-img-top\" src={0}><div class=\"card-body\"><p class=\"card-text\">{1}</p><div class=\"d-flex justify-content-between align-items-center\"><div class=\"btn-group\"><button type=\"button\" class=\"btn btn-sm btn-outline-secondary\" data-toggle=\"modal\" data-target=\"#{3}\" >View</button></div><small class=\"text-muted\">{2}</small></div></div></div></div>"
 
    for(var i=0; i<data.length; ++i){
        var img_url = data[i].img_url;
        var post_title = data[i].post_title
        var post_id = data[i].post_id
        var post_date = new Date(data[i].post_date);

        var posts = String.format(postTemplate, img_url, post_title, post_date.toLocaleString(), post_id)
        container.insertAdjacentHTML('beforeend', posts);
    }

    var container = document.getElementById("main")
    var postPopout = "<div id=\"{0}\" class=\"modal fade\" role=\"dialog\"><div class=\"modal-dialog\"><!-- Modal content--><div class=\"modal-content\"><div class=\"modal-header\"><button type=\"button\" class=\"close\" data-dismiss=\"modal\">&times;</button><h4 class=\"modal-title\">{1}</h4></div><div class=\"modal-body\"><p>{2}</p></div><div class=\"modal-footer\"><button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Close</button></div></div></div></div>"
    for(var i=0; i<data.length; ++i){
        var post_title = data[i].post_title
        var post_id = data[i].post_id
        var post_content = data[i].post_content

        var popout = String.format(postPopout, post_id, post_title, post_content)
        container.insertAdjacentHTML('beforeend', popout);
    }

    // DEBUG PRINT
    console.log(data)
}

function ajaxLoadPost(){
    $.ajax({  
      url: window.location.origin + '/api/headlines/',  
      type: 'GET',
      success: renderPost,  
      dataType: "json"  
    });  

    //return true;
}