async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        /*const response = await fetch('http://51.20.153.103:8000/predict/', {
            method: 'POST',
            body: formData,
        });*/
        const response = await fetch('http://127.0.0.1:8000/predict/', {
            method: 'POST',
            body: formData,
        });
        const result = await response.json();
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `<h2>Predictions:</h2><pre>${JSON.stringify(result.predictions, null, 2)}</pre>`;
    } catch (error) {
        console.error('Error:', error);
    }
}
