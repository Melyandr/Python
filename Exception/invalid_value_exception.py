class invalidValueException(Exception):
    def __init__(self, error_message="review your vallue"):
        self.error_message = error_message
        