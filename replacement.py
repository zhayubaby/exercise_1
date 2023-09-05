def replace_even_odd(word):
    global count
    if word == "terrible":
        count += 1
        if count % 2 == 0:
            return "pathetic"
        else:
            return "marvellous"
    return word

count = 0

with open("file_to_read.txt", "r") as file:
    text = file.read()

words = text.split()

new_words = [replace_even_odd(word) for word in words]

new_text = " ".join(new_words)

with open("result.txt", "w") as file:
    file.write(new_text)

total_terrible_count = words.count("terrible")

print(f"Total occurrences of 'terrible': {total_terrible_count}")

print('success!')