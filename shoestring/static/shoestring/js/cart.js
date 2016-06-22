
function dollar_fmt (value) { return new Number(value).toFixed(2); }

// Container for cart details
function Cart() {
    this.total = 0;
    this.items = [];
}
Cart.prototype.update = function (data) {
    this.total = data.total;
    this.items = data.items;
    ractive.update('cart');
};
Cart.prototype.load = function () {
    rpc_call(SS.url.cart, 'content', {}, this.update.bind(this));
};
Cart.prototype.clear = function () {
    rpc_call(SS.url.cart, 'clear', {}, this.update.bind(this));
};
Cart.prototype.add = function (sku, qty) {
    rpc_call(SS.url.cart, 'add', {sku: sku, qty: qty || 1}, this.update.bind(this));
};
Cart.prototype.remove = function (sku) {
    rpc_call(SS.url.cart, 'quantity', {sku: sku, qty: 0}, this.update.bind(this));
};
Cart.prototype.quantity = function (sku, qty) {
    rpc_call(SS.url.cart, 'quantity', {sku: sku, qty: qty}, this.update.bind(this));
};

// Ractive for full cart
var FullCart = Ractive.extend({
    template: '#cart',
    isolated: true,
    magic: true,
    append: true,
    data: {
        total: function (item) { return dollar_fmt(item.qty * item.price); },
        dollar_fmt: dollar_fmt
    },
    oninit: function () {
        this.on({
            incCartItem: function (ev) {
                this.get('cart').quantity(ev.context.sku, ev.context.qty + 1);
            }.bind(this),
            decCartItem: function (ev) {
                if(ev.context.qty > 1) {
                    this.get('cart').quantity(ev.context.sku, ev.context.qty - 1);
                } else {
                    this.get('cart').remove(ev.context.sku);
                }
            }.bind(this),
            remCartItem: function (ev) {
                this.get('cart').remove(ev.context.sku);
            }.bind(this),
            clearCart: function (ev) {
                this.get('cart').clear();
            }.bind(this)
        });
    }
});

var MiniCart = FullCart.extend({template: '#mini-cart'});
