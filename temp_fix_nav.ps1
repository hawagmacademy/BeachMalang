$root = 'd:\GM\Tour-pro\Tour-pro'
$activeMap = @{
  'index.html' = 'Beranda'
  'about.html' = 'Tentang Kami'
  'destinations.html' = 'Destinasi'
  'destination-details.html' = 'Destinasi'
  'tours.html' = 'Paket Wisata'
  'tour-details.html' = 'Paket Wisata'
  'gallery.html' = 'Galeri'
  'blog.html' = 'Artikel'
  'blog-details.html' = 'Artikel'
  'contact.html' = 'Kontak'
}

Get-ChildItem -Path $root -Filter *.html -File | ForEach-Object {
  $text = Get-Content -Path $_.FullName -Raw
  $active = if ($activeMap.ContainsKey($_.Name)) { $activeMap[$_.Name] } else { '' }

  $activeAttr = if ($active -eq 'Beranda') { ' class="active"' } else { '' }
  $aboutAttr = if ($active -eq 'Tentang Kami') { ' class="active"' } else { '' }
  $destinationsAttr = if ($active -eq 'Destinasi') { ' class="active"' } else { '' }
  $toursAttr = if ($active -eq 'Paket Wisata') { ' class="active"' } else { '' }
  $galleryAttr = if ($active -eq 'Galeri') { ' class="active"' } else { '' }
  $blogAttr = if ($active -eq 'Artikel') { ' class="active"' } else { '' }
  $contactAttr = if ($active -eq 'Kontak') { ' class="active"' } else { '' }

  $newNav = @"
      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html"$activeAttr>Beranda</a></li>
          <li><a href="about.html"$aboutAttr>Tentang Kami</a></li>
          <li><a href="destinations.html"$destinationsAttr>Destinasi</a></li>
          <li><a href="tours.html"$toursAttr>Paket Wisata</a></li>
          <li><a href="gallery.html"$galleryAttr>Galeri</a></li>
          <li><a href="blog.html"$blogAttr>Artikel</a></li>
          <li><a href="contact.html"$contactAttr>Kontak</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
"@

  $updatedText = [regex]::Replace($text, '<nav id="navmenu" class="navmenu">.*?</nav>', $newNav, 1)
  Set-Content -Path $_.FullName -Value $updatedText -Encoding utf8
}
