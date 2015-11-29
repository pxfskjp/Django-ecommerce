var order = Ractive.extend({
    template: '#order',
    isolated: true,
    magic: true,
    append: true,
    data: function () {
        return {
            items: [],
            discount: null,
            shipping: null,
        };
    }
});
