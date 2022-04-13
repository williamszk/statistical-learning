class EmailClient(object):
    def __init__(self, config) -> None:
        self._config = config
        self.connect(self._config)

    def connect(self, config):
        # implement function here
        pass
