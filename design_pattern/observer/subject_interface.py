from abc import ABC, abstractmethod
from observer_interface import FitnessDataObserver

class FitnessDataSubject:

    @abstractmethod
    def RegisterObserver(self, observer: FitnessDataObserver) -> None:
        pass

    @abstractmethod
    def RemoveObserver(self, observer: FitnessDataObserver) -> None:
        pass

    @abstractmethod
    def NotifyObservers(self, observer: FitnessDataObserver) -> None:
        pass