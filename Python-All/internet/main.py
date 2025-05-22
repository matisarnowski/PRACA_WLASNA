def BuyMe(prefix="Please buy me", what="something nice."):
    print(prefix, what)


BuyMe("Please buy me", "a new car.")
BuyMe(what="a new car.", prefix="Please buy me")
BuyMe("Please")
BuyMe(prefix="Please buy me")
BuyMe(what="something sweet.")

carBrand = "Seat"
carModel = "Ibiza"
carIsAirbagOk = True
carIsPaintingOk = True
carIsMechanicOk = True


def printIsCarDamged(carIsAirbagOk, carIsPaintingOk, carIsMechanicOk):
    return not (carIsAirbagOk and carIsPaintingOk and carIsMechanicOk)


print(printIsCarDamged(carIsAirbagOk, carIsPaintingOk, carIsMechanicOk))
