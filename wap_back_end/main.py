from flask import Flask, request
from flask_cors import CORS

from wap.domain.model import WorksheetInput


def main():
    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['GET'])
    def get_worksheet_input() -> str:

        json_file = request.get_json()
        worksheet_input = WorksheetInput(json_file)
        return worksheet_input.get_gpt_response()

    app.run(host="0.0.0.0", debug=True, port=8000)


if __name__ == '__main__':
    main()
