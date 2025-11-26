import streamlit as st


@st.dialog('Aviso de Login')
# Função para validar o login
def validacao_login(usr, passw):
    # Aqui você pode adicionar a lógica de validação, como verificar contra um banco de dados
    if usr == '' or passw == '':
        st.error("Por favor, preencha todos os campos.")
    else:
        st.success("Login realizado com sucesso!")


# Configuração da página
with st.form('login_form'):
    # Definindo o título e a legenda da página de login
    st.title("Fazer login")
    st.caption("Informe seu usuario e senha para acessar.")

    # Adicionando um divisor visual entre o título e os campos de entrada
    st.divider()

    # Campos de entrada para nome de usuário e senha
    nome_usuario = st.text_input("Nome de Usuário")
    senha_usuario = st.text_input("Senha", type="password")
    # Botão de envio do formulário
    enviar = st.form_submit_button(
        label="Entrar", type="primary", use_container_width=True, help="Clique para fazer login")
    # Fazer login com Google
    # Para adicionar um icone, voce pode usar o material icons do google adicionando o parametro icon="" no botao
    google_btn = st.form_submit_button(
        label="Fazer login com google", type="secondary", use_container_width=True, help="Clique para fazer login")

    # Adicionando opções adicionais em colunas, deixando mais organizado um lado do outro
    col_1, col_2 = st.columns(2)
    with col_1:
        # Box para salvar a senha
        salvar_senha = st.checkbox("Salvar senha")
    with col_2:
        # Link para recuperação de senha
        esqueceu_senha = st.html('<a href="#">Esqueceu a senha?</a>')

# Chamando a função de validação ao enviar o formulário
if enviar:
    validacao_login(nome_usuario, senha_usuario)
# Botao criar conta fora do form para evitar conflito de envio
criar_conta = st.button(label="Criar uma conta", type="secondary", use_container_width=True,
                        help="Clique para criar uma nova conta")
