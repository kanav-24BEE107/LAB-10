
print("Name : Kanav ShahPatel , Roll No.: 24BEE107")
def copy_and_convert(file_source, file_destination):
    try:
        with open(file_source, 'r') as source_file:
            with open(file_destination, 'w') as destination_file:
                for line in source_file:
                    destination_file.write(line.upper())
        print(f"File copied and converted successfully to '{file_destination}'.")
    except FileNotFoundError:
        print(f"Source file '{file_source}' not found.")

# Define the source and destination file paths
file_source = 'source.txt'
file_destination = 'destination.txt'

# Call the function
copy_and_convert(file_source, file_destination)
