from github import Github
import time
while True:
    # Substitua 'seu_token', 'seu_usuario' e 'seu_repositorio' com seus valores
    token = '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'
    g = Github(token)

    # Repositório de exemplo
    repo = g.get_repo('fezarosa-dev/auto_git')

    # Caminho do arquivo
    path = 'contribuicao.txt'

    # Obtém o conteúdo atual do arquivo
    file = repo.get_contents(path)
    current_content = file.decoded_content.decode('utf-8')

    # Modifica o conteúdo
    new_content = current_content + '\nEsta é uma nova linha de conteúdo.'

    # Realiza o commit das alterações
    repo.update_file(path, "Commit de modificação", new_content, file.sha)

    print(f'Arquivo modificado em {repo.name}')
    time.sleep(21600)
