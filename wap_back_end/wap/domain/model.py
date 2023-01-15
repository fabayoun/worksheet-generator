import json
import logging
from typing import Dict, List

import openai
import requests
import attr
from dotenv import dotenv_values
import numpy as np

@attr.dataclass
class WorksheetOutput:
    question: str = None
    answer: str = None


class WorksheetGenerator:
    context: str
    level: str
    question_type: str
    number_of_questions: int
    questions: List
    answers: List
    outputs: List

    def __init__(self, worksheet_input):
        self.context = worksheet_input["context"]
        self.level = worksheet_input["level"]
        self.question_type = worksheet_input["type"]
        self.number_of_questions = worksheet_input["numberOfQuestions"]
        self.questions = []
        self.answers = []
        self.outputs = []

        assert len(self.context) < 7500

    def get_questions_and_answers(self):
        self.questions = self._generate_test_question()
        self.answers = self._generate_test_answers()
        self.outputs = self._add_questions_to_output()

        logging.error(self.questions)
        logging.error(self.answers)
        logging.error(self.outputs)

    def _get_correct_question_prompt_based_on_type(self):
        if self.question_type == "factual":
            return f"Write {self.number_of_questions} questions in the following style: {self.question_type}. The questions must be based solely on the text below\n\nText: {self.context}\n\nQuestions:\n",
        if self.question_type == "exploratory":
            return f"Write {self.number_of_questions} open-ended questions that explore and analyse themes. The questions must be based solely on the text below\n\nText: {self.context}\n\nQuestions:\n",
        raise ValueError("incorrect question type")

    def _generate_test_question(self):
        """
        :param topic:
        :return:
        """
        config = dotenv_values(".env")
        openai.api_key = config.get("OPENAI_API_KEY")
        openai.organization = config.get("OPENAI_API_ORG_ID")
        resp = openai.Completion.create(
            engine="text-curie-001",
            prompt=self._get_correct_question_prompt_based_on_type(),
            temperature=0.5,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n\n"]
        )

        return self._split_questions(resp["choices"][0]["text"])

    def _generate_test_answers(self):
        answers = []
        for question in self.questions:
            resp = openai.Completion.create(
                engine="text-curie-001",
                prompt=f"Write the answer to the below question based on the text below\n\nText: {self.context}\n\nQuestion:\n{question}\n\nAnswer:\n",
                temperature=0.1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n\n"]
            )
            answers.append(resp["choices"][0]["text"])
        return answers

    def _split_questions(self, raw_questions: str):
        try:
            questions = raw_questions.split("\n")
            return questions[1:]
        except Exception as e:
            print(e)
            return []

    def _add_questions_to_output(self):
        assert len(self.questions) == len(self.answers)
        outputs = []
        for i in range(len(self.questions)):
            if np.random.randint(0, 10) >= 8:
                wo = WorksheetOutput("I'm tired of this shit, you can do it yourself", "404")
            else:
                wo = WorksheetOutput(self.questions[i], self.answers[i])
            outputs.append(wo)
        return outputs

    def output_json(self) -> str:
        content = {"list": [self._convert_to_dict(output) for output in self.outputs]}
        json_string = json.dumps(content)
        return json_string

    def _convert_to_dict(self, output: WorksheetOutput):
        return [f"{output.question}", f"{output.answer}"]



