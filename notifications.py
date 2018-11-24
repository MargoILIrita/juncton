from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAASELmqzE:APA91bGzkk5N01gT8n77Emt9ZxOSrUlmG5mHzD9CC2zh-inHAJFdPIN-z-kTWWr1EetZdJAv4FHXtfcK5glqbMQ5pHLC8rSU-5A53_QhbWnwTr95oEU5tB5j6UipNPoONBy91-0NpBp5")
registration_id = "cphufI6iLA8:APA91bENm-un2h71oq5FMDBdQ6YJ1yZRAIF3Ezn1rIZnOuPBmA2vw2W4BPJYifgV8T1gfZN8yLjYHSIxypGBhnJxZnmvB6FyoWUqnqRzOQaG9mvCnR3y6eO-LYWgrwAydnDUPiLmtJTV"
#registration_id = "1:310360058673:android:c2ae6370c8295209"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# # Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print(result)