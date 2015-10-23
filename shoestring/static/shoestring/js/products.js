
var ProductList = Ractive.extend({
    template: '#product-list',
    computed: {
        sku_map: function () {
            var o = {};
            this.get('products').forEach(function (rec) { o[rec.sku] = rec; });
            return o;
        }
    }
});


var ProductDetail = Ractive.extend({
    template: '#product-detail'
});
