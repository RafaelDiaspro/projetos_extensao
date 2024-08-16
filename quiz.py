import tkinter as tk  # Para criar a interface gráfica da aplicação
from tkinter import messagebox  # Para exibir caixas de diálogo
from tkinter import PhotoImage  # Para carregar imagens na interface
import pandas as pd
import random  # Para embaralhar as questões

# Carregando as perguntas do excel
df = pd.read_excel('questoes.xlsx')
questoes = df.sample(n=10).values.tolist()  # sample permite que as perguntas sejam exibidas aleatoriamente

# Variáveis globais
pontuacao = 0
pergunta_atual = 0

# Função para verificar a resposta
def verificar_resposta(resposta, btn):
    global pontuacao, pergunta_atual

    resposta_certa = resposta_correta.get()
    btn_correto = None

    # Encontrando o botão correto
    if resposta_certa == 1:
        btn_correto = opcao1_btn
    elif resposta_certa == 2:
        btn_correto = opcao2_btn
    elif resposta_certa == 3:
        btn_correto = opcao3_btn
    elif resposta_certa == 4:
        btn_correto = opcao4_btn

    if resposta == resposta_certa:
        pontuacao += 1
        btn.config(bg='blue')  # Marca a resposta correta do usuário em azul
        messagebox.showinfo('Resposta', 'Correto!')
    else:
        btn.config(bg='red')  # Marca a resposta incorreta do usuário em vermelho
        btn_correto.config(bg='blue')  # Marca a resposta correta em azul
        resposta_certa_texto = questoes[pergunta_atual][resposta_certa]
        messagebox.showinfo('Resposta', f'Errado! A resposta correta é: {resposta_certa_texto}')

    # Desabilitar todos os botões após resposta
    opcao1_btn.config(state=tk.DISABLED)
    opcao2_btn.config(state=tk.DISABLED)
    opcao3_btn.config(state=tk.DISABLED)
    opcao4_btn.config(state=tk.DISABLED)

    pergunta_atual += 1

    # Mostrar próxima questão após um pequeno delay
    janela.after(2000, lambda: [mostrar_questao() if pergunta_atual < len(questoes) else mostrar_pontuacao()])


# Função para exibir a próxima questão
def mostrar_questao():
    questao, opcao1, opcao2, opcao3, opcao4, resposta = questoes[pergunta_atual]
    questao_label.config(text=questao)
    opcao1_btn.config(text=opcao1, state=tk.NORMAL, bg=button_color, command=lambda: verificar_resposta(1, opcao1_btn))
    opcao2_btn.config(text=opcao2, state=tk.NORMAL, bg=button_color, command=lambda: verificar_resposta(2, opcao2_btn))
    opcao3_btn.config(text=opcao3, state=tk.NORMAL, bg=button_color, command=lambda: verificar_resposta(3, opcao3_btn))
    opcao4_btn.config(text=opcao4, state=tk.NORMAL, bg=button_color, command=lambda: verificar_resposta(4, opcao4_btn))

    resposta_correta.set(resposta)


# Função para mostrar a pontuação final
def mostrar_pontuacao():
    messagebox.showinfo('Quiz Finalizado', f'Parabéns! Você terminou o quiz.\n\n Pontuação Final: {pontuacao}/{len(questoes)}')
    opcao1_btn.config(state=tk.DISABLED)
    opcao2_btn.config(state=tk.DISABLED)
    opcao3_btn.config(state=tk.DISABLED)
    opcao4_btn.config(state=tk.DISABLED)
    jogar_novamente_btn.pack(pady=80)

# Função para jogar novamente
def jogar_novamente():
    global pontuacao, pergunta_atual, questoes
    pontuacao = 0
    pergunta_atual = 0

    #random.shuffle(questoes) # comentado para verificar a linha abaixo
    questoes = df.sample(n=10).values.tolist()  # Recarrega as perguntas aleatórias do Excel na tela

    opcao1_btn.config(state=tk.NORMAL)
    opcao2_btn.config(state=tk.NORMAL)
    opcao3_btn.config(state=tk.NORMAL)
    opcao4_btn.config(state=tk.NORMAL)
    jogar_novamente_btn.pack_forget()
    mostrar_questao()


janela = tk.Tk()
janela.title('Quiz')
janela.geometry('800x600')
background_color = '#bdd6d2'
text_color = '#333333'
button_color = '#28761A'
button_text_color = '#FFFFFF'

janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')

# Colocando ícone na interface
icone = PhotoImage(file='icone.png')
icone_label = tk.Label(janela, image=icone, bg=background_color)
icone_label.pack(pady=10)

questao_label = tk.Label(janela, text='', wraplength=570, bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
questao_label.pack(pady=20)

resposta_correta = tk.IntVar()  # Para mostrar a resposta correta das questões

# Configurando botões para respostas
opcao1_btn = tk.Button(janela, text='', width=50, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
opcao1_btn.pack(pady=10)

opcao2_btn = tk.Button(janela, text='', width=50, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
opcao2_btn.pack(pady=10)

opcao3_btn = tk.Button(janela, text='', width=50, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
opcao3_btn.pack(pady=10)

opcao4_btn = tk.Button(janela, text='', width=50, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
opcao4_btn.pack(pady=10)

jogar_novamente_btn = tk.Button(janela, command=jogar_novamente, text='Jogar Novamente', width=50, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))

mostrar_questao()

janela.mainloop()

