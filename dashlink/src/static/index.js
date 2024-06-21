function deleteLink(linkId){
    fetch("/delete-link", {
        method:"POST",
        body: JSON.stringify({linkId:linkId})
    }).then((_res) => {
        window.location.href = "/";
    });
}
