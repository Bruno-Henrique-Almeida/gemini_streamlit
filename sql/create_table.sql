/*
DROP TABLE categoria;
DROP TABLE produto;
DROP TABLE venda;
DROP TABLE item_venda;
DROP TABLE fornecedor;
DROP TABLE produto_fornecedor;
DROP TABLE cliente;
*/

-- Criar tabela de Categorias
CREATE TABLE IF NOT EXISTS categoria (
  id_categoria   INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_categoria TEXT    NOT NULL
);
CREATE INDEX idx_nome_categoria ON categoria (nome_categoria);

-- Criar tabela de Produtos
CREATE TABLE IF NOT EXISTS produto (
  id_produto     INTEGER PRIMARY KEY AUTOINCREMENT,
  id_categoria   INTEGER NOT NULL,
  id_fornecedor  INTEGER NOT NULL,
  nome_produto   TEXT    NOT NULL,
  descricao      TEXT,
  preco_unitario REAL    NOT NULL,
  estoque_atual  INTEGER NOT NULL,
  FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);
CREATE INDEX idx_produto_categoria ON produto (id_categoria, nome_produto);

-- Criar tabela de Vendas
CREATE TABLE IF NOT EXISTS venda (
  id_venda       INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente     INTEGER NOT NULL,
  id_produto     INTEGER NOT NULL,
  data_venda     DATE    NOT NULL,
  valor_total    REAL    NOT NULL,
  quantidade     INTEGER NOT NULL,
  preco_unitario REAL    NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);
CREATE INDEX idx_venda_cliente ON venda (data_venda, id_cliente);

-- Criar tabela Itens da Venda
CREATE TABLE IF NOT EXISTS item_venda (
  item_id_venda  INTEGER PRIMARY KEY AUTOINCREMENT,
  id_venda       INTEGER NOT NULL,
  id_produto     INTEGER NOT NULL,
  quantidade     INTEGER NOT NULL,
  preco_unitario REAL    NOT NULL,
  FOREIGN KEY (id_venda)   REFERENCES vendas(id_venda),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);
CREATE INDEX idx_item_venda ON item_venda (id_venda, id_produto);

-- Criar tabela Fornecedores
CREATE TABLE IF NOT EXISTS fornecedor (
  id_fornecedor   INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_fornecedor TEXT    NOT NULL,
  email           TEXT,
  telefone        TEXT
);
CREATE INDEX idx_nome_fornecedor ON fornecedor (nome_fornecedor);

-- Criar tabela Produtos dos Fornecedores
CREATE TABLE IF NOT EXISTS produto_fornecedor (
  produto_id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
  id_produto            INTEGER NOT NULL,
  id_fornecedor         INTEGER NOT NULL,
  preco_compra          REAL    NOT NULL,
  FOREIGN KEY (id_produto)    REFERENCES produtos(id_produto),
  FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor)
);
CREATE INDEX idx_produto_fornecedor ON produto_fornecedor (id_produto, id_fornecedor);

-- Criar tabela Clientes
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT    NOT NULL,
    email        TEXT    UNIQUE,
    telefone     TEXT,
    endereco     TEXT
);