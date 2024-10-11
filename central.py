import mercadopago
import json
import time
import telebot
import uuid
import datetime
import random
import html
import pytz
from datetime import timezone
from pytz import timezone

class ViewTime():
    def data_atual():
        data_e_hora_atuais = datetime.datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
        return data_e_hora_em_texto
    def hora_atual():
        data_e_hora_atuais = datetime.datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%H:%M:%S')
        hora_sao_paulo = datetime.datetime.strptime(hora_sao_paulo_em_texto, '%H:%M:%S').time()
        return hora_sao_paulo
class CredentialsChange():
    def user_bot():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return str(data["user_bot"])
    def mudar_user_bot(user):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["user_bot"] = str(user)
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def token_bot():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return str(data["api-bot"])
    def mudar_token_bot(token):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["api-bot"] = str(token)
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def versao_bot():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return str(data["version"])
    def mudar_versao_bot(version):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["version"] = version
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def verificar_premium():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        if int(data["premium"]) == 0:
            return False
        elif int(data["premium"]) == 1:
            return True
    def separador():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return str(data["separador"])
    def mudar_separador(separador):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["separador"] = separador
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def status_manutencao():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        if data["maintance"] == 'on':
            return True
        else:
            return False
    def mudar_status_manutencao():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        if data["maintance"] == "on":
            data["maintance"] = "off"
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
                return
        else:
            data["maintance"] = "on"
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
                return
    def id_dono():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        dono_id = data["id_dono"]
        return int(dono_id)
    def mudar_dono(id):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["id_dono"] = int(id)
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    class SuporteInfo():
        def link_suporte():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            return str(data["link_suporte"])
        def mudar_link_suporte(link):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["link_suporte"] = str(link)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
    class StatusPix():
        def pix_manual():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            if str(data["status_pix_manu"]) == 'on':
                return True
            else:
                return False
        def pix_auto():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            if str(data["status_pix_auto"]) == 'on':
                return True
            else:
                return False
    class ChangeStatusPix():
        def change_pix_manual():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            if str(data["status_pix_manu"]) == 'on':
                data["status_pix_manu"] = 'off'
                with open('settings/credenciais.json', 'w') as f:
                    json.dump(data, f, indent=4)
                return
            else:
                data["status_pix_manu"] = 'on'
                with open('settings/credenciais.json', 'w') as f:
                    json.dump(data, f, indent=4)
                return False
        def change_pix_auto():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            if str(data["status_pix_auto"]) == 'on':
                data["status_pix_auto"] = 'off'
                with open('settings/credenciais.json', 'w') as f:
                    json.dump(data, f, indent=4)
                return
            else:
                data["status_pix_auto"] = 'on'
                with open('settings/credenciais.json', 'w') as f:
                    json.dump(data, f, indent=4)
                return False
    class BonusPix():
        def quantidade_bonus():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            return int(data["bonus_pix"])
        def mudar_quantidade_bonus(porcentagem):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["bonus_pix"] = int(porcentagem)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
                return
        def valor_minimo_para_bonus():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            return int(data["bonus_pix_min"])
        def mudar_valor_minimo_para_bonus(valor_min):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["bonus_pix_min"] = int(valor_min)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
    class BonusRegistro():
        def bonus():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            return float(data["bonus_registro"])
        def mudar_bonus(novo_bonus):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["bonus_registro"] = float(novo_bonus)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
    class InfoPix():
        def token_mp():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            token = data["token_mp"]
            return str(token)
        def mudar_tokenmp(token):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["token_mp"] = str(token)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
            return
        def deposito_minimo_pix():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            return float(data["min_pix"])
        def trocar_deposito_minimo_pix(min):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["min_pix"] = float(min)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
                return
        def deposito_maximo_pix():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            return float(data["max_pix"])
        def trocar_deposito_maximo_pix(max):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["max_pix"] = float(max)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
                return
        def expiracao():
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            expiracao_time = data["expiracao_pix"]
            return int(expiracao_time)
        def mudar_expiracao(minutes):
            with open('settings/credenciais.json', 'r') as f:
                data = json.load(f)
            data["expiracao_pix"] = int(minutes)
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
                return True
