const contentDiv = document.getElementById('content');
const message = document.getElementById('message');
const deleteBtn = document.getElementById('deleteBtn');
const pasteId = new URLSearchParams(window.location.search).get('id');

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function fetchContent() {
    const response = await fetch(`/api/view/${pasteId}`, { method: 'POST' });
    if (response.status == 200) {
        const data = await response.json();
        contentDiv.innerHTML = data.content;
    } else {
        contentDiv.innerHTML = 'NOT FOUND';
        deleteBtn.setAttribute("disabled", true);
    }
}

deleteBtn.addEventListener('click', async () => {
    const response = await fetch(`/api/delete/${pasteId}`, { method: 'POST' });
    const data = await response.json();

    message.innerHTML = data.msg;
    message.classList.remove('hidden');
    contentDiv.innerHTML = 'DELETED';

    await sleep(3000);
    location.href = "/";
});

fetchContent();