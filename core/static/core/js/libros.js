//Crear funcion ready
$(document).ready(function () {

    //Crear invocación de la api donde se obtienen los datos:
    //https://freetestapi.com/api/v1/books
    $.get('https://freetestapi.com/api/v1/actors', function (data) {
        //usando $.get recorrer la lista de ropas

        $.each(data, function (i, item) {
            //Crear codigo html para agregar los productos al contenedor
            html = `
                <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
                    <div class="card" style="heigth:100px !important">
                        <img src="${item.image}" class="card-img-top" style="heigth:100px !important" alt="...">
                        <div class="card-body">
                        <h5 class="card-title">
                        ${item.name}
                        </h5>
                        <h6 class="card-title">
                        ${item.nationality}
                        </h6>
                        <p class="card-text">
                        ${item.biography}
                        </p>
                        <a href="#" class="btn btn-primary">
                        Buscar</a>
                        </div>
                    </div>
            </div>
            `;

            $('#recuadro-de-ropa').append(html);
        });
    });
});