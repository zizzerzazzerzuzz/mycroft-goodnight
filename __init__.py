from mycroft import MycroftSkill, intent_file_handler


class Goodnight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('goodnight.intent')
    def handle_goodnight(self, message):
        self.speak_dialog('goodnight')

    @intent_file_handler('goodmorning.intent')
    def handle_goodmorning(self, message):
        self.speak_dialog('goodmorning')

def create_skill():
    return Goodnight()

