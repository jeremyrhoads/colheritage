/**
 * Created by MCR on 2/26/15.
 */
$(document).ready(function() {

    /*alert('hey');*/

    $('#id_username').on('change', function(){

        var username = $(this).val();

        //console.log(username);

        $.ajax({
            url: '/account/signup.check_username/',
            data: {
                u: username,
            }, //data
            type: 'POST',
            success: function(resp){
		   		if (resp = '1'){
					$('#username_message').text('username is available');
				}else{
				    $('#username_message').text('username is taken');
				}
		   }//success
        }); //ajax


    }); //change

    /*console.log('world');*/

}); //ready