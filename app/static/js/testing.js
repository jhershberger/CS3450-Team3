
$(document).ready(function(){


		var id = $('#id-input').val()
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
					appendDom(obj.list[i],obj.title[i],obj.score[i]);

					i++;
				}
				$("#loading").hide();
				// appendDom(obj.url);
			}
		});
})

function appendDom(response,title,score){
	$('#main-block').append(
		'<div class = "row new_block">'
			+ '<div class ="col-sm-3"><a href ="/moviePage" ><img id="poster_image" src="' + response + '">'
				+ '</img></a></div><div class="col-sm-8"><h1>'+ title +'</h1>'
					+'<h1 id="main-score">'+ score +'</h1>'
						+ '</div></div>')
}
