from enum import Enum

class EngineType(Enum):
    DIESEL = 'diesel'
    GASOLINE = 'gasoline'
    
    

class Engine:
    
    def __init__(self, cylinder: float = 0.00, engine_type: EngineType = None):
        self.cylinder = cylinder
        self.engine_type = engine_type