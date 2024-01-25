# enc_pyramid
Pyramid Encryptor

Function _decode_ takes the _filename_ as an input and read all it content (readlines). A variable is set (_decoded_message_) where the encrypted message will be encoded and an empty array (_pyramid_). A for cycle is initialized in which I read the lines variable previously set where I split all the lines and append each word to a number inside of the empty _pyramid array_.
The function decodes the message and append words from the sorted pyramid (sort key lambda) and removes trailing spaces (strip).
