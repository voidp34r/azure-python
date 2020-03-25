# Entry point for the application.
#from . import app     # For application discovery by the 'my' command. 
#from . import tools  # For import side-effects of setting up tools. 

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')
import ctk
import qtpy

def app():
  print("app initialized")
  print(ctk)
  print(qtpy)
  return 0