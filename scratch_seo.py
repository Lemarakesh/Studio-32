import os

def update_file(filepath, is_en=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update JSON-LD
    old_json = '''"address": {
          "@type": "PostalAddress",
          "addressLocality": "Namur",
          "addressCountry": "BE"
        },
        "priceRange": "€€"'''
    
    if is_en:
        desc = "Affordable and high quality web design agency in Belgium and France. Web specialist based in Rixensart."
    else:
        desc = "Création de sites web performants, de haute qualité et abordables en Belgique et en France. Spécialiste web design Rixensart."
        
    new_json = f'''"address": {{
          "@type": "PostalAddress",
          "addressLocality": "Rixensart",
          "addressCountry": "BE"
        }},
        "areaServed": [
          {{
            "@type": "Country",
            "name": "Belgium"
          }},
          {{
            "@type": "Country",
            "name": "France"
          }}
        ],
        "description": "{desc}",
        "priceRange": "€€"'''
        
    content = content.replace(old_json, new_json)
    
    # 2. Add Preload
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&amp;display=swap"'
    if font_link in content and 'rel="preload"' not in content:
        preload_tag = '<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&amp;display=swap" />\n    '
        content = content.replace(font_link, preload_tag + font_link)
        
    # 3. Add decoding="async" to images
    content = content.replace('<img loading="lazy"', '<img loading="lazy" decoding="async"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file(r'c:\Projects\dark-landing-page\index.html', is_en=False)
update_file(r'c:\Projects\dark-landing-page\en\index.html', is_en=True)
