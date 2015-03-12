/**
 * Created by MCR on 2/26/15.
 */
$(document).ready(function() {

    //alert('hey');

    //$('#id_username').on('change', function(){
    //
    //    var username = $(this).val();
    //
    //    //console.log(username);
    //
    //    $.ajax({
    //       
		//		}
		//   }//success
    //    }); //ajax
    //
    //
    //
    //}); //change

    $('#c-pwd').on('change', function() {

        var cpwd = $(this).val();
        var pwd = $('#pwd').val();

        if (cpwd != pwd){
            //console.log('no match');
            $(this).css({
                "border": "thin solid red"
            });
            $('#pwd_message').attr({
                "class": "alert alert-danger"
            }).text('Your passwords do not match');
        }else{
            $(this).css({
                "border": "thin solid green"
            });
            $('#pwd_message').attr({
                "class": "alert alert-success"
            }).text('Noice');
            console.log('match');
        }
    });

    /*console.log('world');*/

}); //ready