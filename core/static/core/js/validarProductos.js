$.validator.addMethod("soloLetras", function(value, element) {
    return this.optional(element) || /^[a-zA-Z\s]*$/.test(value);
}, "Sólo se permiten letras y espacios en blanco.");

$(document).ready(function() {
    $("#form-producto").validate({
        rules:{
            idProducto:{
                required:true,
                number: true,
                min: 1,
                max:100,
            },
            categoria:{
                required:true
            },
            nombre:{
                required:true,
            },
            descripcion:{
                required:true,
                soloLetras:true
            },
            precio:{
                required:true,
                number: true,
                min: 1
            },
            descuento:{
                required:true,
                number: true,
                min: 0,
                max:100
            },
            oferta:{
                required:true,
                number:true,
                min: 0,
                max: 100
            }
        },
        messages:{
            idProducto:{
                required:"El campo ID de Producto es obligatorio.",
                number:"Solo puede ser un número.",
                min:"El valor debe ser mayor o igual a 1.",
                max:"El valor debe ser menor o igual a 100."
            },
            categoria:{
                required:"El campo Categoria es obligatorio."
            },
            nombre:{
                required:"El campo Nombre es obligatorio."
            },
            precio:{
                required:"El campo Precio es obligatorio.",
                number: "El campo debe ser un número.",
                min: "El campo debe ser mayor o igual a 1."
            },
            descuento:{
                required:"El campo Descuento Subscriptor es obligatorio.",
                number: "El campo debe ser un número.",
                min: "El campo debe ser mayor o igual a 0.",
                max: "El campo debe ser menor o igual a 100."
            },
            descripcion:{
                required:"El campo Descripción del producto es obligatorio.",
                soloLetras:"El campo solo puede contener letras."
            },
            oferta:{
                required:"El campo Oferta es obligatorio.",
                number: "El campo debe ser un número.",
                min: "El campo debe ser mayor o igual a 0.",
                max: "El campo debe ser menor o igual a 100."
            }
        }
    });
});
