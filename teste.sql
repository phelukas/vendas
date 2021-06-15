--CREATE categoia
INSERT INTO core_categoria (nome) VALUES ('Frutas');
INSERT INTO core_categoria (nome) VALUES ('Proteínas');
INSERT INTO core_categoria (nome) VALUES ('Cereais');
INSERT INTO core_categoria (nome) VALUES ('Leguminosas');
INSERT INTO core_categoria (nome) VALUES ('Sementes');

--CREATE forncecedor
INSERT INTO core_fornecedor (nome, cnpj) VALUES ('fornecedor 1', '10.331.608/0001-52');
INSERT INTO core_fornecedor (nome, cnpj) VALUES ('fornecedor 2', '00.333.725/0001-00');
INSERT INTO core_fornecedor (nome, cnpj) VALUES ('fornecedor 3', '88.550.421/0001-37');
INSERT INTO core_fornecedor (nome, cnpj) VALUES ('fornecedor 4', '03.251.500/0001-94');
INSERT INTO core_fornecedor (nome, cnpj) VALUES ('fornecedor 5', '25.862.630/0001-04');

--Frutas, FORNECEDOR = 1
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('abacaxi ', 2.6, 50, true,  ' ',1, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('abacate ', 1.5, 660, true,  ' ',1, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('amora', 1.6, 674, true,  ' ',1, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('banana ', 2.6, 856, true,  ' ',1, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('bacuri', 7.9, 159, true,  ' ',1, 1);

--Proteínas, FORNECEDOR = 1
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Camarão', 8.9, 42, true,  ' ',1, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Carne de frango', 1.5, 65, true,  ' ',1, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Carne de vaca', 4.6, 74, true,  ' ',1, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Presunto', 4.3, 86, true,  ' ',1, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Mexilhão', 5.4, 16, true,  ' ',1, 2);

--Cereais, FORNECEDOR = 1
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Arroz', 2.6, 50, true,  ' ',1, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('aveia', 1.5, 660, true,  ' ',1, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('centeio', 1.6, 674, true,  ' ',1, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('cevada', 2.6, 856, true,  ' ',1, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('milho', 7.9, 15, true,  ' ',1, 3);

--Leguminosas, FORNECEDOR = 1
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Alfafa, ' , 7.5, 74, true, ' ', 1, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('amendoim' , 2.5, 38, true, ' ', 1, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('ervilha' , 2.7, 72, true, ' ', 1, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('fava' , 1.5, 85, true, ' ', 1, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('feijões' , 5, 76, true, ' ', 1, 4);

--Sementes, FORNECEDOR = 1
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Cânhamo, ' , 5.6, 98, true, ' ', 1, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Abóbora' , 7.5, 378, true, ' ', 1, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Chia' , 6.71, 452, true, ' ', 1, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Gergelim' , 5.57, 987, true, ' ', 1, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Girassol' , 8, 142, true, ' ', 1, 5);

--Frutas, FORNECEDOR = 2
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('buriti ', 9.5, 83, true,  ' ',2, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('caju ', 7.5, 345, true,  ' ',2, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('carambola', 8.9, 354, true,  ' ',2, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('cacau ', 4, 89, true,  ' ',2, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('damasco', 9, 87, true,  ' ',2, 1);

--Proteínas, FORNECEDOR = 2
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Carne de porco (lombo)', 84, 65, true,  ' ',2, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Carne de pato', 50, 74, true,  ' ',2, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Carne de codorna', 44, 123, true,  ' ',2, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Carne de coelho', 23, 849, true,  ' ',2, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Queijos em geral', 80, 160, true,  ' ',2, 2);

--Cereais, FORNECEDOR = 2
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Quinoa', 6, 84, true,  ' ',2, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Amaranto', 5, 60, true,  ' ',2, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('centeio', 6, 64, true,  ' ',2, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Trigo sarraceno', 2, 86, true,  ' ',2, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Granola', 7, 5, true,  ' ',2, 3);

--Leguminosas, FORNECEDOR = 2
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Lentilha, ' , 8.2, 74, true, ' ', 2, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Ervilha' , 2.5, 849, true, ' ', 2, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Grão de bico' , 2, 635, true, ' ', 2, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Amendoim' , 5.6, 785, true, ' ', 2, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Feijão branco' , 5.7, 854, true, ' ', 2, 4);

--Sementes, FORNECEDOR = 2
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Linhaça, ' , 4.1, 741, true, ' ', 2, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Abóbora' , 5, 98, true, ' ', 2, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Chia' , 4.5, 487, true, ' ', 2, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Gergelim' , 1.35, 457, true, ' ', 2, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Girassol' , 3, 165, true, ' ', 2, 5);

--Frutas, FORNECEDOR = 3
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('durião ', 4.8, 54, true,  ' ',3, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('embaúba ', 7.9, 64, true,  ' ',3, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('figo', 5.6, 86, true,  ' ',3, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('framboesa ', 8.9, 76, true,  ' ',3, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('goiaba', 8.6, 68, true,  ' ',3, 1);

--Proteínas, FORNECEDOR = 3
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Salmão sem pele, fresco e cru', 65, 574, true,  ' ',3, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Atum fresco', 23, 104, true,  ' ',3, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Bacalhau salgado cru', 87, 95, true,  ' ',3, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Peixes em geral', 54, 85, true,  ' ',3, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Ovo', 85, 106, true,  ' ',3, 2);

--Cereais, FORNECEDOR = 3
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Cereais em flocos', 4, 155, true,  ' ' ,3, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais', 8, 75, true,  ' ' ,3, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais em grãos', 6, 7, true,  ' ' ,3, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais em amêndoas', 3, 84, true,  ' ' ,3, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('sementes', 5, 50, true,  ' ' ,3, 3);

--Leguminosas, FORNECEDOR = 3
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Aveção', 4.6, 428, true, ' ', 3, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Nozes', 7.8, 576, true, ' ', 3, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Macadâmia', 2, 985, true, ' ', 3, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Amendoim', 6.4, 653, true, ' ', 3, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Fava', 7.3, 368, true, ' ', 3, 4);

--Sementes, FORNECEDOR = 3
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Papoula' , 8.4, 981, true, ' ', 3, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Abóbora' , 6, 928, true, ' ', 3, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Chia' , 3.5, 789, true, ' ', 3, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Semente preta' , 5.7, 477, true, ' ', 3, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Girassol' , 8, 555, true, ' ', 3, 5);

--Frutas, FORNECEDOR = 4
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('graviola ', 5.8, 840, true,  ' ', 4, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('groselha ', 6.5, 325, true,  ' ', 4, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('heisteria', 4.7, 635, true,  ' ', 4, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('ingá ', 5.7, 849, true,  ' ', 4, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('jambo', 6.7, 648, true,  ' ', 4, 1);

--Proteínas, FORNECEDOR = 4
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Iogurte', 21, 894, true,  ' ',4, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Leite', 15, 955, true,  ' ',4, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Kefir', 40, 456, true,  ' ',4, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Camarões', 60, 958, true,  ' ',4, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Caranguejo cozido', 50, 456, true,  ' ',4, 2);

--Cereais, FORNECEDOR = 4
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Arroz', 5.6, 845, true,  ' ' ,4, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('centeio', 4, 150, true,  ' ' ,4, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais em grãos', 6, 7, true,  ' ' ,4, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Sorgo', 2, 100, true,  ' ' ,4, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('sementes', 7, 20, true,  ' ' ,4, 3);

--Leguminosas, FORNECEDOR = 4
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Aveção', 5.7, 157, true, ' ', 4, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Nozes', 8, 984, true, ' ', 4, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Macadâmia', 2.7, 800, true, ' ', 4, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Amendoim', 8.6, 842, true, ' ', 4, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Fava', 8;.3, 984, true, ' ', 4, 4);

--Sementes, FORNECEDOR = 4
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Papoula' , 9, 981, true, ' ', 4, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Abóbora' , 4, 928, true, ' ', 4, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Chia' , 5, 789, true, ' ', 4, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Semente preta' , 6, 477, true, ' ', 4, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Girassol' , 8, 5, true, ' ', 4, 5);


--Frutas, FORNECEDOR = 5
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('abacaxi ', 2.6, 50, true,  ' ',5, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('abacate ', 1.5, 660, true,  ' ',5, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('amora', 1.6, 674, true,  ' ',5, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('banana ', 2.6, 856, true,  ' ',5, 1);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('bacuri', 7.9, 159, true,  ' ',5, 1);

--Proteínas, FORNECEDOR = 5
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Salmão sem pele, fresco e cru', 65, 574, true,  ' ',5, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Atum fresco', 23, 104, true,  ' ',5, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Bacalhau salgado cru', 87, 95, true,  ' ',5, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Peixes em geral', 54, 85, true,  ' ',5, 2);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Ovo', 85, 106, true,  ' ',5, 2);

--Cereais, FORNECEDOR = 5
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Cereais em flocos', 4, 155, true,  ' ' ,5, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais', 8, 75, true,  ' ' ,5, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais em grãos', 6, 7, true,  ' ' ,5, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Barras de cereais em amêndoas', 3, 84, true,  ' ' ,5, 3);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('sementes', 5, 50, true,  ' ' ,5, 3);

--Leguminosas, FORNECEDOR = 5
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Lentilha, ' , 8.2, 74, true, ' ', 5, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Ervilha' , 2.5, 849, true, ' ', 5, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Grão de bico' , 2, 635, true, ' ', 5, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Amendoim' , 5.6, 785, true, ' ', 5, 4);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Feijão branco' , 5.7, 854, true, ' ', 5, 4);

--Sementes, FORNECEDOR = 5
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Cânhamo, ' , 5.6, 98, true, ' ', 5, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Abóbora' , 7.5, 378, true, ' ', 5, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Chia' , 6.71, 452, true, ' ', 5, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Gergelim' , 5.57, 987, true, ' ', 5, 5);
INSERT INTO core_produtos (nome, preco, quantidade, disponivel, descricao,fornecedor_id, categoria_id) VALUES ('Girassol' , 8, 142, true, ' ', 5, 5);

-- select count(distinct categoria_id) from core_produtos where fornecedor_id=1;

-- select 
--     f.id ,f.nome, f.cnpj, sum(p.quantidade) as "Quantidade de Produtos", 
--     count(distinct categoria_id) as "Categorias com Produtos "
-- from 
--     core_produtos p
-- inner join 
--     core_fornecedor f
-- on 
--     p.fornecedor_id=f.id
-- group by 
--     f.nome, f.cnpj, f.id
-- order by 
--     f.nome ASC;
