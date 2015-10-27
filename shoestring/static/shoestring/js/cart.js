
function dollar_fmt (value) { return value.toFixed(2); }

var Cart = Ractive.extend({
    template: '#cart',
    isolated: true,
    data: {
        total: function (item) { return dollar_fmt(item.qty * item.price); },
        dollar_fmt: dollar_fmt
    },
    update: function (data) { this.set('cart', data); },
    load: function () {
        rpc_call(SS.url.cart, 'content', {}, this.update.bind(this));
    },
    add: function (sku, qty) {
        rpc_call(SS.url.cart, 'add', {sku: sku, qty: qty || 1}, this.update.bind(this));
    },
    remove: function (sku) {
        rpc_call(SS.url.cart, 'quantity', {sku: sku, qty: 0}, this.update.bind(this));
    },
    quantity: function (sku, qty) {
        rpc_call(SS.url.cart, 'quantity', {sku: sku, qty: qty}, this.update.bind(this));
    },
    oninit: function () {
        this.on({
            'incCartItem': function (ev) {
                this.quantity(ev.context.sku, ev.context.qty + 1);
            }.bind(this),
            'decCartItem': function (ev) {
                if(ev.context.qty > 1) {
                    this.quantity(ev.context.sku, ev.context.qty - 1);
                } else {
                    this.remove(ev.context.sku);
                }
            }.bind(this)
        });
    }
});
