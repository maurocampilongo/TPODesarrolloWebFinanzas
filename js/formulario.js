/* Obtener el elemento del área de texto donde se deja el comentario
 para  ajustar la altura del área de texto al escribir en ella*/
const textarea = document.getElementById("consulta");
const minHeight = textarea.offsetHeight; // Guardamos la altura inicial del textarea.
// Esto nos asegura que no se achique el textarea
textarea.addEventListener("input", () => {	
	textarea.style.height = Math.max(textarea.scrollHeight, minHeight) + "px"; // Set the new height
});

/* Constante para acceder al Formulario de nuestro HTML 
y a todos los inputs que hay dentro del formulario */
const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll("#formulario input");

/* El objeto expresiones tienen propiedades que son para cada campo del
Formulario usando Expresiones Regulares. Usar el mismo nombre
que se encuentra en el Id HTML para acceder a ellos. */
const expresiones = {
 nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
 apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
 correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
 telefono: /^\d{7,14}$/, // 7 a 14 numeros.
}

const campos = {
 nombre: false,
 apellido: false,
 correo: false,
 telefono: false
}
/*Función para validar los campos del formulario.
Hay que usar el "name=" de cada <input> para acceder a ellos.*/
const validarFormulario = (e) => {
	switch (e.target.name) {
		case "nombre":
			validarCampo(expresiones.nombre, e.target, "nombre");
		break;
		case "apellido":
			validarCampo(expresiones.apellido, e.target, "apellido");
		break;
		case "correo":
			validarCampo(expresiones.correo, e.target, "correo");
		break;
		case "telefono":
			validarCampo(expresiones.telefono, e.target, "telefono");
		break;
	}
}
/* Función para mostrar u ocultar los mensajes de error e iconos sobre los campos
del formulario en función de su validación.*/
const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo_${campo}`).classList.remove("formulario_grupo-incorrecto");
		document.getElementById(`grupo_${campo}`).classList.add("formulario_grupo-correcto");
		document.querySelector(`#grupo_${campo} i`).classList.add("fa-check-circle");
		document.querySelector(`#grupo_${campo} i`).classList.remove("fa-times-circle");
		document.querySelector(`#grupo_${campo} .formulario_input-error`).classList.remove("formulario_input-error-activo");
		campos[campo] = true;
	} else {
		document.getElementById(`grupo_${campo}`).classList.add("formulario_grupo-incorrecto");
		document.getElementById(`grupo_${campo}`).classList.remove("formulario_grupo-correcto");
		document.querySelector(`#grupo_${campo} i`).classList.add("fa-times-circle");
		document.querySelector(`#grupo_${campo} i`).classList.remove("fa-check-circle");
		document.querySelector(`#grupo_${campo} .formulario_input-error`).classList.add("formulario_input-error-activo");
		campos[campo] = false;
	}
}

/* Por cada entrada, ejecuta un código que va validando lo que se escribe.
O sea, cada vez que el usuario teclea algo, va validando, o bien,
cuándo deja de hacerlo hace un último chequeo*/
inputs.forEach((input) => {
	input.addEventListener("keyup", validarFormulario); //Evento para cuando se presione una tecla
	input.addEventListener("blur", validarFormulario); //Evento para cuando se deje de presionar una tecla
});

/*Evento para cuando se haga click en el boton de enviar el Formulario
Se valida que todos los campos esten llenos y que no haya errores*/
formulario.addEventListener("submit", (e) => { //e es el evento
	e.preventDefault(); //Evita que se envie el Formulario
	if(campos.nombre && campos.apellido && campos.correo && campos.telefono){
		formulario.reset();
		document.getElementById("formulario_mensaje-exito").classList.add("formulario_mensaje-exito-activo");
		setTimeout(() => {
			document.getElementById("formulario_mensaje-exito").classList.remove("formulario_mensaje-exito-activo");
		}, 5000);
		document.querySelectorAll(".formulario_grupo-correcto").forEach((icono) => {
			icono.classList.remove("formulario_grupo-correcto");
		});
	} else {
		document.getElementById("formulario_mensaje").classList.add("formulario_mensaje-activo");
	}
});