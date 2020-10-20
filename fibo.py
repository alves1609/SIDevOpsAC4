import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__fibo__)

@app.route('/')
def fibo():
   proximo = 1
   anterior = 0
   limite = 50
   f = 0
   resposta = "0,"
   while (f < limite):
       t = proximo
       proximo = proximo + anterior
       anterior = t
       f=f+1
       resposta+= str(proximo) + ","


   return resposta

if __fibo__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
