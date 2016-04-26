
$(document).ready(function(){

		$.ajax({
			type: 'POST',
			url: '/baseUpdater',
			async: true,
			success: function(response) {
				var obj = JSON.parse(response);
				var i=0;

				while(i<10){
					console.log("GOING")
					// console.log(i)
					// console.log(obj.list[i]);
					appendDom2(obj.title[i],obj.ids[i]);
					appendDom3(obj.besttitles[i],obj.ids[i]);

					i++;
				}


				$("#loading").hide();
			}
		});

});




function appendDom2(title,id){
	$('#top-ten-list-friends').append(
		'<form id = "formSend" action = "/movieUpdate" method="post">'
		+'<li class = "top-ten-item"><a onclick="document.getElementById("formSend").submit()>'+title+'</a></li>'
		+'<input type = "hidden" name = "really" value = "'+id+'"'
		+'</form>'
	)
}
function appendDom3(besttitle,id){
	$('#top-ten-list').append(
		'<form id = "formSend" action = "/movieUpdate" method="post">'
		+'<li class = "top-ten-item"><a onclick="document.getElementById("formSend").submit()>'+besttitle+'</li>'
		+'<input type = "hidden" name = "really" value = "'+id+'"'
		+'</form>'
	)
}