class AfiliadosInfo():
    def status_afiliado():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        if data["afiliados"] == 'on':
            return True
        else:
            return False
    def mudar_status_afiliado():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        if data["afiliados"] == 'on':
            data["afiliados"] = "off"
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
            return
        else:
            data["afiliados"] = "on"
            with open('settings/credenciais.json', 'w') as f:
                json.dump(data, f, indent=4)
            return
    def pontos_por_recarga():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return int(data["pontos_by_indicate_buy"])
    def mudar_pontos_por_recarga(pontos):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["pontos_by_indicate_buy"] = int(pontos)
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
        return
    def minimo_pontos_pra_saldo():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return data["min_points_saldo"]
    def trocar_minimo_pontos_pra_saldo(min):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["min_points_saldo"] = int(min)
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def multiplicador_pontos():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return float(data["multiplicador_pontos"])
    def trocar_multiplicador_pontos(multiplicador):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["multiplicador_pontos"] = float(multiplicador)
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
class Notificacoes():
    def modo_servico():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return int(data["tipo_texto"])
    def mudar_modo_servico():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        if data["tipo_texto"] == 0:
            data["tipo_texto"] = 1
        else:
            data["tipo_texto"] = 0
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
    def status_notificacoes():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        if data["status_notify"] == 'on':
            return True
        else:
            return False
    def mudar_status_notificacoes():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        if data["status_notify"] == 'on':
            data["status_notify"] = 'off'
            with open('settings/notify.json', 'w') as f:
                json.dump(data, f, indent=4)
            return
        else:
            data["status_notify"] = 'on'
            with open('settings/notify.json', 'w') as f:
                json.dump(data, f, indent=4)
            return
    def id_grupo():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return int(data["id_grupo"])
    def trocar_id_grupo(id_grupo):
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        data["id_grupo"] = int(id_grupo)
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
        return
    def tempo_minimo_compras():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return int(data["time_min_compras"])
    def quantidade_de_servicos_pra_sortear():
        with open('settings/notificacao/servicos.txt', 'r') as f:
            file = f.read()
        quantidade = 0
        servicos = file.strip().split('\n')
        for servico in servicos:
            if len(servico) > 0:
                quantidade += 1
            pass
        return quantidade
    def pegar_servico_random():
        with open('settings/notificacao/servicos.txt', 'r') as f:
            file = f.read()
        file = file.splitlines()
        servico = random.choice(file)
        separar = servico.strip().split('R$')
        servico = separar[0]
        valor = separar[1]
        return servico, f'R${valor}'
    def pegar_servicos_disponiveis():
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        nomes = []
        for acesso in data["acessos"]:
            if acesso["nome"] in nomes:
                pass
            nomes.append({"nome": acesso["nome"], "valor": acesso["valor"]})
        sort = random.choice(nomes)
        return sort["nome"], f'R${sort["valor"]:.2f}'
    def mudar_servicos_random(lista):
        with open('settings/notificacao/servicos.txt', 'w') as f:
            f.write(lista)
    def trocar_tempo_minimo_compras(min):
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        data["time_min_compras"] = int(min)
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
    def tempo_maximo_compras():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return int(data["time_max_compras"])
    def trocar_tempo_maximo_compras(max):
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        data["time_max_compras"] = int(max)
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
    def tempo_minimo_saldo():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return int(data["time_min_saldo"])
    def trocar_tempo_minimo_saldo(min):
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        data["time_min_saldo"] = int(min)
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
    def tempo_maximo_saldo():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return int(data["time_max_saldo"])
    def trocar_tempo_maximo_saldo(max):
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        data["time_max_saldo"] = int(max)
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
    def min_max_saldo():
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        return float(data["saldo_min"]), float(data["saldo_max"])
    def trocar_min_max_saldo(min, max):
        with open('settings/notify.json', 'r') as f:
            data = json.load(f)
        data["saldo_min"] = int(min)
        data["saldo_max"] = int(max)
        with open('settings/notify.json', 'w') as f:
            json.dump(data, f, indent=4)
    def pegar_texto_saldo():
        with open('settings/notificacao/saldo.txt', 'r') as f:
            return f.read()
    def mudar_texto_saldo(texto):
        with open('settings/notificacao/saldo.txt', 'w') as f:
            f.write(texto)
    def pegar_texto_compra():
        with open('settings/notificacao/compra.txt', 'r') as f:
            return f.read()
    def mudar_texto_compra(texto):
        with open('settings/notificacao/compra.txt', 'w') as f:
            f.write(texto)
    def texto_notificacao_saldo():
        texto = Notificacoes.pegar_texto_saldo()
        id = random.randint(898012903, 4290812093)
        saldo_min, saldo_max = Notificacoes.min_max_saldo()
        saldo =  random.randint(int(saldo_min), int(saldo_max))
        texto = texto.replace('{id}', f'{id}').replace('{saldo}', f'{saldo}')
        return texto
    def texto_notificacao_compra():
        texto = Notificacoes.pegar_texto_compra()
        id = random.randint(898012903, 4290812093)
        if Notificacoes.modo_servico() == 0:
            servico, valor = Notificacoes.pegar_servico_random()
        else:
            servico, valor = Notificacoes.pegar_servicos_disponiveis()
        texto = texto.replace('{id}', f'{id}').replace('{servico}', f'{servico}').replace('{valor}', f'{valor}')
        return texto
