def send_messages(messages,sent_messages):
    while messages:
        sending = messages.pop()
        print("sending message:" + sending)
        sent_messages.append(sending)


messages = ['hello world', 'i love python','this is a message']
sent_messages = []
print(messages)
print(sent_messages) 

send_messages(messages[:],sent_messages) 
#the[:] makes the copy of list instead of moving the original items
print(messages)
print(sent_messages) 
