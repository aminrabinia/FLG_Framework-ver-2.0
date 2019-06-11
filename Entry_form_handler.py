# @amin_rabinia
# functions below receive the data from data entry form and store in json db

import json
from flask import Flask, render_template, request

app = Flask(__name__)

my_list=[[]]

@app.route('/', methods=['Get'])
def index():
    result={}
    return render_template('index.html',result=result)

@app.route('/result', methods=['POST', 'GET'])
def result():
    mini_list = []
    if request.method == 'POST':
        result= request.form        # receive data from entry form
        for key, value in result.items():
            mini_list.append(value)     # put data in temp list

    stor_in_JSON(mini_list)
    mini_list.append(str(int(mini_list[1])+1))  # generate next element ID
    my_list.append(mini_list)   # store data in total list

    return render_template("index.html", result=my_list)    # send list to entry form


def stor_in_JSON(data):
    jobj={"actor": str(data[0]),"id":str(data[1]),"name":str(data[2]),"type":str(data[3]),"decomp":str(data[4]),"parent":str(data[5])}
    with open("data.json", "a+") as jf:
        jdata=json.dumps(jobj, indent=True)
        jf.write(jdata)
        jf.write(',\n')
    print("stored one entity in db!")

if __name__ == '__main__':
    app.run(debug=True)
