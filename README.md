# Projeto: Sistema PCP Têxtil

Sistema web para lançamento, planejamento e acompanhamento da produção têxtil.

## Tecnologias
- Python (Flask)
- HTML/CSS/JavaScript
- SQLite
- Pandas (para importar planilha)

## Como usar

1. Instale dependências:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Crie o banco de dados:
```bash
sqlite3 backend/db.sqlite3 < backend/models.sql
python backend/import_excel.py
```

3. Execute o servidor:
```bash
python backend/app.py
```

4. Acesse via navegador:
```
http://localhost:5000
```

## Hospedagem

Use GitHub Pages para o frontend (index.html etc) e serviços como PythonAnywhere para o backend.
