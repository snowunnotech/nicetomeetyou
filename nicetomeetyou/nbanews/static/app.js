$(document).ready(() =>{
    $.ajax({
      url: window.location.origin + '/newsapi/',
      dataType: 'json',
      type: 'GET',
      success: (data) => {
        updateNewsList(data)
      },
      error: console.error.bind(console)
    });
});

function updateNewsList(data) {
  data.forEach((d) => {
    var row = document.createElement('div');
    $(row)
      .addClass('news-title-item')
      .append(d.post_title)
      .hover(() => {
        updateNewsDetail(d.post_id);
        $(row).addClass('news-title-item-hover');
      }, () => {
        $(row).removeClass('news-title-item-hover');
      });

    $('#news-list').append(row)
  });
}

function updateNewsDetail(newsid) {
    $.ajax({
      url: window.location.origin + '/newsapi/' + newsid,
      dataType: 'json',
      type: 'GET',
      success: (data) => {
        $('#news-image').attr('src', data.image_url);
        $('#news-content').html(data.post_content);
      },
      error: console.error.bind(console)
    });
}
