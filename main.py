##    Pointless clicker game
##    Copyright (C) 2024  angrypig555

##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.

##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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