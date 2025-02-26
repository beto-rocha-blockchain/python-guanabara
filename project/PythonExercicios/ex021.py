import pygame

def tocar_audio(arquivo):
    # Inicializa o mixer do pygame
    pygame.mixer.init()
    
    # Carrega o arquivo MP3
    pygame.mixer.music.load(arquivo)
    
    # Reproduz o áudio
    pygame.mixer.music.play()
    
    # Mantém o programa rodando enquanto o áudio toca
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    arquivo_mp3 = r"C:\Users\00026718\OneDrive - PROGEN S.A\Documentos\GitHub\python-guanabara\Mídia\Áudio\audio.mp3"
    tocar_audio(arquivo_mp3)