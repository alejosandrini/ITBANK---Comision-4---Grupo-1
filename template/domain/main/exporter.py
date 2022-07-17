class Exporter():
    def generarReporte(cliente):
        f = open(f'.\entradas-salidas\\reporte.html', 'w')
        html_template = """
        <html>
            <head>
                <title>Title</title>
            </head>
            <body>
                <h2>Reporte</h2>
            </body>
        </html>
        """
        f.write(html_template)
        f.close()