class InfoUser():
    def verificar_usuario(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return True
            pass
        return False
    def novo_afiliado(usuario, indicador):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(usuario):
                if user["afiliado_por"] != 0:
                    return
                user["afiliado_por"] = int(indicador)
                break
        for user in data["users"]:
            if int(user["id"]) == int(indicador):
                if int(usuario) in user["afiliados"]:
                    return
                user["afiliacoes"] +=1
                user["afiliados"].append({"id_afiliado": int(usuario)})
                break
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
        return
    def novo_usuario(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        data["users"].append({"id": int(id), "banned": "False", "afiliado_por": 0, "saldo": 0, "gift_redeemed": 0, "total_compras": 0, "compras": [], "total_pagos": 0, "pagamentos": [], "pontos_indicado": 0, "afiliacoes": 0, "afiliados": []})
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def verificar_ban(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                if user["banned"] == 'True':
                    return True
                else:
                    return False
            pass
    def dar_ban(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                user["banned"] = "True"
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def tirar_ban(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                user["banned"] = "False"
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def saldo(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return float(user["saldo"])
    def add_saldo(id, novo_saldo):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                user["saldo"] += float(novo_saldo)
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def tirar_saldo(id, novo_saldo):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                saldo = user["saldo"]
                user["saldo"] = float(saldo) - float(novo_saldo)
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def mudar_saldo(id, novo_saldo):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                user["saldo"] = float(novo_saldo)
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def gifts_resgatados(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return float(user["gift_redeemed"])
            pass
        return 0
    def total_compras(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return user["total_compras"]
            pass
    def total_pagos(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return user["total_pagos"]
            pass
        return False
    def pix_inseridos(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        quantity = 0.0
        for user in data["users"]:
            if int(user["id"]) == int(id):
                if len(user["pagamentos"]) > 0:
                    for pagamento in user["pagamentos"]:
                        quantity += float(pagamento["valor"])
                    pass
                pass
            pass
        return float(quantity)
    def pontos_indicacao(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return user["pontos_indicado"]
            pass
    def trocar_pontos(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                if int(user["pontos_indicado"]) >= int(AfiliadosInfo.minimo_pontos_pra_saldo()):
                    somar = int(user["pontos_indicado"]) * AfiliadosInfo.multiplicador_pontos()
                    user["pontos_indicado"] = 0
                    user["saldo"] = float(somar)
                    with open('database/users.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    return True
                else:
                    return False
            pass
    def fazer_txt_do_historico(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                #if len(user["compras"]) > 0:
                    historico = f'HISTORICO DETALHADO @{CredentialsChange.user_bot()}\n_______________________'
                    historico += '\n\nCOMPRAS:'
                    for compra in user["compras"]:
                        servico = compra["servico"]
                        valor = compra["valor"]
                        email = compra["email"]
                        senha = compra["senha"]
                        data = compra["data"]
                        historico += f'\nServiço: {servico}\nValor: {valor}\nEmail: {email}\nSenha: {senha}\nData: {data}'
                        pass
                    historico += '\n_______________________\n\nPAGAMENTOS:'
                    for pagamento in user["pagamentos"]:
                        id_pagamento = pagamento["id_pagamento"]
                        valor = pagamento["valor"]
                        data = pagamento["data"]
                        historico += f'\nId pagamento: {id_pagamento}\nValor: {valor}\n Data: {data}'
                        break
                #pass
            pass
        with open(f'historicos/{id}.txt', 'w') as f:
            f.write(historico)
        return True
    def quantidade_afiliados(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                return int(user["afiliacoes"])
        return None
class MudancaHistorico():
    def mudar_gift_resgatado(id, valor):
        with open('database/users.json') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                user["gift_redeemed"] += float(valor)
                with open('database/users.json', 'w') as f:
                    json.dump(data, f, indent=4)
                break
            pass
    def add_compra(id, servico, valor, email, senha):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(id) == int(user["id"]):
                user["total_compras"] +=1
                user["compras"].append({"servico": servico, "valor": valor, "email": email, "senha": senha, "data": f"{ViewTime.data_atual()} as {ViewTime.hora_atual()}"})
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
    def add_pagamentos(id, valor, id_pag):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                afiliado_por = user["afiliado_por"]
                user["total_pagos"] += 1
                user["pagamentos"].append({"id_pagamento": id_pag, "valor": valor, "data": f"{ViewTime.data_atual()} as {ViewTime.hora_atual()}"})
                break
            pass
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=4)
        if AfiliadosInfo.status_afiliado() == True and int(afiliado_por) != 0:
            with open('database/users.json', 'r') as f:
                data = json.load(f)
            for user in data["users"]:
                if int(afiliado_por) == int(user["id"]):
                    user["pontos_indicado"] += int(AfiliadosInfo.pontos_por_recarga())
                    break
                pass
            with open('database/users.json', 'w') as f:
                json.dump(data, f, indent=4)
            return
        else:
            return
    def zerar_pontos(id):
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        for user in data["users"]:
            if int(user["id"]) == int(id):
                user["pontos_indicado"] = 0
                with open('database/users.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    break
            else:
                pass
class GiftCard():
    def validar_gift(codigo):
        with open("database/gift_card.json", 'r') as f:
            data = json.load(f)
        for gift in data['gift']:
            if gift["codigo"] == codigo:
                valor = float(gift["valor"])
                return True, valor
        return False, 0
    def listar_gift():
        with open('database/gift_card.json', 'r') as f:
            data = json.load(f)
        msg = ''
        for gift in data["gift"]:
            msg += f'<code>{gift["codigo"]}</code> R${float(gift["valor"]):.2f}\n'
        return msg
    def create_gift(codigo, valor):
        with open("database/gift_card.json", 'r') as f:
            data = json.load(f)
        data["gift"].append({"codigo": codigo, "valor": float(valor)})
        with open("database/gift_card.json", 'w') as j:
            json.dump(data, j, indent=4)
        return True
    def del_gift(codigo):
        with open("database/gift_card.json", 'r') as f:
            data = json.load(f)
        for gift in data["gift"]:
            if gift["codigo"] == codigo:
                data["gift"].remove(gift)
                with open("database/gift_card.json", 'w') as f:
                    json.dump(data, f, indent=4)
                return True
            pass
        return False

class FuncaoTransmitir():
    def formatar_html(texto, entities):
        padrao_tags_html = r"<\/?[a-zA-Z]+[^>]*>"
        tags_encontradas = re.findall(padrao_tags_html, texto)
        if tags_encontradas:
            return texto
        tags_html = {
            'bold': ('<b>', '</b>'),
            'italic': ('<i>', '</i>'),
            'code': ('<code>', '</code>')
        }
        formatted_text = texto
        offset_adjustment = 0
        entities = sorted(entities, key=lambda e: e["offset"], reverse=True)
        for entity in entities:
            entity_type = entity["type"]
            start_offset = entity["offset"] + offset_adjustment
            end_offset = start_offset + entity["length"]
            if entity_type in tags_html:
                tag_abertura, tag_fechamento = tags_html[entity_type]
                formatted_text = formatted_text[:start_offset] + tag_abertura + formatted_text[start_offset:end_offset] + tag_fechamento + formatted_text[end_offset:]
                offset_adjustment += len(tag_abertura) + len(tag_fechamento)
        return formatted_text
    def pegar_foto():
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
            return data["photo"]
    def pegar_texto():
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
            return data["texto"]
    def pegar_markup():
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
            return data["markup"]
    def adicionar_foto(photo):
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
        data["photo"] = photo
        with open('database/info_transmitir.json', 'w') as f:
            data = json.dump(data, f, indent=4)
    def adicionar_texto(txt):
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
        data["texto"] = txt
        with open('database/info_transmitir.json', 'w') as f:
            json.dump(data, f, indent=4)
    def adicionar_entitie(ent):
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
        entities = []
        if ent == None:
            return
        for entity in ent:
            entities.append(entity.to_dict())
        txt = FuncaoTransmitir.formatar_html(data["texto"], entities)
        data["texto"] = txt
        with open('database/info_transmitir.json', 'w') as f:
            json.dump(data, f, indent=4)
    def adicionar_markup(markup):
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
        if markup is not None:
            inline_keyboard = []
            for row in markup.keyboard:
                row_buttons = []
                for but in row:
                    button_dict = {
                        'text': but.text,
                        'url': but.url
                    }
                    row_buttons.append(button_dict)
                inline_keyboard.append(row_buttons)
            data["markup"] = inline_keyboard
        else:
            data["markup"] = None
        with open('database/info_transmitir.json', 'w') as f:
            json.dump(data, f, indent=4)
    def zerar_infos():
        with open('database/info_transmitir.json', 'r') as f:
            data = json.load(f)
        data["texto"] = None
        data["photo"] = None
        data["markup"] = None
        with open('database/info_transmitir.json', 'w') as f:
            json.dump(data, f, indent=4)


class ControleLogins():
    # add login
    def add_login(nome, valor, descricao, email, senha, duracao):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        data["acessos"].append({"nome": nome, "valor": valor, "descricao": descricao, "email": email, "senha": senha, "duracao": duracao})
        with open('database/acessos.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    # remover login
    def remover_login(nome, email):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            if acesso["nome"] == nome and acesso["email"] == email:
                data["acessos"].remove(acesso)
                with open('database/acessos.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    return True
            pass
        return False
    # listar servicos
    def pegar_servicos():
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        lista = []
        for acesso in data["acessos"]:
            lista.append({"nome": acesso["nome"], "valor": acesso["valor"]})
            pass
        return lista
    def estoque_total():
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        quantity = 0
        for acesso in data["acessos"]:
            quantity +=1
        return quantity
    # pegar estoque por nome
    def pegar_estoque(nome):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        quantidade = 0
        for acesso in data["acessos"]:
            if acesso["nome"] == nome:
                quantidade +=1
            pass
        return quantidade
    def pegar_estoque_detalhado():
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        ja_foram = []
        lista = []
        for acesso in data["acessos"]:
            if acesso["nome"] not in ja_foram:
                quant = ControleLogins.pegar_estoque(acesso["nome"])
                lista.append({"nome": acesso["nome"], "quantidade": quant})
                ja_foram.append(acesso["nome"])
                continue
            else:
                pass
        montagem = "<b>ACESSOS EM ESTOQUE:</b>\n"
        logins = ''
        for login in lista:
            nome = login["nome"]
            quantidade = login["quantidade"]
            logins += f'\n{nome}: {quantidade}'
        montagem += f"\n<code>{logins}</code>"
        return montagem
    def criar_estoque_detalhado():
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        mensagem = "ACESSOS EM ESTOQUE:\n"
        for acesso in data["acessos"]:
            mensagem += f'\n\nNome: {acesso["nome"]}\nValor: {acesso["valor"]}\nDescricao: {acesso["descricao"]}\nEmail: {acesso["email"]}\nSenha: {acesso["senha"]}\nDuracao: {acesso["duracao"]}'
        with open('historicos/estoque_detalhado.txt', 'w') as f:
            f.write(mensagem)
        return True
    def arquivo_estoque_detalhado():
        with open('historicos/estoque_detalhado.txt', 'rb') as file:
            return file
    def remover_por_nome(nome):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            if str(acesso["nome"]) == str(nome):
                data["acessos"].remove(acesso)
            else:
                pass
        with open('database/acessos.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    def zerar_estoque():
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        data["acessos"] = []
        with open('database/acessos.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    def mudar_valor_por_nome(nome, novo_valor):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            if acesso["nome"] == nome:
                acesso["valor"] = float(novo_valor)
                continue
            pass
        with open('database/acessos.json', 'w') as f:
            json.dump(data, f, indent=4)
    def mudar_valor_de_todos(valor):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            acesso["valor"] = float(valor)
            continue
        with open('database/acessos.json', 'w') as f:
            json.dump(data, f, indent=4)
    def pegar_info(nome):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            if acesso["nome"] == nome:
                return acesso["nome"], acesso["valor"], acesso["descricao"],  acesso["duracao"], acesso["email"]
    def entregar_acesso(nome, email):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            if acesso["nome"] == nome:
                if acesso["email"] == email:
                    return acesso["nome"], acesso["valor"], acesso["email"], acesso["senha"], acesso["descricao"],  acesso["duracao"]
                else:
                    pass
            else:
                pass
    def pegar_info_entrega(nome, email):
        with open('database/acessos.json', 'r') as f:
            data = json.load(f)
        for acesso in data["acessos"]:
            if acesso["nome"] == nome:
                if acesso["email"] == email:
                    return acesso
                else:
                    pass
            else:
                pass
class Admin():
    def total_users():
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        quantity = 0
        for user in data["users"]:
            quantity +=1
        return int(quantity)
    def verificar_vencimento():
        time = Admin.tempo_ate_o_vencimento()
        if int(time) <= 0:
            return True
    def data_vencimento():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return str(data["vencimento_bot"])
    def tempo_ate_o_vencimento():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data_vencimento_str = data['vencimento_bot']
        data_vencimento = datetime.datetime.strptime(data_vencimento_str, '%d/%m/%Y').date()
        data_atual = datetime.datetime.now().date()
        diferenca = data_vencimento - data_atual
        return diferenca.days
    def aumentar_vencimento(dias):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        vencimento = int(dias)
        vencimento_bot_str = data['vencimento_bot']
        vencimento_bot = datetime.datetime.strptime(vencimento_bot_str, '%d/%m/%Y')
        nova_data = vencimento_bot + datetime.timedelta(days=vencimento)
        data["vencimento_bot"] = nova_data.strftime('%d/%m/%Y')
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
            return True
    def diminuir_vencimento(days):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        vencimento = int(days)
        vencimento_str = data["vencimento_bot"]
        vencimento_bot = datetime.datetime.strptime(vencimento_str, '%d/%m/%Y')
        nova_data = vencimento_bot - datetime.timedelta(days=vencimento)
        data["vencimento_bot"] = nova_data.strftime('%d/%m/%Y')
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def zerar_vencimento():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["vencimento_bot"] = '01/01/2023'
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def receita_total():
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        receita = 0.0
        for user in data["users"]:
            if user["total_pagos"] > 0:
                for pagamento in user["pagamentos"]:
                    receita += float(pagamento["valor"])
                    continue
                continue
            pass
        return float(receita)
    def receita_hoje():
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        tz = pytz.timezone('America/Sao_Paulo')
        today = datetime.datetime.now(tz).strftime('%d/%m/%Y')
        receita_dia = 0.0
        for user in data["users"]:
            if user["total_pagos"] > 0:
                for pagamento in user["pagamentos"]:
                    if str(pagamento['data'].split(' ')[0]) == str(today):
                        receita_dia += float(pagamento['valor'])
                        pass
                pass
            pass
        return receita_dia
    def acessos_vendidos():
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        quantity = 0
        for user in data["users"]:
            if user["total_compras"] > 0:
                quantity += user["total_compras"]
                continue
            pass
        return int(quantity)
    def acessos_vendidos_hoje():
        with open('database/users.json', 'r') as f:
            data = json.load(f)
        tz = pytz.timezone('America/Sao_Paulo')
        today = datetime.datetime.now(tz).strftime('%d/%m/%Y')
        quantidade = 0
        for user in data["users"]:
            if user["total_compras"] > 0:
                for compras in user["compras"]:
                    if str(compras["data"].split(' ')[0]) == str(today):
                        quantidade += 1
                        continue
                    pass
                pass
            pass
        return quantidade
    def verificar_admin(id):
        with open('database/admins.json', 'r') as f:
            data = json.load(f)
        for admin in data["admins"]:
            if int(admin["id"]) == int(id):
                return True
            pass
        return False
    def add_admin(id):
        with open('database/admins.json', 'r') as f:
            data = json.load(f)
        data["admins"].append({"id": int(id)})
        with open('database/admins.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    def quantidade_admin():
        with open('database/admins.json', 'r') as f:
            data = json.load(f)
        quantity = 0
        for admin in data["admins"]:
            quantity +=1
        return quantity
    def listar_admins():
        with open('database/admins.json', 'r') as f:
            data = json.load(f)
        adm_list = '<b>👮 LISTA DE ADMINS:</b> 🚨\n\n'
        for admin in data["admins"]:
            adm_list += f'\n<b>ADMIN ID</b>: <code>{admin["id"]}</code>'
        return adm_list
    def remover_admin(id):
        with open('database/admins.json', 'r') as f:
            data = json.load(f)
        for admin in data["admins"]:
            if int(admin["id"]) == int(id):
                data["admins"].remove(admin)
                with open('database/admins.json', 'w') as f:
                    json.dump(data, f, indent=4)
                return True
            pass
class Textos():
    def start(message):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        if str(message.chat.id).startswith('-'):
            id = message.from_user.id
            first_name = message.from_user.first_name
            username = message.from_user.username
        link_afiliado = f'https://t.me/{CredentialsChange.user_bot()}?start={message.chat.id}'
        saldo = InfoUser.saldo(id)
        pontos_indicacao = InfoUser.pontos_indicacao(id)
        quantidade_afiliados = InfoUser.quantidade_afiliados(id)
        quantidade_compras = InfoUser.total_compras(id)
        pix_inseridos = f'{InfoUser.pix_inseridos(id):.2f}'
        gifts_resgatados = f'{InfoUser.gifts_resgatados(id):.2f}'
        with open('textos/start.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{link_afiliado}', f'{link_afiliado}').replace('{saldo}', f'{saldo:.2f}').replace('{pontos_indicacao}', f'{pontos_indicacao}').replace('{quantidade_afiliados}', f'{quantidade_afiliados}').replace('{quantidade_compras}', f'{quantidade_compras}').replace('{pix_inseridos}', f'{pix_inseridos}').replace('{gifts_resgatados}', f'{gifts_resgatados}')
        return texto
    def perfil(message):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        link_afiliado = f'https://t.me/{CredentialsChange.user_bot()}?start={message.chat.id}'
        saldo = InfoUser.saldo(id)
        pontos_indicacao = InfoUser.pontos_indicacao(id)
        quantidade_afiliados = InfoUser.quantidade_afiliados(id)
        quantidade_compras = InfoUser.total_compras(id)
        pix_inseridos = f'{InfoUser.pix_inseridos(id):.2f}'
        gifts_resgatados = f'{InfoUser.gifts_resgatados(id):.2f}'
        with open('textos/perfil.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{link_afiliado}', f'{link_afiliado}').replace('{saldo}', f'{saldo:.2f}').replace('{pontos_indicacao}', f'{pontos_indicacao}').replace('{quantidade_afiliados}', f'{quantidade_afiliados}').replace('{quantidade_compras}', f'{quantidade_compras}').replace('{pix_inseridos}', f'{pix_inseridos}').replace('{gifts_resgatados}', f'{gifts_resgatados}')
        return texto
    def adicionar_saldo(message):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        link_afiliado = f'https://t.me/{CredentialsChange.user_bot()}?start={message.chat.id}'
        saldo = InfoUser.saldo(id)
        pontos_indicacao = InfoUser.pontos_indicacao(id)
        quantidade_afiliados = InfoUser.quantidade_afiliados(id)
        quantidade_compras = InfoUser.total_compras(id)
        pix_inseridos = f'{InfoUser.pix_inseridos(id):.2f}'
        gifts_resgatados = f'{InfoUser.gifts_resgatados(id):.2f}'
        with open('textos/adicionar_saldo.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{link_afiliado}', f'{link_afiliado}').replace('{saldo}', f'{saldo:.2f}').replace('{pontos_indicacao}', f'{pontos_indicacao}').replace('{quantidade_afiliados}', f'{quantidade_afiliados}').replace('{quantidade_compras}', f'{quantidade_compras}').replace('{pix_inseridos}', f'{pix_inseridos}').replace('{gifts_resgatados}', f'{gifts_resgatados}')
        return texto
    def pix_manual(message):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        saldo = InfoUser.saldo(id)
        deposito_minimo = f'{CredentialsChange.InfoPix.deposito_minimo_pix():.2f}'
        with open('textos/pix_manual.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{saldo}', f'{saldo:.2f}').replace('{deposito_minimo}', f'{deposito_minimo}')
        return texto
    def pix_automatico(message, pix_copia_cola, expiracao, id_pagamento, valor):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        saldo = InfoUser.saldo(id)
        deposito_minimo = f'{CredentialsChange.InfoPix.deposito_minimo_pix():.2f}'
        pix_inseridos = f'{InfoUser.pix_inseridos(id):.2f}'
        with open('textos/pix_automatico.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{saldo}', f'{saldo:.2f}').replace('{pix_inseridos}', f'{pix_inseridos}').replace('{pix_copia_cola}', f'{pix_copia_cola}').replace('{expiracao}', f'{expiracao}').replace('{id_pagamento}', f'{id_pagamento}').replace('{valor}', f'{valor}').replace('{deposito_minimo}', f'{deposito_minimo}')
        return texto
    def pagamento_expirado(message, id_pagamento, valor):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        link_afiliado = f'https://t.me/{CredentialsChange.user_bot()}?start={message.chat.id}'
        saldo = InfoUser.saldo(id)
        with open('textos/pagamento_expirado.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{link_afiliado}', f'{link_afiliado}').replace('{saldo}', f'{saldo:.2f}').replace('{id_pagamento}', f'{id_pagamento}').replace('{valor}', f'{valor}')
        return texto
    def pagamento_aprovado(message, id_pagamento, valor):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        link_afiliado = f'https://t.me/{CredentialsChange.user_bot()}?start={message.chat.id}'
        saldo = InfoUser.saldo(id)
        with open('textos/pagamento_aprovado.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{link_afiliado}', f'{link_afiliado}').replace('{saldo}', f'{saldo:.2f}').replace('{id_pagamento}', f'{id_pagamento}').replace('{valor}', f'{valor}')
        return texto
    def menu_comprar(message):
        first_name = message.chat.first_name
        username = message.chat.username
        id = message.chat.id
        link_afiliado = f'https://t.me/{CredentialsChange.user_bot()}?start={message.chat.id}'
        saldo = InfoUser.saldo(id)
        pontos_indicacao = InfoUser.pontos_indicacao(id)
        quantidade_afiliados = InfoUser.quantidade_afiliados(id)
        quantidade_compras = InfoUser.total_compras(id)
        pix_inseridos = InfoUser.pix_inseridos(id)
        gifts_resgatados = InfoUser.gifts_resgatados(id)
        with open('textos/menu_comprar.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{first_name}', f'{first_name}').replace('{username}', f'@{username}').replace('{id}', f'{id}').replace('{link_afiliado}', f'{link_afiliado}').replace('{saldo}', f'{saldo:.2f}').replace('{pontos_indicacao}', f'{pontos_indicacao}').replace('{quantidade_afiliados}', f'{quantidade_afiliados}').replace('{quantidade_compras}', f'{quantidade_compras}').replace('{pix_inseridos}', f'{pix_inseridos}').replace('{gifts_resgatados}', f'{gifts_resgatados}')
        return texto
    def exibir_servico(message, nome):
        saldo = InfoUser.saldo(message.chat.id)
        nome_servico, valor, descricao, duracao, email = ControleLogins.pegar_info(nome)
        estoque = ControleLogins.pegar_estoque(nome)
        with open('textos/exibir_servico.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{nome_servico}', f'{nome_servico}').replace('{valor}', f'{float(valor):.2f}').replace('{descricao}', f'{descricao}').replace('{saldo}', f'{float(saldo):.2f}').replace('{estoque}', f'{estoque}').replace('{duracao}', f'{duracao}')
        return texto, email
    def mensagem_comprou(message, nome, valor, email, senha, descricao, duracao):
        saldo = InfoUser.saldo(message.chat.id)
        with open('textos/mensagem_comprou.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{nome}', f'{nome}').replace('{valor}', f'{valor}').replace('{saldo}', f'{saldo:.2f}').replace('{email}', f'{email}').replace('{senha}', f'{senha}').replace('{duracao}', f'{duracao}').replace('{descricao}', f'{descricao}')
        return texto
class MudarTexto():
    def alugar_bot(texto):
        with open('botoes/alugar_bot.txt', 'w') as f:
            f.write(texto)
    def start(texto):
        with open('textos/start.txt', 'w') as f:
            f.write(texto)
    def perfil(texto):
        with open('textos/perfil.txt', 'w') as f:
            f.write(texto)
    def adicionar_saldo(texto):
        with open('textos/adicionar_saldo.txt', 'w') as f:
            f.write(texto)
    def pix_manual(texto):
        with open('textos/pix_manual.txt', 'w') as f:
            f.write(texto)
    def pix_automatico(texto):
        with open('textos/pix_automatico.txt', 'w') as f:
            f.write(texto)
    def pagamento_expirado(texto):
        with open('textos/pagamento_expirado.txt', 'w') as f:
            f.write(texto)
    def pagamento_aprovado(texto):
        with open('textos/pagamento_aprovado.txt', 'w') as f:
            f.write(texto)
    def menu_comprar(texto):
        with open('textos/menu_comprar.txt', 'w') as f:
            f.write(texto)
    def exibir_servico(texto):
        with open('textos/exibir_servico.txt', 'w') as f:
            f.write(texto)
    def mensagem_comprou(texto):
        with open('textos/mensagem_comprou.txt', 'w') as f:
            f.write(texto)
class Botoes():
    def alugar_bot():
        with open('botoes/alugar_bot.txt', 'r') as f:
            return f.read()
    def comprar():
        with open('botoes/comprar.txt', 'r') as f:
            return f.read()
    def perfil():
        with open('botoes/perfil.txt', 'r') as f:
            return f.read()
    def addsaldo():
        with open('botoes/addsaldo.txt', 'r') as f:
            return f.read()
    def suporte():
        with open('botoes/suporte.txt', 'r') as f:
            return f.read()
    def voltar():
        with open('botoes/voltar.txt', 'r') as f:
            return f.read()
    def comprar_login():
        with open('botoes/comprar_loguin.txt', 'r') as f:
            return f.read()
    def pix_manual():
        with open('botoes/pix_manual.txt', 'r') as f:
            return f.read()
    def pix_automatico():
        with open('botoes/pix_automatico.txt', 'r') as f:
            return f.read()
    def download_historico():
        with open('botoes/download_historico.txt', 'r') as f:
            return f.read()
    def trocar_pontos_por_saldo():
        with open('botoes/trocar_pontos_por_saldo.txt', 'r') as f:
            return f.read()
    def aguardando_pagamento():
        try:
            with open('botoes/aguardando_pagamento.txt', 'r') as f:
                return f.read()
        except:
            with open('botoes/aguardando_pagamnto.txt', 'w') as f:
                f.write('⏰ AGUARDANDO PAGAMENTO')
                return '⏰ AGUARDANDO PAGAMENTO'
class MudarBotao():
    def alugar_bot(texto):
        with open('botoes/alugar_bot.txt', 'w') as f:
            f.write(texto)
    def comprar(texto):
        with open('botoes/comprar.txt', 'w') as f:
            f.write(texto)
    def perfil(texto):
        with open('botoes/perfil.txt', 'w') as f:
            f.write(texto)
    def addsaldo(texto):
        with open('botoes/addsaldo.txt', 'w') as f:
            f.write(texto)
    def suporte(texto):
        with open('botoes/suporte.txt', 'w') as f:
            f.write(texto)
    def voltar(texto):
        with open('botoes/voltar.txt', 'w') as f:
            f.write(texto)
    def comprar_login(texto):
        with open('botoes/comprar_login.txt', 'w') as f:
            f.write(texto)
    def pix_manual(texto):
        with open('botoes/pix_manual.txt', 'w') as f:
            f.write(texto)
    def pix_automatico(texto):
        with open('botoes/pix_automatico.txt', 'w') as f:
            f.write(texto)
    def download_historico(texto):
        with open('botoes/download_historico.txt', 'w') as f:
            f.write(texto)
    def trocar_pontos_por_saldo(texto):
        with open('botoes/trocar_pontos_por_saldo.txt', 'w') as f:
            f.write(texto)
    def aguardando_pagamento(texto):
        with open('botoes/aguardando_pagamento.txt', 'w') as f:
            f.write(texto)
class Log():
    def id_log_destino():
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        return data["destino_log"]
    def mudar_destino_logs(id):
        with open('settings/credenciais.json', 'r') as f:
            data = json.load(f)
        data["destino_log"] = id
        with open('settings/credenciais.json', 'w') as f:
            json.dump(data, f, indent=4)
    def log_registro(message):
        with open('log/registro.txt', 'r') as f:
            txt = f.read()
        if message == None:
            return txt
        id = message.chat.id
        name = message.chat.first_name
        username = message.chat.username
        link = f'https://t.me/{username}'
        texto = txt.replace('{id}', f'{id}').replace('{name}', f'{name}').replace('{username}', f'@{username}').replace('{link}', f'{link}').replace('\\n', '\n')
        return texto
    def log_compra(message, servico, email, senha, valor, descricao):
        with open('log/compra.txt', 'r') as f:
            txt = f.read()
        if message == None:
            return txt
        id = message.chat.id
        name = message.chat.first_name
        username = message.chat.username
        link = f'https://t.me/{username}'
        data = ViewTime.data_atual()
        hora = ViewTime.hora_atual()
        saldo = InfoUser.saldo(message.chat.id)
        texto = txt.replace('{id}', f'{id}').replace('{name}', f'{name}').replace('{username}', f'@{username}').replace('{link}', f'{link}').replace('{data}', f'{data}').replace('{hora}', f'{hora}').replace('{email}', f'{email}').replace('{senha}', f'{senha}').replace('{valor}', f'{float(valor):.2f}').replace('{servico}', f'{servico}').replace('\\n', '\n').replace('{saldo}', f'{float(saldo):.2f}').replace('{descricao}', f'{descricao}')
        return texto
    def log_recarga(message, id_pagamento, valor):
        with open('log/recarga.txt', 'r') as f:
            txt = f.read()
        if message == None:
            return txt
        id = message.chat.id
        name = message.chat.first_name
        username = message.chat.username
        link = f'https://t.me/{username}'
        data = ViewTime.data_atual()
        hora = ViewTime.hora_atual()
        saldo = InfoUser.saldo(message.chat.id)
        texto = txt.replace('{id}', f'{id}').replace('{name}', f'{name}').replace('{username}', f'@{username}').replace('{link}', f'{link}').replace('{data}', f'{data}').replace('{hora}', f'{hora}').replace('{id_pagamento}', f'{id_pagamento}').replace('{valor}', f'{float(valor):.2f}').replace('{saldo}', f'{float(saldo):.2f}').replace('\\n', '\n')
        return texto
class MudarLog():
    def log_registro(txt):
        with open('log/registro.txt', 'w') as f:
            f.write(txt)
    def log_compra(txt):
        with open('log/compra.txt', 'w') as f:
            f.write(txt)
    def log_recarga(txt):
        with open('log/recarga.txt', 'w') as f:
            f.write(txt)
class TextoInline():
    def giftcard(message, codigo, quantidade, valor):
        with open('textos/giftcard.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{codigo}', f'{codigo}').replace('{quantidade}', f'{quantidade}').replace('{valor}', f'{valor}')
        return texto
    def pix_gerado_inline(valor, pix_copia_cola, id_pagamento):
        with open('textos/pix_gerado_inline.txt', 'r') as f:
            texto = f.read()
        expiracao = CredentialsChange.InfoPix.expiracao()
        texto = texto.replace('{valor}', f'{valor}').replace('{id_pagamento}', f'{id_pagamento}').replace('{pix_copia_cola}', f'{pix_copia_cola}').replace('{expiracao}', f'{expiracao}')
        return texto
    def pagamento_aprovado(message, valor, id_pagamento):
        with open('textos/aprovado_inline.txt', 'r') as f:
            texto = f.read()
        texto = texto.replace('{valor}', f'{valor}').replace('{id_pagamento}', f'{id_pagamento}')
        return texto
class MudarTextoInline():
    def mudar_giftcar(txt):
        with open('textos/giftcard.txt', 'w') as f:
            f.write(txt)
    def mudar_pix_gerado(txt):
        with open('textos/pix_gerado_inline.txt', 'w') as f:
            f.write(txt)
    def mudar_pagamento_aprovado(txt):
        with open('textos/aprovado_inline.txt', 'w') as f:
            f.write(txt)
class CriarPix():
    def gerar(valor, id):
        sdk = mercadopago.SDK(str(CredentialsChange.InfoPix.token_mp()))
        expiracao_time = CredentialsChange.InfoPix.expiracao()
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=int(expiracao_time))
        expire = expire.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        payment_data = {
            "transaction_amount": float(valor),
            "description":f'Recarga de {valor} para {id}',
            "payment_method_id": 'pix',
            "date_of_expiration": f'{expire}',
            "payer": {
                "email": 'maxwilliam.saraiva@outlook.com'
            }
        }
        result = sdk.payment().create(payment_data)
        return result