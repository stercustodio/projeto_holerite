import mysql.connector

cnx = mysql.connector.connect(user='stercustodio', password='senhaChata40*', host='127.0.0.1', database='projeto_holerite')
cursor = cnx.cursor()

DB_NAME = 'projeto_holerite'

TABLES = {}
TABLES['tabela_funcionarios'] = (
    "CREATE TABLE `tabela_funcionarios` ("
    "  `matricula` int(6) NOT NULL,"
    "  `nome` varchar(100) NOT NULL,"
    "  `cpf` varchar(14) NOT NULL,"
    "  `data_admissao` varchar(10) NOT NULL,"
    "  `cargo` int(2) NOT NULL,"
    "  `comissao` enum('True','False') NOT NULL,"
    "  PRIMARY KEY (`cpf`)"
    ") ENGINE=InnoDB")

TABLES['tabela_cargos'] = (
    "CREATE TABLE `tabela_cargos` ("
    "  `codigo` int(2) NOT NULL,"
    "  `descricao` varchar(80) NOT NULL,"
    "  `salario_base` float NOT NULL,"
    "  `coissao` float NOT NULL,"
    "  PRIMARY KEY (`codigo`), UNIQUE KEY `tabela_cargos` (`tabela_cargos`)"
    ") ENGINE=InnoDB")

cursor.close()
cnx.close()

