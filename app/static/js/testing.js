
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
					console.log(i)
					console.log(obj.list[i]);
					appendDom(obj.list[i],obj.title[i],obj.score[i],obj.ids[i]);

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
			// data: {'var': id},
			success: function(response) {
				// console.log("response: ", response)
				console.log("we're here")
				console.log(response);
				var obj = JSON.parse(response);
				// console.log(obj.list)
				console.log(obj);
				// console.log(obj.list);
				var i=0;
				while(i<10){
					console.log(i)
					// console.log(obj.list[i]);
					appendDom2(obj.title[i]);
					appendDom3(obj.besttitles[i]);

					i++;
				}
				$("#loading").hide();
				// appendDom(obj.url);
			}
		});
	// $(document).on("click", ".poster_image", function(){
	// 	// TODO
	// 	console.log("doing stuff");
	// 	var movieId = $('#submit').val();
	// 	console.log("We're here!");
	// 	$.ajax({
	// 		type:'POST',
	// 		url:'/movieUpdate',
	// 		async: true,
	// 		data: {'var': movieId},
	// 		success: function(response){
	// 			console.log("We win");
	// 			console.log(response);
	// 		}
	// 	})
	// });

});

// function appendDom(response,title,score,id){
// 	$('#main-block').append(
// 		'<div class = "row new_block">'
// 			+ '<div class ="col-sm-4"><input id="submit" type="hidden" value="'+ id + '"><a href ="/moviePage" ><img class="poster_image" src="' + response + '">'
// 				+ '</img></a></div><div class="col-sm-8"><h1>'+ title +'</h1>'
// 					+'<h1 id="main-score">'+ score +'</h1>'
// 						+ '</div></div>')
// }
function appendDom(response,title,score,id){
	$('#main-block').append(
		'<div class = "row new_block">'
			+ '<div class ="col-sm-4"><form action = "/movieUpdate" method="post"><input type = "hidden" id= "thisOne" name= "really" value="'+id+'"><input class="poster_image" type ="image" src="' + response + '"></form>'
				+ '</img></div><div class="col-sm-8"><h1>'+ title +'</h1>'
					+'<h1 id="main-score">'+ score +'</h1>'
						+ '</div></div>')
}

function appendDom2(title){
	$('#top-ten-list-friends').append(
		'<li>'+title+'</li>')
}
function appendDom3(besttitle){
	$('#top-ten-list').append(
		'<li>'+besttitle+'</li>')
}
