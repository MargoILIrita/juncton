from pyfcm import FCMNotification


def send_fb_notification():
    push_service = FCMNotification(
        api_key="AAAASELmqzE:APA91bGzkk5N01gT8n77Emt9ZxOSrUlmG5mHzD9CC2zh-inHAJFdPIN-z-kTWWr1EetZdJAv4FHXtfcK5glqbMQ5pHLC8rSU-5A53_QhbWnwTr95oEU5tB5j6UipNPoONBy91-0NpBp5")
    registration_id = "cvDp_dCNhJ0:APA91bEJIH3Fcy_mG0WZ3KsJMY7NIeGt3roRVSN7q1348W9eARx2yfXiJecdHJt6HkTzFWXAk5kzFttOmLQ-vqlFnZd2BnxJmXWQP4l54wWUc0Dc2oOTuGBLL-7ORlaF5fs_xzZg0wEn"
    message_title = "Congratulations"
    message_body = "You have reached new destination"
    data_message = {
        "notification": "true"
    }

    push_service.notify_single_device(registration_id=registration_id,
                                               message_title=message_title,
                                               message_body=message_body,
                                               data_message=data_message)


