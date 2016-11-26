
class GameRegister():
    """Classe singleton dans lequel le développeur peut enregister les objets qu'il souhaiterais utiliser"""

    class __GameRegister():
        def __init__(self):
            self.registre = {}

        def register(self, type, object):
            try:
                self.registre[type].append(object)
            except:
                self.registre[type] = []
                self.registre[type].append(object)


    singleton = None

    def __new__(cls, *args, **kwargs):
        if(GameRegister.singleton == None):
            GameRegister.singleton = GameRegister.__GameRegister()
        return GameRegister.singleton
