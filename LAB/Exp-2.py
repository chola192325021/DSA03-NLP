#exp-2

def ends_with_ab(string):
    state = "q0"

    for ch in string:
        if state == "q0" and ch ==  'a':
                state = "q1"
        elif state == "q0" and ch == 'b':
                state = "q0"
        elif state == "q1" and ch == 'a':
                state = "q1"
        elif state == "q1" and ch == 'b':
                state = "q2"
        elif state == "q2" and ch == 'a':
                state = "q1"
        elif state == "q2" and ch == 'b':
                state = "q0"

    return state == "q2"


# Input
text = input("Enter a string: ")

# Output
if ends_with_ab(text):
    print("Accepted: String ends with 'ab'")
else:
    print("Rejected: String does not end with 'ab'")
