
$(document).ready(function(){
    $("#form-bodega").validate({
        rules:{
            categoria:{
                required:true,
            },
            nombre:{
                required:true,
            },
            cantidad:{
                required:true,
                number: true,
                min: 1
            }
        },
        messages:{
            categoria:{
                required:"El campo es obligatorio.",
            },
            nombre:{
                required:"El campo es obligatorio.",
            },
            cantidad:{
                required:"El campo es obligatorio.",
                number: "El campo debe ser un número.",
                min: "El campo debe ser mayor o igual a 1.",
            }
        }
    });
});