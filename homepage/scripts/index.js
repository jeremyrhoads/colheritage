/**
 * Created by MCR on 2/24/15.
 * This is the script we built in class to be able to use AJAX to check username availability
 */
$(function() {

    /**
    $('#id_username').on('change', function() {
        console.log('change'); //this will let us know that the trigger is working
    }); //change
     */

    $('#id_username').on('change', function() {

        $.ajax({
           url: '/account/index.check_username'
        });

    }); //change


}); //ready