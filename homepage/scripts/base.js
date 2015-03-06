/**
 * Created by MCR on 3/2/15.
 */
$(function() {

    //modal
    $('#show_login_dialogue').on('click', function(){

        $.loadmodal('/account/login.login_form')

    });//show modal

    ////ajax
    //$('#login_form').ajaxForm(function(data){
    //
    //    //console.log('#login_form_container');
    //    $('#login_form_container').html(data);
    //
    //});//ajaxForm

});//ready