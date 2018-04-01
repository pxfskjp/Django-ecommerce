
let image_url = (alias, url) => { return SS.url.product + alias + '/' + url; }

let dollarFormat = (value) => new Number(value).toFixed(2);

export {
    dollarFormat,
    imageUrl
}