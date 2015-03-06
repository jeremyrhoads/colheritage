/**
 * Created by MCR on 3/2/15.
 */
$(function() {

    //modal
    $('.add-button ').on('click', function(){

        var itemid = $(this).attr('data-itemid');
        var qyt; //this will pull the .val() from a text field in the form


        //$.loadmodal({
        //    url: '/catalogue/shopping_cart.add',
        //    title: 'Shopping Cart',
        //    width: '700px',
        //});

    });//show modal

    ////ajax
    //$('#login_form').ajaxForm(function(data){
    //
    //    //console.log('#login_form_container');
    //    $('#login_form_container').html(data);
    //
    //});//ajaxForm

});//ready