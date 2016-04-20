
$(document).ready(function(){

	// $("#rating_sloth1").mouseover(function(){
  //        $("#rating_sloth").css("opacity", 1);
  //    });

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
				// console.log(obj);
				// console.log(obj.list);
				var i=0;
				while(i<10){
					// console.log(i)
					// console.log(obj.list[i]);
					appendDom(obj.list[i],obj.title[i],obj.score[i],obj.ids[i],i);

					i++;
				}
				$("#loading").hide();
				// appendDom(obj.url);
			}
		});
		$.ajax({
			type: 'POST',
			url: '/baseUpdater',
			async: true,
			success: function(response) {
				var obj = JSON.parse(response);
				var i=0;

				while(i<10){
					// console.log(i)
					// console.log(obj.list[i]);
					appendDom2(obj.title[i]);
					appendDom3(obj.besttitles[i]);

					i++;
				}


				$("#loading").hide();
			}
		});

});



function appendDom(response,title,score,id,i){
	$('#main-block').append(
		'<div class = "row new_block">'
			+ '<div class ="col-sm-4"><form action = "/movieUpdate" method="post">'
			+ '<input type = "hidden" id= "thisOne" name= "really" value="'+id+'">'
			+ '<input class="poster_image" type ="image" src="' + response + '"></form>'
				+ '</img><div class= "ratings_box">'
					+ '<input id="slider" type="range" min="0" max="10" value="0" step=".5" onchange="showValue'+i+'(this.value)"/>'
					+'<script type="text/javascript">'
					+'function showValue'+i+'(newValue)'
					+'{'
						+'document.getElementById("val'+i+'").innerHTML=newValue;'
						+'document.getElementById("rating'+i+'").value=newValue;'
					+'}'
					+'</script>'
					+'<form action="/rateMovie" method="post">'
				 +'<span id="val'+i+'">0</span>'
				 + '<input type = "hidden" id= "rating'+i+'" name= "score" value="k">'
				 +'<input id= "buttonpush" type="submit" value="RATE THIS MOVIE">'
			  	+'</form>'
					+	'</div></div><div class="col-sm-8"><h1>'+ title +'</h1>'
					+'<h1 id="main-score">'+ score +'</h1>'
						+ '</div>' + '</div>')
}

function appendDom2(title){
	$('#top-ten-list-friends').append(
		'<li>'+title+'</li>')
}
function appendDom3(besttitle){
	$('#top-ten-list').append(
		'<li>'+besttitle+'</li>')
}
