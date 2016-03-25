$(document).ready(function(){console.log("this is a test!@!@!@!")})
$(document).ready(function(){
	$('#getMovieInfo').click(getInfo)
	$(#posts).append("<div><img src= '" + response + "'" + "<div>")
})
function getInfo(){
	
}
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
