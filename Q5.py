print("Name : Kanav ShahPatel , Roll No.: 24BEE107")

# Define file paths
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_path = 'merged.txt'

# Open the files
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_path, 'w') as output:
    # Read lines from both files
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    # Find the maximum length
    max_len = max(len(lines1), len(lines2))

    # Merge lines alternatively
    for i in range(max_len):
        if i < len(lines1):
            output.write(lines1[i])
        if i < len(lines2):
            output.write(lines2[i])

print("Files merged successfully into", output_path)
