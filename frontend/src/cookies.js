export function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';').map(function (c) {
            return c.trim().match(/(\w+)=(.*)/);
        }).forEach(function (m) {
            if(m !== undefined && m[1] == name) {
                cookieValue = decodeURIComponent(m[2]);
            }
        });
    }
    return cookieValue;
}
