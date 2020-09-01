var wsUrl = "ws://" + window.location.host + '/index';
function init(){
    initWebsocket();
}
function initWebsocket() {
    socket = new WebSocket(wsUrl);
    socket.onmessage = function (e) {
        updateSta(e)    
    };
    socket.onopen = function (e) {
        console.log('open adhome websocket..');
        // socket.send("hello world");
    };
    socket.onclose = function(e){
        console.log('adhome websocket is closed.');
        setTimeout(function(){
            initWebsocket();
        },1500);
    };
    socket.onerror = function(e){
        console.log('adhome websocket has Error.');
        socket.close();
    }; 
}


function updateSta(e){ 
    try{
    	var data = (e.data); 
		var dataObj = JSON.parse(data);
        var objid_status = dataObj.message;
        console.log( dataObj.message );
        //重新整理
        if(objid_status.indexOf("refresh") !== -1){
        	
        	alertify.alert('注意', '抓取到新消息!', function(){
        		
        		window.location.reload();
        	});
        	
        }
        
    } catch (e) {

    }
}


// 啟動local websocket
// init();
window.addEventListener("load", init, false);
