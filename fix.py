import codecs
with codecs.open('en/index.html', 'r', 'utf-8') as f:
    idx = f.read()
with codecs.open('en/landingpage2.html', 'r', 'utf-8') as f:
    l2 = f.read()

marker = '<section class=\"py-12 border-y border-white/5'
idx_split = idx.split(marker, 1)
l2_split = l2.split(marker, 1)

if len(idx_split) == 2 and len(l2_split) == 2:
    new_l2 = l2_split[0] + marker + idx_split[1]
    with codecs.open('en/landingpage2.html', 'w', 'utf-8') as f:
        f.write(new_l2)
    print('Sync successful')
else:
    print('Marker not found')
