##### Dia 18/02
Crirei o app, fiz o requirements, e chamei o banco de dados no app.py.
Modelei os dados do pagamento, gerando um tempo de validação do pagamento
juntamente com; qr_code, id, value, paid e bank_payment_id. Criei rota de pagamento,
criar fatura e do pix

##### Dia 19/02
Hoje fiz um aprimoramento na rota de pix, onde agora ele cria um qr_code(uuid.uuid4()) de forma
randomica, juntamente com bank_payment_id(hash), onde cada requisição post gera uma
imagem de qr_code única. Depois pegamos umas estilizações, onde o endpoint de ver pagamento
será renderizado por render_template(), onde passa os seus parâmetros. 

##### Dia 24/02
Hoje terminamos a confirmação do endpoit, colocando umas condicionais, e passando
a usar o id do bank, para ele ser pago com esse id.
Depois de passar em todas as confirmações, nos alteramos o valor de payment.paid
para True. Importamos o socketIO, onde fizemos a conexão tanto com o backend
quanto com o frontend, onde ambos esperam receber um escutador. Vimos também o 
.emit(), que consegue enviar uma notificação a todos os usuários conectados. 
Criamos o connected e disconnect do socketIO. Colocamos em jogo duas novas renderizações
payment, quando o cliente paga ele automaticamente será direcionado a esta pagina 
e também disparará um disconnect do socketIO, e caso mandem um ID de pagamento
não existente, caira na 404, que também esta rodando perfeitamente.


##### Dia 25/02
Hoje, fizemos alguns testes unitarios utilizando o pytest e configurando 
a função create_payment para sempre retornar a raiz do projeto.