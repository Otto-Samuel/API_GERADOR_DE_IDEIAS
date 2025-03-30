async function gerarIdeia() {
    const tema = document.getElementById('tema').value;
    const resultadoDiv = document.getElementById('resultado');

    if (!tema) {
        resultadoDiv.innerText = "Por favor, selecione um tema!";
        return;
    }

    const url = `http://127.0.0.1:5000/gerar?tema=${tema}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.erro) {
            resultadoDiv.innerText = data.erro;
        } else {
            resultadoDiv.innerText = data.ideia;
        }
    } catch (error) {
        resultadoDiv.innerText = "Erro ao conectar com a API!";
    }
}