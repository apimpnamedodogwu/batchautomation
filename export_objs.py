import rhinoscriptsyntax as rs
import create_boxes as cb

def run(objs, dir, ext):
    rs.EnableRedraw(False)
    for obj in objs:
        filepath = dir + "/exported" + str(obj) + "." + ext
        rs.SelectObject(obj)
        rs.Command("!_-Export \"" + filepath + "\"  -Enter - Enter")
        rs.UnselectAllObjects()
    rs.EnableRedraw(True)

boxes = cb.run(4, 4)
dir = rs.BrowseForFolder(None, "Select folder")

run(boxes, dir, "3dm")