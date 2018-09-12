var authToken='';

function setToken(token){
	if(token!=null&&token!=''&&token!=undefined){
		authToken=token;
	}
}

function getToken(){
	return authToken;
}

function initToken(){
	var token = '';
	  $.ajax({
			url : '/users/systemInit',
			data : {
				'x-auth-token' : token
			},
			type : 'POST',
			dataType : 'json',
			success : function(res) {
				if (res.header.status == 1000) {
					console.log(res.header.message)
				} else {
					layer.msg(res.header.message, {
						icon : 2,
						time : 2000
					})
				}
			},
			complete : function(request) {
				token = request.getResponseHeader("x-auth-token");
			}
		})
		return token;
}