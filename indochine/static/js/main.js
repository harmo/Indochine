jQuery(function($) {

    $('.navbar').on('mouseenter', 'ul li a:not(.active)', function(){
        $(this).find('img').toggle();
    });
    $('.navbar').on('mouseleave', 'ul li a:not(.active)', function(){
        $(this).find('img').toggle();
    });

    $('#news').carousel();


    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('body').on('click', '.back-to-top', function(){
        $('body, html').animate({scrollTop: 0}, 'slow');
    });

});