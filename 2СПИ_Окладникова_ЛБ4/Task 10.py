message = "ППррииввеетт!!  ККаакк  ддееллаа??  ССееггоодднняя  ттааккааяя  ххоорроошшааяя  ппооггооддаа,,  ммоожжеетт  ппооггуулляяеемм??"
corrected_message = ""
i = 0

while i < len(message):
    corrected_message += message[i]
    if i + 1 < len(message) and message[i] == message[i + 1]:
        i += 1
    i += 1

print(corrected_message)