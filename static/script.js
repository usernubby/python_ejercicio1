const formulario = document.getElementById("formulario");

formulario.addEventListener("submit", async function(evento) {
    evento.preventDefault();

    const numero = document.getElementById("numero").value;

    const respuesta = await fetch("/par-impar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            numero: numero
        })
    });

    const datos = await respuesta.json();

    document.getElementById("resultado").textContent = datos.resultado;
});