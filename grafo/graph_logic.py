# Foi escolhido a estrutura de fila BFS por uma maior familiaridade.
# Durante o trabalho tivemos algumas dúvidas, sendo necessário relembrar alguns conceitos que foram abordados durante as aula. 
# Tivemos bastante dificuldade em criar o commit e o Pull Request, precisei seguir esses passo a passo:
# 1 - Fazer um fork do repositório.
# 2 - Clonar o seu fork.
# 3 - Criar uma branch no seu fork.
# 4 - Fazer as alterações.
# 5 - Dar push nessa branch.
# 6 - Criar o pull request do seu fork → branch principal do projeto 
# A sintaxe do código foi validada com o auxílio da IA (ChatGPT), com isso pedir ajuda para a IA explicar as funções de cada código, pois alguns haviamos esquecidos. 
# Após o processo validamos o código via VS CODE e simulamos os possíveis cenários. 
# Como aprendizado, podemos relatar que foi na utilização da ferramenta GITHUB e as Estruturas de Dados. 




# graph_logic.py — você edita APENAS este arquivo nesta atividade.
# Dica: use apenas LISTAS para a fila/estrutura de dados (nada de deque).
# Você pode fazer BFS com:
#   fila = [a]; visitados = [a]
#   while fila:
#       u = fila.pop(0)          # remove o primeiro
#       if u == b: return True
#       for v in graph.get(u, []):
#           if v not in visitados:
#               visitados.append(v)
#               fila.append(v)
#   return False
#
# Alternativamente, pode usar DFS com uma lista como "pilha":
#   pilha = [a]; visitados = []
#   while pilha:
#       u = pilha.pop()          # remove o último
#       ...
#   return False

def connected(graph, a, b):
    # Verifica se os NÓS a e b existem no grafo
    if a not in graph or b not in graph:
        return False  # Se não existirem, irá sinalizar como falso

    # Foi criado a fila de BFS contendo inicialmente apenas o nó de partida
    fila = [a]

    # Lista de NÓ visitados, começando pelo NÓ inicial
    visitados = [a]

    # Nesse caso, enquanto ainda houver vértices na fila, a busca será continuada
    while fila:
        # Remove o primeiro item da fila
        u = fila.pop(0)

        # Se o NÓ atual for o destino, daí encontramos um caminho
        if u == b:
            return True

        # Percorre todos os vizinhos do vértice/NÓ u
        for v in graph.get(u, []):
            # Apenas visita vizinhos que ainda não foram visitados
            if v not in visitados:
                # Marca o vizinho como visitado
                visitados.append(v)
                # Adiciona o vizinho no final da fila para explorar depois
                fila.append(v)

    # Se terminou a fila sem encontrar b, não existe caminho
    return False

    raise NotImplementedError("Implemente a função connected usando apenas listas.")
