# !/usr/bin/env/python3
# Copyright (c) Facebook, Inc. and its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import uuid
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input_text", help="Input text", type=str, required=True)
parser.add_argument("--result_file", help="Path to result file", default="bert_v2.json", type=str)
args = vars(parser.parse_args())

request = {
  "id": str(uuid.uuid4()),
  "inputs": [{
    "name": str(uuid.uuid4()),
    "shape": -1,
    "datatype": "BYTES",
    "data": args["input_text"]
  }]
}

result_file = args["result_file"]
print("Generating input file: ", result_file)
with open(result_file, "w") as outfile:
    json.dump(request, outfile, indent=4)
