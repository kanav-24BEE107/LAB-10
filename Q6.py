print("Name : Kanav ShahPatel , Roll No.: 24BEE107")


with open('text_file.txt', 'r') as src_file:
    with open('destination_file.txt', 'w') as dst_file:
        for line in src_file:
            words = line.split()
            for i, word in enumerate(words):
                if word.lower() in ['a', 'the', 'an']:
                    words[i] = ''
            dst_file.write(' '.join(words)+'\n')

print("Done")
