import json
import requests


class WorksheetInput:
    context: str
    level: str
    question_type: str
    number_of_questions: int

    def __init__(self, worksheet_input):
        self.context = worksheet_input["context"]
        self.level = worksheet_input["level"]
        self.question_type = worksheet_input["type"]
        self.number_of_questions = worksheet_input["numberOfQuestions"]

    def get_gpt_response(self):
        response = requests.get("URL")
        response_dict = json.loads(response.text)

    def output_json(self) -> str:
        content = {"sentence": self.sentence}
        json_string = json.dumps(content)
        return json_string






