import rhinoscriptsyntax as rs
import create_boxes as cb
import export_objs as eo

def main():
    xnum = rs.GetInteger("X number", 5, 1)
    ynum = rs.GetInteger("Y number", 5, 1)
    boxes = cb.create_boxes(xnum, ynum)


main()