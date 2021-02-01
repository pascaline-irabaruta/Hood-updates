$(document).ready(function () {
    $(".navbar-burger").click(function () {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");

    });

    $('#tab_header ul li.item').on('click', function () {
        var number = $(this).data('option');
        $('#tab_header ul li.item').removeClass('is-active');
        $(this).addClass('is-active');
        $('#tab_container .container_item').removeClass('is-active');
        $('div[data-item="' + number + '"]').addClass('is-active');
    });


    $('#business_search').submit(function (e) {
        e.preventDefault();
    });
});
