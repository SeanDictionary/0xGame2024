const form = document.getElementById('reportForm');
const message = document.getElementById('message');
const pasteIdInput = document.getElementById('pasteId');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const response = await fetch(`/api/report/${pasteIdInput.value}`, { method: 'POST' });
    const data = await response.json();

    message.textContent = data.msg;
    message.classList.remove('hidden');
    pasteIdInput.value = '';
});