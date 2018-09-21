import gin


@gin.configurable
class Backup:

    def __init__(self, save_as_json=True, save_as_txt=True):
        self.save_as_json = save_as_json
        self.saves_as_txt = save_as_txt

    def save(self):
        pass
