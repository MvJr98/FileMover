import os
import shutil

# Diretório onde estão os arquivos de vídeo
diretorio_videos = r'diretorio-da-pasta'

# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio_videos)

# Loop pelos arquivos
for arquivo in arquivos:
    # Verifica se o arquivo é um arquivo de vídeo (por extensão, você pode personalizar)
    if arquivo.endswith('.txt') or arquivo.endswith('.ts'):
        # Cria o nome da pasta com o mesmo nome do arquivo (sem extensão)
        nome_pasta = os.path.splitext(arquivo)[0]

        # Caminho completo para a pasta a ser criada
        caminho_pasta = os.path.join(diretorio_videos, nome_pasta)

        # Cria a pasta se ela não existir
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

        # Move o arquivo para a pasta
        shutil.move(os.path.join(diretorio_videos, arquivo), os.path.join(caminho_pasta, arquivo))

print("Arquivos movidos para suas respectivas pastas.")
