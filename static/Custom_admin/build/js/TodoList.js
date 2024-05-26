/**
 * --------------------------------------------
 * AdminLTE  List.js
 * License MIT
 * --------------------------------------------
 */

const  List = (($) => {
  /**
   * Constants
   * ====================================================
   */

  const NAME               = ' List'
  const DATA_KEY           = 'lte. list'
  const EVENT_KEY          = `.${DATA_KEY}`
  const JQUERY_NO_CONFLICT = $.fn[NAME]

  const Selector = {
    DATA_TOGGLE: '[data-widget=" -list"]'
  }

  const ClassName = {
     _LIST_DONE: 'done'
  }

  const Default = {
    onCheck: function (item) {
      return item;
    },
    onUnCheck: function (item) {
      return item;
    }
  }

  /**
   * Class Definition
   * ====================================================
   */

  class  List {
    constructor(element, config) {
      this._config  = config
      this._element = element

      this._init()
    }

    // Public

    toggle(item) {
      item.parents('li').toggleClass(ClassName. _LIST_DONE);
      if (! $(item).prop('checked')) {
        this.unCheck($(item));
        return;
      }

      this.check(item);
    }

    check (item) {
      this._config.onCheck.call(item);
    }

    unCheck (item) {
      this._config.onUnCheck.call(item);
    }

    // Private

    _init() {
      var that = this
      $(Selector.DATA_TOGGLE).find('input:checkbox:checked').parents('li').toggleClass(ClassName. _LIST_DONE)
      $(Selector.DATA_TOGGLE).on('change', 'input:checkbox', (event) => {
        that.toggle($(event.target))
      })
    }

    // Static

    static _jQueryInterface(config) {
      return this.each(function () {
        let data      = $(this).data(DATA_KEY)
        const _config = $.extend({}, Default, $(this).data())

        if (!data) {
          data = new  List($(this), _config)
          $(this).data(DATA_KEY, data)
        }

        if (config === 'init') {
          data[config]()
        }
      })
    }
  }

  /**
   * Data API
   * ====================================================
   */

  $(window).on('load', () => {
     List._jQueryInterface.call($(Selector.DATA_TOGGLE))
  })

  /**
   * jQuery API
   * ====================================================
   */

  $.fn[NAME] =  List._jQueryInterface
  $.fn[NAME].Constructor =  List
  $.fn[NAME].noConflict = function () {
    $.fn[NAME] = JQUERY_NO_CONFLICT
    return  List._jQueryInterface
  }

  return  List
})(jQuery)

export default  List
