from handlers.langchain_handler import SalesBotChain

class ConversationService:
    def __init__(self):
        self.chain = SalesBotChain()

    def handle_message(self, message):
        response = self.chain.generate(message)
        return response

conversation_service = ConversationService()
