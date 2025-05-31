# Censoring a list of words
censoredWords = ['peach', 'head', 'smack', 'cardio', 'do', 'smooth']

with open("Censor/blog_02.txt", "r", encoding="utf-8") as file:
    content = file.read().lower()

censoredBlog = content
    
for text in censoredWords:
    censoredBlog = censoredBlog.replace(text, '#' * len(text))
    
# Why this works now: 
# You're always building on the previous version (censoredBlog), instead of resetting to content every time.
    
with open("Censor/blog_02.txt", "w") as blog:
        blog.write(censoredBlog)
    
