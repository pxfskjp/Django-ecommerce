var FilterList = Ractive.extend({
    template: '#filter-list',
    magic: true,
    oninit: function () {
        this.on('toggleFilter', function (event) {
            this.set(event.keypath + ".active", !event.context.active);
        }.bind(this));
    }
});
