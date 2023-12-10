const formulario = document.getElementById('form');

formulario.addEventListener('submit',async (e) => {
    e.preventDefault();

    try{
        await fetch('https://sheet.best/api/sheets/dcb57438-7383-4ef8-b2e4-1becc6301f12', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "Nombre": formulario.nombre.value,
                "Email": formulario.email.value,
                "Telefono": formulario.telefono.value,
                "Asunto": formulario.asunto.value,
                "Mensaje": formulario.mensaje.value,

            })
        });
    }catch(error){
        console.log(error);
    }

    alert("Gracias por tu mensaje");

    
});

