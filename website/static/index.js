function deleteNote(nodeId) {
    fetch('/delete-node', 
         {method: 'POST', 
            body: JSON.stringify({nodeId}),
         }).then((_res) => { window.location.href = "/";});
        }