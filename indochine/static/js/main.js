jQuery(function($) {

    $('.navbar').on('mouseenter', 'ul li a:not(.active)', function(){
        $(this).find('img').toggle();
    });
    $('.navbar').on('mouseleave', 'ul li a:not(.active)', function(){
        $(this).find('img').toggle();
    });

    $('#news').carousel();

});