const form = document.getElementById('pasteForm');
const message = document.getElementById('successMessage');
const content = document.getElementById('pasteContent');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const response = await fetch('/api/paste', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ content: content.value }),
    });
    const data = await response.json();

    message.innerHTML = `Paste successful! View it <a href="/view?id=${data.id}"><b>here</b></a>`;
    message.classList.remove('hidden');
    content.value = '';
});