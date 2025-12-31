import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)

HEADERS = {
    "Content-Type": "text/plain",
    "Access-Control-Allow-Origin": "*",
}


def _to_numbers(op_1, op_2):
    """Convert two operands to numbers using util."""
    return util.convert_to_number(op_1), util.convert_to_number(op_2)


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = _to_numbers(op_1, op_2)
        result = CALCULATOR.add(num_1, num_2)
        return (f"{result}", http.client.OK, HEADERS)
    except TypeError as exc:
        return (str(exc), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/subtract/<op_1>/<op_2>", methods=["GET"])
def subtract(op_1, op_2):
    try:
        num_1, num_2 = _to_numbers(op_1, op_2)
        result = CALCULATOR.subtract(num_1, num_2)
        return (f"{result}", http.client.OK, HEADERS)
    except TypeError as exc:
        return (str(exc), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = _to_numbers(op_1, op_2)
        result = CALCULATOR.multiply(num_1, num_2)
        return (f"{result}", http.client.OK, HEADERS)
    except TypeError as exc:
        return (str(exc), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = _to_numbers(op_1, op_2)

        if num_1 == 0 or num_2 == 0:
            # Requisito: responder 406 "NOT_ACCEPTABLE" en división por cero
            return (
                "Division by zero not allowed",
                http.client.NOT_ACCEPTABLE,
                HEADERS,
            )

        result = CALCULATOR.divide(num_1, num_2)

    
    # Formateo: si es entero exacto -> sin decimales
    try:
        as_float = float(result)
        body = (
            str(int(as_float))
            if as_float.is_integer()
            else str(as_float)
        )
        
        except Exception:
            body = str(result)

        return (body, http.client.OK, HEADERS)

    except ZeroDivisionError:
        # Por si la lógica interna lanza la excepción
        return (
            "Division by zero not allowed",
            http.client.NOT_ACCEPTABLE,
            HEADERS,
        )

    except TypeError as exc:
        # Conversión/entrada inválida
        return (str(exc), http.client.BAD_REQUEST, HEADERS)
