from PyPDF2 import PdfWriter, PdfReader

# Créer un PdfWriter pour fusionner les PDF
pdf_writer = PdfWriter()
pdf_list = ['pdf/Billon Yannis CV.pdf', 'pdf/Planning Mastère AIBD 14102024 (1).pdf', 'pdf/SQLv2.pdf']

# Étape 1 : Fusionner tous les PDF
for pdf in pdf_list:
    pdf_reader = PdfReader(pdf)
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

# Écrire le PDF fusionné temporaire
with open('merge.pdf', 'wb') as temp_file:
    pdf_writer.write(temp_file)

# Recharger le PDF fusionné pour manipuler les pages
pdf_reader = PdfReader('merge.pdf')
pdf_writer = PdfWriter()

# Créer une liste de toutes les pages dans le PDF fusionné
pages = [pdf_reader.pages[i] for i in range(len(pdf_reader.pages))]

# Étape 2 : Manipuler les pages du PDF fusionné
print(f"Le PDF fusionné a {len(pages)} pages.")

# Copie une page
while True:
    try:
        print('Indiquer le numéro de la page à copier (1 à {0}): '.format(len(pages)))
        numero_de_la_page = int(input()) - 1
        if numero_de_la_page < 0 or numero_de_la_page >= len(pages):
            raise ValueError("Numéro de page invalide.")
        page_to_move = pages[numero_de_la_page]
        break
    except ValueError as e:
        print(f"Erreur: {e}. Veuillez entrer un numéro de page valide.")

# Demande la position cible de la page
while True:
    try:
        print('Indiquer le numéro de la page à remplacer (1 à {0}): '.format(len(pages)))
        numero_page_remplacer = int(input()) - 1
        if numero_page_remplacer < 0 or numero_page_remplacer >= len(pages):
            raise ValueError("Numéro de page invalide.")
        break
    except ValueError as e:
        print(f"Erreur: {e}. Veuillez entrer un numéro de page valide.")

# Supprimer la page de sa position actuelle et l'insérer à la nouvelle position
pages.pop(numero_de_la_page)
pages.insert(numero_page_remplacer, page_to_move)

# Ajouter les pages modifiées au PdfWriter
for page in pages:
    pdf_writer.add_page(page)

# Crypter le PDF final
pdf_writer.encrypt('password')

# Écrire le nouveau fichier PDF fusionné et modifié
with open('merge.pdf', 'wb') as out:
    pdf_writer.write(out)

print("PDF fusionné et modifié avec succès ")