var like = function(){
	var button = $(this) 
	is_like = $(this).hasClass('like')
	
	$.ajax({
		type: "POST",
		url: $(this).attr('href'),
		data: {
			csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
			record_pk: $(this).attr('record-id'), 
			is_like: is_like,
		},
		success: function(data){
			button.html(data)
		},
		error: function(xhr, textStatus, errorThrown) {
            alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
        }

	})
} 


var main = function(){
	$(".like,.dislike").click(like);
}

$(document).ready(main);



