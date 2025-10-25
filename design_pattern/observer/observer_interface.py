from abc import ABC, abstractmethod

class FitnessDataObserver:
    @abstractmethod
    def update(self, data) -> None:
        pass

    