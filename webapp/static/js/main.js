
$('#submitTxt').on('click', function(){
    var msgTxt = $('#inputtxtarea').val();
    $.ajax({
        url: URL + "messages",
        type: "POST",
        data: {
            text: msgTxt,
        },
        headers: { "X-CSRFToken": getCookie("csrftoken")},
        success:function(data){
            $('#notificationbox').text('Message sent successfully');
            $('#notificationbox').removeClass('error').addClass('success');
            renderList();
        },
        error: function(xhr, txtStatus, errorThrown){
            console.log(xhr.responseText);
            $('#notificationbox').text('Unexpected error while saving data. Error: ' + errorThrown);
            $('#notificationbox').removeClass('success').addClass('error');
        }
    });
});

$(document).on("click", ".dltbtn", function () {
	var pk = $(this).attr('pk');
    $.ajax({
        url: URL + "messages/" + pk,
        type: "DELETE",
        headers: { "X-CSRFToken": getCookie("csrftoken")},
        success:function(data){
            renderList();
        },
        error: function(xhr, txtStatus, errorThrown){
            $('#notificationbox').text('Error: Unexpected error while deleting message.');
            $('#notificationbox').addClass('error');
        }
    });
});

$(document).on("click", ".listtext", function () {
	var txt = $(this).val();
	var id = $(this).attr('id');
	$(this).removeClass('font-weight-bold');
	$(this).prev('.unseen').removeClass('unseen');
	localStorage.setItem(id,'seen');
    $("#textViewModal #viewtxtarea").val(txt);
    $('#textViewModal').modal('show');
});

function renderList() {
    $.ajax({
        url: URL + "listview",
        type: "GET",
        success:function(data){
            $('#tableview').html(data);
            $('.listtext').each(function(i, obj) {
                if (localStorage.getItem(obj.id) && localStorage.getItem(obj.id) == 'seen') {
                    obj.classList.remove('font-weight-bold');
                    obj.previousElementSibling.classList.remove('unseen');
                }
            });
        },
        error: function(xhr, txtStatus, errorThrown){
            $('#notificationbox').text('Error: Unexpected error while fetching data.');
            $('#notificationbox').addClass('error');
        }
    });
}

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

$(document).ready(function () {
    renderList();
});