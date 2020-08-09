sent = "merhabalar arabalar"
new_sent = {}
for i in sent:
    if i in new_sent:
        new_sent[i] += 1
    else:
        new_sent[i] = 1
print(new_sent)