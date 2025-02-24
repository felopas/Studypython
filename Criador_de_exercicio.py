import os

def criar_arquivo():
    # Caminho da pasta onde os arquivos serão criados
    caminho_pasta = r"C:\Users\Felipe\Documents\1estudo geral\python\projetoguanabara"
    prefixo_arquivo = "ex"
    extensao = ".py"
    
    # Certifica-se de que a pasta existe
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    # Encontra o próximo número disponível
    numero = 1
    while True:
        nome_arquivo = f"{prefixo_arquivo}{numero:03d}{extensao}"  # Formato: ex001.py, ex002.py, etc.
        caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
        if not os.path.exists(caminho_completo):
            break
        numero += 1

    # Cria o arquivo no próximo número disponível
    with open(caminho_completo, "w") as arquivo:
        arquivo.write("# Este é um novo arquivo Python gerado automaticamente.\n")
    
    print(f"Arquivo criado: {caminho_completo}")

# Chama a função para criar o arquivo
if __name__ == "__main__":
    criar_arquivo()
