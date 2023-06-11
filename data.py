import requests


def request(cat, num):
    cat_num = 0
    if cat.lower() == 'general knowledge':
        cat_num = 9
    elif cat.lower() == 'computer':
        cat_num = 18
    elif cat.lower() == 'animal':
        cat_num = 27
    elif cat.lower() == 'celebrities':
        cat_num = 26

    parameter = {
        'amount': num,
        'category': cat_num,
        'type': 'boolean'
    }
    response = requests.get(url='https://opentdb.com/api.php', params=parameter)
    response.raise_for_status()

    data = response.json()
    question_data = data['results']
    return question_data
