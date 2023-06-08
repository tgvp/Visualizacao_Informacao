use Produtividade;
SET SQL_SAFE_UPDATES = 0;

/* DESCRIBES */
describe Clientes;
describe Colaboradores;
describe Equipas;
describe Tarefas;
describe Rel_Clientes_Colaboradores_Tarefas;

/* CONSULTAS */
SELECT * FROM Clientes;
SELECT * FROM Colaboradores;
SELECT * FROM Tarefas;
SELECT * FROM Equipas;
SELECT * FROM Rel_Clientes_Colaboradores_Tarefas;

/* COUNTS */
SELECT COUNT(id_cliente) FROM Clientes;
SELECT COUNT(id_colaborador) FROM Colaboradores;
SELECT COUNT(id_tarefa) FROM Tarefas;
SELECT COUNT(id_equipa) FROM Equipas;
SELECT COUNT(id_rel) FROM Rel_Clientes_Colaboradores_Tarefas;