from typing import Optional

class Person:
    def __init__(self, 
                 first_name: str | None = None, 
                 last_name: Optional[str] = None,
                 email: Optional[str] = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def speak(self):
        return 'Persona conversa un tema'
    
    def greet(self):
        return f'Hola, que tal?'