(function ($) {
  'use strict';

  /*
  |--------------------------------------------------------------------------
  | Template Name: Zivan
  | Author: Laralink
  | Version: 1.0.0
  |--------------------------------------------------------------------------
  |--------------------------------------------------------------------------
  | TABLE OF CONTENTS:
  |--------------------------------------------------------------------------
  |
  | 1. Preloader
  | 2. Mobile Menu
  | 3. Sticky Header
  | 4. Dynamic Background
  | 5. Swiper Initialize
  | 6. Modal Video
  | 7. Isotop Initialize
  | 8. Parallax
  | 9. Scroll Up
  | 10. Dynamic contact form
  | 11. Ripple
  | 12. Counter Animation
  | 13. Accordian
  | 14. Tabs
  | 15. Hover Tab
  | 16. Award Wining
  | 17. Hover To Active
  | 18. Progress Bar
  | 19. Review
  | 20. Ecommerce
  | 21. Round Percent
  | 22. Cursor Animation
  |
  */

  /*--------------------------------------------------------------
    Scripts initialization
  --------------------------------------------------------------*/
  $.exists = function (selector) {
    return $(selector).length > 0;
  };

  $(window).on('load', function () {
    preloader();
    isotopInit();
  });

  $(function () {
    mainNav();
    stickyHeader();
    dynamicBackground();
    counterInit();
    swiperInit();
    modalVideo();
    isotopInit();
    parallaxEffect();
    scrollUp();
    rippleInit();
    accordian();
    tabs();
    hoverTab();
    awardHover();
    hoverActive();
    progressBar();
    roundPercentInit();
    review();
    ecommerce();
    if ($.exists('.wow')) {
      new WOW().init();
    }
  });

  $(window).on('scroll', function () {
    parallaxEffect();
    showScrollUp();
  });

  /*--------------------------------------------------------------
    1. Preloader
  --------------------------------------------------------------*/
  function preloader() {
    $('.cs_perloader').fadeOut();
    $('cs_perloader_in').delay(150).fadeOut('slow');
  }

  /*--------------------------------------------------------------
    2. Mobile Menu
  --------------------------------------------------------------*/
  function mainNav() {
    $('.cs_nav').append('<span class="cs_menu_toggle"><span></span></span>');
    $('.menu-item-has-children').append(
      '<span class="cs_munu_dropdown_toggle"><span></span></span>',
    );
    $('.cs_menu_toggle').on('click', function () {
      $(this)
        .toggleClass('cs_toggle_active')
        .siblings('.cs_nav_list')
        .toggleClass('cs_active');
    });
    $('.cs_menu_toggle')
      .parents('body')
      .find('.cs_side_header')
      .addClass('cs_has_main_nav');
    $('.cs_menu_toggle')
      .parents('body')
      .find('.cs_toolbox')
      .addClass('cs_has_main_nav');
    $('.cs_munu_dropdown_toggle').on('click', function () {
      $(this).toggleClass('active').siblings('ul').slideToggle();
      $(this).parent().toggleClass('active');
    });
  }

  /*--------------------------------------------------------------
    3. Sticky Header
  --------------------------------------------------------------*/
  function stickyHeader() {
    var $window = $(window);
    var lastScrollTop = 0;
    var $header = $('.cs_sticky_header');
    var headerHeight = $header.outerHeight() + 30;

    $window.scroll(function () {
      var windowTop = $window.scrollTop();

      if (windowTop >= headerHeight) {
        $header.addClass('cs_gescout_sticky');
      } else {
        $header.removeClass('cs_gescout_sticky');
        $header.removeClass('cs_gescout_show');
      }

      if ($header.hasClass('cs_gescout_sticky')) {
        if (windowTop < lastScrollTop) {
          $header.addClass('cs_gescout_show');
        } else {
          $header.removeClass('cs_gescout_show');
        }
      }

      lastScrollTop = windowTop;
    });
  }

  /*--------------------------------------------------------------
    4. Dynamic Background
  --------------------------------------------------------------*/
  function dynamicBackground() {
    $('[data-src]').each(function () {
      var src = $(this).attr('data-src');
      $(this).css({
        'background-image': 'url(' + src + ')',
      });
    });
  }

  /*--------------------------------------------------------------
    5. Swiper Initialize
  --------------------------------------------------------------*/
  function swiperInit() {
    if ($.exists('.cs_slider_1')) {
      var swiper = new Swiper('.cs_slider_1', {
        slidesPerView: 1,
        loop: true,
        speed: 1000,
        spaceBetween: 24,
        pagination: {
          el: '.cs_pagination',
          clickable: true,
        },
        breakpoints: {
          450: {
            slidesPerView: 2,
            spaceBetween: 15,
          },
          991: {
            slidesPerView: 3,
          },
          1750: {
            slidesPerView: 4,
          },
        },
      });
    }
    if ($.exists('.cs_slider_1_1')) {
      var swiper = new Swiper('.cs_slider_1_1', {
        slidesPerView: 1,
        loop: true,
        speed: 1000,
        spaceBetween: 24,
        pagination: {
          el: '.cs_pagination',
          clickable: true,
        },
        breakpoints: {
          575: {
            slidesPerView: 2,
          },
          991: {
            slidesPerView: 3,
          },
          1300: {
            slidesPerView: 3,
          },
        },
      });
    }
    if ($.exists('.cs_slider_2')) {
      var swiper2 = new Swiper('.cs_slider_2', {
        loop: true,
        speed: 1000,
        navigation: {
          nextEl: '.cs_swiper_next',
          prevEl: '.cs_swiper_prev',
        },
      });
    }
    if ($.exists('.cs_slider_3')) {
      var swiper = new Swiper('.cs_slider_3', {
        slidesPerView: 1,
        loop: true,
        speed: 1000,
        spaceBetween: 24,
        pagination: false,
        breakpoints: {
          575: {
            slidesPerView: 2,
          },
          991: {
            slidesPerView: 4,
          },
          1300: {
            slidesPerView: 6,
          },
        },
      });
    }
    if ($.exists('.cs_slider_4')) {
      var swiper = new Swiper('.cs_slider_4', {
        slidesPerView: 1,
        loop: true,
        speed: 1000,
        pagination: {
          el: '.cs_number_pagination',
          clickable: true,
          renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + '</span>';
          },
        },
      });
    }
  }

  /*--------------------------------------------------------------
    6. Modal Video
  --------------------------------------------------------------*/
  function modalVideo() {
    if ($.exists('.cs_video_open')) {
      $('body').append(`
        <div class="cs_video_popup">
          <div class="cs_video_popup-overlay"></div>
          <div class="cs_video_popup-content">
            <div class="cs_video_popup-layer"></div>
            <div class="cs_video_popup-container">
              <div class="cs_video_popup-align">
                <div class="embed-responsive embed-responsive-16by9">
                  <iframe class="embed-responsive-item" src="about:blank"></iframe>
                </div>
              </div>
              <div class="cs_video_popup-close"></div>
            </div>
          </div>
        </div>
      `);
      $(document).on('click', '.cs_video_open', function (e) {
        e.preventDefault();
        var video = $(this).attr('href');

        $('.cs_video_popup-container iframe').attr('src', `${video}`);

        $('.cs_video_popup').addClass('active');
      });
      $('.cs_video_popup-close, .cs_video_popup-layer').on(
        'click',
        function (e) {
          $('.cs_video_popup').removeClass('active');
          $('html').removeClass('overflow-hidden');
          $('.cs_video_popup-container iframe').attr('src', 'about:blank');
          e.preventDefault();
        },
      );
    }
  }

  /*--------------------------------------------------------------
    7. Isotop Initialize
  --------------------------------------------------------------*/
  function isotopInit() {
    if ($.exists('.cs_isotop')) {
      $('.cs_isotop').isotope({
        itemSelector: '.cs_isotop_item',
        transitionDuration: '0.60s',
        percentPosition: true,
        masonry: {
          columnWidth: '.cs_grid_sizer',
        },
      });
      /* Active Class of Portfolio*/
      $('.cs_isotop_filter ul li').on('click', function (event) {
        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');
        event.preventDefault();
      });
      /*=== Portfolio filtering ===*/
      $('.cs_isotop_filter ul').on('click', 'a', function () {
        var filterElement = $(this).attr('data-filter');
        $('.cs_isotop').isotope({
          filter: filterElement,
        });
      });
    }
  }

  /*--------------------------------------------------------------
    8. Parallax
  --------------------------------------------------------------*/
  function parallaxEffect() {
    $('.cs_parallax').each(function () {
      var windowScroll = $(document).scrollTop(),
        windowHeight = $(window).height(),
        barOffset = $(this).offset().top,
        barHeight = $(this).height(),
        barScrollAtZero = windowScroll - barOffset + windowHeight,
        barHeightWindowHeight = windowScroll + windowHeight,
        barScrollUp = barOffset <= windowScroll + windowHeight,
        barSctollDown = barOffset + barHeight >= windowScroll;

      if (barSctollDown && barScrollUp) {
        var calculadedHeight = barHeightWindowHeight - barOffset;
        var mediumEffectPixel = barScrollAtZero / 7;
        var miniEffectPixel = calculadedHeight / 10;
        var miniEffectPixel2 = calculadedHeight / 3;
        var miniEffectPixel3 = calculadedHeight / 6;
        var miniEffectPixel4 = barScrollAtZero / 5;
        $(this)
          .find('.cs_to_left')
          .css('transform', `translateX(-${miniEffectPixel}px)`);
        $(this)
          .find('.cs_to_right')
          .css('transform', `translateX(${miniEffectPixel}px)`);
        $(this)
          .find('.cs_to_up')
          .css('transform', `translateY(-${miniEffectPixel}px)`);
        $(this)
          .find('.cs_to_up_2')
          .css('transform', `translateY(-${miniEffectPixel2}px)`);
        $(this)
          .find('.cs_to_up_3')
          .css('transform', `translateY(-${miniEffectPixel3}px)`);
        $(this)
          .find('.cs_to_up_4')
          .css('transform', `translateY(-${miniEffectPixel4}px)`);
        $(this)
          .find('.cs_to_down')
          .css('transform', `translateY(${miniEffectPixel}px)`);
        $(this)
          .find('.cs_to_down_4')
          .css('transform', `translateY(${miniEffectPixel4}px)`);
        $(this)
          .find('.cs_to_rotate')
          .css('transform', `rotate(${miniEffectPixel}deg)`);
        $(this)
          .find('.cs_parallax_bg')
          .css('background-position', `center -${mediumEffectPixel}px`);
      }
    });
  }

  /*--------------------------------------------------------------
    9. Scroll Up
  --------------------------------------------------------------*/
  function scrollUp() {
    $('.cs_scrollup').on('click', function (e) {
      e.preventDefault();
      $('html,body').animate(
        {
          scrollTop: 0,
        },
        0,
      );
    });
  }
  // For Scroll Up
  function showScrollUp() {
    let scroll = $(window).scrollTop();
    if (scroll >= 350) {
      $('.cs_scrollup').addClass('cs_scrollup_show');
    } else {
      $('.cs_scrollup').removeClass('cs_scrollup_show');
    }
  }

  /*--------------------------------------------------------------
    10. Dynamic contact form
  --------------------------------------------------------------*/
  if ($.exists('#cs_form')) {
    const form = document.getElementById('cs_form');
    const result = document.getElementById('cs_result');

    form.addEventListener('submit', function (e) {
      const formData = new FormData(form);
      e.preventDefault();
      var object = {};
      formData.forEach((value, key) => {
        object[key] = value;
      });
      var json = JSON.stringify(object);
      result.innerHTML = 'Please wait...';

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        body: json,
      })
        .then(async response => {
          let json = await response.json();
          if (response.status == 200) {
            result.innerHTML = json.message;
          } else {
            console.log(response);
            result.innerHTML = json.message;
          }
        })
        .catch(error => {
          console.log(error);
          result.innerHTML = 'Something went wrong!';
        })
        .then(function () {
          form.reset();
          setTimeout(() => {
            result.style.display = 'none';
          }, 5000);
        });
    });
  }

  /*--------------------------------------------------------------
    11. Ripple
  --------------------------------------------------------------*/
  function rippleInit() {
    if ($.exists('.cs_ripple_activate')) {
      $('.cs_ripple_activate').each(function () {
        $('.cs_ripple_activate').ripples({
          resolution: 512,
          dropRadius: 20,
          perturbance: 0.04,
        });
      });
    }
  }

  /*--------------------------------------------------------------
    12. Counter Animation
  --------------------------------------------------------------*/
  function counterInit() {
    if ($.exists('.odometer')) {
      $(window).on('scroll', function () {
        function winScrollPosition() {
          var scrollPos = $(window).scrollTop(),
            winHeight = $(window).height();
          var scrollPosition = Math.round(scrollPos + winHeight / 1.2);
          return scrollPosition;
        }

        $('.odometer').each(function () {
          var elemOffset = $(this).offset().top;
          if (elemOffset < winScrollPosition()) {
            $(this).html($(this).data('count-to'));
          }
        });
      });
    }
  }

  /*--------------------------------------------------------------
    13. Accordian
  --------------------------------------------------------------*/
  function accordian() {
    $('.cs_accordian').children('.cs_accordian_body').hide();
    $('.cs_accordian.active').children('.cs_accordian_body').show();
    $('.cs_accordian_head').on('click', function () {
      $(this)
        .parent('.cs_accordian')
        .siblings()
        .children('.cs_accordian_body')
        .slideUp(250);
      $(this).siblings().slideDown(250);
      $(this)
        .parent()
        .parent()
        .siblings()
        .find('.cs_accordian_body')
        .slideUp(250);
      /* Accordian Active Class */
      $(this).parents('.cs_accordian').addClass('active');
      $(this).parent('.cs_accordian').siblings().removeClass('active');
    });
  }

  /*--------------------------------------------------------------
    14. Tabs
  --------------------------------------------------------------*/
  function tabs() {
    $('.cs_tabs .cs_tab_links a').on('click', function (e) {
      var currentAttrValue = $(this).attr('href');
      $('.cs_tabs ' + currentAttrValue)
        .fadeIn(400)
        .siblings()
        .hide();
      $(this).parents('li').addClass('active').siblings().removeClass('active');
      e.preventDefault();
    });
  }

  /*--------------------------------------------------------------
    15. Hover Tab
  --------------------------------------------------------------*/
  function hoverTab() {
    $('.cs_hover_tab a').hover(function () {
      $(this)
        .parents('.cs_hover_tab')
        .addClass('active')
        .siblings()
        .removeClass('active');
    });
  }

  /*--------------------------------------------------------------
    16. Award Wining
  --------------------------------------------------------------*/
  function awardHover() {
    const awardItem = document.querySelectorAll('.cs_awaard.cs_style_1');

    function followImageCursor(event, awardItem) {
      const contentBox = awardItem.getBoundingClientRect();
      const dx = event.clientX - contentBox.x;
      const dy = event.clientY - contentBox.y;
      awardItem.children[3].style.transform = `translate(${dx}px, ${dy}px)`;
    }

    awardItem.forEach((item, i) => {
      item.addEventListener('mousemove', event => {
        setInterval(followImageCursor(event, item), 1000);
      });
    });
  }

  /*--------------------------------------------------------------
    17. Hover To Active
  --------------------------------------------------------------*/
  function hoverActive() {
    $('.cs_hover_active').hover(function () {
      $(this).addClass('active').siblings().removeClass('active');
    });
  }

  /*--------------------------------------------------------------
    18. Progress Bar
  --------------------------------------------------------------*/
  function progressBar() {
    $('.cs_progress').each(function () {
      var progressPercentage = $(this).data('progress') + '%';
      $(this).find('.cs_progress_in').css('width', progressPercentage);
    });
  }

  /*--------------------------------------------------------------
    19. Review
  --------------------------------------------------------------*/
  function review() {
    $('.cs_rating').each(function () {
      var review = $(this).data('rating');
      var reviewVal = review * 20 + '%';
      $(this).find('.cs_rating_percentage').css('width', reviewVal);
    });
  }

  /*--------------------------------------------------------------
    20. Ecommerce
  --------------------------------------------------------------*/
  function ecommerce() {
    // Star Rating Input
    $('.cs_input_rating i').on('click', function () {
      $(this).siblings().removeClass('fa-solid');
      $(this).addClass('fa-solid').prevAll().addClass('fa-solid');
    });
    // Product Single Slider
    if ($.exists('.cs_single_product_thumb')) {
      $('.cs_single_product_thumb').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.cs_single_product_nav',
      });
    }

    if ($.exists('.cs_single_product_nav')) {
      $('.cs_single_product_nav').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.cs_single_product_thumb',
        focusOnSelect: true,
        arrows: false,
      });
    }
    // Check All
    $('#checkAll').change(function () {
      var isChecked = $(this).prop('checked');
      $('table input[type="checkbox"]').prop('checked', isChecked);
    });
    // Range Slider
    if ($.exists('#slider-range')) {
      $('#slider-range').slider({
        range: true,
        min: 0,
        max: 1000,
        values: [100, 600],
        slide: function (event, ui) {
          $('#amount').val('Price: $' + ui.values[0] + ' - $' + ui.values[1]);
        },
      });
    }
    if ($.exists('#amount')) {
      $('#amount').val(
        'Price: $' +
          $('#slider-range').slider('values', 0) +
          ' - $' +
          $('#slider-range').slider('values', 1),
      );
    }
    // Counter
    $('.cs_increment').click(function () {
      var countElement = $(this).siblings('.cs_quantity_input');
      var count = parseInt(countElement.text());
      count++;
      countElement.text(count);
    });

    $('.cs_decrement').click(function () {
      var countElement = $(this).siblings('.cs_quantity_input');
      var count = parseInt(countElement.text());
      if (count > 0) {
        count--;
        countElement.text(count);
      }
    });
  }

  /*--------------------------------------------------------------
    21. Round Percent
  --------------------------------------------------------------*/
  function roundPercentInit() {
    if ($.exists('.cs_round_progress_percentage')) {
      $(window).on('scroll', function () {
        function winScrollPosition() {
          var scrollPos = $(window).scrollTop(),
            winHeight = $(window).height();
          var scrollPosition = Math.round(scrollPos + winHeight / 1.2);
          return scrollPosition;
        }

        $('.cs_round_progress_percentage').each(function () {
          var roundEffect = $(this).offset().top;
          if (roundEffect < winScrollPosition()) {
            $(this).each(function () {
              let roundRadius = $(this).find('circle').attr('r');
              let roundPercent = $(this).data('percent');
              let roundCircum = 2 * roundRadius * Math.PI;
              let roundDraw = (roundPercent * roundCircum) / 100 - 3;
              $(this).css('stroke-dasharray', roundDraw + ' 999');
            });
          }
        });
      });
    }
  }

  /*--------------------------------------------------------------
    22. Cursor Animation
  --------------------------------------------------------------*/
  $(function () {
    $('body').append('<span class="cs_cursor_lg d"></span>');
    $('body').append('<span class="cs_cursor_sm"></span>');
    $('a, .cs_swiper_next, .cs_swiper_prev').on('mouseenter', function () {
      $('.cs_cursor_lg').addClass('cs_large');
      $('.cs_cursor_sm').addClass('cs_large');
    });
    $('a, .cs_swiper_next, .cs_swiper_prev').on('mouseleave', function () {
      $('.cs_cursor_lg').removeClass('cs_large');
      $('.cs_cursor_sm').removeClass('cs_large');
    });
    $('.cs_portfolio.cs_style_1>a, .cs_awaard.cs_style_1').on(
      'mouseenter',
      function () {
        $('.cs_cursor_lg').addClass('opacity-0');
        $('.cs_cursor_sm').addClass('opacity-0');
      },
    );
    $('.cs_portfolio.cs_style_1>a, .cs_awaard.cs_style_1').on(
      'mouseleave',
      function () {
        $('.cs_cursor_lg').removeClass('opacity-0');
        $('.cs_cursor_sm').removeClass('opacity-0');
      },
    );
  });

  function cursorMovingAnimation(event) {
    try {
      const timing = gsap.timeline({
        defaults: {
          x: event.clientX,
          y: event.clientY,
        },
      });

      timing
        .to('.cs_cursor_lg', {
          ease: 'power2.out',
        })
        .to(
          '.cs_cursor_sm',
          {
            ease: 'power2.out',
          },
          '-=0.4',
        );

      const target = event.target;

      let tl = gsap.timeline({
        defaults: {
          x: event.clientX,
          y: event.clientY,
        },
      });
      let t2 = gsap.timeline({
        defaults: {
          x: event.clientX,
          y: event.clientY,
        },
      });
      var client_cursor = document.getElementById('client_cursor');
      if (target.closest('.cs_portfolio.cs_style_1 .cs_portfolio_thumb')) {
        tl.to(
          client_cursor,
          {
            opacity: 1,
            zoom: 1,
            ease: 'power2.out',
          },
          '-=0.3',
        );
      } else {
        t2.to(
          client_cursor,
          {
            opacity: 0,
            ease: 'power2.out',
          },
          '-=0.3',
        );
      }
    } catch (err) {
      console.log(err);
    }
  }
  document.addEventListener('mousemove', cursorMovingAnimation);
})(jQuery); // End of use strict
