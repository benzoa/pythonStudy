frame = []
msg = "abcdefghijklmnopqrstuvwsyz"
size = 4

for i in range(0, len(msg), size):
    frame.append(msg[i:i+size])

print("fragmented: {}".format(frame))
print("assembled: {}".format(''.join(frame)))
