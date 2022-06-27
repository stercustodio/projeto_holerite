class Cargo: 
    
    def __init__(self, codigo: int, descricao: str, salario_base: float, comissao: float):
        self.__codigo: int = codigo
        self.__descricao: str = descricao
        self.__salario_base: float = salario_base
        self.__comissao: float = comissao
    
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @property
    def salario_base(self) -> float:
        return self.__salario_base
    
    @property
    def comissao(self) -> bool:
        return self.__comissao
        

        
        