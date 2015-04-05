/**
 * Created by MCR on 3/2/15.
 */
$(function() {

    //modal
    $('#show_login_dialogue').on('click', function(){

        $.loadmodal({
            url: '/account/index.login_form',
            title: 'Login',
        });

    });//show modal

    //return alert
    $('#return-btn').on('click', function(){
        alert("Return processed successfully");
    })

});//ready