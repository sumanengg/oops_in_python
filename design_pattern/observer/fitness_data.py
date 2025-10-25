from abc import ABC, abstractmethod
from subject_interface import FitnessDataSubject
from observer_interface import FitnessDataObserver
from typing import List

class FitnessData(FitnessDataSubject):
    def __init__(self):
        self._observer: List[FitnessDataObserver] = []
        self._steps = 0
        self._calories_burned = 0.0
        self._distance_covered = 0.0

    def RegisterObserver(self, observer) -> None:
        self._observer.append(observer)

    def RemoveObserver(self, observer) -> None:
        if observer in self._observer:
            self._observer.remove(observer)

    def NotifyObservers(self) -> None:
        for observer in self._observer:
            observer.update(self)

    def set_fitness_data(self, steps: int, calaries_burned: float, distance_covered: float):
        self._steps = steps
        self._calories_burned = calaries_burned
        self._distance_covered = distance_covered
        print(f"FitnessData updated: Steps={steps}, Calories={calaries_burned}, Distance={distance_covered}")
        self.NotifyObservers()

    #getters

    @property
    def step(self) -> int:
        return self._steps
    
    def calories_burned(self):
        return self._calories_burned
    
    def distance_covered(self):
        return self._distance_covered


                       