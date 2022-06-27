import mysql.connector

cnx = mysql.connector.connect(user='stercustodio', password='senhaChata40*', host='127.0.0.1', database='projeto_holerite')
cursor = cnx.cursor()

DB_NAME = 'projeto_holerite'

TABLES = {}
TABLES['lista_funcionarios'] = (
    "CREATE TABLE `lista_funcionarios` ("
    "  `matricula` int(6) NOT NULL AUTO_INCREMENT,"
    "  `nome` varchar(100) NOT NULL,"
    "  `cpf` varchar(14) NOT NULL,"
    "  `data_admissao` varchar(10) NOT NULL,"
    "  `cargo` int(2) NOT NULL,"
    "  `comissao` enum('True','False') NOT NULL,"
    "  PRIMARY KEY (`cpf`)"
    ") ENGINE=InnoDB")

TABLES['lista_cargos'] = (
    "CREATE TABLE `lista_cargos` ("
    "  `codigo` int(2) NOT NULL,"
    "  `descricao` varchar(80) NOT NULL,"
    "  `salario_base` float NOT NULL,"
    "  `coissao` float NOT NULL,"
    "  PRIMARY KEY (`codigo`), UNIQUE KEY `lista_cargos` (`lista_cargos`)"
    ") ENGINE=InnoDB")

cursor.close()
cnx.close()
