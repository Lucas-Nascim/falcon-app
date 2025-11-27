import streamlit as st
import json
import os


def carregar_credenciais():
    """Retorna lista de credenciais a partir de credenciais.json"""
    try:
        path = "credenciais.json"
        if not os.path.exists(path):
            st.error("Arquivo credenciais.json não encontrado.")
            return None
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if isinstance(dados, list):
                return dados
            if isinstance(dados, dict):
                return [dados]
            st.error("Formato inválido em credenciais.json (esperado lista ou objeto).")
            return None
    except Exception as e:
        st.error(f"Erro ao carregar credenciais: {e}")
        return None


def validacao_login(usr, passw):
    """Valida email+senha contra a lista de credenciais (credenciais.json)"""
    if not usr or not passw:
        st.error("Por favor, preencha todos os campos.")
        return False

    credenciais = carregar_credenciais()
    if not credenciais:
        return False

    for c in credenciais:
        email_c = str(c.get("email", "")).strip()
        senha_c = str(c.get("senha", "")).strip()
        if usr.strip() == email_c and passw.strip() == senha_c:
            st.session_state.autenticado = True
            st.success("Login realizado com sucesso!")
            st.rerun()
            return True

    st.error("Email ou senha incorretos!")
    return False


def tela_login():
    """Tela de login centralizada e estilizada"""
    st.markdown(
        """
        <style>
        .login-card {
            background: linear-gradient(135deg,#1f2937 0%, #111827 100%);
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.3);
            color: #fff;
        }
        .login-title { font-size:24px; margin-bottom:6px; color:#fff }
        .login-caption { color: #cbd5e1; margin-bottom:12px }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("<div class='login-title'>Acesse sua conta</div>", unsafe_allow_html=True)
        st.markdown("<div class='login-caption'>Informe seu email e senha</div>", unsafe_allow_html=True)

        with st.form("login_form"):
            nome_usuario = st.text_input("Email", placeholder="seu@email.com")
            senha_usuario = st.text_input("Senha", type="password", placeholder="••••••••")
            col_a, col_b = st.columns([1, 1])
            with col_a:
                st.checkbox("Salvar senha")
            with col_b:
                st.markdown('[Esqueceu a senha?](#)')
            enviar = st.form_submit_button(label="Entrar", type="primary", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        if enviar:
            validacao_login(nome_usuario, senha_usuario)
