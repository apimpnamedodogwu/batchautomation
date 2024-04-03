import rhinoscriptsyntax as rs
import os

def run(dir, ext):
    files = []
    imported_objects = []
    for file in os.listdir(dir):
        if file.endswith("." + ext):
            files.append(dir + "/" + file)
    rs.EnableRedraw(False)
    for filepath in files:
        rs.Command("!_-Import \"" + filepath + "\"  -Enter - Enter")
        selected_objs = rs.SelectedObjects()
        imported_objects.extend(selected_objs)
    rs.UnselectAllObjects()
    rs.EnableRedraw(True)
    return imported_objects

# dir = rs.BrowseForFolder(None, "Select folder to import files from")

# run(dir, "3dm")