
let imageUrl = (alias, url) => { return SS.url.product + alias + '/' + url; }

let dollarFormat = (value) => new Number(value).toFixed(2);

let itemTotal = (item) => dollarFormat(item.quantity * item.price)

export {
    dollarFormat,
    imageUrl,
    itemTotal
}