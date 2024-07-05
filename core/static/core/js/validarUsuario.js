$.validator.addMethod("soloLetras", function(value, element) {
    return this.optional(element) || /^[a-zA-Z\s]*$/.test(value);
}, "Sólo se permiten letras y espacios en blanco.");

$.validator.addMethod("emailCompleto", function(value, element) {
    // Expresión regular para validar correo electrónico
    var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]{2,}))$/;
    // Validar correo electrónico con la expresión regular
    return regex.test(value);
}, 'El formato del correo no es válido');

// Agregar método de validación para RUT chileno
$.validator.addMethod("rutChileno", function(value, element) {

    // Validar que el RUT tenga el formato correcto (8 o 9 dígitos + guión + dígito verificador)
    var rutPattern = /^\d{7,8}-[\dK]$/;
    if (!rutPattern.test(value)) {
        return false;
    }

    // Validar el dígito verificador
    var rutSinGuion = value.replace("-", "");
    var rut = rutSinGuion.slice(0, -1);
    var dv = rutSinGuion.slice(-1);
    var factor = 2;
    var sum = 0;
    for (var i = rut.length - 1; i >= 0; i--) {
        sum += parseInt(rut.charAt(i)) * factor;
        factor = factor === 7 ? 2 : factor + 1;
    }
    var dvCalculado = 11 - (sum % 11);
    dvCalculado = dvCalculado === 11 ? "0" : dvCalculado === 10 ? "K" : dvCalculado.toString();

    return dv === dvCalculado;
}, "El RUT no es válido (escriba sin puntos y con guión)");

$(document).ready(function(){

    $("#form-usuario").validate({
        rules:{
            idUsuario: {
                required: true,
                number: true,
                min: 1
            },
            tipoUsuario: {
                required: true,
            },
                
            rut: {
                required: true,
                rutChileno: true,


            },
            nombre: {
                required: true,
                soloLetras: true,

            },
            apellido: {
                required: true,
                soloLetras: true,

            },
            correo: {
                required: true,
                emailCompleto: true,

            },
            direccion: {
                required: true,

            },
            password: {
                required: true,
                minlength:8,
                maxlength:15,

            }




        },
        messages: {
            idUsuario: {
                required:"El campo es obligatorio.",
                number: "El campo debe ser un número.",
                min: "El campo debe ser mayor o igual a 1.",
            },
            tipoUsuario: {
                required: "El campo es obligatorio.",
            },
            rut: {
                required: "El campo es obligatorio.",
                rutChileno: "El rut ingresado no es válido, sólo ingresar números, ingresar sin puntos y con guión"
            },
            nombre: {
                required:"El campo es obligatorio.",
                soloLetras:"El campo solo puede contener letras."

            },
            apellido: {
                required: "El campo es obligatorio.",
                soloLetras:"El campo solo puede contener letras."

            },
            correo: {
                required: "El campo es obligatorio.",
                emailCompleto: "El correo debe tener un dominio válido",
                email: "El formato del correo no es válido",
            },
            direccion: {
                required: "El campo es obligatorio.",
            },
            password: {
                required: "El campo es obligatorio.",
                minlength: "Debe tener un mínimo de 8 carácteres",
                maxlength: "Debe tener un máximo de 15 carácteres",
            },

        }

    });

});