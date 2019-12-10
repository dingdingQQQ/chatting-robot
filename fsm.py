from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose(self, event):
        text = event.message.text
        return text.lower() == "start"

    #def is_going_to_choose(self, event):
    #    text = event.message.text
    #    return text.lower() == "hello"

    def on_enter_choose(self, event):
        print("I'm entering choose")
        ###
        message = TemplateSendMessage(
            alt_text='妹妹不開心要怎麼辦？',
            template=ButtonsTemplate(
                #thumbnail_image_url='https://example.com/image.jpg',
                title='Question',
                text='妹妹不開心要怎麼辦？',
                actions=[
                    MessageTemplateAction(
                        label='message',
                        text='帶她去吃甜點'
                    ),
                    '''
                    MessageTemplateAction(
                        label='message',
                        text='帶她去遊樂園玩'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='帶她去買東西'
                    )
                    '''
                ]
            )
        )
        reply_token = event.reply_token
        send_text_message(reply_token, message)
        
        ###
        #reply_token = event.reply_token
        #send_text_message(reply_token, "妹妹不開心要怎麼辦？\n1.帶她去吃甜點\n2.帶她去遊樂園玩\n3.帶她去買東西")
        #self.go_back()
    
    def on_exit_choose(self):
        print("Leaving choose")

    def is_going_to_wellbehave(self, event):
        return text.lower() == "帶她去吃甜點"

    def on_enter_wellbehave(self, event):
        print("I'm entering wellbehave")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger wellbehave")
        self.go_back()

    def on_exit_wellbehave(self):
        print("Leaving wellbehave")

    def is_going_to_cute(self, event):
        return text.lower() == "帶她去遊樂園玩"

    def on_enter_cute(self, event):
        print("I'm entering cute")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger cute")
        self.go_back()
    
    def on_exit_cute(self):
        print("Leaving cute")
