from rtmbot.core import Plugin

class helloworldPlugin(Plugin):

    def process_message(self, data):
        self.outputs.append(["#bot-dev", "hello world"])
