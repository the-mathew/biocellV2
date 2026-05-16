import os
from PIL import Image, ImageDraw

os.chdir(r"c:\Users\Galab_LD\Documents\biocell\public\images")

def create_organelle_images():
    """Crea imágenes individuales de organelos"""
    
    # Membrana Plasmática
    img = Image.new('RGB', (400, 400), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    # Bicapa lipídica
    draw.ellipse([(50, 50), (350, 350)], outline='#00e5ff', width=8)
    draw.text((100, 350), "Bicapa Lipidica", fill='#00e5ff')
    img.save('membrane.png')
    print("✓ Creado: membrane.png")
    
    # Pared Celular
    img = Image.new('RGB', (400, 400), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    draw.rectangle([(50, 50), (350, 350)], outline='#4caf50', width=10)
    for i in range(50, 350, 15):
        draw.line([(50, i), (60, i+5)], fill='#4caf50', width=2)
        draw.line([(350, i), (340, i+5)], fill='#4caf50', width=2)
    draw.text((80, 360), "Pared Celular", fill='#4caf50')
    img.save('cell_wall.png')
    print("✓ Creado: cell_wall.png")
    
    # Vacuola
    img = Image.new('RGB', (400, 400), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    draw.ellipse([(80, 80), (320, 320)], outline='#00b8d4', width=6, fill='#0d1a2d')
    # Contenido
    for x in range(120, 300, 30):
        for y in range(120, 300, 30):
            draw.ellipse([(x-8, y-8), (x+8, y+8)], fill='#00b8d4')
    draw.text((60, 330), "Gran Vacuola", fill='#00b8d4')
    img.save('vacuole.png')
    print("✓ Creado: vacuole.png")
    
    # Ribosomas
    img = Image.new('RGB', (400, 400), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    # Subunidad grande
    draw.ellipse([(100, 100), (250, 220)], outline='#9c27b0', width=4, fill='#1a0d2d')
    # Subunidad pequeña
    draw.ellipse([(150, 180), (280, 300)], outline='#9c27b0', width=4, fill='#1a0d2d')
    draw.text((100, 320), "Ribosoma 80S", fill='#9c27b0')
    img.save('ribosome.png')
    print("✓ Creado: ribosome.png")
    
    # Centriolos
    img = Image.new('RGB', (400, 400), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    # Dos cilindros perpendiculares
    for x in [120, 280]:
        for y in [120, 280]:
            # Cilindro
            draw.rectangle([(x-30, y-60), (x+30, y+60)], outline='#ff5252', width=3)
            # Microtúbulos
            for i in range(-25, 30, 10):
                draw.line([(x-30, y+i), (x+30, y+i)], fill='#ff5252', width=1)
    draw.text((100, 360), "Centrolos", fill='#ff5252')
    img.save('centrioles.png')
    print("✓ Creado: centrioles.png")
    
    # ADN/Nucleoide
    img = Image.new('RGB', (400, 400), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    # Doble hélice
    for i in range(0, 300, 20):
        draw.ellipse([(150-40, 50+i), (150+40, 50+i+15)], outline='#e91e63', width=2)
        draw.line([(110, 50+i), (190, 50+i)], fill='#e91e63', width=1)
    draw.text((100, 360), "ADN/Nucleoide", fill='#e91e63')
    img.save('dna.png')
    print("✓ Creado: dna.png")

create_organelle_images()

print("\nTodas las imágenes han sido generadas.")
print("Total de imágenes PNG en el proyecto:")
for f in sorted([f for f in os.listdir('.') if f.endswith('.png')]):
    size = os.path.getsize(f) / 1024
    print(f"  • {f:30} ({size:6.1f} KB)")
