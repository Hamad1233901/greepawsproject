document.getElementById('clientForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const cnic = document.getElementById('cnic').value;

    fetch('http://127.0.0.1:5000/api/clients', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, phone, cnic })
    })
    .then(res => res.json())
    .then(() => {
        loadClients();
        document.getElementById('clientForm').reset();
    });
});

function loadClients() {
    fetch('http://127.0.0.1:5000/api/clients')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('clientList');
            list.innerHTML = '';
            data.forEach(c => {
                const li = document.createElement('li');
                li.textContent = `${c.name} (${c.phone})`;
                list.appendChild(li);
            });
        });
}

// Load on page open
loadClients();
