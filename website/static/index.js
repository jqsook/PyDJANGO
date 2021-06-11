function deleteNote(noteId) {
    fetch('/delete-note', {  //The delete-note is the end point
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/"; //refreshes the page
    });
}
// Basic request sent to the back end to delete the note and reset the window.