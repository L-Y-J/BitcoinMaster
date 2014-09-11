/**
 * Created by LI on 14-3-22.
 */
function onload(){
    $.get("/onLoad",null,call);
}

function call(data){
    var str = data.toString();

    var obj = eval('(' + str + ')');

    $("#difficutly").val(obj.difficulty);
    $("#hash").val(obj.hash);
    $("#index").val(obj.blocks);
}