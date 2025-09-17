import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# ================== BANCO DE DADOS ==================
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    situacao TEXT NOT NULL,
    data_alteracao TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    funcionario_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    situacao TEXT NOT NULL,
    data_entrega TEXT NOT NULL,
    FOREIGN KEY(funcionario_id) REFERENCES funcionarios(id)
)
""")

conn.commit()

# ================== FUNÇÕES ==================
def cadastrar_funcionario(nome, cpf, situacao):
    if situacao == "I":
        messagebox.showerror("Erro", "Não é permitido cadastrar funcionário inicialmente como Inativo.")
        return
    try:
        data_alteracao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO funcionarios (nome, cpf, situacao, data_alteracao) VALUES (?, ?, ?, ?)",
                       (nome, cpf, situacao, data_alteracao))
        conn.commit()
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "CPF já cadastrado!")

def cadastrar_ticket(funcionario_id, quantidade, situacao):
    if situacao == "I":
        messagebox.showerror("Erro", "Não é permitido cadastrar ticket inicialmente como Inativo.")
        return
    data_entrega = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO tickets (funcionario_id, quantidade, situacao, data_entrega) VALUES (?, ?, ?, ?)",
                   (funcionario_id, quantidade, situacao, data_entrega))
    conn.commit()
    messagebox.showinfo("Sucesso", "Ticket cadastrado com sucesso!")

def gerar_relatorio(inicio, fim):
    cursor.execute("""
        SELECT f.nome, SUM(t.quantidade) as total
        FROM tickets t
        JOIN funcionarios f ON f.id = t.funcionario_id
        WHERE date(t.data_entrega) BETWEEN date(?) AND date(?)
        GROUP BY f.nome
    """, (inicio, fim))
    resultados = cursor.fetchall()

    total_geral = sum([r[1] for r in resultados])
    rel = "Relatório de Tickets:\n\n"
    for r in resultados:
        rel += f"Funcionário: {r[0]} - Total: {r[1]}\n"
    rel += f"\nTotal Geral: {total_geral}"
    messagebox.showinfo("Relatório", rel)

# ================== INTERFACE ==================
root = tk.Tk()
root.title("Sistema de Tickets de Refeição")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Aba Funcionários
aba_func = tk.Frame(notebook)
notebook.add(aba_func, text="Funcionários")

lbl_nome = tk.Label(aba_func, text="Nome:")
lbl_nome.pack()
entry_nome = tk.Entry(aba_func)
entry_nome.pack()

lbl_cpf = tk.Label(aba_func, text="CPF:")
lbl_cpf.pack()
entry_cpf = tk.Entry(aba_func)
entry_cpf.pack()

lbl_sit = tk.Label(aba_func, text="Situação (A/I):")
lbl_sit.pack()
entry_sit = tk.Entry(aba_func)
entry_sit.pack()

btn_add_func = tk.Button(aba_func, text="Cadastrar Funcionário", command=lambda: cadastrar_funcionario(entry_nome.get(), entry_cpf.get(), entry_sit.get()))
btn_add_func.pack(pady=10)

# Aba Tickets
aba_tickets = tk.Frame(notebook)
notebook.add(aba_tickets, text="Tickets")

lbl_func = tk.Label(aba_tickets, text="ID Funcionário:")
lbl_func.pack()
entry_func_id = tk.Entry(aba_tickets)
entry_func_id.pack()

lbl_qtd = tk.Label(aba_tickets, text="Quantidade:")
lbl_qtd.pack()
entry_qtd = tk.Entry(aba_tickets)
entry_qtd.pack()

lbl_sit_t = tk.Label(aba_tickets, text="Situação (A/I):")
lbl_sit_t.pack()
entry_sit_t = tk.Entry(aba_tickets)
entry_sit_t.pack()

btn_add_ticket = tk.Button(aba_tickets, text="Cadastrar Ticket", command=lambda: cadastrar_ticket(entry_func_id.get(), entry_qtd.get(), entry_sit_t.get()))
btn_add_ticket.pack(pady=10)

# Aba Relatórios
aba_rel = tk.Frame(notebook)
notebook.add(aba_rel, text="Relatórios")

lbl_inicio = tk.Label(aba_rel, text="Data Início (YYYY-MM-DD):")
lbl_inicio.pack()
entry_inicio = tk.Entry(aba_rel)
entry_inicio.pack()

lbl_fim = tk.Label(aba_rel, text="Data Fim (YYYY-MM-DD):")
lbl_fim.pack()
entry_fim = tk.Entry(aba_rel)
entry_fim.pack()

btn_rel = tk.Button(aba_rel, text="Gerar Relatório", command=lambda: gerar_relatorio(entry_inicio.get(), entry_fim.get()))
btn_rel.pack(pady=10)

root.mainloop()
