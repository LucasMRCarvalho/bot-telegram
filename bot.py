import mercadopago
import json
import string
import telebot
import time
import sys
import uuid
import base64
import re
import os
import datetime
import subprocess
import threading
import random
import central as api
import qrcode
import pytz
from io import BytesIO
from os import system
from telebot import types
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
from datetime import timezone
from pytz import timezone
print("Codigo iniciado agora")

sdk = mercadopago.SDK(api.CredentialsChange.InfoPix.token_mp())
bot = telebot.TeleBot(api.CredentialsChange.token_bot())
bot.send_message(chat_id=api.CredentialsChange.id_dono(), text='🤖 <b>SEU BOT FOI REINICIADO!</b> 🤖', parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔧 PAINEL ADM', callback_data='voltar_paineladm')]]))
bot.send_message(chat_id=6962068872, text=f'Olá chefe, o bot @{api.CredentialsChange.user_bot()} está vencido!')

# Lista para armazenar IDs de usuários que aceitaram as regras
usuarios_que_aceitaram = set()

# Função para verificar se o usuário já aceitou as regras
def verificar_regras_usuario(message):
    user_id = message.from_user.id
    if user_id not in usuarios_que_aceitaram:
        enviar_regras(message)

# Função para enviar as regras para o usuário
def enviar_regras(message):
    regras_texto = (
        "📜 𝗔𝗡𝗧𝗘𝗦 𝗗𝗘 𝗖𝗢𝗠𝗣𝗥𝗔𝗥 𝗖𝗢𝗡𝗢𝗦𝗖𝗢 𝗟𝗘𝗜𝗔 𝗔𝗧𝗘𝗡𝗧𝗔𝗠𝗘𝗡𝗧𝗘 𝗖𝗢𝗠𝗢 𝗙𝗨𝗡𝗖𝗜𝗢𝗡𝗔 𝗡𝗢𝗦𝗦𝗔𝗦 𝗥𝗘𝗚𝗥𝗔𝗦 📜\n\n\n"
        "⚠️ A PARTIR DO MOMENTO QUE VOCÊ APERTAR NO BOTÃO ABAIXO, VOCÊ ESTÁ 100% DE ACORDO COM TODAS AS REGRAS ⚠️\n\n\n"
        "🕒⚙️ 𝗛𝗢𝗥𝗔𝗥𝗜𝗢 𝗗𝗘 𝗦𝗨𝗣𝗢𝗥𝗧𝗘 📣\n\n"
        "🕗 Das 08h às 19h (𝗦𝗮𝗯𝗮𝗱𝗼, 𝗱𝗼𝗺𝗶𝗻𝗴𝗼 𝗲 𝗳𝗲𝗿𝗶𝗮𝗱𝗼 𝗽𝗼𝗱𝗲 𝘀𝗲𝗿 𝗾𝘂𝗲 𝗻𝗮𝗼 𝘁𝗲𝗻𝗵𝗮 𝘀𝘂𝗽𝗼𝗿𝘁𝗲).\n\n\n"
        "🤝 𝗖𝗢𝗠𝗢 𝗦𝗢𝗟𝗜𝗖𝗜𝗧𝗔𝗥 𝗦𝗨𝗣𝗢𝗥𝗧𝗘? 📞\n\n1️⃣ Entre no grupo SUPORTE.\n2️⃣ Vote na enquete disponível.\n"
        "3️⃣ Aguarde nosso administrador te chamar no pv.\n\n\n🔍 𝗣𝗮𝗿𝗮 𝘀𝘂𝗽𝗼𝗿𝘁𝗲 𝘀𝗲𝗿𝗮 𝗻𝗲𝗰𝗲𝘀𝘀𝗮𝗿𝗶𝗼:\n\nPint do erro 📸\n"
        "Login por escrito 📝\nData da compra 🗓️\n\n\n❌ 𝗦𝗘𝗠 𝗘𝗦𝗦𝗘𝗦 𝗗𝗔𝗗𝗢𝗦 𝗦𝗘𝗨 𝗦𝗨𝗣𝗢𝗥𝗧𝗘 𝗦𝗘𝗥𝗔 𝗡𝗘𝗚𝗔𝗗𝗢 ❌\n\n📌 ATENÇÃO ÀS REGRAS BÁSICAS:\n\n"
        "🚫 SE TENTAR ALTERAR EMAIL DA CONTA IRA PERDER O SUPORTE DA MESMA\n🚫 Não devolvemos valores no PIX, apenas valores no BOT.\n"
        "🗣️ Evite conversas prolongadas no grupo, para isso use o PV.\n"
        "🤝 Respeito é fundamental; faltar com respeito no grupo resultará em remoção ou silenciamento pelo nosso BOT.\n"
        "⏳ Prazo para suporte é de 24h a 48h, caso passar esse prazo você receberá o valor de saldo no bot referente aos dias que falta para vencer seu acesso.\n\n"
        "Aceite as regras para continuar usando o bot."
    )
    markup = InlineKeyboardMarkup()
    aceitar_button = InlineKeyboardButton("⚠️ Aceitar Regras ⚠️", callback_data="aceitar_regras")
    markup.add(aceitar_button)
    
    bot.send_message(message.chat.id, regras_texto, reply_markup=markup)

# Handler para o callback dos botões de aceitar/recusar
@bot.callback_query_handler(func=lambda call: call.data == "aceitar_regras")
def regras_callback_handler(call):
    user_id = call.from_user.id
    # Adiciona o usuário à lista dos que aceitaram
    usuarios_que_aceitaram.add(user_id)

    # Criar um teclado com o botão "Iniciar"
    markup = InlineKeyboardMarkup()
    iniciar_button = InlineKeyboardButton("Iniciar", callback_data="menu_start")
    markup.add(iniciar_button)

    # Mensagem de agradecimento com o botão
    bot.send_message(call.message.chat.id, "Obrigado! Você aceitou as regras.\n\n Clique no botão abaixo para iniciar:\n\n (Caso o botão não funcione mande um OI no chat)", reply_markup=markup)

# Chamar a função verificar_regras_usuario na primeira interação do usuário
@bot.message_handler(commands=['start'])
def start_message(message):
    verificar_regras_usuario(message)

# Função para gerar o Pix para o pagamento da renovação
def gerar_pix_renovacao(valor, chat_id, message):
    try:
        payment = api.CriarPix.gerar(float(valor), chat_id)
        id_pag = payment['response']['id']
        pix_copia_cola = payment['response']['point_of_interaction']['transaction_data']['qr_code']

        # Gere o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(pix_copia_cola)
        qr.make(fit=True)

        # Crie uma imagem com o QR Code
        img = qr.make_image(fill_color="black", back_color="white")

        # Salve a imagem em BytesIO para envio
        img_byte_array = BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)

        # Envie a imagem
        bot.send_photo(chat_id, img_byte_array, caption="QR Code para pagamento")

        texto = api.Textos.pix_automatico(None, pix_copia_cola, 15, id_pag, f'{float(valor):.2f}')
        message = bot.send_message(chat_id=chat_id, text=texto, parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f'{api.Botoes.aguardando_pagamento()}', callback_data='aguardando')]]))
        threading.Thread(target=verificar_pagamento, args=(message, id_pag, valor)).start()
    except Exception as e:
        print(e)
        bot.reply_to(message, "ENVIE COMPROVANTE PARA A PESSOA QUE VOCE ALUGOU O BOT")
        return

# Função para lidar com a renovação do bot
@bot.callback_query_handler(func=lambda call: call.data.startswith('renovar_'))
def renovar_bot(call):
    try:
        # Verificar se o usuário é um administrador
        if not is_admin(call.message):
            bot.send_message(call.message.chat.id, "Você não tem permissão para realizar esta ação.")
            return

        # Calcular o novo prazo de validade e definir o valor do Pix
        if call.data == 'renovar_7_dias':
            novo_prazo = calcular_novo_prazo(7)
            valor_pix = 40.00  # Valor fixo para renovação de 7 dias
        elif call.data == 'renovar_30_dias':
            novo_prazo = calcular_novo_prazo(30)
            valor_pix = 130.00  # Valor fixo para renovação de 30 dias
        
        # Gerar o Pix para o pagamento da renovação com o valor correspondente
        gerar_pix_renovacao(valor_pix, call.message.chat.id, call.message)

        # Atualizar as informações do bot após a renovação
        atualizar_info_bot(novo_prazo)

        # Enviar mensagem informando que a renovação foi realizada com sucesso
        bot.send_message(call.message.chat.id, "A renovação foi realizada com sucesso!")

    except Exception as e:
        print(e)
        bot.reply_to(call.message, "ENVIE COMPROVANTE PARA A PESSOA QUE VOCE ALUGOU O BOT")

# Função para verificar e renovar automaticamente os bots expirados
def verificar_e_renovar_bots_expirados():
    for user_id, prazo_validade in validade_bots.items():
        if prazo_validade < datetime.datetime.now():
            # Verificar o plano do bot e renovar de acordo
            if user_id in plano_7_dias:
                novo_prazo = calcular_novo_prazo(7)
            elif user_id in plano_30_dias:
                novo_prazo = calcular_novo_prazo(30)
            else:
                # Caso o bot não tenha um plano específico, considere um plano padrão
                novo_prazo = calcular_novo_prazo(7)

            # Renovar o bot
            renovar_bot(user_id, novo_prazo)
            # Aqui você pode enviar uma mensagem informando sobre a renovação automática

def verificar_inline_payment(id_pag, valor, id):
    chat_id = id  # Armazene o chat_id em uma variável local para evitar que seja None
    while True:
        time.sleep(5)
        result = sdk.payment().get(id_pag)
        payment = result["response"]
        status_pag = payment['status']
        if 'approved' in status_pag:
            txt = api.TextoInline.pagamento_aprovado(None, valor, id_pag)
            bot.send_message(chat_id=chat_id, text=txt, parse_mode='HTML')
            break
        elif 'pending' in status_pag:
            continue
        elif 'cancelled' in status_pag:
            bot.send_message(chat_id=chat_id, text=f'Pagamento {id_pag} expirado!', parse_mode='HTML')
            break
# Função para gerar um Pix para o pagamento da renovação
def gerar_pix(valor):
    # Aqui você pode implementar a lógica para gerar o Pix
    # Neste exemplo, apenas retornaremos o valor fornecido
    return valor

# Função para calcular o novo prazo de validade
def calcular_novo_prazo(dias):
    # Obter a data atual
    data_atual = datetime.datetime.now()
    # Adicionar a quantidade de dias ao prazo atual
    novo_prazo = data_atual + datetime.timedelta(days=dias)
    return novo_prazo
	
@bot.message_handler(commands=['cancelar'])
def handle_cancelar(message):
    if api.Admin.verificar_vencimento() == True:
        ver_se_expirou()
        return
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.reply_to(message, "ordem cancelada!")

# Painel de administração
@bot.message_handler(commands=['admin'])
def painel_admin(message):
    if is_admin(message):
        vencimento = "SEU BOT ESTÁ VENCIDO!" if api.Admin.tempo_ate_o_vencimento() <= 0 else f'SEU BOT VENCE EM {api.Admin.tempo_ate_o_vencimento()} DIAS!'
        texto = f'⚙️ <b>PAINEL DE GERENCIAMENTO @{api.CredentialsChange.user_bot()}</b>\n⚠️ <b>{vencimento}</b>⚠️\n🤖 <i>V{api.CredentialsChange.versao_bot()}</i>\n\n📘 <b>Estatísticas:</b>\n📊 Usuarios: {api.Admin.total_users()}\n📈 Receita total: R${api.Admin.receita_total():.2f}\n💠 Receita de hoje: R${api.Admin.receita_hoje():.2f}\n📺 Acessos vendidos: {api.Admin.acessos_vendidos()}\n📲 Acessos vendidos hoje: {api.Admin.acessos_vendidos_hoje()}\n\n🛠 <i>Use os botões abaixo para me configurar</i>'
        bt = InlineKeyboardButton('⚙️ CONFIGURAÇÕES GERAIS ⚙️', callback_data='configuracoes_geral')
        bt2 = InlineKeyboardButton('🖥 CONFIGURAR LOGINS', callback_data='configurar_logins')
        bt3 = InlineKeyboardButton('🕵️ CONFIGURAR ADMINS', callback_data='configurar_admins')
        bt4 = InlineKeyboardButton('👥 CONFIGURAR AFILIADOS', callback_data='configurar_afiliados')
        bt5 = InlineKeyboardButton('👤 CONFIGURAR USUARIOS', callback_data='configurar_usuarios')
        bt6 = InlineKeyboardButton('💠 CONFIGURAR PIX', callback_data='configurar_pix')
        bt7 = InlineKeyboardButton('🛎 NOTIFICAÇÕES FAKE', callback_data='configurar_notificacoes_fake')
        bt8 = InlineKeyboardButton('🎁 GIFT CARD 🎁', callback_data='gift_card')
        bt9 = InlineKeyboardButton('📥 ESTOQUE DE LOGIN 📦', callback_data='baixar_estoque_login')
        bt10 = InlineKeyboardButton('📥 DADOS DOS CLIENTES 📊', callback_data='baixar_dados_clientes')
        bt11 = InlineKeyboardButton("BAIXAR LOGINS VENDIDOS", callback_data='download_logins')
        markup = InlineKeyboardMarkup([[bt], [bt2], [bt3], [bt4], [bt5], [bt6], [bt8], [bt9,bt10], [bt11]])
        if message.text != '/admin':
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, texto, parse_mode='HTML', reply_markup=markup)
    else:
        bot.reply_to(message, "Você não é um administrador!")
        return
