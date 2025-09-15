from flask import Flask, jsonify, request,render_template
import config as config
from project_app.utils import Campaign_Effectiveness

app = Flask(__name__)


######### Homepage ###############

@app.route('/')
def car_price_model():
    print('Digital Marketing Campaign Result Prediction')
    return render_template('test.html')

######## Model API #################

@app.route('/predict',methods = ["GET","POST"])
def get_model_results():
    if request.method == "POST":
        print('We are in the POST Method')
        data = request.form
        age = eval(data['age'])
        gender = data['gender']
        income = eval(data['income'])
        channel = data['channel']
        ctype = data['ctype']
        adspend = eval(data['adspend'])
        ctr = eval(data['ctr'])/100
        convRate = eval(data['convRate'])/100
        visits = eval(data['visits'])
        ppv = eval(data['ppv'])
        time = eval(data['time'])
        shares = eval(data['shares'])
        emailOpens = eval(data['emailOpens'])
        emailClicks = eval(data['emailClicks'])
        prevPurchases = eval(data['prevPurchases'])
        loyalty = eval(data['loyalty'])

        print(gender)

        result = Campaign_Effectiveness(age,gender,income,channel,ctype,adspend,ctr,convRate,visits,ppv,time,shares,emailOpens,
                                                 emailClicks,prevPurchases,loyalty)
        pred = result.campaign_result()
        return render_template("test.html", prediction=str(pred))
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=config.PORT,debug=True)