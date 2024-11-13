class Stack:
    def __init__(self, max_size):
        self.stack = [] 
        self.max_size = max_size 
    def push(self, item):
        if len(self.stack) < self.max_size: 
            self.stack.append(item)
            print(f"Elemento '{item}' adicionado à pilha.")
        else:
            print("Erro: A pilha está cheia!")

    def pop(self):
        if not self.is_empty(): 
            removed_item = self.stack.pop()  
            print(f"Elemento '{removed_item}' removido da pilha.")
        else:
            print("Erro: A pilha está vazia!")

    def peek(self):
        if not self.is_empty():  
            print(f"Topo da pilha: '{self.stack[-1]}'")  
        else:
            print("A pilha está vazia!")

    def is_empty(self):
        return len(self.stack) == 0  

def main():
    max_size = int(input("Defina o tamanho máximo da pilha: "))
    stack = Stack(max_size) 
    while True:
        print("\nEscolha uma operação:")
        print("1. Adicionar (push)")
        print("2. Remover (pop)")
        print("3. Ver topo (peek)")
        print("4. Sair")

        choice = input("Opção: ")

        if choice == "1":
            item = input("Digite o elemento: ")
            stack.push(item)  
        elif choice == "2":
            stack.pop()  
        elif choice == "3":
            stack.peek() 
        elif choice == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
