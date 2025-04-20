import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.callbacks_post201_response import CallbacksPost201Response  # noqa: E501
from openapi_server.models.healthcheck_get200_response import HealthcheckGet200Response  # noqa: E501
from openapi_server import util


def callbacks_post(callback_url):  # noqa: E501
    """callbacks_post

    subscribes a client to receive out-of-band data # noqa: E501

    :param callback_url: the location where data will be sent.  Must be network accessible by the source server 
    :type callback_url: str

    :rtype: Union[CallbacksPost201Response, Tuple[CallbacksPost201Response, int], Tuple[CallbacksPost201Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def healthcheck_get():  # noqa: E501
    """healthcheck_get

    This endpoint is used to check the health of the API. It should return a 200 OK response if the API is up and running.  # noqa: E501


    :rtype: Union[HealthcheckGet200Response, Tuple[HealthcheckGet200Response, int], Tuple[HealthcheckGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
