import svelte from 'rollup-plugin-svelte';
import resolve from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs';
import buble from 'rollup-plugin-buble';
import uglify from 'rollup-plugin-uglify';
import scss from 'rollup-plugin-scss'
import sass from 'node-sass';

const production = !process.env.ROLLUP_WATCH;

export default {
	input: 'src/main.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'public/bundle.js'
	},
	plugins: [
		svelte({
			// enable run-time checks when not in production
			dev: !production,
			// we'll extract any component CSS out into
			// a separate file — better for performance
			css: css => {
				css.write('public/bundle.css');
			},

			preprocess: {
				style: ({ content }) => {
					return new Promise((fulfil, reject) => {
						sass.render({ data: content }, (err, result) => {
							if (err) reject(err);
							else fulfil({ code: result.css }); // NOT SURE THIS IS RIGHT!
						});
					});
				}
			},

			// enable https://svelte.technology/guide#state-management
			store: true,

			// this results in smaller CSS files
			cascade: false
		}),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration —
		// consult the documentation for details:
		// https://github.com/rollup/rollup-plugin-commonjs
		resolve(),
		commonjs(),

		scss({
			output: 'public/global.css',
			outputStyle: (production) ? 'compressed' : 'nested'
		}),

		// If we're building for production (npm run build
		// instead of npm run dev), transpile and minify
		production && buble({ exclude: 'node_modules/**' }),
		production && uglify()
	]
};
