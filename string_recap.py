message = "Hello World"
# message = 'Rokib\'s World'

message2 = '''Boby's World was a good cartoon
in 1990's'''

# print(len(message))
# print(message[0:5])
# print(message[:5])
# print(message.lower())
# print(message.upper())
# print(message.count("Hello"))
# print(message.count("l"))
# print(message.find("World"))
print(message.find("d"))

# new_message = message.replace("World", "Universe")
# print(new_message)

msg = "Hello"
name = "Michel"
# message_contact = msg + " " + name
message_format = "{}, {}. Welcome".format(msg,name)

new_format = f'{msg} {name.upper()} Welcome!'
# print(dir(new_format))
print(help(str.lower))