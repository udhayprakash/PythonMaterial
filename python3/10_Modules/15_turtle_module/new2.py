import turtle as tt
import secrets


def draw():
    size = secrets.SystemRandom().randint(40, 300)
    angles = (144, 150, 157.5, 160, 165)
    angle = secrets.SystemRandom().sample(angles, 1)[0]

    colors = [
        ("#922B21", "#E6B0AA"),
        ("#76448A", "#D2B4DE"),
        ("#1F618D", "#AED6F1"),
        ("#515A5A", "#EAEDED"),
        ("#148F77", "#D1F2EB"),
        ("#B7950B", "#F7DC6F"),
        ("#F39C12", "#FDEBD0"),
        ("#BA4A00", "#F6DDCC"),
    ]
    color = secrets.SystemRandom().sample(colors, 1)[0]
    tt.color(color[0], color[1])

    x_pos = secrets.SystemRandom().randint(-200, 200)
    y_pos = secrets.SystemRandom().randint(-200, 200)
    tt.pu()
    tt.setpos(x_pos, y_pos)
    start_position = tt.pos()
    tt.pd()

    tt.begin_fill()
    while True:
        tt.forward(size)
        tt.left(angle)
        if abs(tt.pos() - start_position) < 1:
            break
    tt.end_fill()


tt.circle(100)
for i in range(3):
    tt.pensize(i % 3)
    draw()

tt.done()
