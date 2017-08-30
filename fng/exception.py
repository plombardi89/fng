class AppfileNotFound(Exception):
    def __init__(self, msg):
        super(AppfileNotFound, self).__init__(msg)
