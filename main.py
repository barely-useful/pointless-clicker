import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    #points = Gtk.Label(label='Pointless clicker V0.2')
    btn = Gtk.Button(label='Pointless clicker')
    win.set_child(btn)
    win.set_title("Pointless clicker V0.5")
    win.set_default_size(500, 250)
    win.present()

app = Gtk.Application(application_id='com.example.GtkApplication')
app.connect('activate', on_activate)

app.run(None)