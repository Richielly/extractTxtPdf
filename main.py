import tempfile
import os
from pdf2image import convert_from_path
import easyocr

def extract_text_from_pdf(pdf_path):
    # Verificar se o diretório temporário existe e criá-lo, se necessário
    temp_dir = r'C:\Users\Equiplano\PycharmProjects\extractTxtPdf\temp/'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Converter PDF em imagens JPEG
    images = convert_from_path(pdf_path)

    extracted_text = ""
    for i, image in enumerate(images):
        # Criar um arquivo temporário para salvar a imagem
        temp_image = tempfile.NamedTemporaryFile(suffix='.jpg', dir=temp_dir, delete=False)
        temp_image_path = temp_image.name

        # Salvar a imagem JPEG
        image.save(temp_image_path, 'JPEG')

        # Utilizar OCR para extrair o texto da imagem
        reader = easyocr.Reader(['pt'])
        result = reader.readtext(temp_image_path)
        for r in result:
            extracted_text += r[1] + ' '

        # Remover o arquivo temporário da imagem
        # os.remove(temp_image_path)

    return extracted_text

# Caminho para o arquivo PDF
pdf_file = r'C:\Users\Equiplano\PycharmProjects\extractTxtPdf\esenfs.pdf'

# Extrair o texto do PDF
extracted_text = extract_text_from_pdf(pdf_file)

# Imprimir o texto extraído
print(extracted_text)
