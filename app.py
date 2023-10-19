
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            mdvp_fo=float(request.form['aa'])
            mdvp_fhi=float(request.form['bb'])
            mdvp_flo=float(request.form['cc'])
            mdvp_jitper=float(request.form['dd'])
            mdvp_jitabs=float(request.form['ee'])
            mdvp_rap=float(request.form['ff'])
            mdvp_ppq=float(request.form['gg'])
            jitter_ddp=float(request.form['hh'])
            mdvp_shim=float(request.form['ii'])
            mdvp_shim_db=float(request.form['jj'])
            shimm_apq3=float(request.form['kk'])
            shimm_apq5=float(request.form['ll'])
            mdvp_apq=float(request.form['mm'])
            shimm_dda=float(request.form['nn'])
            nhr=float(request.form['oo'])
            hnr=float(request.form['pp'])
            rpde=float(request.form['qq'])
            dfa=float(request.form['rr'])
            spread1=float(request.form['ss'])
            spread2=float(request.form['tt'])
            d2=float(request.form['uu'])
            ppe=float(request.form['vv'])
            
            filename = 'modelForPrediction.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            scaler = pickle.load(open('standardScalar.sav', 'rb'))
            prediction=loaded_model.predict(scaler.transform([[mdvp_fo,mdvp_fhi,mdvp_flo,mdvp_jitper, mdvp_jitabs,
                mdvp_rap,mdvp_ppq, jitter_ddp, mdvp_shim, mdvp_shim_db,shimm_apq3,shimm_apq5,mdvp_apq,shimm_dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]]))
            print('prediction is', prediction)
            if prediction == 1:
                pred = "You have Parkinson's Disease. Please consult a specialist."
            else:
                pred = "You are Healthy Person."
            # showing the prediction results in a UI
            return render_template('results.html',prediction=pred)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app