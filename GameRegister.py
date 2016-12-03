
class GameRegister():
    """Classe singleton dans lequel le développeur peut enregister les objets qu'il souhaiterais utiliser"""

    class __GameRegister():
        def __init__(self):
            self.registre = {}

        def register(self, type, object, id):
            if (type in self.registre):
                if (id in self.registre[type]):
                    print("[ERROR] ID déjà utilisé")
                else:
                    self.registre[type][id] = object
            else:
                self.registre[type] = {}
                self.registre[type][id] = object

        def get_sprite(self, id):
            return self.registre["sprite"][id]


    singleton = None

    def __new__(cls, *args, **kwargs):
        if(GameRegister.singleton == None):
            GameRegister.singleton = GameRegister.__GameRegister()
        return GameRegister.singleton
