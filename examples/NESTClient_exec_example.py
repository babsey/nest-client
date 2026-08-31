# NESTClient_exec_example.py
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

from pathlib import Path

from nest_client import NESTClient

print("Running client exec example using NEST via NEST Server")

# Load NEST client
nest = NESTClient()

n_events = nest.from_file(Path(__file__).parent / "NESTClient_script.py", "n_events")["data"]
print("Number of events:", n_events)
