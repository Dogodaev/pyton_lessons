characters = 'wasitar'

output=''
lenght = len(characters)
i=0
while i< lenght:
    output = output + characters[i]
    i = i+1

lenght = lenght * -1
i = -2
while i>= lenght:
    output = output + characters[i]
    i = i -1

print(output)
