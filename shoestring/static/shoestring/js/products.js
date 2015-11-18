
var ProductList = Ractive.extend({
    template: '#product-list',
    data: {
        image: function (src) {
            src = src || 'products/default.png';
            return 'products/product-list/' + src;
        }
    },
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
