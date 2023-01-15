import os

import openai
from dotenv import dotenv_values

# config = dotenv_values("wap_back_end/.env")
config = dotenv_values(".env")
openai.api_key = config.get("OPENAI_API_KEY")
openai.organization = config.get("OPENAI_API_ORG_ID")

def generate_test_question(topic: str, num_qa: int) -> str:
    """

    :param topic:
    :return:
    """

    resp = openai.Completion.create(
        engine="text-ada-001",
        prompt=f"Write {num_qa} questions and answers based on the text below\n\nText: {topic}\n\nQuestions:\n\n",
        temperature=0.1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]
    )
    return resp

topic = "World War 1 History GSCE Level"
resp = generate_test_question(topic, 3)

resp["choices"][0]["text"]

def split_questions(resp):
    try:
        questions = resp["choices"][0]["text"].split("\n")
        return questions[1:]
    except Exception as e:
        print(e)
        return []


questions = split_questions(resp)


questions

def get_test_answer(topic: str, question: str):

    resp = openai.Completion.create(
        engine="text-ada-001",
        prompt=f"Write the answer to the below question based on the text below\n\nText: {topic}\n\nQuestion:\n{question}\n\nAnswer:\n",
        temperature=0.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]
    )
    return resp

questions[0]
ans_resp = get_test_answer(topic, questions[0])

ans_resp["choices"][0]["text"]