    $.validator.addMethod("emailCompleto", function(value, element) {

    // Expresión regular para validar correo electrónico
    var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]{2,}))$/;

    // Validar correo electrónico con la expresión regular
    return regex.test(value);

    }, 'El formato del correo no es válido');
  

    $("#form-ingreso").validate({
        rules:{
            correo:{
                required: true,
                emailCompleto: true,
                email:true
                
            },
            password:{
                required:true, 
                minlength:8,
                maxlength:15,
            }
        },
        messages:{
            correo:{
                required:"El campo es obligatorio.",
                emailCompleto:"El formato del correo no es válido.",
                email:"El formato del correo no es válido."
                
             },
            password:{
                required:"El campo es obligatorio.",
                minlength: "Debe tener un mínimo de 8 carácteres",
                maxlength: "Debe tener un máximo de 15 carácteres",
            }
        }
    });

