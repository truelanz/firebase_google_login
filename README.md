## Login App com Firebase e Flet

App simples de login desenvolvido em Python usando a biblioteca [Flet](https://flet.dev/) para a interface gráfica e a API REST do Firebase Authentication para autenticação de usuários via email e senha.

Permite que um usuário faça login com um email e senha registrados no Firebase. Após o login bem-sucedido, a tela é limpa e exibe uma mensagem de sucesso (pós-login), enquanto uma notificação (SnackBar) verde aparece. Em caso de erro, uma SnackBar vermelha informa que as credenciais estão incorretas.

- Python 3.10 ou superior instalado.
- Conta no [Firebase](https://console.firebase.google.com/) para criar um projeto e obter a `API_KEY`.

### Obter a API_KEY do Firebase
1. Acesse o [Firebase Console](https://console.firebase.google.com/).
2. Crie um novo projeto ou use um existente.
3. No menu lateral, clique em **Authentication** > **Get Started** e habilite o provedor "Email/Password".
4. Vá para **Configurações do Projeto** (ícone de engrenagem no topo à esquerda).
5. Na aba **Geral**, role até "Seus aplicativos" e clique em **Adicionar aplicativo** > **Web**.
6. Após registrar o app, copie a **Chave da API da Web** (Web API Key). Essa será sua `API_KEY`.
7. No código (`main.py`), substitua o valor vazio de `API_KEY = ""` pela sua chave:
   ```python
   API_KEY = "sua-chave-aqui"

### Instalando as dependências
Siga os passos abaixo para configurar o ambiente e instalar as bibliotecas necessárias:
- Crie um ambiente virtual:
`python3 -m venv <rep-name>`
Ative o ambiente virtual:
- No Windows:
`venv\Scripts\activate`
- No Linux/Mac:
`source venv/bin/activate`
- Instale as dependências:
`pip install flet requests`

 Após configurar a API_KEY e instalar as dependências, execute o aplicativo:
Certifique-se de que o ambiente virtual está ativo (você verá (venv) no terminal):
`flet run main.py`