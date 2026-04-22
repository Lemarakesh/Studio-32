import os

files = [
    r'c:\Projects\dark-landing-page\index.html',
    r'c:\Projects\dark-landing-page\en\index.html'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('studio-32.vercel.app', 'mw-studio.vercel.app')
    content = content.replace('Studio 32', 'MW Studio')
    # Make sure lower case is also replaced
    content = content.replace('studio 32', 'MW Studio')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
