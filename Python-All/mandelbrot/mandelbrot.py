#!/usr/bin/python3
# brkmtf - Brooks-Matelski proto ASCII Mandelbrot set - scruss, 2022-05
# -*- coding: utf-8 -*-


def valmap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


rows = 31
cols = 71
maxit = 200

for y in range(rows):
    ci = valmap(float(y + 1), 1.0, float(rows), -0.8715, 0.8715)
    for x in range(cols):
        cr = valmap(float(x + 1), 1.0, float(cols), -1.975, 0.475)
        c = complex(cr, ci)
        z = complex(0.0, 0.0)
        ch = "*"
        for k in range(maxit):
            z = z**2 + c
            if abs(z) > 2.0:
                ch = " "
                break
        print(ch, end="")
    print()
