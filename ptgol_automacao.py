import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
import os
from dotenv import load_dotenv
import re

# Carrega variáveis de ambiente
load_dotenv()

# Configurações
PTGOL_LOGIN = os.getenv('PTGOL_LOGIN')
PTGOL_SENHA = os.getenv('PTGOL_SENHA')
PTGOL_URL = os.getenv('PTGOL_URL', 'https://www.ptgol.com.br/index.php?pr=')

# Tempo entre rodadas (5 minutos)
INTERVALO_RODADAS = 300  # 300 segundos = 5 minutos

# Session para manter cookies
session = requests.Session()

def log(mensagem, tipo="INFO"):
    """Printa logs com timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {tipo}: {mensagem}")

def login():
    """Faz login no jogo"""
    log("Iniciando login...")
    
    if not PTGOL_LOGIN or not PTGOL_SENHA:
        log("ERRO: Credenciais não configuradas no .env!", "ERROR")
        return False
    
    try:
        # Primeiro, acessa a página para pegar qualquer token/cookie necessário
        response = session.get(PTGOL_URL, timeout=10)
        log(f"Acessando página principal: Status {response.status_code}")
        
        # Tenta fazer login
        login_data = {
            'login': PTGOL_LOGIN,
            'senha': PTGOL_SENHA,
            'action': 'login'
        }
        
        response = session.post(
            PTGOL_URL,
            data=login_data,
            timeout=10
        )
        
        if response.status_code == 200:
            if 'logout' in response.text.lower() or 'sair' in response.text.lower():
                log("Login realizado com sucesso!")
                return True
            else:
                log("Login pode ter falhado. Continuando...", "WARNING")
                return True
        else:
            log(f"Erro no login: Status {response.status_code}", "ERROR")
            return False
            
    except Exception as e:
        log(f"Erro ao fazer login: {str(e)}", "ERROR")
        return False

def aguardar_captcha():
    """Aguarda CAPTCHA ser digitado manualmente"""
    log("⚠️  CAPTCHA DETECTADO! Digite o CAPTCHA no site e pressione Enter aqui...", "WARNING")
    input()
    log("Continuando...")

def clicar_botao(identifikador):
    """Simula clique em um botão"""
    log(f"Clicando em: {identifikador}")
    
    try:
        response = session.post(
            PTGOL_URL,
            data={'acao': identifikador},
            timeout=10
        )
        
        # Verifica CAPTCHA
        if 'captcha' in response.text.lower():
            aguardar_captcha()
            return False
        
        log(f"Clique executado com sucesso")
        return True
        
    except Exception as e:
        log(f"Erro ao clicar: {str(e)}", "ERROR")
        return False

def escolher_direcao_chute():
    """Escolhe aleatoriamente uma direção para chutar"""
    direcoes = ['esquerda', 'centro', 'direita']
    escolha = random.choice(direcoes)
    log(f"Chutando para: {escolha}")
    return escolha

def escolher_bolinha_trilha():
    """Escolhe aleatoriamente uma bolinha da trilha"""
    posicoes = list(range(1, 10))  # 9 bolinhas possíveis
    escolha = random.choice(posicoes)
    log(f"Escolhendo bolinha #{escolha} da trilha")
    return escolha

def executar_trilha():
    """Executa os 3 cliques da trilha"""
    log("Iniciando TRILHA...")
    
    try:
        if not clicar_botao('trilha'):
            return False
        
        time.sleep(1)
        
        for i in range(3):
            bolinha = escolher_bolinha_trilha()
            clicar_botao(f'trilha_{bolinha}')
            time.sleep(random.uniform(0.5, 1.5))
        
        log("TRILHA concluída!")
        return True
        
    except Exception as e:
        log(f"Erro na trilha: {str(e)}", "ERROR")
        return False

def executar_penalti():
    """Executa o chute de penalti"""
    log("Iniciando PENALTI...")
    
    try:
        if not clicar_botao('penalti'):
            return False
        
        time.sleep(1)
        
        direcao = escolher_direcao_chute()
        clicar_botao(f'penalti_{direcao}')
        
        log("PENALTI concluído!")
        return True
        
    except Exception as e:
        log(f"Erro no penalti: {str(e)}", "ERROR")
        return False

def executar_falta():
    """Executa o chute de falta"""
    log("Iniciando FALTA...")
    
    try:
        if not clicar_botao('falta'):
            return False
        
        time.sleep(1)
        
        direcao = escolher_direcao_chute()
        clicar_botao(f'falta_{direcao}')
        
        log("FALTA concluída!")
        return True
        
    except Exception as e:
        log(f"Erro na falta: {str(e)}", "ERROR")
        return False

def executar_chute_extra():
    """Executa o chute extra"""
    log("Iniciando CHUTE EXTRA...")
    
    try:
        if not clicar_botao('chute_extra'):
            return False
        
        time.sleep(1)
        
        tipo_chute = random.choice(['penalti', 'falta'])
        log(f"Chute extra é: {tipo_chute.upper()}")
        
        direcao = escolher_direcao_chute()
        clicar_botao(f'{tipo_chute}_{direcao}')
        
        log("CHUTE EXTRA concluído!")
        return True
        
    except Exception as e:
        log(f"Erro no chute extra: {str(e)}", "ERROR")
        return False

def executar_rodada():
    """Executa uma rodada completa"""
    log("\n" + "="*60)
    log("INICIANDO NOVA RODADA")
    log("="*60)
    
    executar_chute_extra()
    time.sleep(2)
    
    executar_penalti()
    time.sleep(2)
    
    executar_falta()
    time.sleep(2)
    
    executar_trilha()
    
    log("="*60)
    log("RODADA CONCLUÍDA! Aguardando 5 minutos...")
    log("="*60 + "\n")

def main():
    """Função principal"""
    log("PT GOL - AUTOMAÇÃO INICIADA")
    log(f"URL: {PTGOL_URL}")
    log(f"Intervalo entre rodadas: {INTERVALO_RODADAS} segundos (5 minutos)\n")
    
    if not login():
        log("Falha no login! Abortando...", "ERROR")
        return
    
    rodada = 1
    while True:
        try:
            log(f"RODADA #{rodada}")
            executar_rodada()
            rodada += 1
            
            log(f"Aguardando {INTERVALO_RODADAS} segundos...")
            time.sleep(INTERVALO_RODADAS)
            
        except KeyboardInterrupt:
            log("\nAutomação interrompida pelo usuário.", "INFO")
            break
        except Exception as e:
            log(f"Erro na rodada: {str(e)}", "ERROR")
            log("Tentando reconectar...")
            login()
            time.sleep(5)

if __name__ == "__main__":
    main()