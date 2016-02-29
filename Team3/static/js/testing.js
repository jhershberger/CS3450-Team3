$(document).ready(function(){console.log("this is a test!@!@!@!")})

$(function(){
	$('#get-movie').click(function(){
		var id = $('#id-input').val()
		console.log("id: ", id)
		console.log("clicked!")
		$.ajax({
			type: 'POST',
			url: '/testSERVER',
			async: true,
			data: {'var': id},
			success: function(response) {
				console.log("response: ", response)
			}
		});
	});
});