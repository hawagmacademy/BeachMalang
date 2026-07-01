import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the eye icon with text and remove the info icon
content = re.sub(
    r'<a href="([^"]+)" title="Lihat Foto" class="glightbox"><i class="bi bi-eye"></i></a>\s*<a href="[^"]+"><i class="bi bi-info-circle"></i></a>',
    r'<a href="\1" title="Lihat Foto" class="glightbox" style="font-size: 1rem; text-decoration: none; font-weight: 600;">Lihat Foto</a>',
    content
)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(content)
