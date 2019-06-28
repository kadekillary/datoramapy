def to_json(response):
    """" Convert response to JSON """
    return json.loads(response.content.decode("utf-8"))


def check_response(response):
    """ Check whether query failed """
    if response.status_code != 200:
        err = to_json(response)
        raise BadRequestError(err)
