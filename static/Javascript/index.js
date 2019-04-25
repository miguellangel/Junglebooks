$(document).ready(function() {
    $('form').on('submit', function(event) {
        // alert(document.getElementById('text-query').value)
        $.ajax({
            data : {
                query : document.getElementById('text-query').value
            },
            type : 'POST',
            url : '/process',
            success : function(response) { // refer to https://stackoverflow.com/questions/48015074/flask-render-template-doesnt-work-on-ajax-post
                document.write(response);
            }
        })
        .done(function() {
            //If SQLALchemy wants to return something
        });
        event.preventDefault();
    });
});
