class Debug:

    DEBUG = 0
    WARNING = 1
    DEPLOY = 2

class Mode:
    
    ENCODE = 0
    ADD_NOISE = 1
    DECODE = 2

    def __init__(self, mode = None):
        self.decorators = mode

    def __call__(self):
        return 0

class ENCODE(Mode):

    def __call__(self):

        return self.decorators() + 1

class ADD_NOISE(Mode):

    def __call__(self):
        return self.decorators() + 2

class DECODE(Mode):

    def __call__(self):
        return self.decorators() + 4