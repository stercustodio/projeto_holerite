from src.entities.cargo import Cargo

tabela_cargo = []

cientista_de_dados = Cargo(10, 'Cientista de Dados', 10_200, 0.1)
especialista_bi = Cargo(20, 'Especialista em Business Intelligence', 7_000, 0.08)
dev_mb_sr = Cargo(30, 'Desenvolvedor Mobile Sênior', 6_700, 0.07)
dev_mb_pl = Cargo(31, 'Desenvolvedor Mobile Pleno', 3_550, 0.06)
dev_jr = Cargo(32, 'Desenvolvedor Junior', 3_000, 0.03)
gerente_projeto = Cargo(50, 'Gerente de Projetos', 8_900, 0.08)

tabela_cargo.append(cientista_de_dados)
tabela_cargo.append(especialista_bi)
tabela_cargo.append(dev_mb_sr)
tabela_cargo.append(dev_mb_pl)
tabela_cargo.append(dev_jr)
tabela_cargo.append(gerente_projeto)
