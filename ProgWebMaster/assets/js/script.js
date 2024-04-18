
let usuarios = [];

// Al cargar la página, intenta recuperar los datos de usuarios guardados en localStorage
window.onload = function() {
    const usuariosGuardados = localStorage.getItem('usuarios');
    if (usuariosGuardados) {
        usuarios = JSON.parse(usuariosGuardados);
    }
};


function registro() {
    const nombre = document.getElementById("nombre").value;
    const apellido = document.getElementById("apellido").value;
    const edad = parseInt(document.getElementById("edad").value);
    const genero = document.getElementById("genero").value;
    const email = document.getElementById("emailRegistro").value;
    const ocupacion = document.getElementById("ocupacion").value;
    const password = document.getElementById("passwordRegistro").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Validar correo electrónico con una expresión regular
    const emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegExp.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return;
    }

    // Verificar que las contraseñas coincidan
    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden.");
        return;
    }

    if (!nombre || !apellido || !edad || !genero || !ocupacion || !email || !password || !confirmPassword) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    if (nombre === "" || apellido === "" || isNaN(edad) || edad < 1 || edad > 100 || genero === "" || ocupacion === "" || email === "" || password === "" || confirmPassword === "") {
        alert("Por favor, complete todos los campos correctamente.");
        return;
    }

    // Guardar el nuevo usuario en el arreglo y en localStorage
    usuarios.push({ nombre, apellido, edad, genero, email, ocupacion, password });
    localStorage.setItem('usuarios', JSON.stringify(usuarios));

    // Limpiar los campos del formulario
    document.getElementById("nombre").value = "";
    document.getElementById("apellido").value = "";
    document.getElementById("edad").value = "";
    document.getElementById("genero").value = "";
    document.getElementById("emailRegistro").value = "";
    document.getElementById("ocupacion").value = "";
    document.getElementById("passwordRegistro").value = "";
    document.getElementById("confirmPassword").value = "";

    alert("Usuario registrado con éxito.");
}

function login() {
    const email = document.getElementById("emailLogin").value;
    const password = document.getElementById("passwordLogin").value;

    // Validar correo electrónico con una expresión regular
    const emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegExp.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return;
    }

    // Validar que se haya ingresado una contraseña
    if (!password) {
        alert("Por favor, ingrese una contraseña.");
        return;
    }

    if (!email || !password) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    const usuario = usuarios.find(user => user.email === email && user.password === password);

    if (usuario) {
        alert(`¡Bienvenido, ${usuario.nombre}!`);
    } else {
        alert("Credenciales incorrectos o inexistentes.");
    }

    // Limpiar los campos del formulario de login
    document.getElementById("emailLogin").value = "";
    document.getElementById("passwordLogin").value = "";
}

function enviarMensaje() {
    const nombre = document.getElementById("nombreContacto").value;
    const email = document.getElementById("emailContacto").value;
    const mensaje = document.getElementById("mensajeContacto").value;

    // Validar correo electrónico con una expresión regular
    const emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegExp.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return;
    }

    // Validar que los campos no estén vacíos
    if (!nombre || !email || !mensaje) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    alert("Mensaje enviado con éxito.");

    // Limpiar los campos del formulario
    document.getElementById("nombreContacto").value = "";
    document.getElementById("emailContacto").value = "";
    document.getElementById("mensajeContacto").value = "";
}