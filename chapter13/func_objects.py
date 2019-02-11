def get_msg():
    return 'Hello Python World!'

message = get_msg()
print(message)


message = get_msg
print(message)

another_reference = get_msg
print(another_reference())

def get_some_other_msg():
    return 'Some other message!!!'

get_msg = get_some_other_msg
print(get_msg())

print(another_reference())