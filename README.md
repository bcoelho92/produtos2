#Favoritos

Ao expandir seus negócios e uma das novas missões do time de 
tecnologia é criar uma funcionalidade de Produtos Favoritos de nossos Clientes, em 
que os nossos aplicativos irão enviar requisições HTTP para um novo backend que 
deverá gerenciar nossos clientes e seus produtos favoritos. 
 
#Requisitos 
 
Deve ser possível criar, atualizar, visualizar e remover ​Clientes (CRUD)
O cadastro dos clientes deve conter apenas seu nome e endereço de e-mail 
Um cliente não pode se registrar duas vezes com o mesmo endereço de e-mail 

Cada cliente só deverá ter uma única lista de produtos favoritos 
Em uma lista de produtos favoritos podem existir uma quantidade ilimitada de produtos 
Um produto não pode ser adicionado em uma lista caso ele não exista 
Um produto não pode estar duplicado na lista de produtos favoritos de um cliente 
A documentação da API de produtos pode ser visualizada ​neste link 

#Requisitos técnicos

Utilizar banco de dados Postgres em uma docker
Para implementar API utilizar o framework FastAPI com sqlalchemy. Já no controle de migrações do banco usar o alembic
A listagem de clientes deverá ser ordenada por data de criação e paginada com limite de 20 registros;
API deverá ter um link com a documentação (swagger)
