import json

class PersonaService:

    def __init__(self):
        with open("data/personas.json") as f:
            self.personas=json.load(f)

    def get_persona(self,user_id):
        return self.personas.get(user_id,"RETURNING")

persona_service=PersonaService()