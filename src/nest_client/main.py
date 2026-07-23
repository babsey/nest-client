# -*- coding: utf-8 -*-
#
# nest_client.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

import requests
from werkzeug.exceptions import BadRequest

__all__ = [
    "NESTClient",
]

default_url = "http://localhost:52425"
default_headers = {"Content-type": "application/json", "Accept": "text/plain"}


def encode(response):
    if response.ok:
        return response.json()
    elif response.status_code == 400:
        raise BadRequest(response.text)


class NESTClient:

    def __init__(
        self,
        url: str = default_url,
        headers: dict = default_headers,
    ):
        self.url = url
        self.headers = {**default_headers, **headers}

    def get(self, path: str, params={}, **kwargs):
        return requests.get(f"{self.url}{path}", params, headers=self.headers, **kwargs)

    def post(self, path: str, data={}, json={}, **kwargs):
        return requests.post(f"{self.url}{path}", data=data, json=json, headers=self.headers, **kwargs)

    def __getattr__(self, call: str):
        def method(*args, **kwargs):
            return self.api_call(call, args, kwargs)

        return method

    def api_call(self, call: str, args: list, kwargs: dict):
        kwargs.update({"args": args})
        response = requests.post(f"{self.url}/api/{call}", json=kwargs, headers=self.headers)
        return encode(response)

    def exec_script(self, source: str, return_vars: str | list[str] = None):
        params = {
            "source": source,
            "return": return_vars,
            "return_vars": return_vars,
        }
        response = requests.post(f"{self.url}/exec", json=params, headers=self.headers)
        return encode(response)

    def from_file(self, filename: str, return_vars: str | list[str] = None):
        with open(filename, "r") as f:
            lines = f.readlines()
        script = "".join(lines)

        print(f"Execute script code of {filename}")
        print(f"Return variables: {return_vars}")
        print(20 * "-")
        print(script)
        print(20 * "-")

        return self.exec_script(script, return_vars)
