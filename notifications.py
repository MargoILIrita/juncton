from pyfcm import FCMNotification


def send_fb_notification():
    push_service = FCMNotification(
        api_key="AAAASELmqzE:APA91bGzkk5N01gT8n77Emt9ZxOSrUlmG5mHzD9CC2zh-inHAJFdPIN-z-kTWWr1EetZdJAv4FHXtfcK5glqbMQ5pHLC8rSU-5A53_QhbWnwTr95oEU5tB5j6UipNPoONBy91-0NpBp5")
    registration_id = "cphufI6iLA8:APA91bENm-un2h71oq5FMDBdQ6YJ1yZRAIF3Ezn1rIZnOuPBmA2vw2W4BPJYifgV8T1gfZN8yLjYHSIxypGBhnJxZnmvB6FyoWUqnqRzOQaG9mvCnR3y6eO-LYWgrwAydnDUPiLmtJTV"
    message_title = "Congratulations"
    message_body = "You have reached new destination"
    push_service.notify_single_device(registration_id=registration_id,
                                               message_title=message_title,
                                               message_body=message_body)


