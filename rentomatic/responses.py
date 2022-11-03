class ResponseTypes:
    SUCCESS = "Success"
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"



class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True

class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = message

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(
                msg.__class__.__name__, "{}".format(msg)
            )
        return msg



def build_response_from_invalid_request(invalid_request):
    message = "\n".join(
        [
            "{}: {}".format(err["parameter"], err["message"])
            for err in invalid_request.errors
        ]
    )
    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)