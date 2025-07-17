from PIL import Image
import pytesseract

# Caminho da imagem
imagem_path = 'sua_imagem.png'  # troca pro caminho do seu arquivo

# Abre a imagem
imagem = Image.open(imagem_path)

# Extrai texto da imagem (linguagem 'por' pra português, muda se quiser)
texto = pytesseract.image_to_string(imagem, lang='por')

print(texto)
