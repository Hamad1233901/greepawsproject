// ---------------------------
// CLIENT FORM SUBMIT
// ---------------------------
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
        loadOwnerOptions(); // update owner dropdown too
    });
});

// ---------------------------
// LOAD CLIENTS
// ---------------------------
function loadClients() {
    fetch('http://127.0.0.1:5000/api/clients')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('clientList');
            list.innerHTML = '';
            data.forEach(c => {
                const li = document.createElement('li');
                li.innerHTML = `
                    ${c.name} (${c.phone})
                    <button onclick="editClient(${c.id}, '${c.name}', '${c.phone}', '${c.cnic || ''}')">Edit</button>
                    <button onclick="deleteClient(${c.id})">Delete</button>
                `;
                list.appendChild(li);
            });
        });
}

function deleteClient(id) {
    fetch(`http://127.0.0.1:5000/api/clients/${id}`, {
        method: 'DELETE'
    }).then(() => {
        loadClients();
        loadOwnerOptions();
    });
}

function editClient(id, name, phone, cnic) {
    const newName = prompt("Edit Name:", name);
    const newPhone = prompt("Edit Phone:", phone);
    const newCnic = prompt("Edit CNIC:", cnic);

    if (newName && newPhone) {
        fetch(`http://127.0.0.1:5000/api/clients/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: newName, phone: newPhone, cnic: newCnic })
        }).then(() => {
            loadClients();
            loadOwnerOptions();
        });
    }
}

// ---------------------------
// LOAD OWNER OPTIONS (FOR PET FORM)
// ---------------------------
function loadOwnerOptions() {
    fetch('http://127.0.0.1:5000/api/clients')
        .then(res => res.json())
        .then(clients => {
            const select = document.getElementById('ownerSelect');
            select.innerHTML = '<option value="">-- Select Owner --</option>';
            clients.forEach(c => {
                const option = document.createElement('option');
                option.value = c.id;
                option.textContent = `${c.name} (${c.phone})`;
                select.appendChild(option);
            });
        });
}

// ---------------------------
// PET FORM SUBMIT
// ---------------------------
document.getElementById('petForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('petName').value;
    const species = document.getElementById('species').value;
    const breed = document.getElementById('breed').value;
    const dob = document.getElementById('dob').value;
    const owner_id = document.getElementById('ownerSelect').value;

    fetch('http://127.0.0.1:5000/api/pets', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, species, breed, dob, owner_id })
    })
    .then(res => res.json())
    .then(() => {
        loadPets();
        loadPetOptionsForVisits();
        document.getElementById('petForm').reset();
    });
});

// ---------------------------
// LOAD PETS
// ---------------------------
function loadPets() {
    fetch('http://127.0.0.1:5000/api/pets')
        .then(res => res.json())
        .then(pets => {
            const list = document.getElementById('petList');
            list.innerHTML = '';
            pets.forEach(p => {
                const li = document.createElement('li');
                li.innerHTML = `
                    ${p.name} (${p.species}) - Owner ID: ${p.owner_id}
                    <button onclick="editPet(${p.id}, '${p.name}', '${p.species}', '${p.breed}', '${p.dob}', ${p.owner_id})">Edit</button>
                    <button onclick="deletePet(${p.id})">Delete</button>
                `;
                list.appendChild(li);
            });
        });
}

function deletePet(id) {
    fetch(`http://127.0.0.1:5000/api/pets/${id}`, {
        method: 'DELETE'
    }).then(() => {
        loadPets();
        loadPetOptionsForVisits();
    });
}

function editPet(id, name, species, breed, dob, owner_id) {
    const newName = prompt("Edit Pet Name:", name);
    const newSpecies = prompt("Edit Species:", species);
    const newBreed = prompt("Edit Breed:", breed);
    const newDob = prompt("Edit DOB:", dob);
    const newOwnerId = prompt("Edit Owner ID:", owner_id);

    if (newName && newSpecies && newOwnerId) {
        fetch(`http://127.0.0.1:5000/api/pets/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name: newName,
                species: newSpecies,
                breed: newBreed,
                dob: newDob,
                owner_id: newOwnerId
            })
        }).then(() => {
            loadPets();
            loadPetOptionsForVisits();
        });
    }
}

// ---------------------------
// VISIT FORM SUBMIT
// ---------------------------
document.getElementById('visitForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const pet_id = document.getElementById('visitPetSelect').value;
    const date = document.getElementById('visitDate').value;
    const symptoms = document.getElementById('symptoms').value;
    const treatment = document.getElementById('treatment').value;
    const next_visit = document.getElementById('nextVisit').value;

    fetch('http://127.0.0.1:5000/api/visits', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pet_id, date, symptoms, treatment, next_visit })
    })
    .then(res => res.json())
    .then(() => {
        loadVisitRecords();
        document.getElementById('visitForm').reset();
    });
});

// ---------------------------
// LOAD VISITS
// ---------------------------
function loadVisitRecords() {
    fetch('http://127.0.0.1:5000/api/visits')
        .then(res => res.json())
        .then(visits => {
            const list = document.getElementById('visitList');
            list.innerHTML = '';
            visits.forEach(v => {
                const li = document.createElement('li');
                li.innerHTML = `
                    ${v.date} - ${v.pet_name}: ${v.symptoms} → ${v.treatment} (Next: ${v.next_visit || 'N/A'})
                    <button onclick="deleteVisit(${v.id})">Delete</button>
                `;
                list.appendChild(li);
            });
        });
}

function deleteVisit(id) {
    fetch(`http://127.0.0.1:5000/api/visits/${id}`, {
        method: 'DELETE'
    }).then(() => loadVisitRecords());
}

// ---------------------------
// LOAD VISIT FORM PET DROPDOWN
// ---------------------------
function loadPetOptionsForVisits() {
    fetch('http://127.0.0.1:5000/api/pets')
        .then(res => res.json())
        .then(pets => {
            const select = document.getElementById('visitPetSelect');
            select.innerHTML = '<option value="">-- Select Pet --</option>';
            pets.forEach(p => {
                const option = document.createElement('option');
                option.value = p.id;
                option.textContent = `${p.name} (${p.species})`;
                select.appendChild(option);
            });
        });
}

// ---------------------------
// INITIAL LOAD
// ---------------------------
loadClients();
loadPets();
loadOwnerOptions();
loadPetOptionsForVisits();
loadVisitRecords();
