document.addEventListener('DOMContentLoaded', function() {
    const webSocketBridge = new channels.WebSocketBridge();
    webSocketBridge.connect('/new_post/');
    webSocketBridge.listen(function(action, stream) {
        console.log("Res:", action);

        if (action.event == "New Post") {
            if (confirm("有新的文章加入，是否繼續？")) {
                window.location.href = "http://127.0.0.1:8000/";
            }
        }
    })
})
