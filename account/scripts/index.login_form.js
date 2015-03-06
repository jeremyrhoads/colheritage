/**
 * Created by MCR on 3/2/15.
 */
$(function() {

    //ajax
    $('#login_form').ajaxForm(function(data){

        $('#jquery-loadmodal-js').html(data);

    });//ajaxForm

}); //ready