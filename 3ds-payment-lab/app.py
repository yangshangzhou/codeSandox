from flask import Flask, render_template, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)
transactions = {}
logs = []

def log(msg):
    line = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
    logs.append(line)
    print(line)

@app.get('/')
def index():
    return render_template('payment_demo.html')

@app.get('/bank')
def bank():
    return render_template('bank_app.html')

@app.post('/api/create-payment')
def create_payment():
    data = request.get_json()
    if data.get('card_number') != '4111 1111 1111 1111':
        return jsonify({'error': '仅允许使用实验卡：4111 1111 1111 1111'}), 400
    tx = str(uuid.uuid4())[:8]
    transactions[tx] = {'amount': 1000, 'merchant': 'Demo Shop', 'status': 'requires_action'}
    log(f'Payment created: tx={tx}, USD 1000')
    log('Issuer requires 3DS authentication')
    log(f'Challenge sent to simulated Bank App: tx={tx}')
    return jsonify({'transaction_id': tx, 'status': 'requires_action'})

@app.post('/api/challenge')
def challenge():
    data = request.get_json()
    tx, decision = data.get('transaction_id'), data.get('decision')
    if tx not in transactions:
        return jsonify({'error': 'not found'}), 404
    if decision == 'approve':
        transactions[tx]['status'] = 'authorized'
        log(f'User approved challenge: tx={tx}')
        log('Authentication = SUCCESS')
        log('Payment = AUTHORIZED')
    else:
        transactions[tx]['status'] = 'declined'
        log(f'User declined challenge: tx={tx}')
        log('Authentication = FAILED')
        log('Payment = DECLINED')
    return jsonify(transactions[tx])

if __name__ == '__main__':
    log('Demo server started. No real payment network is connected.')
    app.run(host='127.0.0.1', port=5000, debug=False)
