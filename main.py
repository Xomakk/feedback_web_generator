import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from utils import generating_template

load_dotenv()

giga = GigaChat(credentials=os.getenv('AUTH_KEY'), scope="GIGACHAT_API_PERS")
app = Flask(__name__)

messages = [
    SystemMessage(
        content=generating_template
    )
]

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        creteries = request.form.get('creteries')
        course_name = request.form.get('course_name')

        messages.append(
            HumanMessage(
                content='\n'.join([
                    'ключевые слова: {}'.format(creteries),
                    'имя ученика: {}'.format(name),
                    'предмет: {}'.format(course_name),
                ])
            )
        )
        response = giga(messages)
        messages.append(response)
        return render_template('index.html', feedback=response.content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)