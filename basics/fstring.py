scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    #print("Hello {0[0]}. Your score is {0[1]}.".format(person))
    # Using F-string
    print(f'Hello {person[0]}. Your score is {person[1]:04}')