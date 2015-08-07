$(document).ready(function(){

    $('#product_stock').on('keyup', '#id_stockrecords-0-ttc', function(){
        var ttc = parseFloat($(this).val());
        var tax = parseFloat(TAXES[$('#id_stockrecords-0-fr_tax').val()]);
        var new_val = ttc != 0 ? parseFloat(ttc / ((tax / 100) + 1)).toFixed(2) : '';
        $('#id_stockrecords-0-price_excl_tax').val(new_val);
    });

    $('#product_stock').on('keyup', '#id_stockrecords-0-price_excl_tax', function(){
        var ht = parseFloat($(this).val());
        var tax = parseFloat(TAXES[$('#id_stockrecords-0-fr_tax').val()]);
        var new_val = ht != 0 ? parseFloat(ht + (ht * tax / 100)).toFixed(2) : '';
        $('#id_stockrecords-0-ttc').val(new_val);
    });

    $('#product_stock').on('change', '#id_stockrecords-0-fr_tax', function(){
        var tax = parseFloat(TAXES[$(this).val()]);
        var ttc = parseFloat($('#id_stockrecords-0-ttc').val());
        if (ttc != ''){
            $('#id_stockrecords-0-price_excl_tax').val(parseFloat(ttc / ((tax / 100) + 1)).toFixed(2));
        };
    });

});