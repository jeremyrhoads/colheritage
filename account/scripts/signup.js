/**
 * Created by MCR on 2/26/15.
 */
$(document).ready(function() {

    alert('hey');

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
                    //console.log(username);
                    $('#username_message').attr({
                        "class": "alert alert-success",
                        "role": "alert"
                    }).text('Nice choice. This username is available');
				}else{
				    $('#username_message').attr({
                        "class": "alert alert-danger",
                        "role": "alert"
                    }).text('Sorry, this username is taken');
				}
		   }//success
        }); //ajax



    }); //change

    $('#c-pwd').on('change', function() {

        var cpwd = $(this).val();
        var pwd = $('#pwd').val();

        if (cpwd != pwd){
            //console.log('no match');
            $('#pwd_message').text('Make sure this password matches the first one you entered');
        }else{
            $('#pwd_message').text('');
            console.log('match');
        }
    });

    /*console.log('world');*/

}); //ready