import datetime 
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import json

if __name__ == "__main__":
    print(5)

    auth_user_name = 'JHeVqedvg1ASX6m3N3hJ'
    auth_password = 'xNINQu4Ao9hnyVUOU52ifWNyiGI0y4'
    use_hmac_authentication = False

    client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)
    messages_client = client.messages

    body_value = '''{
        "messages":[
            {
                "content":"My first message",
                "destination_number":"+642102869292"
            }
        ]
    }'''

    body = json.loads(body_value)

    result = messages_client.send_messages(body)

    print(client.messages)