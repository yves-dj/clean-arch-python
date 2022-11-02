from rentomatic.responses import ResponseSuccess

def test_response_succes_is_true():
    assert bool(ResponseSuccess()) is True