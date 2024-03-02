import custom_lib.vector_draw as vd

def draw_dino():
    dino_vec = [(-1, -4), ( 1, -4), ( 2, -3), ( 1, -2), 
                ( 3, -1), ( 5,  1), ( 6,  4), ( 3,  1), 
                ( 1,  2), (-1,  5), (-2,  5), (-3,  4),
                (-4,  4), (-5,  3), (-5,  2), (-2,  2),
                (-5,  1), (-4, 0), (-2, 1), (-1, 0), (0, -3)]
    # draw with segment
    # seg_vec = []
    # for i in range(0, len(dino_vec)-1):
    #     seg_vec.append(vd.Segment(dino_vec[i], dino_vec[i+1]))
    # seg_vec.append(vd.Segment(dino_vec[-1], dino_vec[0]))
    # vd.draw(vd.Points(*dino_vec), *seg_vec)
    # draw with polygon
    vd.draw(vd.Points(*dino_vec), vd.Polygon(*dino_vec))

def draw_squre(start, end):
    points = vd.Points(*[(i, i**2) for i in range(start, end)])
    vd.draw(points, grid=(1, 10))

if __name__ == "__main__":
    draw_dino()
    draw_squre(-10, 11)
