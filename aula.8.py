from tkinter import *
from tkinter import messagebox

# Função para adicionar informações
def add_info():
    info = {
        'first_name': entry_first_name.get(),
        'last_name': entry_last_name.get(),
        'address': entry_address.get(),
        'district': entry_district.get(),
        'country': entry_country.get(),
        'phone': entry_phone.get()
    }
    if all(info.values()):
        data.append(info)
        messagebox.showinfo('Success', 'Information added successfully!')
        for entry in entries:
            entry.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Please fill in all fields.')

# Função para pesquisar informações
def search_info():
    query = entry_search.get().lower()
    results = [info for info in data if query in info['nome'].lower() or
               query in info['sobrenome'].lower() or
               query in info['morada'].lower() or
               query in info['distrito'].lower() or
               query in info['pais'].lower() or
               query in info['telefone']]
    if results:
        result_text = '\n'.join([f"{info['nome']} {info['sobrenome']}, {info['morada']}, {info['distrito']}, {info['pais']}, {info['telefone']}" for info in results])
        messagebox.showinfo('Results', result_text)
    else:
        messagebox.showerror('Error', 'No information found.')

root = Tk()
root.title('Agenda')

data = []

# Frame para adicionar informações
frame_add = Frame(root)
frame_add.pack(pady=10)

labels = ['Nome:', 'Sobrenome:', 'Morada:', 'Distrito:', 'Pais:', 'Telefone:']
entries = []

for i, label in enumerate(labels):
    Label(frame_add, text=label).grid(row=i, column=0, padx=5, pady=5)
    entry = Entry(frame_add)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_first_name, entry_last_name, entry_address, entry_district, entry_country, entry_phone = entries

Button(frame_add, text='Adicionar', command=add_info).grid(row=len(labels), columnspan=2, pady=10)

# Frame para pesquisar informações
frame_search = Frame(root)
frame_search.pack(pady=10)

Label(frame_search, text='Procurar:').grid(row=0, column=0, padx=5, pady=5)
entry_search = Entry(frame_search)
entry_search.grid(row=0, column=1, padx=5, pady=5)

Button(frame_search, text='Procurar', command=search_info).grid(row=1, columnspan=2, pady=10)

root.mainloop()
