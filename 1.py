for first_char in range(ord('a'), ord('z') + 1):
    for second_char in range(ord('a'), ord('z') + 1):
        for third_char in range(ord('a'), ord('z') + 1):
            for fourth_char in range(ord('a'), ord('z') + 1):
                combination = chr(first_char) + chr(second_char) + chr(third_char) + chr(fourth_char)
                print(combination)

