$( document ).ready(function() {
    $('#loginform').submit(function(e){
        return false;
    });
    $('#modaltrigger').leanModal({ top: 110, overlay: 0.45, closeButton: ".hidemodal" });
    $('#login_button').click(function(){
        $('#loginmodal').show();
    });
    // $('#loginbtn').click(function(){
    //     $('#loginmodal').hide();
    // });
});
           