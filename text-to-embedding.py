import os
from docx import Document
from sentence_transformers import SentenceTransformer
import numpy as np

# 1. Belgeleri okuma ve parçalara ayırma
def read_docs_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            doc = Document(os.path.join(folder_path, filename))
            paragraphs = [para.text for para in doc.paragraphs if para.text.strip() != ""]
            documents.extend(paragraphs)  # Belgelerdeki tüm paragrafları al
    return documents

# 2. Belgeleri okuma
folder_path = 'C:/Users/'  # Belgelerinizin bulunduğu klasörün yolunu buraya yazın
documents = read_docs_from_folder(folder_path)

# 3. Sentence Transformers ile embedding oluşturma
model = SentenceTransformer('all-MiniLM-L6-v2')  # Embedding modelini seçiyoruz
embeddings = model.encode(documents)  # Belgeleri embedding'e dönüştür

# 4. Embedding'leri numpy array formatına dönüştürme ve kaydetme
np_embeddings = np.array(embeddings)  # Embedding'leri numpy array olarak sakla

# Kaydetme (embeddings.npy dosyasına kaydediyoruz)
np.save('embeddings.npy', np_embeddings)

# Sonuç olarak embedding'leri numpy formatında kaydettik
print(f"{len(documents)} belge işlendi ve embedding'ler kaydedildi.")
