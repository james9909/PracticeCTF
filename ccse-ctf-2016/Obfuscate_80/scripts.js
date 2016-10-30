$(document).ready(function() {
	$('form').submit(function() {
		$.ajax({
			type: 'POST',
			url: $(this).attr('action'),
			data: $(this).serialize(),
			dataType: 'JSON',
			success: function(data) {
				if (data.success === 0) {
					$('#response').empty();
					$('#response').text('Incorrect.').css('color', 'red').show().fadeOut(2000);
				} else {
					$('#response').empty();
					$('#response').text(data.reply).css('color', '#0e0').show();
				}
			}
		});
		return false;
	});
});

function forgotPassword() {
	eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 2=["\\8\\9\\7\\b\\6\\4\\3\\5\\a\\i\\c\\j\\h\\g\\d\\e"];1 f=2[0];',20,20,'|var|_0x2785|x50|x7D|x51|x2A|x62|x67|x39|x63|x2B|x6F|x45|x70|password|x66|x56|x58|x42'.split('|'),0,{}));
}