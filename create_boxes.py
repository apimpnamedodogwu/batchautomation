import rhinoscriptsyntax as rs
import Rhino.Geometry as geo
import math

def run(xnum, ynum):
    boxes = []
    rs.EnableRedraw(False)
    for i in range(xnum):
        for j in range(ynum):
            # rs.AddPoint(i, j, 0)
            points = []
            for s in range(2):
                for t in range(4):
                    x = math.cos(math.radians(45 + 90 * t)) * math.sqrt(2)
                    y = math.sin(math.radians(45 + 90 * t)) * math.sqrt(2)
                    z = -1 + 2 * s
                    point = geo.Point3d(x,y,z)
                    points.append(point)
            box = rs.AddBox(points)
            box = rs.RotateObject(box, geo.Point3d(0, 0, 0), 90/(xnum - 1) * i, geo.Vector3d.ZAxis)
            box = rs.RotateObject(box, geo.Point3d(0, 0, 0), 90/(ynum - 1) * j, geo.Vector3d.XAxis)
            box = rs.MoveObject(box, geo.Vector3d(i * 5, j * 5, 0))
            boxes.append(box)
    rs.EnableRedraw(True)
    return boxes 

            