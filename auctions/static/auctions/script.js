async function closeListing(id){
    console.log(id)
    const response = await fetch(`/api/close?id=${id}`)
    const json = await response.json()

    if (json.status){
        // listing closed
        document.getElementById('listing-content').style.display ='none'
        document.getElementById('closed').style.display='block'
    }else{
        alert(json.error)
    }

}