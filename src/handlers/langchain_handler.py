from langchain.chains import SimpleChain
from langchain.prompts import SimplePrompt

class SalesBotChain(SimpleChain):
    def __init__(self):
        super().__init__()
        self.prompt = SimplePrompt("You are a helpful sales assistant. {input}")

    def generate(self, input_text):
        return self.prompt.format(input=input_text)

sales_bot_chain = SalesBotChain()
