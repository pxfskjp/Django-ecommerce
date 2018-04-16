import request from '@funkybob/request';
import { Store } from 'svelte/store.js';

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

	loadCart() {
		request.rpc(SS.url.cart, 'content')
		.then( data => this.set({cart: data}) )
	}

	clearCart() {
		request.rpc(SS.url.cart, 'clear')
		.then( data => this.set({cart: data}) )
	}

	addCartItem(item) {
		request.rpc(SS.url.cart, 'add', {sku: item.sku, quantity: 1})
		.then( data => this.set({cart: data}) )
	}

	decCartItem(item) {
		request.rpc(SS.url.cart, 'quantity', {sku: item.sku, quantity: item.quantity - 1})
		.then( data => this.set({cart: data}) )
	}

	incCartItem(item) {
		request.rpc(SS.url.cart, 'quantity', {sku: item.sku, quantity: item.quantity + 1})
		.then( data => this.set({cart: data}) )
	}

	remCartItem(item) {
		request.rpc(SS.url.cart, 'quantity', {sku: item.sku, quantity: 0})
		.then( data => this.set({cart: data}) )
	}


	loadOrder() {
		return request.json(SS.url.order)
		.then( data => this.set({order: data}) )
		.catch( err => this.set({order: undefined}) )
	}

	createOrder() {
		return request.json(SS.url.order, {method: 'POST'})
		.then( data => this.set({order: data}) )
	}

	cancelOrder() {
		request.json(SS.url.order, {method: 'DELETE'})
		.then( data => this.set({order: undefined}) )
	}
}

export {
    ShoestringStore
}