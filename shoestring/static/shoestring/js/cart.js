
var Cart = Ractive.extend({
    template: '#cart',
    load: function () {
        rpc_call(SS.url.cart, 'content', {}, function (data) {
            this.set(data);
        }.bind(this));
    }
});
