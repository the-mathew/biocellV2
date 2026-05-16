import os
from PIL import Image, ImageDraw, ImageFont
import math

os.chdir(r"c:\Users\Galab_LD\Documents\biocell\public\images")

def create_animal_cell():
    """Crea un diagrama de célula animal"""
    size = 800
    img = Image.new('RGB', (size, size), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Membrana plasmática
    draw.ellipse([(50, 50), (size-50, size-50)], outline='#00e5ff', width=3)
    
    # Núcleo
    nucleus_x, nucleus_y = size//2, size//2
    draw.ellipse([(nucleus_x-80, nucleus_y-80), (nucleus_x+80, nucleus_y+80)], outline='#76ff03', width=2, fill='#1a2d1a')
    draw.text((nucleus_x-30, nucleus_y-10), "Nucleus", fill='#76ff03')
    
    # Mitocondrias
    for x, y in [(200, 200), (600, 200), (200, 600), (600, 600)]:
        draw.ellipse([(x-40, y-20), (x+40, y+20)], outline='#ffeb3b', width=2, fill='#2d2d1a')
    draw.text((200-60, 200+30), "Mitochondria", fill='#ffeb3b', font=None)
    
    # Ribosomas
    for x, y in [(300, 300), (500, 350), (350, 500)]:
        draw.ellipse([(x-10, y-10), (x+10, y+10)], outline='#9c27b0', width=1, fill='#1a0d2d')
    draw.text((300-40, 300+30), "Ribosoma", fill='#9c27b0')
    
    # Aparato de Golgi
    golgi_x, golgi_y = 300, 150
    for i in range(5):
        draw.rectangle([(golgi_x+i*20, golgi_y), (golgi_x+i*20+15, golgi_y+40)], outline='#ff9800', width=1)
    draw.text((golgi_x-50, golgi_y-30), "Golgi", fill='#ff9800')
    
    # Centriolos
    for x, y in [(150, 150), (650, 150)]:
        draw.line([(x-20, y), (x+20, y)], fill='#ff5252', width=2)
        draw.line([(x, y-20), (x, y+20)], fill='#ff5252', width=2)
    draw.text((150-40, 150+30), "Centriolo", fill='#ff5252')
    
    # Citoplasma
    draw.text((size//2-100, size-40), "CELULA ANIMAL", fill='#00e5ff', font=None)
    
    img.save('animal_cell.png')
    print("✓ Creado: animal_cell.png")

def create_plant_cell():
    """Crea un diagrama de célula vegetal"""
    size = 800
    img = Image.new('RGB', (size, size), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Pared celular
    draw.rectangle([(30, 30), (size-30, size-30)], outline='#4caf50', width=4)
    
    # Membrana plasmática
    draw.ellipse([(50, 50), (size-50, size-50)], outline='#00e5ff', width=2)
    
    # Núcleo
    nucleus_x, nucleus_y = size//2-80, size//2-80
    draw.ellipse([(nucleus_x-70, nucleus_y-70), (nucleus_x+70, nucleus_y+70)], outline='#76ff03', width=2, fill='#1a2d1a')
    draw.text((nucleus_x-30, nucleus_y-10), "Nucleus", fill='#76ff03')
    
    # Gran vacuola central
    vacuole_x, vacuole_y = size//2+100, size//2+100
    draw.ellipse([(vacuole_x-120, vacuole_y-120), (vacuole_x+120, vacuole_y+120)], outline='#00b8d4', width=2, fill='#0d1a2d')
    draw.text((vacuole_x-80, vacuole_y-10), "Vacuola Central", fill='#00b8d4')
    
    # Cloroplastos
    for x, y in [(300, 250), (550, 300), (400, 500), (250, 600)]:
        draw.ellipse([(x-50, y-30), (x+50, y+30)], outline='#4caf50', width=2, fill='#0d2d0d')
        draw.text((x-50, y+40), "Cloroplasto", fill='#4caf50')
        break  # Solo uno con etiqueta
    
    # Mitocondrias
    for x, y in [(200, 150), (600, 150)]:
        draw.ellipse([(x-40, y-20), (x+40, y+20)], outline='#ffeb3b', width=1, fill='#2d2d1a')
    
    # Aparato de Golgi
    golgi_x, golgi_y = 150, 450
    for i in range(4):
        draw.rectangle([(golgi_x+i*15, golgi_y), (golgi_x+i*15+12, golgi_y+35)], outline='#ff9800', width=1)
    
    # Ribosomas
    for x, y in [(400, 350), (500, 450)]:
        draw.ellipse([(x-8, y-8), (x+8, y+8)], outline='#9c27b0', width=1)
    
    draw.text((size//2-100, size-40), "CELULA VEGETAL", fill='#00e5ff')
    
    img.save('plant_cell.png')
    print("✓ Creado: plant_cell.png")

def create_prokaryote_cell():
    """Crea un diagrama de célula procariota"""
    size = 800
    img = Image.new('RGB', (size, size), color='#0a0e27')
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Membrana plasmática
    draw.ellipse([(50, 50), (size-50, size-50)], outline='#e91e63', width=3)
    
    # Nucleoide (ADN)
    center_x, center_y = size//2, size//2
    for i in range(8):
        angle = (i / 8) * 2 * math.pi
        x = center_x + 100 * math.cos(angle)
        y = center_y + 100 * math.sin(angle)
        draw.line([(center_x, center_y), (x, y)], fill='#e91e63', width=1)
    draw.ellipse([(center_x-40, center_y-40), (center_x+40, center_y+40)], outline='#e91e63', width=2, fill='#2d0d1a')
    draw.text((center_x-40, center_y-10), "Nucleoide", fill='#e91e63')
    
    # Ribosomas procarióticos
    for x, y in [(250, 200), (550, 250), (300, 500), (600, 450)]:
        draw.ellipse([(x-12, y-12), (x+12, y+12)], outline='#9c27b0', width=1, fill='#1a0d2d')
    draw.text((250-50, 200+30), "Ribosoma 70S", fill='#9c27b0')
    
    # Flagelos
    flagella_x, flagella_y = size-100, size//2
    draw.line([(flagella_x, flagella_y), (flagella_x+150, flagella_y-100)], fill='#00e5ff', width=2)
    draw.line([(flagella_x, flagella_y), (flagella_x+150, flagella_y+100)], fill='#00e5ff', width=2)
    draw.text((flagella_x+150+10, flagella_y-30), "Flagelos", fill='#00e5ff')
    
    # Pili
    for angle in [0.3, 0.6, 2.8]:
        x = center_x + 250 * math.cos(angle)
        y = center_y + 250 * math.sin(angle)
        draw.line([(center_x, center_y), (x, y)], fill='#76ff03', width=1)
    draw.text((size//2-30, 100), "Pili", fill='#76ff03')
    
    draw.text((size//2-120, size-40), "CELULA PROCARIOTA", fill='#e91e63')
    
    img.save('prokaryote_cell.png')
    print("✓ Creado: prokaryote_cell.png")

# Crear las imágenes
print("Generando imágenes educativas de células...\n")
create_animal_cell()
create_plant_cell()
create_prokaryote_cell()

print("\nArchivos creados exitosamente:")
for f in ['animal_cell.png', 'plant_cell.png', 'prokaryote_cell.png']:
    if os.path.exists(f):
        size = os.path.getsize(f) / 1024
        print(f"  ✓ {f} ({size:.1f} KB)")
