def intersect(p0, p1, q0, q1):
    """checks if two lines intersect"""
    x0, y0 = p0
    x1, y1 = p1
    X0, Y0 = q0
    X1, Y1 = q1
    
    a = y0 - y1
    b = x1 - x0

    A = Y0 - Y1
    B = X1 - X0

    d = a*B - b*A

    if d == 0: return False

    c = a*x0 + b*y0
    C = A*X0 + B*Y0
    d = float(d)
    x = (B*c - b*C) / d
    y = (-A*c + a*C) / d

    point = None
    if  min(x0,x1) <= x <= max(x0,x1) \
        and min(y0,y1) <= y <= max(y0,y1) \
        and min(X0,X1) <= x <= max(X0,X1) \
        and min(Y0,Y1) <= y <= max(Y0,Y1):
        point = [x,y]

    return point

def distsq(p0, p1):
    dx = p0[0] - p1[0]
    dy = p0[1] - p1[1]
    return dx*dx + dy*dy

def incircle(p, center, r):
    dx = p[0] - center[0]
    dy = p[1] - center[1]
    return (dx*dx + dy*dy <= r*r)

def get_collideds(p0, p1, v, r, bricks):
    """
    should have bricks replaced by list of rects
    """
    collideds = []
    v = [p1[0] - p0[0], p1[1] - p0[1]]
    for brick in bricks:
        if not brick['alive']: continue

        """
              p0                    p1
              +-------------------+
              | +---------------+ |
              | |               | |
              | +---------------+ |
              +-------------------+
              p2                    p3                    
        """
        x0 = brick['rect'].x
        y0 = brick['rect'].y
        x1 = brick['rect'].right
        y1 = brick['rect'].bottom

        crightpoint = intersect(p1, p0, [x1+r, y0], [x1+r, y1])
        cright  = v[0] < 0 and crightpoint
        cleftpoint = intersect(p1, p0, [x0-r, y0], [x0-r, y1])
        cleft   = v[0] > 0 and intersect(p1, p0, [x0-r, y0], [x0-r, y1])
        cbottompoint = intersect(p1, p0, [x0, y1+r], [x1, y1+r])
        cbottom = v[1] < 0 and cbottompoint
        ctoppoint = intersect(p1, p0, [x0, y0-r], [x1, y0-r])
        ctop    = v[1] > 0 and ctoppoint

        # circle corners in minkowski span
        ccircle = (v[0] >= 0 and v[1] >= 0 and incircle(p1, [x0,y0], r)) or \
                  (v[0] <= 0 and v[1] >= 0 and incircle(p1, [x1,y0], r)) or \
                  (v[0] >= 0 and v[1] <= 0 and incircle(p1, [x0,y1], r)) or \
                  (v[0] <= 0 and v[1] <= 0 and incircle(p1, [x1,y1], r))
        ccornerpoint = p1 # just use this since there is no fast way to compute the point of intersection
        
        if cleft:   collideds.append((distsq(p0, cleftpoint), 'left', cleftpoint, brick))
        if cright:  collideds.append((distsq(p0, crightpoint), 'right', crightpoint, brick))
        if cbottom: collideds.append((distsq(p0, cbottompoint), 'bottom', cbottompoint, brick))
        if ctop:    collideds.append((distsq(p0, ctoppoint), 'top', ctoppoint, brick))
        if ccircle: collideds.append((distsq(p0, ccornerpoint), 'corner', ccornerpoint, brick))

    return collideds
