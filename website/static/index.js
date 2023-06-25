function deleteNote(nodeId) {
    fetch('/delete-note', 
         {method: 'POST', 
            body: JSON.stringify({nodeId}),
         }).then((_res) => { window.location.href = "/";});
        }