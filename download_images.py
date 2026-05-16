import urllib.request
import os

os.chdir(r"c:\Users\Galab_LD\Documents\biocell\public\images")

urls = [
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Animal_cell_structure_en.svg/1200px-Animal_cell_structure_en.svg.png", "animal_cell.png"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Plant_cell_structure_svg_en.svg/1000px-Plant_cell_structure_svg_en.svg.png", "plant_cell.png"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Prokaryote_cell_and_Eukaryote_cell_en.svg/1200px-Prokaryote_cell_and_Eukaryote_cell_en.svg.png", "prokaryote_cell.png"),
]

print("Descargando imágenes educativas de células...\n")

for url, filename in urls:
    try:
        print(f"Descargando {filename}...")
        urllib.request.urlretrieve(url, filename)
        size = os.path.getsize(filename) / 1024
        print(f"✓ Descargado: {filename} ({size:.1f} KB)\n")
    except Exception as e:
        print(f"✗ Error descargando {filename}: {e}\n")

print("\nArchivos PNG en el directorio:")
for f in sorted([f for f in os.listdir('.') if f.endswith('.png')]):
    size = os.path.getsize(f) / 1024
    print(f"  - {f} ({size:.1f} KB)")
