// Cambia esta URL cuando uses ngrok, ej: 'https://tu-id.ngrok-free.app'
const API_URL = 'http://127.0.0.1:8000';

// Navegacion de pestanas
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab, .view').forEach(el => el.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(`${tab.dataset.tab}-view`).classList.add('active');
  });
});

// Buscar Fondas
const searchBtn = document.getElementById('search-btn');
const resultsDiv = document.getElementById('results');

async function searchFondas() {
  const q = document.getElementById('q').value;
  const barrio = document.getElementById('barrio').value;
  const precio = document.getElementById('precio').value;

  resultsDiv.innerHTML = 'Buscando...';
  
  try {
    const params = new URLSearchParams({ q, barrio, precio_rango: precio });
    const response = await fetch(`${API_URL}/fondas?${params}`);
    const data = await response.json();
    
    resultsDiv.innerHTML = '';
    if (data.fondas.length === 0) {
      resultsDiv.innerHTML = '<p>No se encontraron fondas baratas aqui.</p>';
      return;
    }

    data.fondas.forEach(fonda => {
      const el = document.createElement('div');
      el.className = 'card fonda-item';
      el.innerHTML = `
        <div class="fonda-name">${fonda.nombre} ${fonda.precio_rango}</div>
        <div class="fonda-meta">${fonda.barrio} - ${fonda.descripcion || ''}</div>
        <button class="report-btn" data-id="${fonda.id}">Reportar Cerrado</button>
      `;
      resultsDiv.appendChild(el);
    });

    // Eventos para reportar
    document.querySelectorAll('.report-btn').forEach(btn => {
      btn.addEventListener('click', () => reportarCerrado(btn.dataset.id));
    });

  } catch (err) {
    resultsDiv.innerHTML = 'Error de conexion. Esta el servidor corriendo?';
  }
}

// Registrar nueva fonda
const saveBtn = document.getElementById('save-btn');
async function registrarFonda() {
  const nombre = document.getElementById('add-nombre').value;
  const barrio = document.getElementById('add-barrio').value;
  const precio_rango = document.getElementById('add-precio').value;
  const descripcion = document.getElementById('add-desc').value;

  if (!nombre || !barrio) return alert('Nombre y Barrio son obligatorios');

  saveBtn.disabled = true;
  try {
    const response = await fetch(`${API_URL}/fondas`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, barrio, precio_rango, descripcion })
    });
    
    if (response.ok) {
      alert('Gracias! La fonda sera revisada.');
      document.getElementById('add-nombre').value = '';
      document.querySelector('[data-tab="search"]').click();
    }
  } catch (err) {
    alert('Error al guardar');
  } finally {
    saveBtn.disabled = false;
  }
}

async function reportarCerrado(id) {
  if (!confirm('Seguro que este lugar esta cerrado?')) return;
  try {
    await fetch(`${API_URL}/reportes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ fonda_id: id, tipo: 'cerrado' })
    });
    alert('Reporte enviado');
  } catch (err) {
    alert('Error al reportar');
  }
}

searchBtn.addEventListener('click', searchFondas);
saveBtn.addEventListener('click', registrarFonda);