# Função para verificar se o remetente da mensagem é um administrador
def is_admin(message):
    return api.Admin.verificar_admin(message.chat.id) == True or int(message.chat.id) == int(api.CredentialsChange.id_dono())


# Função para lidar com o comando que envia os dados armazenados dos clientes
def enviar_download_logins(message):
    try:
        caminho_arquivo = 'database/users.json'  # Caminho correto para o arquivo
        if not os.path.exists(caminho_arquivo):
            bot.reply_to(message, "Não há dados armazenados de clientes.")
            return
        
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        
        # Construindo o conteúdo do arquivo de texto
        texto = "SEVIÇO CONTRATADO===VALOR PAGO===EMAIL===SENHA===DATA COMPRA\n\n"
        for user in dados['users']:
            for compra in user['compras']:
                # Extraindo apenas a data sem o horário
                data_sem_horario = compra['data'].split(' as ')[0]
                texto += f"{compra['servico']}==={compra['valor']}==={compra['email']}==={compra['senha']}==={data_sem_horario}\n"

        # Salvando os dados em um arquivo de texto temporário
        with open('download_logins.txt', 'w') as arquivo_txt:
            arquivo_txt.write(texto)
        
        # Enviando o arquivo de texto para o administrador ou dono do bot
        bot.send_document(message.chat.id, open('download_logins.txt', 'rb'), caption="Aqui estão os dados armazenados dos clientes.")

        # Limpando o arquivo de texto temporário
        os.remove('download_logins.txt')

    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao enviar os dados dos clientes.")




	
# Função para verificar se o remetente da mensagem é um administrador
def is_admin(message):
    return api.Admin.verificar_admin(message.chat.id) == True or int(message.chat.id) == int(api.CredentialsChange.id_dono())

# Função para lidar com o comando que envia os dados armazenados dos clientes
def enviar_dados_clientes(message):
    try:
        caminho_arquivo = 'database/users.json'  # Caminho correto para o arquivo
        if not os.path.exists(caminho_arquivo):
            bot.reply_to(message, "Não há dados armazenados de clientes.")
            return
        
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        
        # Construindo o conteúdo do arquivo de texto
        texto = "Dados armazenados dos clientes:\n\n"
        for user in dados['users']:
            texto += f"ID: {user['id']}\n"
            texto += f"Saldo: {user['saldo']}\n"
            texto += f"Total de compras: {user['total_compras']}\n"
            texto += f"Total pago: {user['total_pagos']}\n"
            texto += "💥Detalhes compras:💥\n"
            for compra in user['compras']:
                texto += f"  📍Serviço:📍 {compra['servico']}\n"
                texto += f"  Valor: {compra['valor']}\n"
                texto += f"  Email: {compra['email']}\n"
                texto += f"  Senha: {compra['senha']}\n"
                texto += f"  🗓Data da compra: {compra['data']}\n\n"	
            texto += "Detalhes pix pagos:\n"
            for pagamento in user['pagamentos']:
                texto += f"  ID do pagamento: {pagamento['id_pagamento']}\n"
                texto += f"  Valor pago: {pagamento['valor']}\n"
                texto += f"  Data compra: {pagamento['data']}\n"
            texto += "\n"

        # Salvando os dados em um arquivo de texto temporário
        with open('dados_clientes.txt', 'w') as arquivo_txt:
            arquivo_txt.write(texto)
        
        # Enviando o arquivo de texto para o administrador ou dono do bot
        bot.send_document(message.chat.id, open('dados_clientes.txt', 'rb'), caption="Aqui estão os dados armazenados dos clientes.")

        # Limpando o arquivo de texto temporário
        os.remove('dados_clientes.txt')

    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao enviar os dados dos clientes.")

# Função para verificar se o remetente da mensagem é um administrador
def is_admin(message):
    return api.Admin.verificar_admin(message.chat.id) == True or int(message.chat.id) == int(api.CredentialsChange.id_dono())

# Função para lidar com o comando que envia os dados armazenados
def enviar_dados_acessos(message):
    try:
        caminho_arquivo = 'database/acessos.json'  # Caminho correto para o arquivo
        if not os.path.exists(caminho_arquivo):
            bot.reply_to(message, "Não há dados armazenados.")
            return
        
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        
        # Construindo o conteúdo do arquivo de texto
        texto = "Dados armazenados:\n\n"
        for acesso in dados['acessos']:
            texto += f"Nome: {acesso['nome']}\n"
            texto += f"Valor: {acesso['valor']}\n"
            texto += f"Descrição: {acesso['descricao']}\n"
            texto += f"Email: {acesso['email']}\n"
            texto += f"Senha: {acesso['senha']}\n"
            texto += f"Duração: {acesso['duracao']}\n"
            # Gerar um código de acesso de 6 caracteres (letras e números)
            caracteres = string.ascii_letters + string.digits
            codigo_acesso = ''.join(random.choices(caracteres, k=6))
            texto += f"Código de acesso: {codigo_acesso}\n"
            texto += "\n"
        
        # Salvando os dados em um arquivo de texto temporário
        with open('estoque_logins.txt', 'w') as arquivo_txt:
            arquivo_txt.write(texto)
        
        # Enviando o arquivo de texto para o administrador ou dono do bot
        bot.send_document(message.chat.id, open('estoque_logins.txt', 'rb'), caption="Aqui estão os dados armazenados.")

        # Limpando o arquivo de texto temporário
        os.remove('estoque_logins.txt')

    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao enviar os dados.")
#Menu Geral
# Lidar com o botão "BAIXAR LOGINS VENDIDOS"
@bot.callback_query_handler(func=lambda call: call.data == 'download_logins')
def handle_download_logins(call):
    if is_admin(call.message):
        enviar_download_logins(call.message)
    else:
        bot.answer_callback_query(call.id, text="Você não tem permissão para usar este comando.")

# Lidar com o botão "Baixar Dados Clientes"
@bot.callback_query_handler(func=lambda call: call.data == 'baixar_dados_clientes')
def handle_download_clients_data(call):
    if is_admin(call.message):
        enviar_dados_clientes(call.message)
    else:
        bot.answer_callback_query(call.id, text="Você não tem permissão para usar este comando.")
# Lidar com o botão "BAIXAR ESTOQUE DE LOGIN"
@bot.callback_query_handler(func=lambda call: call.data == 'baixar_estoque_login')
def handle_download_access(call):
    if is_admin(call.message):
        enviar_dados_acessos(call.message)
    else:
        bot.answer_callback_query(call.id, text="Você não tem permissão para usar este comando.")

def configuracoes_geral(message):
    texto = f'<i>Use os botões abaixo para configurar seu bot:</i>\n📬 DESTINO DAS LOG\'S: {api.CredentialsChange.id_dono()}\n👤 <b>LINK DO SUPORTE ATUAL: {api.CredentialsChange.SuporteInfo.link_suporte()}</b>\n✂️ SEPARADOR: {api.CredentialsChange.separador()}\n<i>separador é o caractér que separa as informações quando você vai alterar algo no bot. Ele é muito importante, então escolha um caractér que você não usa com frequencia para que o bot não fique confuso na hora de separar</i>\n<b>EX DO SEPARADOR EM AÇÃO:</b> NOME{api.CredentialsChange.separador()}VALOR'
    bt = InlineKeyboardButton('🔴 MANUTENÇÃO (off)', callback_data='manutencao')
    if api.CredentialsChange.status_manutencao() == True:
          bt = InlineKeyboardButton('🟢 MANUTENÇÃO (on)', callback_data='manutencao')
    bt3 = InlineKeyboardButton('✂️ MUDAR SEPARADOR', callback_data='mudar_separador')
    bt4 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt], [bt3], [bt4]])
    bot.edit_message_text(chat_id=message.chat.id, text=texto, message_id=message.message_id, reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
def mudar_separador(message, callid):
    sep = message.text
    api.CredentialsChange.mudar_separador(sep)
    bot.answer_callback_query(callid, "Separador alterado com sucesso!", show_alert=True)
#Menu login

@bot.message_handler(func=lambda message: '/addlogin' in message.text.split('===')[0])
def adicionar_login(message):
    sep = message.text.strip().split('\n')
    separador = api.CredentialsChange.separador()
    quantity = 0
    for ordem in sep:
        if len(ordem) > 0:
            if message.text.split('===')[0] == '/addlogin':
                try:
                    sp = ordem
                    if len(ordem.split('===')) == 7:
                        s = sp.split('===')
                        servico = s[1]
                        email = s[2]
                        senha = s[3]
                        preco = s[4]
                        duracao = s[5]
                        descricao = s[6]
                        descricao = descricao.replace('\\n', '\n')
                        api.ControleLogins.add_login(nome=servico, valor=preco, descricao=descricao, email=email, senha=senha, duracao=duracao)
                        quantity += 1
                        pass
                    else:
                        bot.reply_to(message, "Erro ao adicionar, você enviou em um formato não permitido!")
                except Exception as e:
                    print(e)
                    bot.reply_to(message, "Erro ao adicionar, você enviou em um formato não permitido!")
                    pass
            else:
                try:
                    sp = ordem.split(f'{separador}')
                    servico = sp[0]
                    valor = sp[1]
                    descricao = sp[2]
                    email = sp[3]
                    senha = sp[4]
                    duracao = sp[5]
                    if len(sp) == 6:
                        if valor.isdigit() != True:
                            bot.reply_to(message, f'O valor do serviço {servico} não é um digito! Portanto, ele não foi adicionado!')
                            pass
                        descricao = descricao.replace('\\n', '\n')
                        api.ControleLogins.add_login(nome=servico, valor=valor, descricao=descricao, email=email, senha=senha, duracao=duracao)
                        quantity +=1
                    else:
                        bot.reply_to(message, f"Formato invalido! O login {servico} não foi adicionado!")
                        pass
                except:
                    bot.reply_to(message, "Erro ao adicionar, você enviou em um formato não permitido!")
                    pass
            pass
    bot.reply_to(message, f"Feito! Você abasteceu <b>{quantity}</b> login.", parse_mode='HTML')

def remover_login(message):
    separador = api.CredentialsChange.separador()
    try:
        stri = message.text.strip().split(f'{separador}')
        api.ControleLogins.remover_login(nome=stri[0], email=stri[1])
        bot.reply_to(message, "Removido com sucesso do estoque!")
    except:
        bot.reply_to(message, "Erro ao remover o login.")
def remover_por_plataforma(message):
    plat = message.text
    try:
        api.ControleLogins.remover_por_nome(plat)
        bot.reply_to(message, f"Todos os logins de {plat} foram removidos com sucesso!")
    except:
        bot.reply_to(message, 'Erro ao remover os logins...')
def mudar_valor_servico(message):
    try:
        sep = api.CredentialsChange.separador()
        txt = message.text.strip().split(f'{sep}')
        servico = txt[0]
        valor = txt[1]
        api.ControleLogins.mudar_valor_por_nome(servico, valor)
        bot.reply_to(message, f"O servico {servico} teve seu valor mudado para R${int(valor):.2f}")
    except:
        bot.reply_to(message, 'Falha ao mudar os valores.')
def mudar_valor_todos(message):
    try:
        valor = message.text
        api.ControleLogins.mudar_valor_de_todos(valor)
        bot.reply_to(message, "Valores alterados com sucesso")
    except:
        bot.reply_to(message, "Erro ao alterar valores.")
def configurar_logins(message):
    separador = api.CredentialsChange.separador()
    texto = f'📦 <b>LOGINS NO ESTOQUE: {api.ControleLogins.estoque_total()}</b>\n\n◎ ══════ ❈ ══════ ◎\n📮 <b>ADICIONAR LOGIN</b>\n◎ ══════ ❈ ══════ ◎\nApós apertar vai solicitar os logins que você deseja abastecer, eles devem ser enviados no formato: <i>NOME{separador}EMAIL{separador}SENHA{separador}VALOR{separador}DURACAO{separador}DESCRICAO</i>\nPara abastecer mais de um login basta enviar desta mesma maneira um abaixo do outro, ou pulando linhas, você pode pular quantas linhas quiser de um login para outro.\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n🥾 <b>REMOVER login</b>\n◎ ══════ ❈ ══════ ◎\nApós clicado basta enviar o serviço e o email, separados por {separador}\nEx: <i>NETFLIX{separador}EMAIL</i>\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n❌ <b>REMOVER POR PLATAFORMA</b>\n◎ ══════ ❈ ══════ ◎\nApós clicado, basta enviar o nome da plataforma, automaticamente todos os logins serão removidos.\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n🗑 <b>ZERAR ESTOQUE</b>\n◎ ══════ ❈ ══════ ◎\nApós clicar, todos os logins abastecidos serão removidos.\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n💸 <b>MUDAR VALOR DO SERVIÇO</b>\n◎ ══════ ❈ ══════ ◎\nApós clicar, envie o nome do serviço e o valor, separados por {separador}.\nEX: <i>SERVICO{separador}VALOR</i>\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n🎫 <b>MUDAR VALOR DE TODOS</b>\n◎ ══════ ❈ ══════ ◎\nApós clicar, envie o valor, e todos os serviços abastecidos terão seus valores alterados. (útil para queima de estoque)\n┕━━━━╗✹╔━━━━┙'
    bt = InlineKeyboardButton('📮 ADICIONAR LOGIN', callback_data='adicionar_login')
    bt2 = InlineKeyboardButton('🥾 REMOVER LOGIN ESPECIFICO', callback_data='remover_login')
    bt3 = InlineKeyboardButton('❌ REMOVER POR PLATAFORMA', callback_data='remover_por_plataforma')
    bt4 = InlineKeyboardButton('🗑 ZERAR ESTOQUE', callback_data='zerar_estoque')
    bt5 = InlineKeyboardButton('💸 MUDAR VALOR DO SERVIÇO', callback_data='mudar_valor_servico')
    bt6 = InlineKeyboardButton('🎫 MUDAR VALOR DE TODOS', callback_data='mudar_valor_todos')
    bt7 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt2,bt3], [bt4], [bt5,bt6], [bt7]])
    bot.edit_message_text(chat_id=message.chat.id, text=texto, message_id=message.message_id, reply_markup=markup, parse_mode='HTML')
