sentence = input("Write a sentence: ")

output = {}
for n in sentence:
    keys = output.keys()
    if n in keys:
        output[n] += 1
    else:
        output[n] = 1
print(output)