

$(document).on('click', '#add-to-cart', function(e) {
    e.preventDefault();
    var cartUrl = $(this).data('cart-url');
    $.ajax({
        type: 'POST',
        url: cartUrl,
        data: {
            product_id: $(this).val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },
        success: function(json) {
            document.getElementById('cart_quantity').textContent = json.qt;
        },
        error: function(xhr, errmsg, err) {
            // Handle error
        }
    });
});


