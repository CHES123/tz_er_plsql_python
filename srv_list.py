from flask import Flask, request
from functions import  f_sort_avg


app = Flask(__name__)

@app.errorhandler(404)
def pageNotFount(error):
    return {"error":404}

@app.route('/api/sort_avg/', methods=['GET', 'POST'])
def add_message():
    try:
        content = request.json
        result = f_sort_avg(content['l_data'])
        return {"result_data":result}
    except Exception as e:
        print(e)


#flask --app srv_list --debug  run
#fuser -k 5000/tcp