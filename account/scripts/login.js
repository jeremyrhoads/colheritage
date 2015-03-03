/**
 * Created by MCR on 3/2/15.
 */
$(function() {

    $('#login_form').ajaxForm(function(data){

        //console.log('#login_form_container');
        $('#login_form_container').html(data);

    });//ajaxForm

});//ready