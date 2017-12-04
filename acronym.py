class Acronym:
    def __init__(self,name,definition):
        self.name = name
        self.definition = definition


    def toJSON(self):
        return {"Acronym": {'name': self.name, 'definition': self.definition}}