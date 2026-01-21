from file_ops import read_file, write_file
from text_utils import word_count, line_count, char_count, to_upper
filename = "sample.txt"

# Read file
text = read_file(filename)

# Process data
words = word_count(text)
lines = line_count(text)
chars = char_count(text)
upper_text = to_upper(text)

# Display output
print("Word Count:", words)
print("Line Count:", lines)
print("Character Count:", chars)

# Save processed text
write_file("output.txt", upper_text)
print("Processed text saved to output.txt")
