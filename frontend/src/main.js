import App from './App.html';
import { Store } from 'svelte/store.js';
import { getCookie } from './cookies.js';
import request from './request.js';

const store = new Store({
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