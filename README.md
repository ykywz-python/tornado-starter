# Tornado Starter
mempermudah pembuatan aplikasi web dengan tornado, DRY (Don't Repeat Yourself)

![preview](preview.avif)

## Cara Penggunaan
- clone repo `git clone https://github.com/ykywz-python/tornado-starter`
- install uv (jika belum ada) `powershell -c "irm https://astral.sh/uv/install.ps1 | more"`
- jalankan uv: `uv sync`
- jalankan program: `uv run main.py`

## Fitur yang tersedia
- CRUD (Create, Read, Update, Delete)
- Validasi Form
- Hanya Satu Proses yang berjalan (single instance)
- Kompilasi jadi aplikasi exe `jalankan build_binary.bat`
- database menggunakan json `tinydb`
- pattern MVC (Model View Controller)

## Struktur Folder
```
.
├── main.py
└── src/
    ├── config/
    ├── controllers/
    ├── models/
    ├── resources/
    │   ├── static/
    │   │   ├── js
    │   │   ├── css
    │   │   └── img
    │   └── templates/
    ├── utils/
    ├── boot.py
    └── routes.py
```

## Catatan Perubahan
4 November 2025
- buat project

## Referensi Librari
- appdirs
- async_timeout
- cloudscraper
- click
- colorama
- cssselect
- et_xmlfile
- openpyxl
- Pillow
- winotify
- win10toast
- tornado
- tinydb
- textwrap3
- sqlparse
- selenium
- pywin32
- pywebpush
- pycryptodome
- pychrome
- py3rijndael


## Beri Dukungan

[![Buka Halaman Donasi](https://irfanykywz.github.io/donate/donate.png)](https://irfanykywz.github.io/donate/)