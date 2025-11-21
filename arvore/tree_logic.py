# Durante o desenvolvimento, surgiram dúvidas sobre lógica, sintaxe e fluxo de navegação na árvore. 
# A IA (ChatGPT) foi usada apenas para validar sintaxe, esclarecer erros e auxiliar na organização do raciocínio.
# Compreensão da diferença entre os operadores is e in.
# Durante o processo foi compreendido o aprimoramento da normalização de strings para tornar as entradas do usuário mais robustas.
# Esclarecimento de erros presentes no código.
# Validação da correção e coerência da abordagem adotada.
# Prevenção de equívocos relacionados à sintaxe da linguagem.
# Melhoria da clareza e consistência do código como um todo.


class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

# Parte feita com ajuda de IA, dúvidas na questão do navigate_tree

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):
   
    if node is None:
        raise ValueError("Árvore invalida.")
    
    current = node
    index = 0

# Adicionando as opções para as respostas possiveis:

    while not is_leaf(current):
        if index >= len(answers):
            raise ValueError("Erro: Sem respostas.")
        
        raw = answers[index].strip().lower()

        if raw == "nao":
            raw = "não"

        if raw == "sim":
            next_node = current.yes
        elif raw == "não":
            next_node = current.no
        else:
            raise  ValueError(f"Resposta invalida:'{answers[index]}'")


    # Caso novamente não encontre conexão
        
        if next_node is None:
            raise ValueError("Árvore sem caminho a trilhar")
        
        current = next_node
        index += 1

# Aqui em cima, o index 1 serve para ler as duas respostas. 
# Eu estava com um problema porque o meu código lia apenas a primeira resposta e não lia a segunda, logo vi que o erro estava na comparação.
# Isso causava erro, pois eu tinha escrito "if next_node in None", usando "in" em vez de "is" e essa troca resolveu o problema. 

    return current.question