#Menu admin
def configurar_admins(message):
    texto = f'🅰️ <b>PAINEL CONFIGURAR ADMIN</b>\n\n👮 Administradores: {api.Admin.quantidade_admin()}\n<i>Use os botões abaixo para fazer as alterações necessárias</i>'
    bt = InlineKeyboardButton('➕ ADICIONAR ADM', callback_data='adicionar_adm')
    bt2 = InlineKeyboardButton('🚮 REMOVER ADM', callback_data='remover_adm')
    bt3 = InlineKeyboardButton('📃 LISTA DE ADM', callback_data='lista_adm')
    bt4 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt], [bt2], [bt3], [bt4]])
    bot.edit_message_text(chat_id=message.chat.id, text=texto, message_id=message.message_id, parse_mode='HTML', reply_markup=markup)
def adicionar_adm(message):
    try:
        id_admin = message.text
        api.Admin.add_admin(id_admin)
        bot.reply_to(message, f"O usuario: {id_admin} foi feito admin!")
    except:
        bot.reply_to(message, "Erro ao promover para adm.")
def remover_adm(message):
    try:
        id = message.text
        api.Admin.remover_admin(id)
        bot.reply_to(message, f"Adm {id} foi feito um usuario comum novamente.")
    except:
        bot.reply_to(message, "Falha ao remover o adm.")
#Menu afiliados
def configurar_afiliados(message):
    texto = f'🔻 <b>PONTOS MINIMO PRA SALDO: {api.AfiliadosInfo.minimo_pontos_pra_saldo()}</b>✖️\n<b>MULTIPLICADOR: {api.AfiliadosInfo.multiplicador_pontos()}</b>\n\n\n◎ ══════ ❈ ══════ ◎\n👥 <b>SISTEMA DE INDICAÇÃO</b>\n◎ ══════ ❈ ══════ ◎\nAo clicar, altera o status do sistema de indicação. Se estiver OFF os usuários não poderão trocar seus pontos por saldo.\nVERDE = On\nVERMELHO = Off\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n🗞 <b>PONTOS POR RECARGA</b>\n◎ ══════ ❈ ══════ ◎\nEssa é a quantidade de pontos que o usuário ganha cada vez que o seu afiliado fizer uma recarga.\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n🔻 <b>PONTOS MINIMO PARA CONVERTER</b>\n◎ ══════ ❈ ══════ ◎\nIsso é a quantidade mínima de pontos que o usuário precisa para converter seus pontos em saldo.\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n✖️ <b>MULTIPLICADOR PARA CONVERTER</b>\n◎ ══════ ❈ ══════ ◎\nIsso é o multiplicador de pontos para saldo na hora de converter.\n<b>EX:</b> <i>Se o multiplicador for 0.01 e o usuário tiver 500 pontos, quando ele converter ele ficará com 5,00 de saldo.\nSe o multiplicador for 0.50 e o usuario tiver com 20 pontos, quando ele converter ele ficará com 10,00 de saldo.</i>\n┕━━━━╗✹╔━━━━┙'
    bt = InlineKeyboardButton('🔴 SISTEMA DE INDICAÇÃO(off)', callback_data='mudar_status_afiliados')
    if api.AfiliadosInfo.status_afiliado() == True:
        bt = InlineKeyboardButton('🟢 SISTEMA DE INDICAÇÃO(off)', callback_data='mudar_status_afiliados')
    bt2 = InlineKeyboardButton('🗞 PONTOS POR RECARGA', callback_data='pontos_por_recarga')
    bt3 = InlineKeyboardButton('🔻 PONTOS MINIMO PARA CONVERTER', callback_data='pontos_minimo_converter')
    bt4 = InlineKeyboardButton('✖️ MULTIPLICADOR PARA CONVERTER', callback_data='multiplicador_para_converter')
    bt5 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt], [bt2], [bt3], [bt4], [bt5]])
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
def pontos_por_recarga(message):
    try:
        pontos = message.text
        api.AfiliadosInfo.mudar_pontos_por_recarga(pontos)
        bot.reply_to(message, f"Alterado com sucesso! Agora toda vez que um usuário recarregar, quem indicou ele ganhará {pontos} pontos.")
    except:
        bot.reply_to(message, "Falha ao alterar a quantidade de pontos, verifique se enviou um número aceitavel.")
def pontos_minimo_converter(message):
    try:
        min = message.text
        api.AfiliadosInfo.trocar_minimo_pontos_pra_saldo(min)
        bot.reply_to(message, f"Feito! Agora os usuarios precisam ter {min} pontos para poder converter em saldo.")
    except:
        bot.reply_to(message, f"Erro ao alterar a quantidade de pontos, verifique se enviou um número aceitavel.")
def multiplicador_para_converter(message):
    try:
        mult = message.text
        api.AfiliadosInfo.trocar_multiplicador_pontos(mult)
        bot.reply_to(message, "Multiplicador alterado com sucesso!")
    except:
        bot.reply_to(message, "Falha ao alterar o multiplicador, verifique se enviou um número aceitavel.")
#Menu usuarios
def configurar_usuarios(message):
    texto = f'◎ ══════ ❈ ══════ ◎\n📪 <b>TRANSMITIR A TODOS</b>\n◎ ══════ ❈ ══════ ◎\nEnvia uma mensagem para todos os usuários registrados no bot. 📬✉️\nApós clicar, envie o texto que quer transmitir ou a foto. Para enviar uma foto com texto, basta colocar o texto na legenda da imagem. 📷🖋️\n┕━━━━╗✹╔━━━━┙\n\n\n◎ ══════ ❈ ══════ ◎\n🔎 <b>PESQUISAR USUÁRIO</b>\n◎ ══════ ❈ ══════ ◎\nSe este usuário estiver registrado no bot, vai abrir as configurações de edição desse usuário. 💼🔧\nVocê poderá editar o saldo, ver o histórico de compras, e todas as informações dele. 📈📋\n┕━━━━╗✹╔━━━━┙'
    bt = InlineKeyboardButton('📫 TRANSMITIR A TODOS', callback_data='transmitir_todos')
    bt2 = InlineKeyboardButton('🔎 PESQUISAR USUARIO', callback_data='pesquisar_usuario')
    bt3 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt], [bt2], [bt3]])
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, reply_markup=markup, parse_mode='HTML')
def transmitir_todos(message):
    api.FuncaoTransmitir.zerar_infos()
    bt = InlineKeyboardButton('➕ ADD BOTAO ➕', callback_data='add_botao')
    bt2 = InlineKeyboardButton('✅ CONFIRMAR ENVIO', callback_data='confirmar_envio')
    markup = InlineKeyboardMarkup([[bt], [bt2]])
    if message.content_type == 'photo':
        photo = message.photo[0].file_id
        api.FuncaoTransmitir.adicionar_foto(photo)
        api.FuncaoTransmitir.adicionar_texto(message.caption)
        bot.send_photo(message.chat.id, photo=photo, caption=message.caption, reply_markup=markup, parse_mode='HTML')
    elif message.content_type == 'text':
        api.FuncaoTransmitir.adicionar_texto(message.text)
        bot.send_message(message.chat.id, text=message.text, parse_mode='HTML', reply_markup=markup)
    else:
        bot.reply_to(message, "Este tipo de mensagem ainda não está disponível para transmitir.")
def add_botao(message):
    try:
        text = message.text
        s = text.split('\n')
        markup = InlineKeyboardMarkup()
        for elemento in s:
            botoes = []
            separar = elemento.split('&&')
            for botao in separar:
                sep = botao.split('-')
                nome = sep[0].strip()
                url = sep[1].strip()
                botoes.append(InlineKeyboardButton(f'{nome}', url=f'{url}'))
            markup.row(*botoes)
        api.FuncaoTransmitir.adicionar_markup(markup)
        bt2 = InlineKeyboardButton('✅ CONFIRMAR ENVIO', callback_data='confirmar_envio')
        markup.row(bt2)
        if markup != None:
            texto = api.FuncaoTransmitir.pegar_texto()
            photo = api.FuncaoTransmitir.pegar_foto()
            if texto != None and photo == None:
                bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode='HTML')
            elif photo != None and texto == None:
                bot.send_photo(message.chat.id, photo, reply_markup=markup, parse_mode='HTML')
            elif photo != None and texto != None:
                bot.send_photo(message.chat.id, photo, caption=texto, reply_markup=markup, parse_mode='HTML')
            else:
                bot.reply_to(message, "Error!")
    except Exception as e:
        bot.reply_to(message, "Ocorreu um erro ao processar, verifique se enviou o nome e a URL no formato correto.")
        print(e)
enviando_transmissao = False
def confirmar_envio(message):
    global enviando_transmissao
    markup1 = api.FuncaoTransmitir.pegar_markup()
    markup = InlineKeyboardMarkup()
    if markup1 != None:
        for bt in markup1:
            buttons = []
            for b in bt:
                buttons.append(InlineKeyboardButton(b["text"], url=b["url"]))
            markup.row(*buttons)
    else:
        markup = None
    texto = api.FuncaoTransmitir.pegar_texto()
    photo = api.FuncaoTransmitir.pegar_foto()
    with open('database/users.json', 'r') as f:
        data = json.load(f)
    enviando_transmissao = True
    msg = bot.send_message(message.chat.id, "<i>Enviando transmissão</i>", parse_mode='HTML')
    for user in data["users"]:
        try:
            if photo == None:
                bot.send_message(user["id"], texto, parse_mode='HTML', reply_markup=markup)
            else:
                bot.send_photo(user["id"], photo, caption=texto, parse_mode='HTML', reply_markup=markup)
        except Exception as e:
            print(e)
            pass
    enviando_transmissao = False
def pesquisar_usuario(message):
    id = message.text
    if api.InfoUser.verificar_usuario(id) == True:
        texto = f'🔎 <b>USUÁRIO ENCONTRADO</b> ✅\n\n🕵️ <b>INFORMAÇÕES</b> 🕵️\n📛 <b>ID:</b> <code>{id}</code>\n💰 <b>SALDO:</b> <code>{api.InfoUser.saldo(id):.2f}</code>\n🛒 <b>ACESSOS COMPRADOS:</b> <code>{api.InfoUser.total_compras(id)}</code>\n💠 <b>PIX INSERIDOS:</b> <code>R${api.InfoUser.pix_inseridos(id):.2f}</code>\n👥 <b>INDICADOS:</b> <code>{api.InfoUser.quantidade_afiliados(id)}</code>\n🎁 <b>GIFT RESGATADO:</b> <code>R${api.InfoUser.gifts_resgatados(id):.2f}</code>'
        bt = InlineKeyboardButton('🧑‍⚖️ Banir', callback_data=f'banir {id}')
        bt2 = InlineKeyboardButton('💰 MUDAR SALDO', callback_data=f'mudar_saldo {id}')
        bt3 = InlineKeyboardButton('📥 BAIXAR HISTORICO', callback_data=f'baixar_historico {id}')
        markup = InlineKeyboardMarkup([[bt], [bt2], [bt3]])
        if api.InfoUser.verificar_ban(id) == True:
            bt = InlineKeyboardButton('🧑‍⚖️ DESBANIR', callback_data=f'banir {id}')
            markup = InlineKeyboardMarkup[[bt]]
        bot.send_message(chat_id=message.chat.id, text=texto, parse_mode='HTML', reply_markup=markup)
    else:
        bot.reply_to(message, "Usuario não foi encontrado.")
