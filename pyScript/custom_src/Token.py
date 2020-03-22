class Token:
    def __init__(self, ni):
        self.token_holders = [ni]

    def register(self, ni):
        self.token_holders.append(ni)

    def registered(self, ni):
        return ni in self.token_holders