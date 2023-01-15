from dotenv import dotenv_values
from flask import Flask, request
from flask_cors import CORS
import logging

from wap.domain.model import WorksheetGenerator


def main():
    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['PUT'])
    def get_worksheet_input() -> str:
        # json_file = request.get_json()
        json_file = {
          "context": "At the Battle of Hastings on October 14, 1066, King Harold II of England was defeated by the invading Norman forces of William the Conqueror. By the end of the bloody, all-day battle, Harold was dead and his forces were destroyed. Harold was the last Anglo-Saxon king of England, and the battle changed the course of history and established the French-speaking Normans as the new rulers of England, which in turn brought about a significant cultural, economic and military transformation, and helped to create the modern English language.\nWilliam the Conqueror\n\nWilliam the Conqueror was the son of Robert I, duke of Normandy in northern France, and his mistress Herleva (also called Arlette), a tanner’s daughter from Falaise. The duke, who had no other sons, designated William his heir, and with his death in 1035 William became duke of Normandy.\n\nDid you know? William, an Old French name composed of Germanic elements (“wil,” meaning desire, and “helm,” meaning protection), was introduced to England by William the Conqueror and quickly became extremely popular. By the 13th century, it was the most common given name among English men.\n\nWilliam was of Viking origin. He spoke a dialect of French and grew up in Normandy, a fiefdom loyal to the French kingdom, but he and other Normans descended from Scandinavian invaders. One of William’s relatives, Rollo, pillaged northern France with Viking raiders in the late ninth and early 10th centuries, eventually accepting his own territory (Normandy, named for the Norsemen who controlled it) in exchange for peace.",
          "level": "gcse",
          "type": "factual",
          "numberOfQuestions": 3
        }
        worksheet_input = WorksheetGenerator(json_file)
        worksheet_input.get_questions_and_answers()
        output = worksheet_input.output_json()
        return output

    app.run(host="0.0.0.0", debug=True, port=9000)


if __name__ == '__main__':
    main()
