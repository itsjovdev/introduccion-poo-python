class Person:
    def __init__(self, first_name: str = None, last_name: str = None):
        self.firts_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f'Person(first_name={self.firts_name}, last_name={self.last_name})'
        