# Dokumentasi Tugas API Fetcher

## 1. Nama API dan Link Endpoint
- **Nama API**: PokeAPI (The RESTful Pokémon API)
- **Endpoint yang digunakan**: `https://pokeapi.co/api/v2/pokemon/garchomp`

## 2. Struktur Respons JSON
Respons asli dari endpoint PokeAPI mengembalikan objek JSON yang sangat besar dan bersarang (nested), mencakup detail abilities, moves, stats, hingga sprites. Dari struktur yang kompleks tersebut, script ini melakukan parsing dan mengekstrak 4 properti spesifik menjadi struktur JSON yang lebih rapi di `output.json`:
- `nama` (String): Mengambil nilai dari key `name`.
- `tinggi_dm` (Integer): Mengambil nilai dari key `height` (dalam satuan decimeter).
- `berat_hg` (Integer): Mengambil nilai dari key `weight` (dalam satuan hectogram).
- `tipe` (Array of Strings): Melakukan iterasi dari dalam array of objects `types` untuk mengambil nama tipe (seperti "dragon" dan "ground").

## 3. Penjelasan Error Handling
Script ini menerapkan validasi dan error handling menggunakan blok `try-except` dari pustaka `requests`:
- **`response.raise_for_status()`**: Digunakan untuk memvalidasi status code HTTP. Fungsi ini akan otomatis melempar `HTTPError` jika respons dari server bukan 200 OK (contoh: 404 Not Found jika URL salah ketik).
- **`requests.exceptions.ConnectionError`**: Menangani kendala jaringan lokal, seperti internet terputus atau DNS yang gagal diselesaikan.
- **`requests.exceptions.Timeout`**: Memastikan program tidak berjalan tanpa henti (*hang*) dengan membatasi waktu tunggu respons selama 10 detik.
- **`requests.exceptions.RequestException`**: Berperan sebagai jaring pengaman utama (*catch-all*) untuk menangani segala error terkait HTTP request yang tidak tertangkap oleh exception spesifik di atas.