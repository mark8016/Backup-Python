import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir):
    """
    Função para realizar backup automático de arquivos.
    :param source_dir: Diretório de origem
    :param backup_dir: Diretório de backup
    :return: None
    """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_path)

    try:
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            backup_item = os.path.join(backup_path, item)
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, backup_item)
            else:
                shutil.copy2(source_item, backup_item)
        
        print(f"Backup realizado com sucesso para {backup_path}")
    except Exception as e:
        print(f"Erro ao realizar o backup: {e}")

# Exemplo de uso
source_dir = "/path/to/source/folder"  # Substitua com o diretório de origem
backup_dir = "/path/to/backup/folder"  # Substitua com o diretório de backup
create_backup(source_dir, backup_dir)
