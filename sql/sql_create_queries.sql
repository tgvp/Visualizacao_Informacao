 CREATE TABLE IF NOT EXISTS Equipas (
        id_equipa INT NOT NULL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
        );
 CREATE TABLE IF NOT EXISTS Colaboradores (
        id_colaborador INT NOT NULL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        salario_base DECIMAL NOT NULL,
        horas_semanais INT NOT NULL,
        idade INT NOT NULL,
        qualificacao VARCHAR(255) NOT NULL,
        id_equipa INT NOT NULL,
        FOREIGN KEY (id_equipa) REFERENCES Equipas(id_equipa)
        );
 CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        morada VARCHAR(255),
        distrito VARCHAR(255),
        valor_hora INT NOT NULL,
        horas_mensais_orcamentadas INT NOT NULL,
        satisfacao INT NOT NULL,
        id_colaborador INT NOT NULL,
        FOREIGN KEY (id_colaborador) REFERENCES Colaboradores(id_colaborador)
        ); 
CREATE TABLE IF NOT EXISTS Tarefas (
        id_tarefa INT NOT NULL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        descricao VARCHAR(255)
        );
CREATE TABLE IF NOT EXISTS Rel_Clientes_Colaboradores_Tarefas (
        id_rel INT NOT NULL,
        id_cliente INT NOT NULL,
        id_colaborador INT NOT NULL,
        id_tarefa INT NOT NULL,
        data_tarefa DATE NOT NULL,
        hora_inicio TIME NOT NULL,
        hora_fim TIME NOT NULL,
        horas DECIMAL(3, 1),
        PRIMARY KEY (id_rel, id_cliente, id_colaborador, id_tarefa),
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON DELETE CASCADE,
        FOREIGN KEY (id_colaborador) REFERENCES Colaboradores(id_colaborador) ON DELETE CASCADE,
        FOREIGN KEY (id_tarefa) REFERENCES Tarefas(id_tarefa) ON DELETE CASCADE
        );