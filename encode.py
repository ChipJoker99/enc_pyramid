def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    decoded_message = ""
    pyramid = []
    
    for line in lines:
        number, word = line.split()
        pyramid.append((int(number), word))
    
    pyramid.sort(key=lambda x: x[0])
    
    for _, word in pyramid:
        decoded_message += word + " "
    
    return decoded_message.strip()
