##### Dia 18/01
Crirei o app, fiz o requirements, e chamei o banco de dados no app.py.
Modelei os dados do pagamento, gerando um tempo de validação do pagamento
juntamente com; qr_code, id, value, paid e bank_payment_id. Criei rota de pagamento,
criar fatura e do pix

##### Dia 19/01
Hoje fiz um aprimoramento na rota de pix, onde agora ele cria um qr_code(uuid.uuid4()) de forma
randomica, juntamente com bank_payment_id(hash), onde cada requisição post gera uma
imagem de qr_code única. Depois pegamos umas estilizações, onde o endpoint de ver pagamento
será renderizado por render_template(), onde passa os seus parâmetros. 