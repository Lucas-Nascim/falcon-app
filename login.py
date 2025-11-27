import streamlit as st
import json


def carregar_credenciais():
    """Carrega as credenciais do arquivo credenciais.json"""
    try:
        with open('credenciais.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            email = dados.get('email', '')
            senha = dados.get('senha', '')
            return email, senha
    except Exception as e:
        st.error(f"Erro ao carregar credenciais: {e}")
        return None, None


def validacao_login(usr, passw):
    """Valida o login contra as credenciais"""
    if usr == '' or passw == '':
        st.error("Por favor, preencha todos os campos.")
        return False

    email_correto, senha_correta = carregar_credenciais()

    # Debug: descomente para inspecionar
    # st.write(f"Email lido: '{email_correto}' | Senha lida: '{senha_correta}'")
    # st.write(f"Email digitado: '{usr}' | Senha digitada: '{passw}'")

    if email_correto is None or senha_correta is None:
        st.error("Erro ao ler credenciais. Verifique credenciais.json")
        return False

    if usr == email_correto and passw == senha_correta:
        st.session_state.autenticado = True
        st.success("Login realizado com sucesso!")
        st.rerun()
        return True
    else:
        st.error("Email ou senha incorretos!")
        return False


def tela_login():
    """Renderiza a tela de login mais agradável e centralizada"""
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
        with st.container():
            st.markdown("<div class='login-card'>", unsafe_allow_html=True)
            st.markdown("<div class='login-title'>Acesse sua conta</div>", unsafe_allow_html=True)
            st.markdown("<div class='login-caption'>Informe seu email e senha</div>", unsafe_allow_html=True)

            with st.form('login_form'):
                nome_usuario = st.text_input("Email", placeholder="seu@email.com")
                senha_usuario = st.text_input("Senha", type="password", placeholder="••••••••")

                col_a, col_b = st.columns([1, 1])
                with col_a:
                    salvar_senha = st.checkbox("Salvar senha")
                with col_b:
                    st.markdown('[Esqueceu a senha?](#)')

                enviar = st.form_submit_button(
                    label="Entrar", type="primary", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            if enviar:
                validacao_login(nome_usuario, senha_usuario)
