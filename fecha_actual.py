from datetime import datetime


def formato_fecha(date):
    dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    nom_dias = dias[date.isoweekday() - 1]
    dia = date.day
    mes = meses[date.month - 1]
    year = date.year

    return f"{nom_dias}, {dia} de {mes} de {year}"


hoy = datetime.now()
fecha = formato_fecha(hoy)


if __name__ == '__main__':
    print(f"\nHoy es: {fecha}")