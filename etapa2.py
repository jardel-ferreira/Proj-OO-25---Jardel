from abc import ABC, abstractmethod

# Classe abstrata
class RouteStrategy(ABC):
    @abstractmethod
    def calculateRoute(self, map_data):
        pass

# Estratégias concretas
class ShorterStrategy(RouteStrategy):
    def calculateRoute(self, map_data):
        return f"Calculando rota mais curta em {map_data}"

class FasterStrategy(RouteStrategy):
    def calculateRoute(self, map_data):
        return f"Calculando rota mais rápida em {map_data}"

class CheaperStrategy(RouteStrategy):
    def calculateRoute(self, map_data):
        return f"Calculando rota mais barata em {map_data}"

class EcoStrategy(RouteStrategy):
    def calculateRoute(self, map_data):
        return f"Calculando rota mais ecológica em {map_data}"

# Classe que usa a estratégia
class MyWay:
    def __init__(self, strategy: RouteStrategy):
        self.method = strategy

    def calculate(self, map_data):
        return self.method.calculateRoute(map_data)


def main():
    
    choose = input("Qual tipo de rota? (rapida)/(curta)/(eco)/(economica): ")
    if choose == "economica":
        rota = MyWay(CheaperStrategy())
        resultado = rota.calculate("mapa X")
        print(resultado)
    elif choose == "eco":
        rota = MyWay(EcoStrategy())
        resultado = rota.calculate("mapa X")
        print(resultado)
    elif choose == "curta":
        rota = MyWay(ShorterStrategy())
        resultado = rota.calculate("mapa X")
        print(resultado)
    elif choose == "rapida":
        rota = MyWay(FasterStrategy())
        resultado = rota.calculate("mapa X")
        print(resultado)
        


if __name__ == "__main__":
    main()

