create table clientes(
	id_cliente serial,
	nome varchar(100) not null,
	email varchar(30),
	cidade varchar(20),
	constraint pk_id_cliente primary key (id_cliente)
);


create table livros(
	id_livro serial,
	titulo varchar(100) not null,
	categoria varchar(20),
	preco decimal(10,2),
	constraint pk_id_livro primary key (id_livro)
);


create table vendas(
	id_venda serial,
	id_cliente integer not null,
	id_livro integer not null,
	data_venda integer not null,
	quantidade integer,
	valor_total decimal(10,2),
	constraint pk_id_venda primary key (id_venda),
	constraint fk_id_cliente foreign key (id_cliente) references clientes (id_cliente),
	constraint fk_id_livro foreign key (id_livro) references livros (id_livro)
);

-- COMANDOS DDL

--truncate table clientes restart identity cascade;

--truncate table clientes, livros, vendas restart identity cascade;

--truncate table clientes restart identity cascade;
--alter table clientes add column cidade varchar(20);

--alter table livros 
--alter column categoria type varchar(60);

--alter table vendas 
--drop column data_venda;

--alter table vendas 
--add column data_venda date not null;

-- COMANDOS DML

select * from clientes;
select * from livros;
select * from vendas;
