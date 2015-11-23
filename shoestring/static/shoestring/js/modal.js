// Create our Modal subclass
var Modal = Ractive.extend({
  // by default, the modal should sit atop the <body>...
  el: document.body,

  // ...but it should append to it rather than overwriting its contents
  append: true,

  // all Modal instances will share a template (though you can override it
  // on a per-instance basis, if you really want to)
  template: '#modal',

  // the onrender function will be called as soon as the instance has
  // finished rendering
  onrender: function () {
    var self = this, resizeHandler;

    // store references to the background, and to the modal itself
    // we'll assume we're in a modern browser and use querySelector
    this.outer = this.find( '.modal-outer' );
    this.modal = this.find( '.modal' );

    // if the user taps on the background, close the modal
    this.on( 'close', function ( event ) {
      if ( !this.modal.contains( event.original.target ) ) {
        this.teardown();
      }
    });

    // when the window resizes, keep the modal horizontally and vertically centred
    window.addEventListener( 'resize', resizeHandler = function () {
      self.center();
    }, false );

    // clean up after ourselves later
    this.on( 'teardown', function () {
      window.removeEventListener( 'resize', resizeHandler );
    }, false );

    // manually call this.center() the first time
    this.center();
  },

  center: function () {
    var outerHeight, modalHeight, verticalSpace;

    // horizontal centring is taken care of by CSS, but we need to
    // vertically centre
    outerHeight = this.outer.clientHeight;
    modalHeight = this.modal.clientHeight;

    verticalSpace = ( outerHeight - modalHeight ) / 2;

    this.modal.style.top = verticalSpace + 'px';
  }
});
