async function shortenUrl() {
    const url = document.getElementById('url-input').value;
    const response = await fetch('http://localhost:8000/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ original_url: url })
    });
    const data = await response.json();
    document.getElementById('result').textContent = `Shortened URL: ${window.location.origin}/${data.short_url}`;
}
