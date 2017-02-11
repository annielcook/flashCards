$(document).ready(function() {
	$("#artist").click(function(){
		$("#artist").toggleClass("hidden-lg");
	});
});

var toggleHiddenAll = function (){
	$("#artist").toggleClass("hidden-lg");
	$("#name").toggleClass("hidden-lg");
	$("#year").toggleClass("hidden-lg");
	$("#place").toggleClass("hidden-lg");
	$("#medium").toggleClass("hidden-lg");
}

$(document).ready(function() {
	$("#cards").on('click', '.img', function(){
        $('.text-col').toggleClass('hidden-lg');
    });
})
