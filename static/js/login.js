$(".form-reset").submit(function(e) {
    e.preventDefault();
    $(".btn-send-reset").data("original", $(".btn-send-reset").text());
    $(".btn-send-reset").text("Aguarde...").attr("disabled", true);
    $.ajax({
        type: 'POST',
        url: '/login/reset',
        data: $('.form-reset').serialize(),
        complete: function(response) {
            if(parseFloat(response.status) == 201){
                bootbox.alert("Você receberá um email com os detalhes para criar uma nova senha!");
                $(".btn-send-reset").text($(".btn-send-reset").data("original")).attr("disabled", false);
            } else {
                bootbox.alert("Falha ao tentar solicitar nova senha, tente novamente mais tarde!");
                $(".btn-send-reset").text($(".btn-send-reset").data("original")).attr("disabled", false);
            }
    }});
    return false;
});