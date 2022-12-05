$(document).on('submit', '#comment-form', function(e) {
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url : '/course/sync-session/stream/comments/submit/',
		data: {
			username: $('#username').val(),
			text: $('#text').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success: function(data) {
			// alert(data)
		}
	});
	document.getElementById('username').value = '';
	document.getElementById('text').value = '';
})