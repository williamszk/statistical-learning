class EmailReader(object):
    def __init__(self, client) -> None:
        try:
            self._client = client
        except Exception as e:
            raise e

    def read(self):
        # implement function here
        return "I ran here!"
