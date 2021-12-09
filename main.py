# Código do dev aqui

spanish_fruits = {
    'peach',
    'tangerine',
    'orange',
    'damask',
    'pear',
    'watermelon'
}

brazilian_fruits = {
    'strawberry',
    'apple',
    'orange',
    'tangerine',
    'mango',
    'jenipapo',
    'pineapple',
    'cambuci',
    'banana',
    'mandacaru'
}

japanese_fruits = {
    'orange',
    'nashi pear',
    'satonishiki cherries',
    'sudachi',
    'kinkan'
}

popular_fruits = {
    'banana',
    'orange',
    'apple',
    'watermelon',
    'pineapple'
}

def fruit_intersection(conj_one, conj_two):
    result = []
    for x_fruit in conj_one:
        for y_fruit in conj_two:
            if x_fruit == y_fruit:
                result.append(x_fruit)
    return result

def spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits):
    intersection = fruit_intersection(spanish_fruits, brazilian_fruits)    
    return intersection
spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits)


def spanish_and_japan_fruits(spanish_fruits, japanese_fruits):
    intersection = fruit_intersection(spanish_fruits, japanese_fruits)
    return intersection
spanish_and_japan_fruits(spanish_fruits, japanese_fruits)


def brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits):
    intersection = fruit_intersection(brazilian_fruits, japanese_fruits)
    return intersection
brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits)


def popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits):
    union = []
    for s_fruit in spanish_fruits:
        union.append(s_fruit)
    for b_fruit in brazilian_fruits:
        union.append(b_fruit)

    intersection = fruit_intersection(union, popular_fruits)
    return intersection
popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits)


def popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits):
    union = []
    diff_between_union_n_spanish = []

    for j_fruit in japanese_fruits:
        union.append(j_fruit)
    for b_fruit in brazilian_fruits:
        union.append(b_fruit)

    for u_fruit in union:
        for s_fruit in spanish_fruits:
            if u_fruit != s_fruit:
                diff_between_union_n_spanish.append(u_fruit)
    diff_between_union_n_spanish = set(diff_between_union_n_spanish)
    
    intersection = fruit_intersection(diff_between_union_n_spanish, popular_fruits)
    return intersection
popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits)


