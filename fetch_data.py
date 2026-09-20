import requests
import json

def fetch_pokemon_data():
    # Target endpoint untuk mengambil data satu entitas (Garchomp)
    url = "https://pokeapi.co/api/v2/pokemon/garchomp"
    
    try:
        # Mengirim HTTP GET request dengan batas waktu 10 detik
        response = requests.get(url, timeout=10)
        
        # Mengecek status code, akan memicu exception jika bukan 200 OK
        response.raise_for_status()
        
        # Parsing respons JSON
        data = response.json()
        
        # Mengambil minimal 3 properti spesifik: name, height, weight, dan types
        pokemon_info = {
            "nama": data.get("name"),
            "tinggi_dm": data.get("height"),
            "berat_hg": data.get("weight"),
            "tipe": [t["type"]["name"] for t in data.get("types", [])]
        }
        
        # Menyimpan hasil ekstraksi ke file output.json lokal
        with open("output.json", "w") as json_file:
            json.dump(pokemon_info, json_file, indent=4)
            
        print("Berhasil! Data telah diekstrak dan disimpan di output.json")
        
    # Error Handling
    except requests.exceptions.HTTPError as http_err:
        print(f"Gagal: HTTP error terjadi. Status: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Gagal: Tidak dapat terhubung ke server. Periksa koneksi internet.")
    except requests.exceptions.Timeout:
        print("Gagal: Request timeout. Server terlalu lama merespons.")
    except requests.exceptions.RequestException as err:
        print(f"Gagal: Terjadi kesalahan yang tidak terduga - {err}")
    except KeyError as key_err:
        print(f"Gagal: Struktur JSON tidak sesuai harapan. Key {key_err} tidak ditemukan.")

if __name__ == "__main__":
    fetch_pokemon_data()