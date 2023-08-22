from Task_01.in_memory_model.i_model_changer import IModelChanger
from Task_01.in_memory_model.i_model_changer_observer import IModelChangeObserver
from Task_01.model_elements.flash import Flash
from Task_01.model_elements.camera import Camera
from Task_01.model_elements.poligonal_model import PoligonalModel
from Task_01.model_elements.scene import Scene


class ModelStore(IModelChanger):

    def __init__(self,
                 models: PoligonalModel,
                 scenes: Scene,
                 flashes: Flash,
                 cameras: Camera,
                 changeObservers: IModelChangeObserver) -> None:
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.__changeObservers = changeObservers

    def get_scena(arg1: int) -> Scene:
        return 

    def notify_change(arg1: IModelChanger) -> None:
        pass