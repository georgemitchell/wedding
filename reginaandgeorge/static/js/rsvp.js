$.validator.setDefaults({
    highlight: function (element) { 
    	$(element).closest('.form-group').addClass('has-error');
    }, unhighlight: function (element) { 
    	$(element).closest('.form-group').removeClass('has-error'); 
    }, errorElement: 'span',
    errorClass: 'help-block',
    errorPlacement: function (error, element) {
        if (element.parent('.input-group').length) { 
        	error.insertAfter(element.parent()); 
        } else if (element.parent('label').length) { 
        	error.insertAfter(element.parent()); 
        } else { error.insertAfter(element); }
    }
});

$('.floating-label .form-control').on('keyup change', function (e) {
    			var input = $(e.currentTarget);
    			if ($.trim(input.val()) !== '') {
    				input.addClass('dirty').removeClass('static');
    			} else {
    				input.removeClass('dirty').removeClass('static');
    			}
    		});
$('.floating-label .form-control').each(function () {
	var input = $(this);
	if ($.trim(input.val()) !== '') {
		input.addClass('dirty');
	}
});

$('.form-horizontal .form-control').each(function () {
	$(this).after('<div class="form-control-line"></div>');
});

$('.form-validate').each(function () {
	var validator = $(this).validate({
		submitHandler: function(form) {
            if(form.is_ajax.value) {
                var form_type = form.form_type.value
                var form_div = "#" + form_type + "_div"
                $(form_div).css("display", "none");
                $("#loading_div").css("display", "block");
                var url = form.action + '?' + $(form).serialize();
                $.get(url, function( data ) {
                    $("#rsvp_content").html( data );
                    /*
                    $('#access_code_form').on('submit', function (e) {
                        $("#access_code_div").css("display", "none");
                        $("#loading_div").css("display", "block");
                        e.preventDefault();
                        var url = $("#access_code_form").attr("action") + "?access_code=" + $("#access_code").val();
                        $.get(url, function( data ) {
                            $("#rsvp_content").html( data );
                        });
                    });*/

                });
            } else {
                form.submit();
            }
    	}
    });
	$(this).data('validator', validator); 
});

/*

(function (namespace, $) {
    "use strict"; 
    var AppForm = function () { 
    	var o = this; 
    	$(document).ready(function () { o.initialize(); }); }; 
    	var p = AppForm.prototype;
    	p.initialize = function () { 
    		//this._enableEvents();
    		//this._initRadioAndCheckbox();
    		//this._initFloatingLabels();
    		this._initValidation(); 
    	};
    	p._enableEvents = function () { 
    		var o = this;
    		$('[data-submit="form"]').on('click', function (e) { 
    			e.preventDefault();
    			var formId = $(e.currentTarget).attr('href');
    			$(formId).submit(); 
    		});
    		$('textarea.autosize').on('focus', function () {
    			$(this).autosize({ append: '' }); 
    		}); 
    	};
    	p._initRadioAndCheckbox = function () {
    		$('.checkbox-styled input, .radio-styled input').each(function () {
    			if ($(this).next('span').length === 0) {
    				$(this).after('<span></span>'); 
    			}
    		}); 
    	};
    	p._initFloatingLabels = function () {
    		var o = this;
    		$('.floating-label .form-control').on('keyup change', function (e) {
    			var input = $(e.currentTarget);
    			if ($.trim(input.val()) !== '') {
    				input.addClass('dirty').removeClass('static');
    			} else {
    				input.removeClass('dirty').removeClass('static');
    			}
    		});
    		$('.floating-label .form-control').each(function () {
    			var input = $(this);
    			if ($.trim(input.val()) !== '') {
    				input.addClass('static').addClass('dirty');
    			}
    		});
    		$('.form-horizontal .form-control').each(function () {
    			$(this).after('<div class="form-control-line"></div>');
    		});
    	};
    	p._initValidation = function () {
        	if (!$.isFunction($.fn.validate)) { return; }
        	$.validator.setDefaults({
	            highlight: function (element) { 
	            	$(element).closest('.form-group').addClass('has-error');
	            }, unhighlight: function (element) { 
	            	$(element).closest('.form-group').removeClass('has-error'); 
	            }, errorElement: 'span',
	            errorClass: 'help-block',
	            errorPlacement: function (error, element) {
	                if (element.parent('.input-group').length) { 
	                	error.insertAfter(element.parent()); 
	                } else if (element.parent('label').length) { 
	                	error.insertAfter(element.parent()); 
	                } else { error.insertAfter(element); }
	            }
        	});
        	$('.form-validate').each(function () {
        		var validator = $(this).validate();
        		$(this).data('validator', validator); 
        	});
    	}; 
    	window.materialadmin.AppForm = new AppForm;
	}(this.materialadmin, jQuery));


*/