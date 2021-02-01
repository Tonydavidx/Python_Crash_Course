def send_messages(messages, sent_messages):
    while messages:
        sending = messages.pop()
        print("sending message:" + sending)
        sent_messages.append(sending)
