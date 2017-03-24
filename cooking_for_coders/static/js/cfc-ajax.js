/**
 * Created by jonathansaje on 24/03/2017.
 */


$('#recipe-store').click(function() {
    $.post('/store/{{ recipe.id }}/', function(data) {
        $('div.alert-info').html(data).fadeIn(600).delay(3000).fadeOut(900);
    });
});
