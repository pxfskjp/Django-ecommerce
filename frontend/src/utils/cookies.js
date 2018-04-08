export function getCookie(name) {

    (document.cookie || '')
        .split(';')
        .map(c => c.trim().match(/(\w+)=(.*)/))
        .forEach(m => {
            if(m !== undefined && m[1] == name) {
                return decodeURIComponent(m[2]);
            }
        });
    return undefined;
}
