
let clickme = (node, callback) => {
  let handler = ev => {
    ev.stopPropagation();
    callback(ev)
  };
  node.addEventListener('click', handler);
  return {
    destroy() {
      node.removeEventListener('click', handler);
    }
  }
}

export {
  clickme
}
