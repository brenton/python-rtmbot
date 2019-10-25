from rtmbot.core import Plugin

class hellowworldPlugin(Plugin):

    def process_message(self, data):
        self.outputs.append(["#bot-dev", "hello world"])
