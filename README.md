# PT GOL - Automação de Chutes 🎮⚽

Script de automação para o jogo online PT GOL que executa chutes automaticamente a cada 5 minutos.

## 📋 Funcionalidades

- ✅ Login automático
- ✅ Aguarda 5 minutos entre rodadas
- ✅ Clica em: Chute Extra, Penalti, Falta e Trilha
- ✅ Escolhe direções/posições **aleatoriamente**
- ✅ Trata CAPTCHA (você digita quando aparecer)
- ✅ Executa continuamente
- ✅ Logs detalhados de cada ação

## 🔧 Configuração

### 1. Criar arquivo `.env` (LOCAL - NÃO COMMITIR NO GIT)

Na raiz do projeto, crie um arquivo chamado `.env`:

```
PTGOL_LOGIN=seu_usuario_aqui
PTGOL_SENHA=sua_senha_aqui
PTGOL_URL=https://www.ptgol.com.br/index.php?pr=
```

⚠️ **IMPORTANTE:** Este arquivo `.env` é pessoal e **nunca deve ser commitado** no GitHub!

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o script

**Na extensão Python Code Runner do Chrome:**
1. Copie o conteúdo de `ptgol_automacao.py`
2. Cole na extensão
3. Configure para **rodar a cada 5 minutos**
4. Execute!

**Ou localmente (terminal):**
```bash
python ptgol_automacao.py
```

## 📝 Como Funciona

1. **Faz login** com as credenciais do `.env`
2. **Aguarda 5 minutos** (300 segundos)
3. **Executa a sequência:**
   - Clica em **Chute Extra** (aparece Penalti ou Falta aleatoriamente)
   - Escolhe direção aleatoriamente
   - Clica em **Penalti** (3 opções)
   - Escolhe direção aleatoriamente
   - Clica em **Falta** (3 opções)
   - Escolhe direção aleatoriamente
   - Clica em **Trilha** (escolhe 3 bolinhas aleatoriamente)
4. **Se CAPTCHA aparecer:** Pausa e avisa para você digitar
5. **Repete continuamente**

## 🚨 Tratamento de Erros

- ✅ Reconecta automaticamente se deslogar
- ✅ Trata erros de rede
- ✅ Pausa para CAPTCHA manual
- ✅ Logs de tudo que acontece

## 📌 Notas Importantes

- **Altere sua senha** no jogo frequentemente
- **Nunca compartilhe** seu arquivo `.env`
- **Adicione `.env` ao `.gitignore`** (já está configurado)
- **Monitore os logs** para ver se está funcionando

## 🐛 Troubleshooting

**Erro: "Login falhou"**
- Verifique as credenciais no `.env`
- Altere a senha no site e atualize no `.env`

**Erro: "Página não carrega"**
- Verifique sua conexão de internet
- Tente acessar o site manualmente

**CAPTCHA aparece frequentemente**
- Isso é normal, o site trata como proteção
- Você digita quando aparecer

## 📞 Suporte

Se tiver problemas, crie uma **Issue** no GitHub com:
- O erro exato
- O log da execução
- Passos para reproduzir

---

**Desenvolvido com ❤️ para automação do PT GOL**