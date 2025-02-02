from PIL import Image

def convert_to_black(image_path):
    # Charger l'image
    img = Image.open(image_path)

    # Convertir l'image en mode RGBA si elle ne l'est pas déjà
    img = img.convert("RGBA")

    # Obtenir les dimensions de l'image
    largeur, hauteur = img.size

    # Parcourir tous les pixels de l'image
    for x in range(largeur):
        for y in range(hauteur):
            # Obtenir les valeurs RGBA du pixel
            r, g, b, a = img.getpixel((x, y))

            # Vérifier si le pixel est non transparent
            if a > 0:
                # Rendre le pixel noir
                img.putpixel((x, y), (0, 0, 0, a))

    # Sauvegarder l'image modifiée
    img.save("image_noire.png")
    print("L'image a été transformée en noir avec succès et sauvegardée sous le nom 'image_noire.png'.")

# Appel de la fonction avec le chemin de votre image en argument
convert_to_black("razor.png")
