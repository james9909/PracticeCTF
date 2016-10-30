$(document).ready(function() {
	$('form').submit(function() {
		if (flag($('input').val())) {
			$('#response').empty();
			$('#response').text($('input').val()).css('color', '#0e0').show();
		} else {
			$('#response').empty();
			$('#response').text('Incorrect.').css('color', 'red').show().fadeOut(2000);
		}
		return false;
	});
});

function flag(q) {
	if ((q.charCodeAt(16) ^ 128) != 253) {
		return false;
	}
	if ((q.charCodeAt(0) & q.charCodeAt(16)) != 121) {
		return false;
	}
	if ((q.charCodeAt(0) + 2) % 5 != 0) {
		return false;
	}

	var x; // We need to find out what x is to continue.

	if (q.charCodeAt(x) != 95 && x % 11 != 0) {
		return false;
	}
	if (q.charCodeAt(5) >> (q.charCodeAt(16) - q.charCodeAt(0)) != 16) {
		return false;
	}
	if (q.charCodeAt(5) << (q.charCodeAt(16) - q.charCodeAt(0)) != 260) {
		return false;
	}
	if ((q.charCodeAt(13) ^ q.charCodeAt(11)) != 110) {
		return false;
	}
	if (q.charCodeAt(13) / q.charCodeAt(10) != 7 / 11) {
		return false;
	}
	if (((q.charCodeAt(13) & q.charCodeAt(11)) * 4) + 1 != q.charCodeAt(6)) {
		return false;
	}
	if (q.indexOf('n') != (q.charCodeAt(5) & q.charCodeAt(13))) {
		return false;
	}
	if (q.charCodeAt(1) - 9 != q.charCodeAt(9)) {
		return false;
	}
	if ((q.charCodeAt(7) & q.charCodeAt(9)) != q.charCodeAt(11) + (q.charCodeAt(5) & q.charCodeAt(13))) {
		return false;
	}
	if (q.charCodeAt(7) % 57 != 0) {
		return false;
	}
	if ((q.charCodeAt(9) + q.charCodeAt(11)) / (11 - 9) != q.charCodeAt(12)) {
		return false;
	}
	if ((q.charCodeAt(7) ^ q.charCodeAt(3)) != q.charCodeAt(11)) {
		return false;
	}
	if ((q.charCodeAt(3) ^ q.charCodeAt(8)) != 0) {
		return false;
	}
	if ((q.charCodeAt(15) & q.charCodeAt(3)) != (q.charCodeAt(9) & q.charCodeAt(8))) {
		return false;
	}
	if (q.charCodeAt(15) >> 3 != 6) {
		return false;
	}
	if (q.charCodeAt(15) % 5 != 3) {
		return false;
	}
	if ((q.charCodeAt(4) ^ q.charCodeAt(7)) != (q.charCodeAt(5) - q.charCodeAt(8))) {
		return false;
	}
	if ((q.charCodeAt(2) & q.charCodeAt(8)) != 32) {
		return false;
	}
	if (q.charCodeAt(2) << 2 != q.charCodeAt(0) + q.charCodeAt(6)) {
		return false;
	}
	if (q.charCodeAt(14) % 29 != 0) {
		return false;
	}
	if (q.charCodeAt(14) % 9 != 8) {
		return false;
	}

	return true;
}
