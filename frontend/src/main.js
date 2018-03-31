import App from './App.html';
import { Store } from 'svelte/store.js';
import { getCookie } from './cookies.js';
import request from './request.js';

import './global.scss';

class ShoestringStore extends Store {
	toggleFilter(key, name) {
		let items = this.get(key);
		items.forEach(item => (item.name == name) && (item.active = !item.active));
		let update = {}
		update[key] = items;
		this.set(update);
		this.loadProducts();
	}

	loadProducts() {
		request.json(SS.url.product, {
			data: {
				tag: this.get('tags').filter(tag => tag.active).map(tag => tag.name),
				brand: this.get('brands').filter(brand => brand.active).map(brand => brand.name)
			}
		})
		.then(data => this.set(data))
	}
}
const store = new ShoestringStore({
	products: [],
	tags: [],
	brands: [],
	cart: {
		items: []
	}
})

request.request.commonHeaders['X-CSRFToken'] = getCookie('csrftoken');

var app = new App({
	target: document.body,
	store
});

export default app;