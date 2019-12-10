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
        '''
        message = TemplateSendMessage(
            alt_text='手機才看得到哦!',
            template=ButtonsTemplate(
                thumbnail_image_url= 'https://scontent-bru2-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s750x750/71116056_526709801498282_8687347445923093354_n.jpg?_nc_ht=scontent-bru2-1.cdninstagram.com&_nc_cat=102&oh=bfc7418c3041d769e52f6aa357c76a16&oe=5E83F8D8&ig_cache_key=MjE1Mjg0ODYyNzkyNDIwNTc3MA%3D%3D.2',
                title='Question',
                text='妹妹不開心要怎麼辦？',
                actions=[
                    
                    MessageTemplateAction(
                        label='message',
                        text='帶她去吃甜點'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='帶她去遊樂園玩'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='帶她去買東西'
                    )
                    
                ]
            )
        )
        '''
        #reply_token = event.reply_token
        #send_text_message(reply_token, message)
        #line_bot_api.reply_message(event.reply_token, message)
        
        ###
        reply_token = event.reply_token
        send_text_message(reply_token, "妹妹不開心要怎麼辦？\n1.帶她去吃甜點(sweet)\n2.帶她去遊樂園玩(play)\n3.帶她去買東西(buy)")
        #self.go_back()
    '''
    def on_exit_choose(self):
        print("Leaving choose")
    '''

    def is_going_to_wellbehave(self, event):
        text = event.message.text
        #return text.lower() == "帶她去吃甜點"
        return text.lower() == "sweet" or text.lower() == "clarify"

    def is_going_to_cute(self, event):
        text = event.message.text
        return text.lower() == "play"

    def on_enter_wellbehave(self, event):
        print("I'm entering wellbehave")

        reply_token = event.reply_token
        send_text_message(reply_token, "養成乖巧的妹妹>w<")
        self.go_back()

    def on_exit_wellbehave(self):
        print("Leaving wellbehave")

    def on_enter_cute(self, event):
        print("I'm entering cute")

        reply_token = event.reply_token
        send_text_message(reply_token, "養成可愛的妹妹>w<")
        self.go_back()
    
    def on_exit_cute(self):
        print("Leaving cute")

    def is_going_to_princess(self, event):
        text = event.message.text
        return text.lower() == "buy"

    def on_enter_princess(self, event):
        print("I'm entering princess")

        reply_token = event.reply_token
        send_text_message(reply_token, "妹妹在學校和別人打架，你會？\n1.去學校揍那個人(fight)\n2.責怪妹妹(blame)\n3.釐清事情真相(clarify)")
    
    def on_exit_princess(self):
        print("Leaving princess")

    def is_going_to_bad(self, event):
        text = event.message.text
        return text.lower() == "blame"

    def on_enter_bad(self, event):
        print("I'm entering bad")

        reply_token = event.reply_token
        send_text_message(reply_token, "養成脾氣不好的妹妹:(")
        self.go_back()
    
    def on_exit_bad(self):
        print("Leaving bad")

    def is_going_to_princessfinish(self, event):
        text = event.message.text
        return text.lower() == "fight"

    def on_enter_princessfinish(self, event):
        print("I'm entering princessfinish")

        reply_token = event.reply_token
        send_text_message(reply_token, "養成公主病妹妹:(")
        self.go_back()
    
    def on_exit_princessfinish(self):
        print("Leaving princessfinish")