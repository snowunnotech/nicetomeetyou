String.prototype.format = function(){
    var str = this;
    for(var i=0; i<arguments.length; i++){
        var str = str.replace(new RegExp('\\{'+ i + '\\}', 'g'), arguments[i]);
    }
    return str;
}