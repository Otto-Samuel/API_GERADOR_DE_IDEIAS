from flask import Flask, request, jsonify, render_template
import random
import os

app = Flask(__name__)

# Listas para gerar ideias criativas
temas = {
    "filmes": ["astronauta", "detetive", "pirata", "robô", "mago"],
    "jogos": ["corrida", "aventura", "estratégia", "puzzle", "sobrevivência"],
    "histórias": ["floresta mágica", "cidade futurista", "reino perdido", "escola secreta", "ilha misteriosa"]
}

ações = ["descobre", "luta contra", "explora", "constrói", "salva"]
detalhes = ["um planeta estranho", "uma conspiração antiga", "um tesouro escondido", "uma máquina do tempo",
            "um vilão inesperado"]


# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')


# Rota para gerar ideias
@app.route('/gerar', methods=['GET'])
def gerar_ideia():
    tema = request.args.get('tema', '').lower()
    if tema not in temas:
        return jsonify({"erro": "Tema inválido. Escolha entre: filmes, jogos, histórias"}), 400

    personagem = random.choice(temas[tema])
    acao = random.choice(ações)
    detalhe = random.choice(detalhes)

    ideia = f"Uma ideia para {tema}: Um {personagem} que {acao} {detalhe}."
    return jsonify({"ideia": ideia})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)