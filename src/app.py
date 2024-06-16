from fastapi import FastAPI
from handlers.openai_handler import generate_response
from services.conversation_service import SalesBotChain

app = FastAPI()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
