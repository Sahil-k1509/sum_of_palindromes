$(document).ready(function(){
    $("#pal1").html('');
    $("#pal2").html('');
    $("#pal3").html('');
    $("#result").html('');
    $("#error-display").html('');

    $("#number-sub").click(function(event){
        event.preventDefault();

        function isNum(n){return /^-?\d+$/.test(n);}

        let number = document.getElementById("numberField").value;
        // console.log(number);
        // console.log(isNum(number));
        if (isNum(number)){
            if (parseInt(number)>=0){
                $("#error-display").html("")
                $("#pal1").html('');
                $("#pal2").html('');
                $("#pal3").html('');
                $("#result").html('');
                $('#pal1').removeClass('appearing');
                $('#pal2').removeClass('appearing');
                $('#pal3').removeClass('appearing');
                $('#result').removeClass('appearing');

                $.ajax({
                    type: "POST",
                    url: "/",
                    data: {'number': number},
                    success: function(response){
                        setTimeout(function(){
                            $('#pal1').addClass('appearing');
                            $('#pal1').html(response.number1);
                        }, 1000);
                        setTimeout(function(){
                            $('#pal2').addClass('appearing');
                            $('#pal2').html(response.number2);
                        }, 2000);
                        setTimeout(function(){
                            $('#pal3').addClass('appearing');
                            $('#pal3').html(response.number3);
                        }, 3000);
                        setTimeout(function(){
                            $('#result').addClass('appearing');
                            $('#result').html(response.number3+response.number2+response.number1);
                        }, 5000);
                    }
                });
            } else {
                $("#error-display").html("Please Enter Positive Integer.")
            }
        } else {
            $("#error-display").html("Please Enter a Natural Number.")
        }
        
    });
});