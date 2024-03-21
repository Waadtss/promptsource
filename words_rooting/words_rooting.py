# coding=utf-8
# Copyright 2020 HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
import pandas as pd

import datasets


_DESCRIPTION = """\
words_rooting
"""
_HOMEPAGE_URL = ""
_CITATION = """\

"""

_TRAIN_URL = "C:\\Users\\aalmazrua\\Documents\\مؤشر النضج\\dataset\\words_rooting.csv"


class WordsRooting(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.0.0")

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "_id": datasets.Value("string"),
                    "lemma": datasets.Value("string"),
                    "root": datasets.Value("string"),
                    
                },
            ),
            supervised_keys=None,
            homepage=_HOMEPAGE_URL,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        train_path = _TRAIN_URL
        # valid_path = dl_manager.download_and_extract(_VALID_URL)
        # test_path = dl_manager.download_and_extract(_TEST_URL)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={"datapath": train_path, "datatype": "train"},
            ),
            # datasets.SplitGenerator(
            #     name=datasets.Split.VALIDATION,
            #     gen_kwargs={"datapath": valid_path, "datatype": "valid"},
            # ),
            # datasets.SplitGenerator(
            #     name=datasets.Split.TEST,
            #     gen_kwargs={"datapath": test_path, "datatype": "test"},
            # ),
        ]

    def _generate_examples(self, datapath, datatype):
        
        data = pd.read_csv(datapath)

        for index, d in data.iterrows():
            resp = {
                "_id": d["_id"],
                "lemma": d["lemma"],
                "root":d["root"],
            }

            yield index, resp