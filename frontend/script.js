async function carregarDados() {
    const res = await fetch('http://localhost:5000/dados');
    const dados = await res.json();
    const tbody = document.querySelector('#tabela tbody');
    tbody.innerHTML = '';
    dados.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${row.data}</td><td>${row.unidade}</td><td>${row.meta}</td><td>${row.realizado}</td>`;
        tbody.appendChild(tr);
    });
}

document.getElementById('form-dados').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const dados = {
        data: form.data.value,
        unidade: form.unidade.value,
        meta: parseFloat(form.meta.value),
        realizado: parseFloat(form.realizado.value),
    };
    await fetch('http://localhost:5000/dados', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });
    form.reset();
    carregarDados();
});

carregarDados();
