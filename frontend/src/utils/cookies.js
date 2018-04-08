export function getCookie(name) {
    let value = undefined;
    (document.cookie || '')
        .split(';')
        .map(c => c.trim().match(/(\w+)=(.*)/))
        .forEach(m => {
            if(m !== undefined && m[1] == name) {
                value = decodeURIComponent(m[2]);
            }
        });
    return value;
}
