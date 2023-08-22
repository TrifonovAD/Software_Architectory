from Task_01.model_elements.flash import Flash
from Task_01.model_elements.poligonal_model import PoligonalModel
from Task_01.stuff.type import Type


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash) -> None:
        self.id = id
        self.models = models
        self.flashes = flashes

def method1(self, arg1: Type) -> Type:
    # Логика метода 1
    return

def method2(self, arg1: Type, arg2: Type) -> Type:
    # Логика метода 2
    return