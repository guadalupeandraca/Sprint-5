from cliente import Cliente 

class ProcesadorHtml:    
    def __init__(self) -> None:
        self.elementos =[]

    def append(self, elemento:dict):
        self.elementos.append(elemento)

    def crear_html(self,cliente: Cliente):
        transacciones = ""
        for e in self.elementos:
            transacciones += "<tr><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td></tr>".format(
            fecha = e["fecha"],
            tipo = e["tipo"].replace("_","_"),
            estado = e["estado"],
            monto = e["monto"],
            razon = e["razon"]
            )
        
        html = """"
            <hmtl>
                <head>   
                    <title>Listado de transacciones</title>
                    <link rel="stylesheet" href="index.css"
                </head> 
                <body>
                    <div class = "conteiner">
                        <h1>{apellido}, {nombre}</h1>
                        <div>DNI: {dni}</div>
                        <div>Direccion: {direccion}</div>
                    </div>
                    <div class = "table-conteiner">
                        <table class="table table-striped">
                            <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
                            {transacciones}
                        </table>
                    </div>
                </body>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
            </hmtl>
        """.fomrat(
                direccion = str[cliente.direccion],
                numero = cliente.numero,
                nombre = cliente.nombre,
                apellido = cliente.apellido,
                dni = cliente.dni,
                transacciones = transacciones
                )

        archivo = open ("index.html","w")
        archivo.write(html)
        archivo.close()