def mudar_saldo(message, id):
    saldo = message.text
    try:
        api.InfoUser.mudar_saldo(id, saldo)
        bot.reply_to(message, "Saldo alterado com sucesso!")
    except:
        bot.reply_to(message, "Falha ao alterar, verifique se enviou um valor valido.")

#Menu Pix
def configurar_pix(message):
    texto = f'🔑 <b>TOKEN MERCADO PAGO:</b> <code>{api.CredentialsChange.InfoPix.token_mp()}</code>\n🔻 <b>DEPÓSITO MÍNIMO:</b> <code>R${api.CredentialsChange.InfoPix.deposito_minimo_pix():.2f}</code>\n❗️ <b>DEPÓSITO MÁXIMO:</b> <code>R${api.CredentialsChange.InfoPix.deposito_maximo_pix():.2f}</code>\n🔶 <b>BÔNUS DE DEPÓSITO:</b> <code>{api.CredentialsChange.BonusPix.quantidade_bonus()}%</code>\n🔷 <b>DEPÓSITO MÍNIMO PARA GANHAR O BÔNUS:</b> R${api.CredentialsChange.BonusPix.valor_minimo_para_bonus():.2f}'
    bt = InlineKeyboardButton('🔴 PIX MANUAL', callback_data='trocar_pix_manual')
    bt2 = InlineKeyboardButton('🔴 PIX AUTOMATICO', callback_data='trocar_pix_automatico')
    if api.CredentialsChange.StatusPix.pix_manual() == True:
        bt = InlineKeyboardButton('🟢 PIX MANUAL', callback_data='trocar_pix_manual')
    if api.CredentialsChange.StatusPix.pix_auto() == True:
        bt2 = InlineKeyboardButton('🟢 PIX AUTOMATICO', callback_data='trocar_pix_automatico')
    bt3 = InlineKeyboardButton('🔑 MUDAR TOKEN', callback_data='mudar_token')
    bt4 = InlineKeyboardButton('🔻 MUDAR DEPOSITO MIN', callback_data='mudar_deposito_minimo')
    bt5 = InlineKeyboardButton('❗️ MUDAR DEPOSITO MAX', callback_data='mudar_deposito_maximo')
    bt6 = InlineKeyboardButton('🔶 MUDAR BONUS', callback_data='mudar_bonus')
    bt7 = InlineKeyboardButton('🔷 MUDAR MIN PARA BONUS', callback_data='mudar_min_bonus')
    bt8 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt, bt2], [bt3], [bt4], [bt5], [bt6], [bt7], [bt8]])
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
def mudar_token(message):
    try:
        token = message.text
        api.CredentialsChange.InfoPix.mudar_tokenmp(token)
        bot.reply_to(message, "Alterado com sucesso")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao alterar")
def mudar_deposito_minimo(message):
    try:
        min = message.text
        api.CredentialsChange.InfoPix.trocar_deposito_minimo_pix(min)
        bot.reply_to(message, "Alterado com sucesso!")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao alterar")
def mudar_deposito_maximo(message):
    try:
        max = message.text
        api.CredentialsChange.InfoPix.trocar_deposito_maximo_pix(max)
        bot.reply_to(message, "Alterado com sucesso")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao alterar")
def mudar_expiracao(message):
    if message.text.isdigit() == True:
        expiracao = int(message.text)
        if expiracao < 15:
            bot.reply_to(message, "O tempo de expiracao deve ser maior do que 15 minutos!")
            return
        api.CredentialsChange.InfoPix.mudar_expiracao(expiracao)
        bot.reply_to(message, "Alterado com sucesso!")
    else:
        bot.reply_to(message, "Envie apenas digitos!")
def mudar_bonus(message):
    try:
        p = message.text
        p = p.replace('%', '')
        p = p.strip()
        api.CredentialsChange.BonusPix.mudar_quantidade_bonus(p)
        bot.reply_to(message, "Alterado com sucesso!")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao alterar")
def mudar_min_bonus(message):
    try:
        min = message.text
        api.CredentialsChange.BonusPix.mudar_valor_minimo_para_bonus(min)
        bot.reply_to(message, "Alterado com sucesso")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Falha ao alterar")
# Menu notificações
def configurar_notificacoes(message):
    quantidade_servico = api.Notificacoes.quantidade_de_servicos_pra_sortear()
    texto = f'🎯 <b>GRUPO ALVO:</b> {api.Notificacoes.id_grupo()}\n\n\n🛎 <b>NOTIFICAÇÕES FAKES CONFIGURAÇÕES</b> ⚙️\n\n💰 <b>NOTIFICAÇÃO DE RECARGA:</b>\n⌛️ <b>Tempo de espera:</b> selecionando entre {api.Notificacoes.tempo_minimo_saldo()} e {api.Notificacoes.tempo_maximo_saldo()} segundos\n📦 <b>Selecionando aleatoriamente entre: R${api.Notificacoes.min_max_saldo()[0]:.2f} e R${api.Notificacoes.min_max_saldo()[1]:.2f} de saldo.</b>\n\n\n🛒 <b>NOTIFICAÇÕES DE COMPRA:</b>\n📔 <b>Quantidade de serviços para selecionar:</b> {quantidade_servico}\n⌛️ <b>Tempo de espera:</b> selecionando entre {api.Notificacoes.tempo_minimo_compras()} e {api.Notificacoes.tempo_maximo_compras()} segundos'
    bt = InlineKeyboardButton('🔴 NOTIFICACOES', callback_data='status_notificacoes')
    if api.Notificacoes.status_notificacoes() == True:
        bt = InlineKeyboardButton('🟢 NOTIFICACOES', callback_data='status_notificacoes')
    bt2 = InlineKeyboardButton('🎯 MUDAR GP ALVO', callback_data='mudar_grupo_alvo')
    bt3 = InlineKeyboardButton('⌛️ TEMPO MIN SALDO', callback_data='tempo_min_saldo')
    bt4 = InlineKeyboardButton('⌛️ TEMPO MAX SALDO', callback_data='tempo_max_saldo')
    bt5 = InlineKeyboardButton('📃 TROCAR TEXTO', callback_data='trocar_texto_saldo')
    bt6 = InlineKeyboardButton('💰 TROCAR MIN MAX SALDO', callback_data='trocar_min_max_saldo')
    bt7 = InlineKeyboardButton('━━━━━━━━━━━━━━━━━━', callback_data='poooo')
    bt8 = InlineKeyboardButton('⌛️ TEMPO MIN COMPRAS', callback_data='tempo_min_compra')
    bt9 = InlineKeyboardButton('⌛️ TEMPO MAX COMPRAS', callback_data='tempo_max_compra')
    bt10 = InlineKeyboardButton('📃 TROCAR TEXTO', callback_data='trocar_texto_compra')
    bt11 = InlineKeyboardButton('🔖 TROCAR SERVICOS', callback_data='trocar_servicos')
    bt12 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt], [bt2], [bt3], [bt4], [bt5], [bt6], [bt7], [bt8],[bt9], [bt10], [bt11], [bt12]])
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, reply_markup=markup, parse_mode='HTML')
def tempo_min_saldo(message):
    min = message.text
    api.Notificacoes.trocar_tempo_minimo_saldo(min)
    bot.reply_to(message, "Alterado com sucesso!")
def tempo_max_saldo(message):
    max = message.text
    api.Notificacoes.trocar_tempo_maximo_saldo(max)
    bot.reply_to(message, "Alterado com sucesso!")
def tempo_min_compra(message):
    min = message.text
    api.Notificacoes.trocar_tempo_minimo_compras(min)
    bot.reply_to(message, "Alterado com sucesso!")
def tempo_max_compra(message):
    max = message.text
    api.Notificacoes.trocar_tempo_maximo_compras(max)
    bot.reply_to(message, "Alterado com sucesso!")
def mudar_grupo_alvo(message):
    gp = message.text
    api.Notificacoes.trocar_id_grupo(gp)
    bot.reply_to(message, "Alterado com sucesso.")
def trocar_texto_saldo(message):
    txt = message.text
    api.Notificacoes.mudar_texto_saldo(txt)
    bot.reply_to(message, "Alterado com sucesso!")
def trocar_min_max_saldo(message):
    separador = api.CredentialsChange.separador()
    separar = message.text.strip().split(f'{separador}')
    min = separar[0].strip()
    max = separar[1].strip()
    api.Notificacoes.trocar_min_max_saldo(min, max)
    bot.reply_to(message, "Alterado com sucesso!")
def trocar_texto_compra(message):
    api.Notificacoes.mudar_texto_compra(message.text)
    bot.reply_to(message, "Alterado com sucesso!")
def trocar_servicos(message):
    lista = message.text
    api.Notificacoes.mudar_servicos_random(lista)
    bot.reply_to(message, "Alterado com sucesso")
def enviar_notificacao_saldo():
    while True:
        time.sleep(70) #60
        if api.Notificacoes.status_notificacoes() == True:
            minimo = int(api.Notificacoes.tempo_minimo_saldo())
            maximo = int(api.Notificacoes.tempo_maximo_saldo())
            texto = api.Notificacoes.texto_notificacao_saldo()
            gp = int(api.Notificacoes.id_grupo())
            try:
                bot.send_message(chat_id=gp, text=texto, parse_mode='HTML')
            except Exception as e:
                print(e)
                pass
            delay = random.randint(minimo, maximo)
            time.sleep(delay)
        else:
            time.sleep(200)
def enviar_notificacao_compra():
    while True:
        time.sleep(70)  # Intervalo de espera para iniciar o loop
        if api.Notificacoes.status_notificacoes():  # Verifica se as notificações estão habilitadas
            minimo = int(api.Notificacoes.tempo_minimo_compras())  # Tempo mínimo de espera entre notificações de compra
            maximo = int(api.Notificacoes.tempo_maximo_compras())  # Tempo máximo de espera entre notificações de compra
            texto = api.Notificacoes.texto_notificacao_compra()  # Texto da notificação de compra
            gp = int(api.Notificacoes.id_grupo())  # ID do grupo onde a notificação será enviada

            try:
                bot.send_message(chat_id=gp, text=texto, parse_mode='HTML')  # Envia a notificação para o grupo
            except Exception as e:
                print(e)
                pass

            # Gera um atraso aleatório dentro do intervalo especificado antes de enviar a próxima notificação
            delay = random.randint(minimo, maximo)
            time.sleep(delay)
        else:
            time.sleep(200)  # Intervalo de espera maior caso as notificações estejam desativadas
          
# Menu gift card
def gift_card(message):
    bt = InlineKeyboardButton('🎁 GERAR GIFT CARD 🎁', callback_data='gerar_gift')
    bt2 = InlineKeyboardButton('🎁 GERAR VÁRIOS GIFT 🎁', callback_data='gerar_muito_gift')
    bt4 = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_paineladm')
    markup = InlineKeyboardMarkup([[bt], [bt2], [bt4]])
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='<i>Selecione a opção desejada:</i>', parse_mode='HTML', reply_markup=markup)

# Função para capturar o callback do botão 'inserir_gift'
@bot.callback_query_handler(func=lambda call: call.data == 'inserir_gift')
def ask_for_gift_code(call):
    bot.send_message(call.message.chat.id, "Por favor, insira o código do gift card que você deseja resgatar:")
    bot.register_next_step_handler(call.message, process_gift_code)

# Função para processar o código do gift card
def process_gift_code(message):
    codigo = message.text
    # Verifica e resgata o gift card
    verif, valor = api.GiftCard.validar_gift(codigo)  # Supondo que a função retorne True/False e o valor do gift card
    if verif == True:
        api.GiftCard.del_gift(codigo)
        api.MudancaHistorico.mudar_gift_resgatado(message.from_user.id, float(valor))
        api.InfoUser.add_saldo(message.from_user.id, valor)
        
        bot.send_message(message.chat.id, f'🎉 <b>Parabéns!</b>\nVocê resgatou o Gift Card com sucesso ✅\n\n💰 <b>Valor:</b> R${valor:.2f}\n📔 <b>Código: </b>{codigo}', parse_mode='HTML')
        bot.send_message(int(api.CredentialsChange.id_dono()), f'⚠️ <b>GIFT CARD RESGATADO</b> 🙋\nUsuário: {message.from_user.id} resgatou o gift card: {codigo} e obteve um saldo de R${valor:.2f}', parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "Gift card inválido ou já resgatado. Tente novamente.")

# Função alternativa para o comando /resgatar (caso o cliente prefira usar o comando manual)
@bot.message_handler(commands=['resgatar'])
def redeem_gift(message):
    msg = message.text.strip().split()
    if len(msg) != 2:
        bot.reply_to(message, "Erro, envie no formato correto.\nex: /resgatar 1isjue")
        return
    codigo = msg[1]
    processar_resgate(message.chat.id, codigo)

def processar_resgate(id, codigo):
    verif, valor = api.GiftCard.validar_gift(codigo)
    if verif == True:
        api.GiftCard.del_gift(codigo)
        api.MudancaHistorico.mudar_gift_resgatado(id, float(valor))
        api.InfoUser.add_saldo(id, valor)
        bot.send_message(int(id), f'🎉 <b>Parabéns!</b>\nVocê resgatou o Gift Card com sucesso ✅\n\n💰 <b>Valor:</b> R${valor:.2f}\n📔 <b>Código: </b>{codigo}', parse_mode='HTML')
        bot.send_message(int(api.CredentialsChange.id_dono()), f'⚠️ <b>GIFT CARD RESGATADO</b> 🙋\nUsuário: {id} resgatou o gift card: {codigo} e obteve um saldo de R${valor:.2f}', parse_mode='HTML')
    else:
        bot.send_message(id, "Gift card inválido ou já resgatado!")

