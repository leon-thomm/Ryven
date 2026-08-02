window.onload = function() {
  recCarouselEvents();
}

function recCarouselEvents() {
  var recTranslate = 0;
  var carouselList = $('.carousel-list');
  var listItems = $('.carousel-recs .carousel-listitem');
  var singleItem = $(listItems[0]);
  var singleItemWidth = singleItem.outerWidth(true);
  var singleItemWidthWithoutMargin = singleItem.outerWidth(false);
  var margin = singleItemWidth - singleItemWidthWithoutMargin;
  var itemsCount = listItems.length;
  var fullWidth = Math.round((singleItemWidth * listItems.length));
  var visibleWidth = $('.carousel-body').outerWidth(true);
  var visibleItems = visibleWidth / singleItemWidth;
  var widthToScroll = Math.round(fullWidth - visibleWidth - margin);
  var translateInrcem = widthToScroll / Math.round((itemsCount / 3));


  $('.carousel-prev-rec').click(function() {
    if (recTranslate < -1) {
      recTranslate += translateInrcem;
      carouselList.css('transform', 'translatex(' + recTranslate + 'px)');
      $('.carousel-next-rec').addClass("active");
      if (recTranslate > -1) {
        $('.carousel-prev-rec').removeClass("active");
      }
    }
  })

  $('.carousel-next-rec').click(function() {
    if (recTranslate >= ((widthToScroll * -1) + 5)) {
      recTranslate -= translateInrcem;
      carouselList.css('transform', 'translatex(' + recTranslate + 'px)');
      $('.carousel-prev-rec').addClass("active");
      if (recTranslate <= ((widthToScroll * -1) + 5)) {
        $('.carousel-next-rec').removeClass("active");
      }
    }
  });
}