app.py

from flask import Flask, request, jsonify from flask_cors import CORS import sqlite3

app = Flask(name) CORS(app)

DATABASE = 'db.sqlite3'

def query_db(query, args=(), one=False): conn = sqlite3.connect(DATABASE) conn.row_factory = sqlite3.Row cur = conn.execute(query, args) rv = cur.fetchall() conn.commit() conn.close() return (rv[0] if rv else None) if one else rv

@app.route('/dados', methods=['GET']) def get_dados(): resultados = query_db('SELECT * FROM producao ORDER BY data DESC LIMIT 100') return jsonify([dict(row) for row in resultados])

@app.route('/dados', methods=['POST']) def inserir_dado(): data = request.json query_db('INSERT INTO producao (data, unidade, meta, realizado) VALUES (?, ?, ?, ?)', (data['data'], data['unidade'], data['meta'], data['realizado'])) return jsonify({'status': 'ok'})

if name == 'main': app.run(debug=True)

