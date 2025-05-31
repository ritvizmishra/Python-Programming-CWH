# Censoring the text:

with open("Censor/blog.txt", "r", encoding="utf-8") as file:
    content = file.read().lower()
    
censoredBlog = content.replace('donkey', '####')

with open("Censor/blog.txt", "w") as text:
    text.write(censoredBlog)