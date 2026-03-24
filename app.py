from flask import Flask, jsonify, render_template
import os
import socket

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname()
    })
@app.route('/products')
def products():
        products = [
            {"id": 1, "name": "laptop", "price": 50000, "stock": 100},
            {"id": 2, "name": "charger", "price": 1400, "stock": 100},
            {"id": 3, "name": "keyboard","price": 999, "stock": 20},
        ]
        return jsonify({"products": products, "count": len(products)})
if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
  

          
