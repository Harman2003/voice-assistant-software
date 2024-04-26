$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message").text(message);
    }

    //Display response
     eel.expose(DisplayResponse);
     function DisplayResponse(message) {
         $(".siri-response").text(message);
         $(".siri-response").attr("hidden", false);
     }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

});