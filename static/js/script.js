$(document).ready(function () {

    $('#generated-password--button').click(function(event) {
        event.preventDefault()
        var generatedPassword

        url = '/get-a-new-password'
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                generatedPassword = data.password
                console.log("Generated Password is ", generatedPassword)
                $('#generated-password').val(generatedPassword)
            }
        })
    })
});