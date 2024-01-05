from flask import Flask, jsonify,request
import requests

app = Flask(__name__)

class ResponseModel:
    def __init__(self, message = None, result_data = [], status = True):
        self.Message = message
        self.ResultData = result_data
        self.Status = status


@app.route("/Sms/SendOTP",methods = ['POST'])
def SendOTP():
    try:
        inputdata = request.json

        url = "http://182.18.163.39/v3/api.php"
        params = {
            "username": "Perennial",
            "apikey": "94561054cafdaf42a806",
            "senderid": "PERNAl",
            "mobile": inputdata['mobile'],
            "message": f"Dear {inputdata['name']} Your login OTP is {inputdata['otp']}. PERENNIAL CODE"
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            result = eval(response.text)
            if 'campid' in result:
                response = ResponseModel(message='succ', result_data=result, status=True)
                return jsonify(response.__dict__)
            else:
                response = ResponseModel(message=result.get('Error'), result_data=[], status=False)
                return jsonify(response.__dict__)
        else:
            response = ResponseModel(message='Something went wrong,please try again', result_data=[], status=False)
            return jsonify(response.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)





if __name__ == '__main__':
    app.run()
