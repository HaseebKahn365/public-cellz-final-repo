import os
import glob

# Get all md files in current directory
md_files = glob.glob("*.md")

# Create or open the output file
with open("combined_markdown.md", "w", encoding="utf-8") as outfile:
    # Iterate through each md file
    for i, filename in enumerate(md_files):
        with open(filename, "r", encoding="utf-8") as infile:
            # Write the content of each file
            outfile.write(infile.read())
            
            # Add 5 newlines between files (except for the last file)
            if i < len(md_files) - 1:
                outfile.write("\n\n\n\n\n")

print(f"Combined {len(md_files)} markdown files into combined_markdown.md")