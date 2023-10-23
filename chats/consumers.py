import json
from asgiref.sync import async_to_sync
from .models import *

#from channels.auth import AuthMiddleware
from channels.generic.websocket import WebsocketConsumer


class MyConsumer(WebsocketConsumer):
    def connect(self):
        print("connected..")
        my_id = self.scope['user'].id
        other_id=self.scope['url_route']['kwargs']['id']
        if int(my_id) > int(other_id):
            self.room_name = f'{my_id}-{other_id}'
        else:
            self.room_name = f'{other_id}-{my_id}'
        self.group_name = 'chat_%s' % self.room_name 

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
         )
        self.accept()
      

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']

        self.save_message(username, self.group_name, message, receiver)

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
              {
                'type':'chat.message',
                'message': message,
                'username': username,
              }
            )
        
    def chat_message(self,event): 
        message = event['message']
        username = event['username']
        self.send(
            text_data=json.dumps({
            'message': message,
            'username': username,
            })
        )

        

    def disconnect(self, close_code):
        self.close()
     

    
    def save_message(self, username, thread_name, message, receiver):
        chat_obj = ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name) 
