from pathlib import Path
import re

root = Path(r'd:\GM\Tour-pro\Tour-pro')
active_map = {
    'index.html': 'Beranda',
    'about.html': 'Tentang Kami',
    'destinations.html': 'Destinasi',
    'destination-details.html': 'Destinasi',
    'tours.html': 'Paket Wisata',
    'tour-details.html': 'Paket Wisata',
    'gallery.html': 'Galeri',
    'blog.html': 'Artikel',
    'blog-details.html': 'Artikel',
    'contact.html': 'Kontak',
}
pattern = re.compile(r'<nav id="navmenu" class="navmenu">.*?</nav>', re.S)

for path in root.glob('*.html'):
    text = path.read_text(encoding='utf-8')
    active = active_map.get(path.name, '')

    active_attr = ' class="active"' if active == 'Beranda' else ''
    about_attr = ' class="active"' if active == 'Tentang Kami' else ''
    destinations_attr = ' class="active"' if active == 'Destinasi' else ''
    tours_attr = ' class="active"' if active == 'Paket Wisata' else ''
    gallery_attr = ' class="active"' if active == 'Galeri' else ''
    blog_attr = ' class="active"' if active == 'Artikel' else ''
    contact_attr = ' class="active"' if active == 'Kontak' else ''

    new_nav = f'''<nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html"{active_attr}>Beranda</a></li>
          <li><a href="about.html"{about_attr}>Tentang Kami</a></li>
          <li><a href="destinations.html"{destinations_attr}>Destinasi</a></li>
          <li><a href="tours.html"{tours_attr}>Paket Wisata</a></li>
          <li><a href="gallery.html"{gallery_attr}>Galeri</a></li>
          <li><a href="blog.html"{blog_attr}>Artikel</a></li>
          <li><a href="contact.html"{contact_attr}>Kontak</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>'''
    updated, count = pattern.subn(new_nav, text, count=1)
    if count:
        path.write_text(updated, encoding='utf-8')
