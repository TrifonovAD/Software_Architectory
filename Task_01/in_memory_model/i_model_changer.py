from abc import ABC, abstractmethod

class IModelChanger(ABC):
    @abstractmethod
    def NotifyChange(self, sender) -> None:
        pass