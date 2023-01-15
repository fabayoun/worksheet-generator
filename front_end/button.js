const myBtn = document.getElementById("idBtn");

myBtn.addEventListener("click", clickButton)

function clickButton() {

    var context = document.getElementById("context").value;
    var level = obtain_level('level_radio')
    var type = obtain_level('type_radio')
    var no_of_questions = document.getElementById("number_of_questions").value;

    JsonHeaders = {
        'context': context,
        'level': level,
        'type': type,
        'numberOfQuestions': no_of_questions
    };

    console.log(JsonHeaders)

    var json_response = fetch("http://127.0.0.1:5000").then(response =>
        response.text()).then(data => data)

    console.log(data)
}

function obtain_level(element_id_name) {
    var radios = document.getElementById(element_id_name);

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            latest_value = radios[i].value;
            return latest_value;
        }
    }
}

