from abc import ABC, abstractmethod

class FormElement(ABC):
    
    def __init__(self, name: str):
        self._name:str = name
        self._value:str | None = None
    
    
    def set_value(self, value: str):
        self._value = value
        
    @abstractmethod
    def draw_html(self) -> str:
        pass