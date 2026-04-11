import codecs
files = ['en/index.html', 'en/landingpage2.html']

replacements = [
    ('href="/brasserie', 'href="../brasserie'),
    ('src="/brasserie', 'src="../brasserie'),
    ('href="/solar', 'href="../solar'),
    ('src="/lumina', 'src="../lumina'),
    ('href="/ledgerly', 'href="../ledgerly'),
    ('src="/ledgerly', 'src="../ledgerly'),
    ('href="/favicon', 'href="../favicon')
]

for filepath in files:
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

print('Paths fixed.')
