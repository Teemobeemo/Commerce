async function closeListing(id) {
    const response = await fetch(`/api/close?id=${id}`)
    const json = await response.json()

    if (json.status) {
        // listing closed
        document.getElementById('listing-content').style.display = 'none'
        document.getElementById('closed').style.display = 'block'
    } else {
        alert(json.error)
    }

}

async function addToWatchList(id) {
    const response = await fetch(`/api/watchlist?id=${id}`)
    const json = await response.json()

    if (json.status) {
        alert('added to watchlist')
    } else {
        alert(json.error)
    }

}
// Get the csrf token from the browser
function csrfcookie() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

function showBid(id) {
    const divId = `bid-area-${id}`
    document.getElementById(divId).style.display = 'block'
}

async function bid(id) {
    const amt = document.getElementById(`bid-amt-${id}`).value;

    const response = await fetch(`/api/bid`, {
        method: 'POST',
        headers: {
            'Content-Type': "application/json; charset=UTF-8",
            "X-CSRFToken": csrfcookie(),
        },
        body: JSON.stringify({ amt: amt, id: id })
    });
    const json = await response.json()

    if (json.success) {
        const h5 = document.getElementById('max-bid')
        h5.innerText = json.max_bid_amt
        const divId = `bid-area-${id}`
        document.getElementById(divId).style.display = 'none'
    } else {
        alert(json.error)
    }
}
