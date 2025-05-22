import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Początek programu")


def factorial(n):
    logging.debug("Początek wywołania funkcji factorial (%s)" % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug(
            " i wynosi " + str(i) + ", wartość całkowita wynosi " + str(total)
        )
    logging.debug("Koniec wywołania funkcji factorial (%s)" % (n))
    return total


print(factorial(5))
logging.debug("Koniec programu")
