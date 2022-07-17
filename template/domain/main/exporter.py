import html
class Exporter():
    def generarReporte(cliente):
        f = open(f'.\entradas-salidas\\reporte.html', 'w', encoding="utf-8")
        html_template = f"""
        <!--En el reporte se debe incluir el nombre de cliente, número, DNI, dirección y para
        cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la
        cual se rechazó (vacío en caso de ser aceptada).-->
        <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
                <title>Reporte Transferencias</title>
            </head>
            <body>
                <div class="container">
                    <h2>Reporte</h2>
                    <div class="card bg-secondary">
                        <h4 class="card-title m-2 pt-1 text-light">Cliente</h4>
                        <div class="card-body bg-light py-2 m-1">
                            <p class="card-text my-0">Nombre: {cliente.nombre}</p>
                            <p class="card-text my-0">Número: {cliente.numero}</p>
                            <p class="card-text my-0">DNI: {cliente.dni}</p>
                            <p class="card-text my-0">Dirección: {cliente.direccion.calle} {cliente.direccion.numero}</p>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """
        f.write(html_template)
        f.close()