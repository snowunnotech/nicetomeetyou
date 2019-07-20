var counter = 0;


function Get(callback) {
    $(document).ready(function() {
        if (counter===5) {
    		$('#jsonresp').empty();
        counter = 0;
    }

        $.ajax({
            type: "GET",
            url: "https://sarah-nba-news.herokuapp.com/news",
            dataType: "json",
            success: function(data) {
                if(callback) callback(data); 
                counter++;
                // if (counter < 5) Get();
            },
            error: function(xhr, textStatus, error) {
                console.log(xhr.statusText);
            }
        });
    });
}

$(document).ready(() => {
    Get(function(data){
        $.each(data, function(k, v){
            k = k+1
            // $('#jsonresp').append('<li>' + v['title'] +'</li>');
            $('#jsonresp').
            append('<div class="card"> </div>').
            append('<div class="card-body"> </div>').
            append('<a href="/detail/'+ v['id'] +'/"><h5 class="card-title">' + v['title'] + '</h5><a>').
            append('<p class="card-text">' + v['time'] + '</p>');

        })
        
    });
})


