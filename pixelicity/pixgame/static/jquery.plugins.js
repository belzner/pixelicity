(function($) {
	$.fn.toggleHTML = function(t1, t2){
		if (this.html() == t1) this.html(t2);
		else this.html(t1);
		return this;
	};
}(jQuery));