emails = [
    'a_vanessinha_1990@hotmail.com',
    'a3sign@pandora.be',
    'aaanika2@hotmail.com',
    'aaron2003s@bol.com.br',
    'aaron--21@hotmail.com',
    'abidoral@hotmail.com',
    'abk_333@hotmail.com',
    'abner_bim@hotmail.com',
    'abner_bim@hotmail.com',
    'acacio_divix@hotmail.com',
    'ac-ferian@bol.com.br',
    'academia.boaforma@yahoo.com.br',
    'acordarsono@hotmail.com',
    'acsa_lim@yahoo.com.br',
    'adamyth@gmail.com',
    'add_ae_jente@yahoo.com.br',
    'addgeral@gmail.com',
    'addyevusk@yahoo.com.br',
    'adeozemir@yahoo.com.br',
    'adhaha@gmail.com',
    'adhaha@gmail.com',
    'adidas__star@hotmail.com',
    'adidas__star@hotmail.com',
    'adilio-vidaloka@yahoo.com.br',
    'adilson.mariano5@terra.com.br',
    'admgerald1@yahoo.com.br',
    'adri_barboza@hotmail.com',
    'adri_barboza@hotmail.com',
    'adriaens@pandora.be',
    'adrian_boyzinhu@yahoo.com.br',
    'adriana_lemes_farias@hotmail.com',
    'adriana_lemes_farias@hotmail.com',
    'adrianacpx@yahoo.com.br',
    'adriane_do_prado@yahoo.com.br',
    'adrianinhaim@bol.com.br',
    'adrianinhaim@bol.com.br',
    'adrianinhaxp@yahoo.com.br',
    'adriano.fariasnascimento@yahoo.com.br',
    'adriano_wolf1@hotmail.com',
    'adrianogato.2007@hotmail.com',
    'adrianojareck@hotmail.com',
    'adrianonev3s@gmail.com',
    'adrianosenna@yahoo.com.br',
    'adrianraniery@bol.com.br',
    'Adriedson88@hotmail.com',
    'adrieli_baldoria@hotmail.com',
    'adrielle_amaral@yahoo.com.br',
    'adrielli_cr@hotmail.com',
    'adrielly@yaroo.com',
    'adrielly_silva@yaroo.com',
    'adriely_94@hotmail.com',
    'adrienevinhote@hotmail.com',
    'adryana_maia@hotmail.com',
    'adryana_maia@hotmail.com',
    'adryana_maia@hotmail.com',
    'adryshevchenko7@hotmail.com',
    'adryshevchenko7@yahoo.com.br',
    'adryshevchenko7@hotmail.com',
    'a-ferraz@bol.com.br',
    'afonso-catador@hotmail.com',
    'afonso-catador@hotmail.com',
    'afonsoducarmo@yahoo.com.com.br',
    'afrancar15@yahoo.com.br',
    'agatha_rosa8@yahoo.com.br',
    'agente_fbi13@yahoo.com.br',
    'agatha_rosa8@yahoo.com.br',
    'agente_fbi13@yahoo.com.br',
    'agente_fbi13@yahoo.com.br',
    'agloco.com.fake@gmail.com',
    'agloco-sv@bol.com.br',
    'agnaldojt@hotmail.com',
    'agoraeuvodetona2@yahoo.com',
    'agoraeuvodetona2@yahoo.com',
    'agricesar@yahoo.com.br',
    'agricesar@yahoo.com.br',
    'agricesar@yahoo.com.br',
    'aguia_fenix@hotmail.com',
    'aguinaldo4789@hotmail.com',
    'aguinaldo4789@hotmail.com',
    'aguinaldo4789@hotmail.com',
    'ai_@hotmail.com',
    'Aiacos.Kyoto@gmail.com',
    'aim.vip2@hotmail.com',
    'aim.vip25@hotmail.com',
    'aiopam@hotmail.com',
    'aislyn14@yahoo.com.br',
    'aislyn14@yahoo.com.br',
    'ajudasystemonline@gmail.com',
    'ajuding.01@hotmail.com',
    'akitanajura@yahoo.com.br',
    'akitanajura@yahoo.com.br',
    'ala-frei@hotmail.com',
    'alahfilho@gmail.com',
    'alan_gatinho_sjc@yahoo.com.br',
    'alan_kiedis2@yahoo.com.br',
    'alan_morenogato@hotmail.com',
    'alan_schmeiske@hotmail.com',
    'alandenissouza@hotmail.com',
    'alanfarias_18@yahoo.com.br',
    'alaninha_13@hotmail.com',
    'alanjonny_rp89@hotmail.com',
    'alanjonny_rp89@hotmail.com',
    'alanmoreira12@yahoo.com.br',
    'Alanvitim@yahoo.com.br',
    'alanyseyes@msn.com',
    'alanzin.mel@hotmail.com',
    'alareskamartins@hotmail.com',
    'albinorios2@hotmail.com',
    'albinorios2@hotmail.com',
    'aldy.serg@uol.com.br',
    'ale_amor05@hotmail.com',
    'ale_amor05@hotmail.com',
    'ale_amor05@hotmail.com',
    'ale_amor05@hotmail.com',
    'ale_zinha_hta@hotmail.com',
    'aleckis_97@hotmail.com',
    'aleckis_97@hotmail.com',
    'aleckis_97@hotmail.com',
    'aledickinsooon@hotmail.com',
    'alef_saopaulo@yahoo.com.br',
    'alemao_alison@hotmail.com',
    'Aleson_pml@yahoo.com.br',
    'aless_pina25@hotmail.com',
    'alessandrabrittosouza@gmail.com',
    'alessandralazarini@yahoo.com.br',
    'alessandranyzewski@yahoo.com.br',
    'alessandrofortuna1@hotmail.com',
    'alex.3carlos@yahoo.com.br',
    'alex_betalia@hotmail.com',
    'alex_betalia@hotmail.com',
    'alex_farkas@hotmail.com',
    'alex_llk@yahoo.com.br',
    'ALEX91BADBOY@YAHOO.COM.BR',
    'ALEX91BADBOY@YAHOO.COM.BR',
    'ALEX91BADBOY@YAHOO.COM.BR',
    'alexandra_assaf@hotmail.com',
    'alexandra_praca@hotmail.com',
    'alexandre.audi@uol.com.br',
    'alexandre.carreiro@gmail.com',
    'alexandre.goes@hotmail.com',
    'alexandre.stoian2@gmail.com',
    'alexandreairtonreisteles@yahoo.com.br',
    'alexandrecachapus@yahoo.com.br',
    'alexandressmelo@hotmail.com',
    'alexandretormen@hotmail.com',
    'alexandretormen@hotmail.com',
    'alexandrinho_tdb64@yahoo.com.br',
    'alexandrino.thiago@gmail.com',
    'alexbegins@hotmail.com',
    'alexcabeludo2@hotmail.com',
    'alexcabeludo2@hotmail.com',
    'alexd3@gmail.com',
    'alexfonsek@yahoo.com.br',
    'alexmendesskt@yahoo.com.br',
    'alexrosa55@yahoo.com.br',
    'alexrdgs.89@gmail.com',
    'alexsandro004@uol.com.br',
    'alexsandrotavares@msn.com',
    'alextsm10@yahoo.com.br',
    'alexwaldo@globo.com',
    'alfonsogatto10000@hotmail.com',
    'alfredochallco@bol.com.br',
    'algmjaescolheuessenomedeusuario@yahoo.com.br',
    'ALI.SILVA@HOTMAIL.COM',
    'alice_xmedeiros@yahoo.com.br',
    'aline.moretti.sanches@gmail.com',
    'aline.moretti.sanches@gmail.com',
    'aline.rickmann@ig.com.br',
    'aline__patty@hotmail.com',
    'aline_aquino@oi.com.br',
    'aline_boladona2006@hotmail.com',
    'aline_gatinha_13@yahoo.com.br',
    'aline_rbd_rx@hotmail.com',
    'aline_reggae13@hotmail.com',
    'aline_reggae13@hotmail.com',
    'aline_sakuray@hotmail.com',
    'aline_somg@hotmail.com',
    'aline-150793@hotmail.com',
    'alinealg@yahoo.com.br',
    'alinebmb@gmail.com',
    'alinecordeiro_17@hotmail.com',
    'alinecordeiro_17@hotmail.com',
    'alinedaniele_14@yahoo.com.br',
    'alinedantas4@gmail.com',
    'alineferreira_01@yahoo.com.br',
    'alinegcanta@hotmail.com',
    'alinegirl_49@hotmail.com',
    'alineilima@hotmail.com',
    'alinejaque@gmail.com',
    'alinejaque@gmail.com',
    'alinenewjersey@msn.com',
    'alinenj_usa@yahoo.com',
    'alineoliveiraes@gmail.com',
    'alineteacher@yahoo.com.br',
    'alineteacher@yahoo.com.br',
    'alinewolff@hotmail.com',
    'alininhaderaul@yahoo.com.br',
    'alininhaderaul@yahoo.com.br',
    'alinyfereira@yahoo.com.br',
    'alisson.marquessss@gmail.com',
    'alisson.marquessss@gmail.com',
    'allan.teodoro@gmail.com',
    'allan_17_1309@hotmail.com',
    'allan_17_1309@hotmail.com',
    'allanbraga11@hotmail.com',
    'allancalipio@bol.com.br',
    'allannynhah_15@hotmail.com',
    'allansilvasouza@hotmail.com',
    'allansisti@hotmail.com',
    'allex_pe@hotmail.com',
    'allysson.camillo@Gmail.com',
    'allyssoncachorroloko@hotmail.com',
    'alonsomaria@bol.com.br',
    'alonsomaria@bol.com.br',
    'altamirfilho@gmail.com',
    'altamirfilho@gmail.com',
    'altamirfilho@gmail.com',
    'aluapinh@yahoo.com.br',
    'alvaro_borges@hotmail.com',
    'alvarovallecamargos@yahoo.com.br',
    'alyne_ns@hotmail.com',
    'amanda.kell@yahoo.com.br',
    'amanda-_lima@hotmail.com',
    'amanda_rribeiro@hotmail.com',
    'amanda_rribeiro@hotmail.com',
    'amanda_rribeiro@hotmail.com',
    'amandadosreiscardozo@hotmail.com',
    'amandakell@uol.com.br',
    'amandalenzpszybilski14@yahoo.com.br',
    'amandamedeiros22@hotmail.com',
    'amandanayara_nana@hotmail.com',
    'amandapriscila_bq@yahoo.com.br',
    'amandaroveri@hotmail.com',
    'amandaroveri@hotmail.com',
    'amandasantos_cruz@hotmail.com',
    'amdkell@gmail.com',
    'amandashirmay@hotmail.com',
    'amandasmith748@hotmail.com',
    'amandha1993@hotmail.com',
    'amandinha_pink12@hotmail.com',
    'amandinha160@hotmail.com',
    'amandinhah_princess@msn.com',
    'amandinhalinda96@hotmail.com',
    'amandinhaop@gmail.com',
    'amardita@gmail.com',
    'amarlivrementeamar@hotmail.com',
    'amauri_file@hotmail.com',
    'amaury_css@hotmail.com',
    'amavel_ds@yahoo.com.br'
]

emails_list = ''

def only_yahoo_emails(emails_list):
    result = []
    for email in emails_list:
        splited_on_a = email.split('@')
        for font in splited_on_a:
            if font[0:5] == 'yahoo' or font[0:5] == 'YAHOO':
                result.append(email)
    result = set(result)
    return result
only_yahoo_emails(emails)


def only_hotmail_emails(emails_list):
    result = []
    for email in emails_list:
        splited_on_a = email.split('@')
        for font in splited_on_a:
            if font[0:7] == 'hotmail' or font[0:7] == 'HOTMAIL':
                result.append(email)
    result = set(result)
    return result
only_hotmail_emails(emails)


def only_br_emails(emails_list):
    result = []
    for email in emails_list:
        splited_on_a = email.split('@')
        for final in splited_on_a:
            if final[-2:] == 'br' or final[-2:] == 'BR':
                result.append(email)
    result = set(result)
    return result

only_br_emails(emails)






