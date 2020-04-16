$(function() {
  const dataSource = new kendo.data.DataSource({
    transport: {
      read: function(options) {
        $.ajax({
          url: 'http://127.0.0.1:8000/get_news/',
          // jsonp
          dataType: 'json',
          success: function(result) {
            options.success(result);
          },
          error: function(result) {
            options.error(result);
          },
        });
      },
    },
    schema: {
      type: 'json',
      data: 'data',
      parse: function(response) {
        const news = {data: []};
        for (let i = 0; i < response['data'].length; i++) {
          const newResponse = {
            title: response['data'][i].title,
            url: response['data'][i].url,
            image: response['data'][i].image,
            timestamp: new Date(response['data'][i].timestamp * 1000).toLocaleString(),
          };
          news['data'].push(newResponse);
        }
        return news;
      },
      model: {
        fields: {
          title: 'title',
          url: 'url',
          image: 'image',
          timestamp: 'timestamp',
        },
      },
      total: function(data) {
        return data.data.length;
      },
    },
    pageSize: 11,
  });

  $('#pager').kendoPager({
    dataSource: dataSource,
  });

  $('#listView').kendoListView({
    dataSource: dataSource,
    template: kendo.template($('#template').html()),
  });
});
