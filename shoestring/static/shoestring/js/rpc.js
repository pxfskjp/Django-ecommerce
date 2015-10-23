rpc_call = function(url, method, data, callback) {
    $.ajax({
        type: 'POST',
        url: url,
        data: JSON.stringify(data || {}),
        headers: {
            'X-RPC-Action': method,
            'Content-Type': 'application/json'
        },
        success: callback || null
    });
};