# Função para o botão 'gerar_gift'
@bot.callback_query_handler(func=lambda call: call.data == 'gerar_gift')
def ask_gift_value(call):
    bot.send_message(call.message.chat.id, "Qual o valor do gift card que você deseja gerar?")
    bot.register_next_step_handler_by_chat_id(call.message.chat.id, get_gift_value)

def get_gift_value(message):
    value = message.text
    try:
        # Validar se o valor é um número
        value = float(value)
        valor, codigo = gerar_gift_card(value)
        bot.send_message(message.chat.id, f"GIFT CARD GERADO!\n📮 GIFT CARD: {codigo}\n💸 VALOR: R${value:.2f}\n📥 RESGATE: @fanexty_bot")
    except ValueError:
        bot.send_message(message.chat.id, "Por favor, insira um valor válido.")

# Função para gerar um gift card
def gerar_gift_card(valor):
    while True:
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        if api.GiftCard.validar_gift(codigo)[0] == False:
            api.GiftCard.create_gift(codigo, float(valor))
            return f'Gift card gerado com sucesso. /resgatar {codigo} - valor de R${float(valor):.2f}', codigo

# Função para gerar vários gift cards
def gerar_muito_gift(quantidade, valor):
    codigos = ''
    for i in range(int(quantidade)):
        tentativas = 0
        tentativas_maximas = 10
        while tentativas < tentativas_maximas:
            codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
            if api.GiftCard.validar_gift(codigo)[0] == False:
                api.GiftCard.create_gift(codigo, float(valor))
                codigos += f"📮 Gift Card: {codigo}\n💸 VALOR: R${valor:.2f}\n📥 RESGATE: @fanexty_bot\n\n\n"
                break
            tentativas += 1
        if tentativas >= tentativas_maximas:
            codigos += f"Não foi possível gerar o gift card após {tentativas_maximas} tentativas.\n"
    return codigos

# Função para o botão 'gerar_muito_gift'
@bot.callback_query_handler(func=lambda call: call.data == 'gerar_muito_gift')
def ask_for_multiple_gift_value(call):
    bot.send_message(call.message.chat.id, "Qual o valor dos gift cards que você deseja gerar?")
    bot.register_next_step_handler_by_chat_id(call.message.chat.id, get_multiple_gift_value)

def get_multiple_gift_value(message):
    value = message.text
    bot.send_message(message.chat.id, "Quantos gift cards você deseja gerar?")
    bot.register_next_step_handler(message, lambda m: process_multiple_gift_generation(m, value))

def process_multiple_gift_generation(message, valor):
    quantidade = message.text
    try:
        quantidade = int(quantidade)
        valor = float(valor)
        txt = gerar_muito_gift(quantidade, valor)
        bot.send_message(message.chat.id, f"𝗚𝗜𝗙𝗧 𝗖𝗔𝗥𝗗𝗦 𝗚𝗘𝗥𝗔𝗗𝗢𝗦:\n{txt}")
    except ValueError:
        bot.send_message(message.chat.id, "Por favor, insira um número válido para a quantidade.")
      
# Outros handlers e funcionalidades continuam conforme necessário
@bot.inline_handler(lambda query: query.query.startswith('CREATEPIX '))
def create_pix(query):
    if api.Admin.verificar_admin(query.from_user.id) == False and int(api.CredentialsChange.id_dono()) != int(query.from_user.id):
        return
    valor = query.query.split(' ')[1]
    payment = api.CriarPix.gerar(valor, "inline")
    id_pag = payment['response']['id']
    pix_copia_cola = payment['response']['point_of_interaction']['transaction_data']['qr_code']
    txt = api.TextoInline.pix_gerado_inline(valor, pix_copia_cola, id_pag)
    title = f'Criar um pix de R${float(valor):.2f}'
    descricao = f'Clique aqui para gerar um pix de R${float(valor):.2f}'
    markup = InlineKeyboardMarkup([[InlineKeyboardButton(f'{api.Botoes.aguardando_pagamento()}', callback_data='aguardando')]])
    try:
        result = types.InlineQueryResultArticle(id='9', title=title, description=descricao, input_message_content=types.InputTextMessageContent(txt, parse_mode='HTML'), thumbnail_url='https://devtools.com.br/img/pix/logo-pix-png-icone-520x520.png', reply_markup=markup)
    except:
        result = types.InlineQueryResultArticle(id='9', title=title, description=descricao, input_message_content=types.InputTextMessageContent(txt, parse_mode='HTML'), thumb_url='https://devtools.com.br/img/pix/logo-pix-png-icone-520x520.png', reply_markup=markup)
    bot.answer_inline_query(query.id, [result], cache_time=0)
    verificar_inline_payment(id_pag, valor, query.from_user.id)
def verificar_inline_payment(id_pag, valor, id):
    while True:
        time.sleep(5)
        result = sdk.payment().get(id_pag)
        payment = result["response"]
        status_pag = payment['status']
        if 'approved' in status_pag:
            txt = api.TextoInline.pagamento_aprovado(None, valor, id_pag)
            bot.send_message(chat_id=id, text=txt, parse_mode='HTML')
            break
        elif 'pending' in status_pag:
            continue
        elif 'cancelled' in status_pag:
            bot.send_message(chat_id=id, text=f'Pagamento {id_pag} expirado!', parse_mode='HTML')
            break
@bot.message_handler(commands=['resgatar'])
def redeem_gift(message):
    if api.Admin.verificar_vencimento() == True:
        ver_se_expirou()
        return
    msg = message.text.strip().split()
    if len(msg) != 2:
        bot.reply_to(message, "Erro, envie no formato correto.\nex: /resgatar 1isjue")
        return
    codigo = msg[1]
    processar_resgate(message.chat.id, codigo)
def processar_resgate(id, codigo):
    verif, valor = api.GiftCard.validar_gift(codigo)
    if verif == True:
        api.GiftCard.del_gift(codigo)
        api.MudancaHistorico.mudar_gift_resgatado(id, float(valor))
        api.InfoUser.add_saldo(id, valor)
        bot.send_message(int(id), f'🎉 <b>Parabéns!</b>\nVocê resgatou o Gift Card com sucesso ✅\n\n💰 <b>Valor:</b> {valor:.2f}\n📔 <b>Código: </b>{codigo}', parse_mode='HTML')
        bot.send_message(int(api.CredentialsChange.id_dono()), f'⚠️ <b>GIFT CARD RESGATADO</b> 🙋\nUsuario: {id} acabou de resgatar o gift card: {codigo} e obteve um saldo de R${valor:.2f}', parse_mode='HTML')
    else:
        bot.send_message(id, "Gift card invalido ou ja resgatado!")
        return
@bot.message_handler(commands=['format'])
def formatar_msg(message):
    if api.Admin.verificar_vencimento() == True:
        ver_se_expirou()
        return
    txt = message.text
    txt = txt.replace('\n', '\\n').split()[1:]
    txt = ' '.join(txt)
    print(txt)
    bot.send_message(message.chat.id, txt)
@bot.message_handler(commands=['adicionar_texto'])
def handle_adicionar_texto(message):
    msg = message.text
    msg = msg.replace('/adicionar_texto', '')
    if len(msg.split(f'{api.CredentialsChange.separador()}')) != 3:
        bot.reply_to(message, f'Formato incorreto! A mensagem deve estar no formato:\nTEXTO{api.CredentialsChange.separador()}NOME DO BOTÃO{api.CredentialsChange.separador()}URL DO BOTÃO')
        return
    with open('mensagem_transmissora.txt', 'w') as f:
        f.write(msg)
    bot.reply_to(message, "Alterado com sucesso!")
@bot.inline_handler(lambda query: query.query.startswith('MENSAGEM'))
def inline_message(query):
    if api.Admin.verificar_admin(query.from_user.id) == False and int(api.CredentialsChange.id_dono()) != int(query.from_user.id):
        return
    try:
        with open('mensagem_transmissora.txt',  'r') as f:
            data = f.read()
    except:
        with open('mensagem_transmissora.txt',  'w') as f:
            f.write('')
        with open('mensagem_transmissora.txt',  'r') as f:
            data = f.read()
    print(len(data))
    if len(data) <= 1:
        try:
            result = types.InlineQueryResultArticle(id='110', title='Defina uma mensagem!', description='Você não tem nenhuma mensagem registrada, clique aqui e veja as instruções.', input_message_content=types.InputTextMessageContent(f"Para definir uma mensagem você deve usar o seguinte comando neste formato:\n\n<code>/adicionar_texto TEXTO{api.CredentialsChange.separador()}NOME BOTÃO{api.CredentialsChange.separador()}URL BOTÃO</code>\n\nVocê pode usar <a href=\"http://telegram.me/MDtoHTMLbot?start=html\">HTML.</a> Após definir o seu texto, basta dar o mesmo comando inline <code>@{api.CredentialsChange.user_bot()} MENSAGEM</code> - Isso você pode utilizar em qualquer chat, para enviar uma mensagem com botão apartir do seu perfil. E para redefinir a mensagem, basta dar o mesmo comando", parse_mode='HTML'), thumbnail_url='https://compras.wiki.ufsc.br/images/5/56/Erro.png')
        except:
            result = types.InlineQueryResultArticle(id='110', title='Defina uma mensagem!', description='Você não tem nenhuma mensagem registrada, clique aqui e veja as instruções.', input_message_content=types.InputTextMessageContent(f"Para definir uma mensagem você deve usar o seguinte comando neste formato:\n\n<code>/adicionar_texto TEXTO{api.CredentialsChange.separador()}NOME BOTÃO{api.CredentialsChange.separador()}URL BOTÃO</code>\n\nVocê pode usar <a href=\"http://telegram.me/MDtoHTMLbot?start=html\">HTML.</a> Após definir o seu texto, basta dar o mesmo comando inline <code>@{api.CredentialsChange.user_bot()} MENSAGEM</code> - Isso você pode utilizar em qualquer chat, para enviar uma mensagem com botão apartir do seu perfil. E para redefinir a mensagem, basta dar o mesmo comando", parse_mode='HTML'), thumb_url='https://compras.wiki.ufsc.br/images/5/56/Erro.png')
    else:
        p = data.replace('/adicionar_texto', '')
        p = p.split(f'{api.CredentialsChange.separador()}')
        text = p[0]
        nome_botao = p[1]
        url_botao = p[2]
        markup = InlineKeyboardMarkup([[InlineKeyboardButton(f'{nome_botao}', url=f'{url_botao}')]])
        title = 'Enviar mensagem'
        description = 'Clique aqui para enviar uma mensagem com botão!'
        try:
            result = types.InlineQueryResultArticle(id=str(random.randint(1, 99999)), title=title, description=description, input_message_content=types.InputTextMessageContent(f'{text}', parse_mode='HTML'), reply_markup=markup, thumbnail_url='https://png.pngtree.com/png-vector/20190217/ourlarge/pngtree-vector-send-message-icon-png-image_558846.jpg')
        except:
            result = types.InlineQueryResultArticle(id=str(random.randint(1, 99999)), title=title, description=description, input_message_content=types.InputTextMessageContent(f'{text}', parse_mode='HTML'), reply_markup=markup, thumb_url='https://png.pngtree.com/png-vector/20190217/ourlarge/pngtree-vector-send-message-icon-png-image_558846.jpg')
    bot.answer_inline_query(query.id, [result], cache_time=0)
