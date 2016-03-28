$(document).ready(function(){console.log("this is a test!@!@!@!")})

function appendDom(response){
	$('#main-block').append('<div><img src="' + response + '"></img><div>')
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
			// data: {'var': id},
			success: function(response) {
				// console.log("response: ", response)
				console.log("hello")
				console.log(response);
				var obj = JSON.parse(response);
				// console.log(obj.list)
				console.log(obj);
				// console.log(obj.list);
				var i=0;
				while(i<10){
					// console.log("Trying")
					console.log(i)
					console.log(obj.list[i]);
					// console.log(obj.list[i].image.url);
					// webbrowser.open(obj.list[i].image.url);
					appendDom(obj.list[i]);
					i++;
				}
				// appendDom(obj.url);
			}
		});
	});
});
