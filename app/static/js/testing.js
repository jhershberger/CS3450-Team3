
$(document).ready(function(){
		var id = $('#id-input').val()
		$.ajax({
			type: 'POST',
			url: '/testSERVER',
			async: true,
			// data: {'var': id},
			success: function(response) {
				// console.log("response: ", response)
				// console.log("hello")
				// console.log(response);
				var obj = JSON.parse(response);
				// console.log(obj.list)
				console.log(obj);
				// console.log(obj.list);
				var i=0;
				while(i<10){
					// console.log(i)
					// console.log(obj.list[i]);
					appendDom(obj.list[i],obj.title[i],obj.score[i],obj.ids[i],i,obj.ourscore[i],obj.names[i]);

					i++;
				}
				$("#loading").hide();
				// appendDom(obj.url);
			}
		});


});



function appendDom(response,title,score,id,i,ourscore,name){
	$('#main-block').append(
		'<div class = "row new_block">'
			+ '<div class ="col-sm-4"><form action = "/movieUpdate" method="post">'
			+ '<input type = "hidden" id= "thisOne" name= "really" value="'+id+'">'
			+ '<div class="contain"><input class="poster_image" type ="image" src="' + response + '"></form>'
			+'<form class = "rate_movie" action="/rateMovie" method="post">'
		 + '<input type = "hidden" id= "rating'+i+'" name= "score" value="k">'
		 +'<input id="hiddenId" input type="hidden" name="hide" value="'+id+'">'
		 +'<button type="submit" class="btn btn-primary">Rate This Movie!</button>'
		  +'<span id="val'+i+'">0</span>'
			+'</form></div>'
				+ '</img><div class= "ratings_box">'
					+ '<input id="slider" type="range" min="0" max="10" value="0" step=".5" onchange="showValue'+i+'(this.value)"/>'
					+'<script type="text/javascript">'
					+'function showValue'+i+'(newValue)'
					+'{'
						+'document.getElementById("val'+i+'").innerHTML=newValue;'
						+'document.getElementById("rating'+i+'").value=newValue;'
					+'}'
					+'</script>'
					+	'</div></div><div class="col-sm-8"><h3>'+name+ '</h3><h1>'+ title +'</h1>'
					+'<h2 id="main-score">ImDbs Rating: '+ score +'</h1>'
					+'<h2 id="main-score">Sloths Rating: '+ ourscore + '</h1>'
						+ '</div>' + '</div>')
}