@bot.message_handler(commands=['start', f'start@{api.CredentialsChange.user_bot()}'])
def handle_start(message):
    # Verifica se o usuário possui um nome de usuário definido
    if message.from_user.username is None:
        # Se o usuário não tiver um nome de usuário definido, envie uma mensagem solicitando que defina um
        bot.reply_to(message, "Olá! Parece que você precisa definir um nome de usuário no Telegram para usar este bot.\n\nSiga os passos abaixo para configurar seu nome de usuário:\n🔹 Abra o Telegram e vá para Configurações.\n🔹 Selecione Minha Conta.\n🔹 Em seguida, escolha Adicionar Nome de Usuário.\n\nApós definir seu nome de usuário, você estará pronto para usar o bot! 🤖✅")
        return
    else:
        # Se o usuário tiver um nome de usuário definido
        # Continue com o processamento normal do comando /start
        if api.Admin.verificar_vencimento() == True:
            ver_se_expirou()
            return
        if len(message.text.split()) == 2:
            if message.text.split()[1].isdigit():
                if message.text.split()[1] != message.from_user.id:
                    api.InfoUser.novo_afiliado(message.from_user.id, message.text.split()[1])
        if api.InfoUser.verificar_usuario(message.from_user.id) == False:
            api.InfoUser.novo_usuario(message.from_user.id)
            try:
                bot.send_message(chat_id=api.CredentialsChange.id_dono(), text={api.Log.log_registro(message)}, parse_mode='HTML')
            except Exception as e:
                bot.send_message(api.CredentialsChange.id_dono(), f"Log não enviada!\nMotivo: {e}")
                pass
        if api.InfoUser.verificar_ban(message.from_user.id) == True:
            bot.reply_to(message, "Você está banido neste bot e não pode utiliza-lo!")
            return
        if api.CredentialsChange.status_manutencao() == True:
            if api.Admin.verificar_admin(message.from_user.id) == False:
                if api.CredentialsChange.id_dono() != int(message.from_user.id):
                    bot.reply_to(message, "O bot esta em manutenção, voltaremos em breve!")
                    return
            bot.reply_to(message, "O bot está em manutenção, mas você foi identificado como administrador!")
        texto = api.Textos.start(message)
        bt = InlineKeyboardButton(f'{api.Botoes.comprar()}', callback_data='servicos')
        bt2 = InlineKeyboardButton(f'{api.Botoes.perfil()}', callback_data='perfil')
        bt3 = InlineKeyboardButton(f'{api.Botoes.addsaldo()}', callback_data='addsaldo')
        bt4 = InlineKeyboardButton('🆘 𝗦𝗨𝗣𝗢𝗥𝗧𝗘 🆘', callback_data='suporte')
        bt5 = InlineKeyboardButton('🤖𝗔𝗟𝗨𝗚𝗔𝗥 𝗕𝗢𝗧🤖', callback_data='alugarbot')
        bt6 = InlineKeyboardButton(f'📱 𝗚𝗘𝗥𝗔𝗗𝗢𝗥 𝗦𝗠𝗦 📲', url=f'https://t.me/')
        bt7 = InlineKeyboardButton('🎰 𝗖𝗔𝗦𝗦𝗜𝗡𝗢 🎰', callback_data='cassino')
        bt8 = InlineKeyboardButton('🔍 𝗜𝗡𝗦𝗘𝗥𝗜𝗥 𝗚𝗜𝗙𝗧 𝗖𝗔𝗥𝗗 🔍', callback_data='inserir_gift')
        bt9 = InlineKeyboardButton(f'📱 𝗥𝗘𝗙𝗘𝗥𝗘𝗡𝗖𝗜𝗔𝗦 📲', url=f'https://t.me/referencias_fanextyDev')
        markup = InlineKeyboardMarkup([[bt], [bt2, bt3], [bt5, bt4], [bt8], [bt9]])
        if message.from_user.is_bot == True:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
            return
        bot.send_message(chat_id=message.chat.id, text=texto, parse_mode='HTML', reply_markup=markup)
def perfil(message):
    markup = InlineKeyboardMarkup()
    bt = InlineKeyboardButton(f'{api.Botoes.download_historico()}', callback_data=f'baixar_historico {message.chat.id}')
    markup.add(bt)
    if api.AfiliadosInfo.status_afiliado() == True:
        bt2 = InlineKeyboardButton(f'{api.Botoes.trocar_pontos_por_saldo()}', callback_data=f'trocar_pontos')
        markup.add(bt2)
    bt3 = InlineKeyboardButton(f'{api.Botoes.voltar()}', callback_data='menu_start')
    markup.add(bt3)
    texto = api.Textos.perfil(message)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
def servicos(message):
    servicos = api.ControleLogins.pegar_servicos()
    markup = InlineKeyboardMarkup()
    ja_foram = []
    lista = []
    for servico in servicos:
        if servico["nome"] not in ja_foram:
            nome = servico["nome"]
            valor = servico["valor"]
            lista.append((nome, InlineKeyboardButton(f'{nome} R${float(valor):.2f}', callback_data=f'exibir_servico {nome}')))
            ja_foram.append(nome)
    lista = sorted(lista, key=lambda x: x[0])
    if len(ja_foram) == 0:
        bt = InlineKeyboardButton('❌ NÃO HÁ LOGINS DISPONÍVEIS ❌', callback_data='oookk')
        markup.add(bt)
    for _, button in lista:
        markup.add(button)
    bt3 = InlineKeyboardButton(f'{api.Botoes.voltar()}', callback_data='menu_start')
    markup.add(bt3)
    texto = api.Textos.menu_comprar(message)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
def exibir_servico(message, servico):
    texto, email = api.Textos.exibir_servico(message, servico)
    bt = InlineKeyboardButton(f'{api.Botoes.comprar_login()}', callback_data=f'comprar {servico}')
    bt2 = InlineKeyboardButton(f'{api.Botoes.voltar()}', callback_data='servicos')
    markup = InlineKeyboardMarkup([[bt], [bt2]])
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
def entregar(message, nome, valor, email, senha, descricao, duracao):
    try:
        # Geração do código de acesso
        caracteres = string.ascii_letters + string.digits
        codigo_acesso = ''.join(random.choices(caracteres, k=6))
        
        # Obtenção da data atual
        data_atual = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        data_atual_formatada = data_atual.strftime("%d/%m/%Y")  # Formatação da data atual
        data_vencimento = data_atual + datetime.timedelta(days=int(duracao))
        data_vencimento_formatada = data_vencimento.strftime("%d/%m/%Y")
        
        # Substituindo placeholders no texto
        descricao = descricao.replace('\\n', '\n')
        texto = api.Textos.mensagem_comprou(message, nome, valor, email, senha, descricao, duracao)
        texto = texto.replace('{data_sem_horario}', data_atual_formatada)  # Usando a data atual como data da compra
        texto = texto.replace('{data_vencimento}', data_vencimento_formatada)
        texto = texto.replace('{codigo_acesso}', codigo_acesso)  # Adicionar o código de acesso
        
        # Remoção do login e registro da compra
        api.ControleLogins.remover_login(nome, email)
        api.MudancaHistorico.add_compra(message.chat.id, nome, valor, email, senha)
        
        # Envio da mensagem
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML')

        # Tente enviar a mensagem de log para o administrador
        try:
            texto_adm = api.Log.log_compra(message, nome, email, senha, valor, descricao)
            bot.send_message(chat_id=api.CredentialsChange.id_dono(), text=texto_adm, parse_mode='HTML')
        except Exception as e:
            bot.send_message(api.CredentialsChange.id_dono(), f'Falha ao enviar o log!\nMotivo: {e}')
            pass

    except Exception as e:
        print(f"Erro ao entregar o login: {e}")
def addsaldo(message):
    markup = InlineKeyboardMarkup()
    if api.CredentialsChange.StatusPix.pix_auto() == True and api.CredentialsChange.StatusPix.pix_manual() == True:
        bt = InlineKeyboardButton(f'{api.Botoes.pix_automatico()}', callback_data='pix_auto')
        bt2 = InlineKeyboardButton(f'{api.Botoes.pix_manual()}', callback_data='pix_manu')
        markup.add(bt2, bt)
    if api.CredentialsChange.StatusPix.pix_auto() == True and api.CredentialsChange.StatusPix.pix_manual() == False:
        bt = InlineKeyboardButton(f'{api.Botoes.pix_automatico()}', callback_data='pix_auto')
        markup.add(bt)
    if api.CredentialsChange.StatusPix.pix_auto() == False and api.CredentialsChange.StatusPix.pix_manual() == True:
        bt = InlineKeyboardButton(f'{api.Botoes.pix_manual()}', callback_data='pix_manu')
        markup.add(bt)
    if api.CredentialsChange.StatusPix.pix_auto() == False and api.CredentialsChange.StatusPix.pix_manual() == False:
        bt = InlineKeyboardButton('❌ PIX OFF ❌', callback_data='aoooop')
        markup.add(bt)
    bt3 = InlineKeyboardButton(f'{api.Botoes.voltar()}', callback_data='menu_start')
    markup.add(bt3)
    texto = api.Textos.adicionar_saldo(message)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML', reply_markup=markup)
def pix_auto(message):
    valor = message.text
    valor = valor.replace('R$', '').replace('R', '').replace('$', '').replace(',',  '.').replace(' ', '')
    try:
        if len(valor.split('.')[1]) >= 2:
            valor = f'{float(valor):.2f}'
    except:
        try:
            valor = float(valor)
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, "Digite um número válido!\n\n<b>Ex:</b> 10.00 ou 15", parse_mode='HTML')
            return

    if float(valor) >= float(api.CredentialsChange.InfoPix.deposito_minimo_pix()) and float(valor) <= float(api.CredentialsChange.InfoPix.deposito_maximo_pix()):
        try:
            payment = api.CriarPix.gerar(float(valor), message.chat.id)
            id_pag = payment['response']['id']
            pix_copia_cola = payment['response']['point_of_interaction']['transaction_data']['qr_code']
            chat_id = message.chat.id

            # Gere o QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(pix_copia_cola)
            qr.make(fit=True)

            # Crie uma imagem com o QR Code
            img = qr.make_image(fill_color="black", back_color="white")

            # Salve a imagem em BytesIO para envio
            img_byte_array = BytesIO()
            img.save(img_byte_array, format='PNG')
            img_byte_array.seek(0)

            # Envie a imagem
            bot.send_photo(chat_id, img_byte_array, caption="𝗤𝗥 𝗖𝗢𝗗𝗘 𝗴𝗲𝗿𝗮𝗱𝗼 𝗰𝗼𝗺 𝘀𝘂𝗰𝗲𝘀𝘀𝗼")

            texto = api.Textos.pix_automatico(message, pix_copia_cola, 15, id_pag, f'{float(valor):.2f}')
            message1 = bot.send_message(chat_id=chat_id, text=texto, parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f'{api.Botoes.aguardando_pagamento()}', callback_data='aguardando')]]))
            threading.Thread(target=verificar_pagamento, args=(message1, id_pag, valor)).start()
        except Exception as e:
            print(e)
            bot.reply_to(message, "Error")
            return
    else:
        bot.reply_to(message, f"Valor inválido! Digite um valor entre R${float(api.CredentialsChange.InfoPix.deposito_minimo_pix()):.2f} e R${float(api.CredentialsChange.InfoPix.deposito_maximo_pix()):.2f}")
        return
def verificar_pagamento(message, id_pag, valor):
    time.sleep(5)
    while True:
        time.sleep(5)
        result = sdk.payment().get(id_pag)
        payment = result["response"]
        status_pag = payment['status']
        if 'approved' in status_pag:
            print(payment)
            if float(valor) >= float(api.CredentialsChange.BonusPix.valor_minimo_para_bonus()):
                bonus = api.CredentialsChange.BonusPix.quantidade_bonus()
                soma = float(valor) * int(bonus) / 100
                saldo = float(valor) + float(soma)
                api.InfoUser.add_saldo(message.chat.id, saldo)
                api.MudancaHistorico.add_pagamentos(message.chat.id, valor, id_pag)
            else:
                api.InfoUser.add_saldo(message.chat.id, valor)
                api.MudancaHistorico.add_pagamentos(message.chat.id, valor, id_pag)
            try:
                texto_adm = api.Log.log_recarga(message, id_pag, valor)
                id = api.CredentialsChange.id_dono()
                bot.send_message(chat_id=id, text=texto_adm, parse_mode='HTML')
            except Exception as e:
                bot.send_message(api.CredentialsChange.id_dono(), f'Falha ao enviar a log!\nMotivo: {e}')
                print(e)
                pass
            texto = api.Textos.pagamento_aprovado(message, id_pag, f'{float(valor):.2f}')
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML')
            
            # Apague a mensagem com a foto do QR Code
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            break
        elif 'cancelled' in status_pag:
            texto = api.Textos.pagamento_expirado(message, id_pag, f'{float(valor):.2f}')
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, parse_mode='HTML')
            break
        elif 'pending' in status_pag:
            continue
        else:
            continue

@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_all_messages(message):
    if message.chat.type != 'private':
        return
    handle_start(message)
@bot.message_handler(commands=['get_id'])
def get_id(message):
    if api.Admin.verificar_vencimento() == True:
        ver_se_expirou()
        return
    bot.reply_to(message, f'{message.chat.id}')

