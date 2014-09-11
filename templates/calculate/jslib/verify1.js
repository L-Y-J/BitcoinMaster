function verify(){
    var jqueryObj1 = $("#difficutly");
    var difficutly = jqueryObj1.val();

    var jqueryObi2 = $("#caclute");
    var caclute = jqueryObi2.val();

    var jqueryObj3 = $("#hash");
    var hash = jqueryObj3.val();

    var jqueryObj4 = $("#index");
    var index = jqueryObj4.val();

    var jqueryObj5 = $("#total");
    var total = jqueryObj5.val();

    if (caclute == null || caclute==""){
        alert("算力不能为空！");
        return;
    }

    $.get("/calculate",{difficutly:difficutly,caclute:caclute,hash:hash,index:index,total:total},back);
}

function back(data){
    var str = data.toString();
    var obj = eval('(' + str + ')');

    var result = obj.result;
    var income = parseFloat(result);
    $("#LTC1").html(income.toFixed(4));
    $("#LTC2").html((income*7).toFixed(4));
    $("#LTC3").html((income*30).toFixed(4));
}