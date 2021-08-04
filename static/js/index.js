// custom delay function
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

$(document).ready(function(){
	
	// Sign In form submit - Actions 
	$("#form_sign_in").on('submit', function(e){
		$("#form_sign_in_submit").hide("fast");
		$("#form_sign_in_loading").show("fast");
	});


	// Sign Up form submit - Actions 
	$("#form_sign_up").on('submit', function(e){
		

		const password = $("#new_password").val();
		const new_password = $("#new_confirm_password").val();

		if(password != new_password)
		{
			e.preventDefault();
			$("#form_sign_up_error").html("Passwords mismatch");
			$("#form_sign_up_error").append("<button type='button' class='close' data-dismiss='alert'>&times;</button>");
			$("#form_sign_up_error").show("fast");
		}
		else if(password.length < 8)
		{
			e.preventDefault();
			$("#form_sign_up_error").html("Password is too short. \
				Choose a password between 8-16 characters containing a numeric, \
				a letter and special character.");
			$("#form_sign_up_error").append("<button type='button' class='close' data-dismiss='alert'>&times;</button>");
			$("#form_sign_up_error").show("fast");
		}
		else if(password.length > 16)
		{
			e.preventDefault();
			$("#form_sign_up_error").html("Password is too long. \
				Choose a password between 8-16 characters containing atleast one from numeric, \
				letter and special character each.");
			$("#form_sign_up_error").append("<button type='button' class='close' data-dismiss='alert'>&times;</button>");
			$("#form_sign_up_error").show("fast");
		}
		else if(/[A-Z]|[a-z]|/.test(password) == false || 
						/[0-9]/.test(password) == false ||
						/[!-/]|[:-@]|[[-`]|[{-~]/.test(password) == false) // JS Regex to find numeric, letter, special character
		{
			e.preventDefault();
			$("#form_sign_up_error").html("Missing atleast one numeric, letter and special character. \
				Choose a password between 8-16 characters containing atleast one from numeric, \
				letter and special character each.");
			$("#form_sign_up_error").append("<button type='button' class='close' data-dismiss='alert'>&times;</button>");
			$("#form_sign_up_error").show("fast");
		}
		else
		{
			$("#form_sign_up_submit").hide("fast");
			$("#form_sign_up_loading").show("fast");
		}

	});

})