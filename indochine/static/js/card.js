$(function(){

    $('.category').on('click', '.category-control', function(){
        $(this).parent().find('.category-control').toggle();
        $(this).closest('.category').find('.category-products').toggle('linear');
    });

});