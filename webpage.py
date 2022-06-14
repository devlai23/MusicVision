from ._anvil_designer import Form1Template
from anvil import *
from anvil.google.drive import app_files
import anvil.server

class Form1(Form1Template):
  picture = None
  note = ""
  audio_file = ""
  yes_button_is_clicked = False
  name_file = ""

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
#     self.note_drop_down.selected_value = self.note

  def categorise_button_click(self, **event_args):
    """This method is called when the button is clicked"""
  
    note_category = anvil.server.call('predict', self.name_file)
    
    self.species_label.visible = True 
    self.species_label.text = "The note is a " + note_category.capitalize()
    
    if self.yes_button_is_clicked: 
       self.play_sound.visible = True
    
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    
    self.name_file = file.name
    app_files.notes.create_file(file.name, file)
    
    self.file_loader_1.clear()
    pass
  
  def yes_button_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.dropdown_label.visible = True 
    self.note_drop_down.visible = True
    self.save_button.visible = True 
    self.yes_button_is_clicked = True
    pass

  def no_button_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.dropdown_label.visible = False
    self.note_drop_down.visible = False
    self.save_button.visible = False
    self.yes_button_is_clicked = False
    pass


  def play_sound_click(self, **event_args):
    """This method is called when the button is clicked"""
    # src_url = anvil.sever.call('')
    pass

  def file_loader_1_show(self, **event_args):
    """This method is called when the FileLoader is shown on the screen"""
    pass

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass




