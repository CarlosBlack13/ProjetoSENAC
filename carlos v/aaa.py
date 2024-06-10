import tkinter as tk

def create_oval_button(root, text, command):
  canvas = tk.Canvas(root, width=100, height=40, highlightthickness=0)
  canvas.pack()

  oval_id = canvas.create_oval(0, 0, 100, 40, fill="blue")
  label_id = canvas.create_text(50, 20, text=text, fill="white")

  def on_click(event):
    command()

  canvas.tag_bind(oval_id, "<ButtonPress-1>", on_click)
  canvas.tag_bind(label_id, "<ButtonPress-1>", on_click)

root = tk.Tk()
create_oval_button(root, "Botão arredondado", lambda: print("Botão clicado!"))
root.mainloop()
