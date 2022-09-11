from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from .models import Chat,Group
from asgiref.sync import async_to_sync
class MySyncConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name=self.scope['url_route']['kwargs']['gre']
        print("Group Name",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
            )
       
    def receive(self, text_data=None, bytes_data=None):
        print("Data from Client ...",text_data)
        data=json.loads(text_data)
        message=data['msg']
        group=Group.objects.get(name=self.group_name)
        chat=Chat(content=data['msg'],group=group)  
        chat.save()  
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message':message
            }
        )
    def chat_message(self,event):
        print("Event...",event)
        self.send(text_data=json.dumps({
            'msg':event['message']
        }))       
      
    def websocket_disconnect(self,event):
        print("Web Socket dis Connected..",event)
        raise StopConsumer()
    