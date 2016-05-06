function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready( function() {
    $(".edit").click( function(event) {
    	var state = $('#edit').val();
   		var id = $(this).data('id');
    	if (state == "Editar") {
    		$('.product-' + id).removeAttr('disabled');
    		$(this).prop('value', 'Save')
		} else {
			$('.product-' + id).attr('disabled','disabled');
    		$(this).prop('value', 'Editar')
    		var nombre = $('input.nombre.product-'+id).val()
    		var codigo = $('input.codigo.product-'+id).val()
    		var cantidad = $('input.cantidad.product-'+id).val()
    		var csrftoken = getCookie('csrftoken');
    		request = $.ajax({
        		url: "/",
        		type: "post",
        		dataType: "json",
        		data: {
        				'id' : id,
                        'nombre': nombre,
                        'codigo': codigo,
                        'cantidad': cantidad,
                        'csrfmiddlewaretoken': csrftoken
                        },

    		});
		}
    });

});