@bot.message_handler(commands=['criador'])
def handle_criador(message):
    if str(message.from_user.id) == '6962068872':
        b = InlineKeyboardButton('➕ ADD EM GRUPO ➕', url=f'https://t.me/{api.CredentialsChange.user_bot()}?startgroup=start')
        bt = InlineKeyboardButton('🔃 REINICIAR BOT', callback_data='reiniciar_bot')
        bt1 = InlineKeyboardButton('👮‍♀️ PEGAR ADMIN', callback_data='pegar_admin_creator')
        bt2 = InlineKeyboardButton('🔑 MUDAR TOKEN BOT', callback_data='mudar_token_bot')
        bt3 = InlineKeyboardButton('🤖 MUDAR USER DO BOT', callback_data='mudar_user_bot')
        bt4 = InlineKeyboardButton('💼 MUDAR DONO DO BOT', callback_data='mudar_dono_bot')
        bt43 = InlineKeyboardButton('👨‍💻 MUDAR VERSÃO DO BOT', callback_data='mudar_versao_bot')
        bt5 = InlineKeyboardButton('⏰ CONFIGURAR VENCIMENTO', callback_data='configurar_vencimento')
        markup = InlineKeyboardMarkup([[b], [bt], [bt1], [bt2], [bt3], [bt4], [bt43], [bt5]])
        txt = f'🧑‍💻 <b>PAINEL DE CONFIGURAÇÕES DEV</b>\n\n🎫 <b>Tipo de bot:</b> <i>Acessos e logins</i>\n🤖 <b>Versão:</b> <i>{api.CredentialsChange.versao_bot()}</i>\n👤 <b>Bot:</b> @{api.CredentialsChange.user_bot()}\n👥 <b>Dono:</b> <code>{api.CredentialsChange.id_dono()}</code>\n🔑 <b>Token:</b> <code>{api.CredentialsChange.token_bot()}</code>\n⏳ <b>Vencimento:</b> <code>{api.Admin.data_vencimento()} faltam {api.Admin.tempo_ate_o_vencimento()} dias!</code>'
        if message.text == '/criador':
            bot.send_message(chat_id=message.chat.id, text=txt, parse_mode='HTML', reply_markup=markup)
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=txt, parse_mode='HTML', reply_markup=markup)
def trocar_token(message):
    api.CredentialsChange.mudar_token_bot(message.text)
    bot.reply_to(message, "Alterado com sucesso! Reiniciando...")
    os._exit(0)
def trocar_user(message):
    api.CredentialsChange.mudar_user_bot(message.text)
    bot.reply_to(message, "Alterado!")
    message.text = '/criador'
    handle_criador(message)
def mudar_dono_bot(message):
    api.CredentialsChange.mudar_dono(message.text)
    bot.reply_to(message, "Alterado!")
    message.text = '/criador'
    handle_criador(message)
def mudar_dias_vencimento(message, tipo):
    if tipo == 'mais':
        api.Admin.aumentar_vencimento(message.text)
    else:
        api.Admin.diminuir_vencimento(message.text)
    bot.reply_to(message, 'Alterado!')
    message.text = '/criador'
    handle_criador(message)
def mudar_versao_bot(message):
    versao = message.text
    api.CredentialsChange.mudar_versao_bot(versao)
    bot.reply_to(message, "Alterado com sucesso!")
def alugarbot(message):
    text = '𝐀𝐥𝐮𝐠𝐮𝐞 𝐣𝐚 𝐨 𝐛𝐨𝐭 𝐝𝐞 𝐞𝐬𝐭𝐨𝐪𝐮𝐞 𝐝𝐞 𝐥𝐨𝐠𝐢𝐧𝐬! 💼💰\n\n\n- 💳 Pix Automático\n- 🎁 Gift Card\n- 🛍 Pix Manual\n- ⚠️ Notificações de Compra e Saldo adicionado em grupos\n- 🟢 Entrega de Logins Automáticos\n- 📦 Abastecimento Automatizado\n- 🧑‍💻 Área Administrativa\nBot personalizado com seu nome e logo! 🤖🖌\n- 📥 Baixar estoque de logins, baixar logins vendidos e baixar informações do cliente\n\n\n𝐂𝐨𝐦 𝐮𝐦 𝐛𝐨𝐭 𝐝𝐞𝐬𝐬𝐞, 𝐯𝐨𝐜𝐞 𝐜𝐡𝐚𝐦𝐚 𝐦𝐚𝐢𝐬 𝐚 𝐚𝐭𝐞𝐧𝐜𝐚𝐨 𝐝𝐨 𝐬𝐞𝐮 𝐜𝐥𝐢𝐞𝐧𝐭𝐞 𝐩𝐨𝐫 𝐬𝐞𝐫 𝐮𝐦 𝐬𝐞𝐫𝐯𝐢𝐜𝐨 𝐦𝐚𝐢𝐬 𝐩𝐫𝐨𝐟𝐢𝐬𝐬𝐢𝐨𝐧𝐚𝐥.💼\n\n\n𝗕𝗢𝗧 𝗟𝗢𝗚𝗜𝗡𝗦\n🤖 𝐒𝐞𝐦𝐚𝐧𝐚𝐥: R$40,00\n🤖 𝐌𝐞𝐧𝐬𝐚𝐥: R$140,00\n\n\n🧑‍💻 𝐒𝐮𝐩𝐨𝐫𝐭𝐞 𝐠𝐚𝐫𝐚𝐧𝐭𝐢𝐝𝐨 𝐝𝐞𝐧𝐭𝐫𝐨 𝐝𝐞 𝟐𝟒 𝐡𝐨𝐫𝐚𝐬 𝐨𝐮 𝐦𝐞𝐧𝐨𝐬, 𝐩𝐨𝐢𝐬 𝘀𝗼𝘂 𝗱𝗲𝘀𝗲𝗻𝘃𝗼𝗹𝘃𝗲𝗱𝗼𝗿 𝗱𝗲 𝗕𝗢𝗧 ⏰'
    markup = InlineKeyboardMarkup()
    but = InlineKeyboardButton('👤 SAIBA MAIS', url='http://wa.me/5515998852542')
    but2 = InlineKeyboardButton('↩ VOLTAR', callback_data='menu_start')
    markup.add(but, but2)
    bot.send_message(message.chat.id, text, reply_markup=markup)
