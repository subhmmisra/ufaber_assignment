# Third Party Stuff
import rest_framework.response


class Response(rest_framework.response.Response):
    """The various HTTP responses for use in returning proper HTTP codes.
    """

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ):
        super().__init__(data, status, template_name, headers, exception, content_type)


class Ok(Response):
    """200 OK

    Should be used to indicate nonspecific success. Must not be used to
    communicate errors in the response body.
    In most cases, 200 is the code the client hopes to see. It indicates that
    the REST API successfully carried out whatever action the client requested,
    and that no more specific code in the 2xx series is appropriate. Unlike
    the 204 status code, a 200 response should include a response body.
    """

    status_code = 200


class Created(Response):
    """201 Created

    Must be used to indicate successful resource creation.
    A REST API responds with the 201 status code whenever a collection creates,
    or a store adds, a new resource at the client's request. There may also be
    times when a new resource is created as a result of some controller action,
    in which case 201 would also be an appropriate response.
    """

    status_code = 201
