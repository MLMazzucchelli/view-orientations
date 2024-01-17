from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from plotly import graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print("welcome")
    self.repeating_panel_orientations.items = anvil.server.call('get_orientations')

    # Any code you write here will run before the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    new_plot = Plot(
      data=go.Scattergl(
        x=[0, 1, 2, 3, 4],
        y=[0, 1, 4, 9, 16],
      )
    )
    #self.grid_panel_1.add_component(new_plot, width_xs=6)