import App from './App.html';
import { getCookie } from './cookies.js';
import request from './request.js';
import { ShoestringStore } from "./store.js";

import './global.scss';

const store = new ShoestringStore({
	products: [],
	tags: [],
	brands: [],
	cart: {
		items: []
	},
	order: undefined
})

request.request.commonHeaders['X-CSRFToken'] = getCookie('csrftoken');

var app = new App({
	target: document.body,
	store,
});

store.loadProducts()
store.loadCart()

export default app;