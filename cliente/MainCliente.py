class MainCliente:

    def __init__(self) -> None:
        pass

    def getDatosClienteClassic():
        return{
            "limite_extraccion_diario" : 10000,
            "limite_transferencia_recibida" : 150000,
            "costo_transferencia" : 0.005,
            "total_tarjetas_credito" : 0,
            "total_chequeras" : 0,
            "saldo_descubierto_disponible": 0
        }

    def getDatosClienteGold():
        return{
            "limite_extraccion_diario" : 20000,
            "limite_transferencia_recibida" : 500000,
            "costo_transferencia" : 0.005,
            "total_tarjetas_credito" : 1,
            "total_chequeras" : 1,
            "saldo_descubierto_disponible": 10000
        }


    def getDatosClienteBlack():
        return{
            "limite_extraccion_diario" : 100000,
            "costo_transferencia" : 0,
            "total_tarjetas_credito" : 5,
            "total_chequeras" : 2,
            "saldo_descubierto_disponible": 100000
        }