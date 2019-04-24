window.onload = function() {
	// setup the button click
	document.getElementById("search-btn").onclick = function() {
        var query = document.getElementById('text-query').value
		doWork(query)
	};
}

function doWork(query) {
	// ajax the JSON to the server
	$.post("receiver", query, function(){});
	// stop link reloading the page
 event.preventDefault();
}
