CREATE DATABASE Pessoas
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE Pessoas;

CREATE TABLE IF NOT EXISTS tb_pessoa(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nome VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    idade VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    sexo VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    cidade_natal VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    nome_mae VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    nome_pai VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    nome_irmao1 VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    nome_irmao2 VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    nome_avo1 VARCHAR(255) DEFAULT 'NÃO INFORMADO',
    nome_avo2 VARCHAR(255) DEFAULT 'NÃO INFORMADO'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;