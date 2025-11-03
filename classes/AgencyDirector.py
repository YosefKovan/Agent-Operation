
class AgencyDirector:

    _instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls, ):
        if not cls._instance:
           AgencyDirector._instance = AgencyDirector("yossi")

        return AgencyDirector._instance



