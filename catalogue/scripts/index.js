/**
 * Created by MCR on 3/2/15.
 */
$(function() {

    //modal
    $('.add-button ').on('click', function(){

        var itemid = $(this).attr('data-id');
        var id = "qty_" + itemid;
        var qty = $("#" + id).val(); //this will pull the .val() from a text field in the form
        console.log(itemid)
        console.log(id)
        console.log(qty)

        //in case the user leaves qty blank
        if(qty < 1) qty = 1;

        $.loadmodal({
            url: '/catalogue/shopping_cart.add/' + itemid + '/' + qty + '/rental',
            title: 'Shopping Cart',
            width: '700px',
        });

    });//show modal

    //product modal
    $('.add-button-p ').on('click', function(){

        var pid = $(this).attr('data-pid');
        var id = "qty_" + pid;
        var qty = $("#" + id).val(); //this will pull the .val() from a text field in the form
        console.log(pid)
        console.log(id)
        console.log(qty)

        //in case the user leaves qty blank
        if(qty < 1) qty = 1;

        $.loadmodal({
            url: '/catalogue/shopping_cart.add/' + pid + '/' + qty + '/product',
            title: 'Shopping Cart',
            width: '700px',
        });

    });//show modal


    //the search filter for the products
    $("#filter").keyup(function(){

            // Retrieve the input field text and reset the count to zero
            var filter = $(this).val(), count = 0;

            // Loop through the products
            $(".thumbnail").each(function(){
                var nameelem = $(this).find('.name');
                var descelem = $(this).find('.description');
                // If the list item does not contain the text phrase fade it out
                if (nameelem.text().search(new RegExp(filter, "i")) < 0 && descelem.text().search(new RegExp(filter, "i")) < 0) {
                    $(this).fadeOut();
                } else {
                    $(this).show();
                    count++;
                } //else

            // Update the count
            var numberItems = count;
            $("#filter-count").text("Search results : "+count);

        });//thumbnail loop

    }); //keyup

});//ready