$document.ready(function(){
    $("buton").load(function(){
        $("#popup").hide();
    });
    $("button").click(function(){
        $("#popup").show();
    });
});