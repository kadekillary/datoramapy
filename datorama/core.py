import json
from typing import List, Dict

import requests

from .helpers import to_json, check_response
from .exceptions import BadRequestError


class Datorama:
    """Datorama base class"""

    def __init__(self, token: str):
        self.token: str = token
        self._session = requests.session()
        self._session.headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Authorization": self.token,
            "Accept": "application/json",
        }

        # Default URLs for Datorama API
        self._datorama_urls: Dict[str, str] = {
            "query": "https://api.datorama.com/v1/query",
            "query-batch": "https://api.datorama.com/v1/query-batch",
            "accounts": "https://api.datorama.com/v1/accounts",
            "worskpaces": "https://api.datorama.com/v1/workspaces",
            "data_streams": "https://api.datorama.com/v1/data-streams",
            "time_zones": "https://api.datorama.com/v1/reference/time-zones",
            "currencies": "https://api.datorama.com/v1/reference/currencies",
            "cultures": "https://api.datorama.com/v1/reference/cultures",
            "verticals": "https://api.datorama.com/v1/reference/verticals",
            "data_sources": "https://api.datorama.com/v1/reference/data-sources",
            "languages": "https://api.datorama.com/v1/reference/languages",
        }

    def _handle_response(sef, response):
        content = to_json(response)
        check_response(response)
        return content

    def _dat_get_request(self, url_key: str):
        response = self._session.get(self._datorama_urls[url_key])
        return self._handle_response(response)

    def _dat_put_request(self, url_key: str):
        response = self._session.put(self._datorama_urls[url_key])
        return self._handle_response(response)

    def _dat_post_request(self, url_key: str, data=None):
        response = self._session.post(self._datorama_urls[url_key], data)
        return self._handle_response(response)

    def _dat_delete_request(self, url_key: str):
        response = self._session.delete(self._datorama_urls[url_key])
        return self._handle_response(response)

    def query(self, query: dict) -> dict:
        """
        Datorama's Query API will let you access all your data stored in Datorama.

        Example
        -------
        >>> from datorama import Datorama

        >>> datorama = Datorama("your_api_token")

        >>> query_to_send = {
            "workspaceId": "XXXXX",
            "dateRange": "THIS_MONTH",
            "measurements": [
                {
                    "name": "Data Stream Total Rows"
                }
            ],
            "dimensions": [
                "Data Stream"
            ]
        }

        >>> datorama.query(query_to_send)

        Parameters
        ----------
        query: dict
            request sent to Query API

        Returns
        -------
        content: dict
            data returned from request to Query API
        """
        encoded_query = json.dumps(query)
        response = self._dat_post_request("query", data=encoded_query)
        return response

    def data_stream_process(self, id: int, dates: dict):
        encoded_query = json.dumps(dates)
        response = self._dat_post_parameter_request(
            "data_stream", id, data=encoded_query
        )
        return response

    def workspaces(self, action: str, id: int) -> List[dict]:
        """
        The workspace API allows setup and management of entire workspaces.

        Resources
        ---------
        GET - List Workspaces
        GET - Find Workspace by ID
        PUT - Update Workspace
        DELETE - Delete Workspace
        POST - Create Workspace

        Parameters
        ----------
        action: str
            action to perform on workspace
            * find - find a workspace by id
            * update - update a specific workspace
            * delete - delete a specific workspace
            * list - list all available workspaces
            * create - create a new workspace
        id: int
            unique id of workspace to perform action on
        """
        pass

    def accounts(self, id: int = None) -> List[dict]:
        """
        The account API allows setup and management of new and existing accounts.
        """
        #  if id != None:
        pass

    def list_all(self, reference: str) -> List[dict]:
        """
        Reference entities are static lists of objects commonly referenced by ID from other Datorama entities.

        Parameters
        ----------
        reference: str
            defines what reference to list
            * time_zones - list all time zones
            * currencies - list all currencies
            * cultures - list ID, name and country code
            * verticals - list all company verticals
            * data_sources - list all data sources by ID
            * languages - list all languages

        Returns
        -------
        response: List[dict]
            List of dictionaries containing ID and name for the resource.
            """ """
        """
        # response = self._dat_get_request(reference)
        # return response
        pass
