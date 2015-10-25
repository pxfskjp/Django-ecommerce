
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
    }
});
