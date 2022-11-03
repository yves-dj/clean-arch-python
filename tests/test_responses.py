from rentomatic.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request
    )
from rentomatic.requests.room_list import RoomListInvalidRequest

SUCCESS_VALUE = {"key": ["value1", "value2"]}
GENERIC_RESPONSE_TYPE = "Response"
GENERIC_RESPONSE_MESSAGE = "This is a response"


def test_response_succes_is_true():
    response = ResponseSuccess(SUCCESS_VALUE)

    assert bool(response) is True

def test_response_failure_is_false():
    response = ResponseFailure(
        GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE
    )

    assert bool(response) is False

def test_response_success_has_type_and_message():
    response = ResponseSuccess(SUCCESS_VALUE)

    assert response.type == ResponseTypes.SUCCESS
    assert response.value == SUCCESS_VALUE

def test_response_failure_has_type_and_message():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE)

    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == GENERIC_RESPONSE_MESSAGE
    assert response.value == {
        "type": GENERIC_RESPONSE_TYPE,
        "message": GENERIC_RESPONSE_MESSAGE
    }

def test_response_failure_initialisation_with_exception():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE, Exception("Just an error message"))

    assert bool(response) == False
    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == "Exception: Just an error message"

def test_response_failure_from_empty_invalid_request():
    response = build_response_from_invalid_request(
        RoomListInvalidRequest()
    )

    assert bool(response) == False
    assert response.type == ResponseTypes.PARAMETERS_ERROR