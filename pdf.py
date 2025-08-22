import pikepdf

# Open existing PDF
pdf = pikepdf.open("container.pdf")

# Files to embed
files_to_embed = [
    "shell.php",
    "malicious.mp4",
    "poison_image.svg",
    "harmless.txt",
    "mal.csv",
    "zipbomb.py",
    "dangerous_bomb.zip",
    "test.sql"
]

# Attach each file
for f in files_to_embed:
    with open(f, "rb") as file_obj:
        pdf.attachments[f] = file_obj.read()

# Save output
pdf.save("DeadmanXXXII.pdf")
pdf.close()
