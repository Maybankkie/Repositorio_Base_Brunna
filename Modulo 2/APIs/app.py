from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conta')
def conta():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    n3 = int(request.args.get('valor3',0))
    
    conta = n1 + n2 + n3

    return {

            'numero1': n1,
            'numero2': n2,
            'numero3': n3,
            'soma dos 3 numeros': conta
         }

if __name__ =='__main__':
    app.run(debug=True)