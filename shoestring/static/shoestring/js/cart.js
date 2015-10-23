
var Cart = Ractive.extend({
    template: '#cart',
    isolated: true,
    data: {
        price: function (item) { return item.qty * item.amount; }
    },
    load: function () {
        rpc_call(SS.url.cart, 'content', {}, function (data) {
            this.set(data);
        }.bind(this));
    }
});
