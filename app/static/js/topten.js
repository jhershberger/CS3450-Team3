
$(document).ready(function(){

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
					appendDom(obj.titles[i]);

					i++;
				}
				$("#loading").hide();
				// appendDom(obj.url);
			}
		});

    });

    function appendDom(title){
    	$('#top-ten-list').append(
    		'<li class = "top-ten-item">'+title+'</li>')
    }