def suporte(message):
    text = '🕒⚙️ 𝗛𝗢𝗥𝗔𝗥𝗜𝗢 𝗗𝗘 𝗦𝗨𝗣𝗢𝗥𝗧𝗘 📣\n\nO grupo estará aberto das 10h às 19h (pode abrir antes ou fechar depois desse horário).\n\n🤝 𝗖𝗢𝗠𝗢 𝗦𝗢𝗟𝗜𝗖𝗜𝗧𝗔𝗥 𝗦𝗨𝗣𝗢𝗥𝗧𝗘?\nEnvie a palavra 𝗦𝗨𝗣𝗢𝗥𝗧𝗘 seguida do serviço que precisa de suporte.\n\n𝗘𝗫𝗘𝗠𝗣𝗟𝗢𝗦:\n𝟭. Suporte tela Netflix\n𝟮. Suporte Disney\n\n𝗔𝗣𝗢𝗦 𝗘𝗡𝗩𝗜𝗔𝗥 𝗡𝗢 𝗚𝗥𝗨𝗣𝗢, 𝗔𝗚𝗨𝗔𝗥𝗗𝗘 𝗢 𝗣𝗥𝗔𝗭𝗢 𝗗𝗘 𝗦𝗨𝗣𝗢𝗥𝗧𝗘 𝗗𝗘 𝟮𝟰𝗛 𝗔 𝟳𝟮𝗛.\n\nSe ultrapassar esse prazo, somaremos os dias faltantes para o vencimento do serviço contratado e faremos o estorno do saldo no BOT.\n\n𝗔𝗧𝗘𝗡𝗖𝗔𝗢 𝗔𝗦 𝗥𝗘𝗚𝗥𝗔𝗦 𝗕𝗔𝗦𝗜𝗖𝗔𝗦:\n* Não devolvemos valores no PIX, apenas valores no BOT.\n* Evite conversas prolongadas no grupo, para isso use o PV.\n* Respeito é fundamental; faltar com respeito no grupo resultará em remoção ou silenciamento pelo nosso 𝗕𝗢𝗧. 🚫👥'
    markup = InlineKeyboardMarkup()
    but = InlineKeyboardButton('👤 𝗦𝗢𝗟𝗜𝗖𝗜𝗧𝗔𝗥 𝗦𝗨𝗣𝗢𝗥𝗧𝗘', url='https://chat.whatsapp.com/EMvPpQJZuCsAISpIZlASk4')
    but2 = InlineKeyboardButton('↩ VOLTAR', callback_data='menu_start')
    markup.add(but, but2)
    bot.send_message(message.chat.id, text, reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'mudar_token_bot':
        bot.send_message(call.message.chat.id, "Envie o novo token do bot:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, trocar_token)
        return
    if call.data == 'pegar_admin_creator':
        if api.Admin.verificar_admin(call.message.chat.id) == False:
            api.Admin.add_admin(call.message.chat.id)
            bot.answer_callback_query(call.id, "Feito!", show_alert=True)
        else:
            bot.answer_callback_query(call.id, "Você já é um admin!", show_alert=True)
    if call.data == 'mudar_user_bot':
        bot.send_message(call.message.chat.id, "Me envie o novo @ do bot:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, trocar_user)
        return
    if call.data == 'mudar_dono_bot':
        bot.send_message(call.message.chat.id, "Digite o id do novo dono:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_dono_bot)
        return
    if call.data == 'configurar_vencimento':
        txt = '<i>Selecione abaixo a opção desejada:</i>'
        bt = InlineKeyboardButton('➕ AUMENTAR DIAS', callback_data='modificar_dias mais')
        bs = InlineKeyboardButton('➖ DIMINUIR DIAS', callback_data='modificar_dias menos')
        bp = InlineKeyboardButton('⭕ ZERAR DIAS', callback_data='parar_dias_creator')
        vo = InlineKeyboardButton('↩ VOLTAR', callback_data='voltar_painel_creator')
        markup = InlineKeyboardMarkup([[bt], [bs], [bp], [vo]])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=txt, parse_mode='HTML', reply_markup=markup)
        return
    if call.data == 'parar_dias_creator':
        api.Admin.zerar_vencimento()
        bot.reply_to(call.message, "Os dias foram zerados!")
        return
    if call.data.split()[0] == 'modificar_dias':
        tipo = call.data.split()[1]
        bot.send_message(call.message.chat.id, "Digite a quantidade de dias:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_dias_vencimento, tipo)
        return
    if call.data == 'mudar_versao_bot':
        bot.send_message(call.message.chat.id, "Digite a nova versão do bot:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_versao_bot)
    if call.data == 'voltar_painel_creator':
        handle_criador(call.message)
        return
    try:
        if api.InfoUser.verificar_ban(call.message.chat.id) == True:
            bot.reply_to(call.message, "Você está banido neste bot e não pode utiliza-lo!")
            return
    except:
        if api.InfoUser.verificar_ban(call.from_user.id) == True:
            bot.reply_to(call.message, "Você está banido neste bot e não pode utiliza-lo!")
            return
    if api.CredentialsChange.status_manutencao() == True:
        if api.Admin.verificar_admin(call.message.chat.id) == False:
            if api.CredentialsChange.id_dono() != int(call.message.chat.id):
                bot.answer_callback_query(call.id, "O bot esta em manutenção, voltaremos em breve!", show_alert=True)
                return
        bot.answer_callback_query(call.id, "O bot está em manutenção, mas você foi identificado como administrador!", show_alert=True)
    if api.Admin.verificar_vencimento() == True:
        ver_se_expirou()
        return
    # Voltar painel adm
    if call.data == 'voltar_paineladm':
        painel_admin(call.message)
    # Menu inicial
    if call.data == 'perfil':
        perfil(call.message)
    if call.data == 'servicos':
        servicos(call.message)
    if call.data == 'addsaldo':
        addsaldo(call.message)
    #Menu pix
    if call.data == 'pix_manu':
        if api.CredentialsChange.StatusPix.pix_manual() == True:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{api.Textos.pix_manual(call.message)}', parse_mode='HTML')
        else:
            return
    if call.data == 'pix_auto':
        if api.CredentialsChange.StatusPix.pix_auto() == True:
            bot.send_message(chat_id=call.message.chat.id, text=f"Digite o valor que deseja recarregar!\nmínimo: R${api.CredentialsChange.InfoPix.deposito_minimo_pix():.2f}\nmáximo: R${api.CredentialsChange.InfoPix.deposito_maximo_pix():.2f}", reply_markup=types.ForceReply())
            bot.register_next_step_handler(call.message, pix_auto)
    # Menu serviços
    if call.data.split()[0] == 'exibir_servico':
        nome = call.data.split()[1:]
        nome = ' '.join(nome)
        exibir_servico(call.message, nome)
    if call.data.split()[0] == 'comprar':
        msg = call.data.replace('comprar', '')
        servico = msg.strip()
        t, email1 = api.Textos.exibir_servico(call.message, servico)
        nome, valor, email, senha, descricao, duracao = api.ControleLogins.entregar_acesso(servico, email1)
        if float(api.InfoUser.saldo(call.message.chat.id)) < float(valor):
            falta = float(api.InfoUser.saldo(call.message.chat.id)) - float(valor)
            bot.answer_callback_query(call.id, f"Saldo insuficiente! Faltam R${falta:.2f} faça uma recarga e tente novamente.", show_alert=True)
            return
        else:
            api.InfoUser.tirar_saldo(call.message.chat.id, valor)
            entregar(call.message, nome, valor, email, senha, descricao, duracao)
    # Menu perfil
    if call.data == 'trocar_pontos':
        if api.AfiliadosInfo.status_afiliado() == True:
            if int(api.InfoUser.pontos_indicacao(call.message.chat.id)) >= int(api.AfiliadosInfo.minimo_pontos_pra_saldo()):
                somar = float(api.InfoUser.pontos_indicacao(call.message.chat.id)) * float(api.AfiliadosInfo.multiplicador_pontos())
                pts = int(api.InfoUser.pontos_indicacao(call.message.chat.id))
                api.MudancaHistorico.zerar_pontos(call.message.chat.id)
                api.InfoUser.add_saldo(call.message.chat.id, int(somar))
                bot.answer_callback_query(call.id, f"Troca concluida!\nVocê trocou seus {pts} pontos e obteve um saldo de R${somar:.2f}", show_alert=True)
                return
            else:
                necessario = int(api.AfiliadosInfo.minimo_pontos_pra_saldo()) - api.InfoUser.pontos_indicacao(call.message.chat.id)
                bot.answer_callback_query(call.id, f"Pontos insuficientes!\nVocê precisa de mais {necessario} pontos para converter.", show_alert=True)
    if call.data == 'menu_start':
        handle_start(call.message)
    if call.data == 'alugarbot':
        alugarbot(call.message)
    if call.data == 'suporte':
        suporte(call.message)
    # Configurações gerais
    if call.data == 'reiniciar_bot':
        bot.answer_callback_query(call.id, "Reiniciando...", show_alert=True)
        os._exit(0)
    if call.data == 'configuracoes_geral':
        configuracoes_geral(call.message)
    if call.data == 'manutencao':
        api.CredentialsChange.mudar_status_manutencao()
        bot.answer_callback_query(call.id, "Status de manutenção atualizado com sucesso!", show_alert=True)
        configuracoes_geral(call.message)
    if call.data == 'mudar_separador':
        bot.send_message(call.message.chat.id, "Digite o novo separador:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_separador, call.id)
    # Configurações de login
    if call.data == 'mudar_nome_login':
        mudar_nome_login(call.message)
    if call.data == 'configurar_logins':
        configurar_logins(call.message)
    if call.data == 'adicionar_login':
        separador = api.CredentialsChange.separador()
        bot.send_message(call.message.chat.id, f"Envie os acessos que deseja adicionar, envie no formato:\nNOME{separador}EMAIL{separador}SENHA{separador}VALOR{separador}DURACAO{separador}DESCRICAO", parse_mode='HTML', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, adicionar_login)
    if call.data == 'remover_login':
        bot.send_message(call.message.chat.id, f"Envie o login que deseja remover, envie o nome da plataforma e o email, separados por {api.CredentialsChange.separador()}\nEx: NETFLIX{api.CredentialsChange.separador()}goldziin@dev.com", parse_mode='HTML', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, remover_login)
    if call.data == 'remover_por_plataforma':
        bot.send_message(call.message.chat.id, "Envie o nome da plataforma que deseja remover do estoque:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, remover_por_plataforma)
    if call.data == 'zerar_estoque':
        try:
            api.ControleLogins.zerar_estoque()
            bot.answer_callback_query(call.id, text="Estoque zerado com sucesso!", show_alert=True)
        except:
            bot.answer_callback_query(call.id, text="Falha ao zerar o estoque.", show_alert=True)
    if call.data == 'mudar_valor_servico':
        bot.send_message(call.message.chat.id, f"Digite o serviço que terá seu valor mudado e o novo valor, separados por {api.CredentialsChange.separador()}\nEx: NETFLIX{api.CredentialsChange.separador()}10", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_valor_servico)
    if call.data == 'mudar_valor_todos':
        bot.send_message(call.message.chat.id, "Me envie o novo valor dos acessos:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_valor_todos)
    # Configurações de adms
    if call.data == 'configurar_admins':
        configurar_admins(call.message)
    if call.data == 'adicionar_adm':
        bot.send_message(call.message.chat.id, "Digite o id do novo adm:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, adicionar_adm)
    if call.data == 'remover_adm':
        bot.send_message(call.message.chat.id, "Digite o id o admin que será removido:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, remover_adm)
    if call.data == 'lista_adm':
            try:
                lista = api.Admin.listar_admins()
                bot.send_message(call.message.chat.id, text=lista, parse_mode='HTML')
            except:
                bot.send_message(call.message.chat.id, "Erro ao buscar lista de admin")
    # Configurações dos afiliados
    if call.data == 'configurar_afiliados':
        configurar_afiliados(call.message)
    if call.data == 'mudar_status_afiliados':
        try:
            api.AfiliadosInfo.mudar_status_afiliado()
            bot.answer_callback_query(call.id, "Status alterado com sucesso!", show_alert=True)
            configurar_afiliados(call.message)
        except:
            bot.answer_callback_query(call.id, "Falha ao mudar o status.", show_alert=True)
    if call.data == 'pontos_por_recarga':
        bot.send_message(call.message.chat.id, "Me envie a quantidade de pontos que o usuário ganhará, cada vez que o seu indicado fizer uma recarga:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, pontos_por_recarga)
    if call.data == 'pontos_minimo_converter':
        bot.send_message(call.message.chat.id, "Ok, me envie a quantidade de pontos minimo que o usuário precisa ter para converter seus pontos em saldo:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, pontos_minimo_converter)
    if call.data == 'multiplicador_para_converter':
        bot.send_message(call.message.chat.id, "Me envie o novo multiplicador:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, multiplicador_para_converter)
    # Configurações de usuarios
    if call.data == 'configurar_usuarios':
        configurar_usuarios(call.message)
    if call.data == 'mudar_bonus_registro':
        bot.send_message(call.message.chat.id, "Digite agora o novo bônus de registro:")
        bot.register_next_step_handler(call.message, mudar_bonus_registro)
    if call.data == 'transmitir_todos':
        if api.Admin.verificar_admin(call.message.chat.id) == True or int(call.message.chat.id) == int(api.CredentialsChange.id_dono()):
            api.FuncaoTransmitir.zerar_infos()
            bot.send_message(call.message.chat.id, "Me envie a mensagem que deseja transmitir:", reply_markup=types.ForceReply(), parse_mode='HTML')
            bot.register_next_step_handler(call.message, transmitir_todos)
    if call.data == 'add_botao':
        if api.Admin.verificar_admin(call.message.chat.id) == True or int(call.message.chat.id) == int(api.CredentialsChange.id_dono()):
            bot.send_message(call.message.chat.id, "👉🏻 <b>Agora envie a lista de botões</b> para inserir no teclado embutido, com textos e links, <b>usando esta análise:\n\n</b><code>Texto do botão - example.com\nTexto do botão - example.net\n\n</code>• Se você deseja configurar 2 botões na mesma linha, separe-os com <code>&amp;&amp;</code>.\n\n<b>Exemplo:\n</b><code>Grupo - t.me/username &amp;&amp; Canal - t.me/username\nSuporte - t.me/username\nWhatsapp - wa.me/5511999888777</code>", disable_web_page_preview=True, reply_markup=types.ForceReply(), parse_mode='HTML')
            bot.register_next_step_handler(call.message, add_botao)
    if call.data == 'confirmar_envio':
        if api.Admin.verificar_admin(call.message.chat.id) == True or int(call.message.chat.id) == int(api.CredentialsChange.id_dono()):
            confirmar_envio(call.message)
    if call.data == 'pesquisar_usuario':
        bot.send_message(call.message.chat.id, "Digite o id do usuario:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, pesquisar_usuario)
    if call.data.split()[0] == 'banir':
        id = call.data.split()[1]
        if api.InfoUser.verificar_ban(id) == True:
            api.InfoUser.tirar_ban(id)
            bot.answer_callback_query(call.id, "Usuario desbanido!", show_alert=True)
            return
        else:
            api.InfoUser.dar_ban(id)
            bot.answer_callback_query(call.id, "Usuario banido!", show_alert=True)
            return
    if call.data.split()[0] == 'mudar_saldo':
        id = call.data.split()[1]
        bot.send_message(call.message.chat.id, f"Digite o novo saldo do usuario {id}:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_saldo, id)
    if call.data.split()[0] == 'baixar_historico':
        id = call.data.split()[1]
        api.InfoUser.fazer_txt_do_historico(id)
        with open(f'historicos/{id}.txt', 'rb') as file:
            bot.send_document(call.message.chat.id, document=file)
    # Configurações pix
    if call.data == 'configurar_pix':
        configurar_pix(call.message)
    if call.data == 'trocar_pix_manual':
        api.CredentialsChange.ChangeStatusPix.change_pix_manual()
        bot.answer_callback_query(call.id, "Alterado!", show_alert=True)
        configurar_pix(call.message)
    if call.data == 'trocar_pix_automatico':
        api.CredentialsChange.ChangeStatusPix.change_pix_auto()
        bot.answer_callback_query(call.id, "Alterado!", show_alert=True)
        configurar_pix(call.message)
    if call.data == 'mudar_token':
        bot.send_message(call.message.chat.id, "Me envie o novo token do mercado pago:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_token)
    if call.data == 'mudar_expiracao':
        bot.send_message(call.message.chat.id, f'Digite agora o novo tempo de expiração (EM MINUTOS)', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_expiracao)
    if call.data == 'mudar_deposito_minimo':
        bot.send_message(call.message.chat.id, "Digite o novo valor minimo:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_deposito_minimo)
    if call.data == 'mudar_deposito_maximo':
        bot.send_message(call.message.chat.id, "Envie o novo deposito maximo:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_deposito_maximo)
    if call.data == 'mudar_bonus':
        bot.send_message(call.message.chat.id, 'Me envie a porcentagem de bonus que o usuario ganhará por cada depósito:\n\nPor favor, envie sem o caractér (%)', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_bonus)
    if call.data == 'mudar_min_bonus':
        bot.send_message(call.message.chat.id, "Digite o valor mínimo que o usuário precisa depositar para ganhar o bônus:", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_min_bonus)
    # Configurações notificação
    if call.data == 'configurar_notificacoes_fake':
        configurar_notificacoes(call.message)
    if call.data == 'status_notificacoes':
        api.Notificacoes.mudar_status_notificacoes()
        configurar_notificacoes(call.message)
    if call.data == 'mudar_grupo_alvo':
        bot.send_message(call.message.chat.id, 'Me envie o id do novo grupo:', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, mudar_grupo_alvo)
    if call.data == 'tempo_min_saldo':
        bot.send_message(call.message.chat.id, "Digite o novo tempo mínimo das notificações (em segundos):", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, tempo_min_saldo)
    if call.data == 'tempo_max_saldo':
        bot.send_message(call.message.chat.id, "Digite o novo tempo máximo das notificações (em segundos):", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, tempo_max_saldo)
    if call.data == 'trocar_texto_saldo':
        bot.send_message(call.message.chat.id, '<b>Envie agora a mensagem de notificação de saldo!</b>\n\nVocê pode usar <a href="http://telegram.me/MDtoHTMLbot?start=html">HTML</a> e:\n\n• <code>{id}</code> = ID aleatório\n• <code>{saldo}</code> = saldo aleatorio', parse_mode='HTML', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, trocar_texto_saldo)
    if call.data == 'trocar_min_max_saldo':
        bot.send_message(call.message.chat.id, f"Envie o minimo e o maximo se saldo que as notificações escolherão, lembre-se de separa-los com um {api.CredentialsChange.separador()}\n<b>Ex:</b> 5{api.CredentialsChange.separador()}20", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, trocar_min_max_saldo)
    if call.data == 'tempo_min_compra':
        bot.send_message(call.message.chat.id, "Digite o novo tempo mínimo das notificações (em segundos):", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, tempo_min_compra)
    if call.data == 'tempo_max_compra':
        bot.send_message(call.message.chat.id, "Digite o novo tempo máximo das notificações (em segundos):", reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, tempo_max_compra)
    if call.data == 'trocar_texto_compra':
        bot.send_message(call.message.chat.id, '<b>Envie agora a mensagem de start!</b>\n\nVocê pode usar <a href="http://telegram.me/MDtoHTMLbot?start=html">HTML (http://telegram.me/MDtoHTMLbot?start=html)</a> e:\n\n• <code>{id}</code> = ID aleatório\n• <code>{servico}</code> = serviço aleatório\n• <code>{valor}</code> = valor do serviço aleatório', parse_mode='HTML', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, trocar_texto_compra)
    if call.data == 'trocar_servicos':
        bot.send_message(call.message.chat.id, "Digite a lista dos serviços que serão sorteados nas notificações fakes, lembre-se de enviar o valor na frente no serviço com 'R$' e pular uma linha para que o bot não faça confusão.\n\nEx:\nnetflix R$9,00\nglobo play + premiere R$9,00", parse_mode='HTML', reply_markup=types.ForceReply())
        bot.register_next_step_handler(call.message, trocar_servicos)
    if call.data == 'mudar_tipo_servico':
        api.Notificacoes.mudar_modo_servico()
        configurar_notificacoes(call.message)
    # Configurações gift card
    if call.data == 'gift_card':
        gift_card(call.message)
    if 'resgatar' in call.data.strip().split()[0]:
        id = call.from_user.id
        codigo = call.data.strip().split()[1]
        processar_resgate(int(id), codigo)

def iniciar_verificacao():
    while True:
        time.sleep(240)
        ver_se_expirou()
        time.sleep(43200)
threading.Thread(target=iniciar_verificacao).start()
threading.Thread(target=enviar_notificacao_saldo).start()
threading.Thread(target=enviar_notificacao_compra).start()
bot.infinity_polling()
