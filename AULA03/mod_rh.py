def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    return {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

def exibir_colaboradores(lista_colaboradores: list) -> None:
    for colaborador in lista_colaboradores:
        print(f"Nome: {colaborador['nome']} | Cargo: {colaborador['cargo']} | Salário: R$ {colaborador['salario']:.2f}")

if __name__ == "__main__":
    lista = []
    
    c1 = cadastrar_colaborador("Ana Silva", "Desenvolvedora", 7500.00)
    c2 = cadastrar_colaborador("Carlos Souza", "Analista de Dados", 6200.50)
    
    lista.append(c1)
    lista.append(c2)
    
    exibir_colaboradores(lista)