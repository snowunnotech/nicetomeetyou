var API_URI = "/get_news/";


var SearchResult = {
  currentResultTime: Date.now(),
  query: function() {

    $.ajax({
        url: API_URI,
        type: 'POST',
        data: JSON.stringify({query: '', time: Date.now()}),
        contentType: "application/json",
        dataType: 'json',
    })
    .done(this.renderSearchResult)
    .fail(this.renderSearchFail);
  },


  renderSearchFail: function(data) {
    console.log('fail');
    $('div').html("OOPS! Something goes wrong");
  },

  renderSearchResult: function(data) {
    console.log('ok');
    SearchResult.currentResultTime = Math.max(SearchResult.currentResultTime, data.time);
    if (data.time == null || data.time >= SearchResult.currentResultTime) {
      var text = '';
      if (data.news.length > 0) {
        console.log(data.news);

        data.news.forEach(element => {
          var title = element[0];
          var content = element[1];
          var img = element[2];
          var url = element[3]

          text += SearchResult.renderNgramRowHtml(title, content, img, url);
  
          // text += `<tr>
          // <td class="title">${title}</td>
          // <td class="content">${content}</td></tr>`;
        });

        return $('div').html(text);
      }
      return $('div').html("OOPS! Something goes wrong");
    }
  },

  renderNgramRowHtml: function(title, content, img, url) {

    return `<dt><a href=${url}>
              <span class="img-boxs">
                <img src=${img} ></span>
              <h3>${title}</h3>
              <p>${content}</p>
              <br><br>
            </a></dt>`

  },
};

SearchResult.query();
