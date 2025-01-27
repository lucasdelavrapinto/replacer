import re
import argparse

def substituir_em_arquivo(caminho_arquivo, termo_original, termo_substituto):
    try:
        # Lê o conteúdo do arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Substitui o termo original pelo substituto
        conteudo_modificado = re.sub(re.escape(termo_original), termo_substituto, conteudo)

        # Sobrescreve o arquivo com o conteúdo modificado
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo_modificado)

        print(f"Substituições concluídas no arquivo: {caminho_arquivo}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    # Configuração dos argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Substituir texto em um arquivo.")
    parser.add_argument("arquivo", help="Caminho do arquivo a ser processado.")
    parser.add_argument("termo_original", help="Texto que será substituído.")
    parser.add_argument("termo_substituto", help="Texto que substituirá o original.")

    # Obtém os argumentos fornecidos
    args = parser.parse_args()

    # Executa a função de substituição
    substituir_em_arquivo(args.arquivo, args.termo_original, args.termo_substituto)
