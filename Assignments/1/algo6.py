rows = 41
cols = 100

with open("img.txt", "w") as f:
    for r in range(rows):
        line = ""
        for c in range(cols):
            if r < 2:
                ch = "-"
            elif r == 2:
                if c < 43:
                    ch = "-"
                elif c < 53:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 3:
                if c < 39:
                    ch = "-"
                elif c < 56:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 4:
                if c < 36:
                    ch = "-"
                elif c < 59:
                    ch = "+"
                else: ch = "-"
            elif r == 5:
                if c < 34:
                    ch = "-"
                elif c < 60:
                    ch = "+"
                else: ch = "-"
            elif r == 6:
                if c < 32:
                    ch = "-"
                elif c < 50:
                    ch = "+"
                elif c < 54:
                    ch = "%"
                elif c < 61:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 7:
                if c < 31:
                    ch = "-"
                elif c < 40:
                    ch = "+"
                elif c < 44:
                    ch = "*"
                elif c < 47:
                    ch = "#"
                elif c < 54:
                    ch = "%"
                elif c < 56:
                    ch = "#"
                elif c < 62:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 8:
                if c < 30:
                    ch = "-"
                elif c < 38:
                    ch = "+"
                elif c < 46:
                    ch = "#"
                elif c < 55:
                    ch = "%"
                elif c < 57:
                    ch = "#"
                elif c < 63:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 9:
                if c < 29:
                    ch = "-"
                elif c < 36:
                    ch = "+"
                elif c < 49:
                    ch = "#"
                elif c < 56:
                    ch = "%"
                elif c < 57:
                    ch = "#"
                elif c < 59:
                    ch = "="
                elif c < 63:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 10:
                if c < 29:
                    ch = "-"
                elif c < 32:
                    ch = "+"
                elif c < 36:
                    ch = "*"
                elif c < 52:
                    ch = "#"
                elif c < 55:
                    ch = "%"
                elif c < 58:
                    ch = "#"
                elif c == 58:
                    ch = "="
                elif c == 59:
                    ch = "~"
                elif c == 60:
                    ch = "+"
                elif c == 61:
                    ch = "~"
                elif c == 62:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 11:
                if c < 29:
                    ch = "-"
                elif c < 32:
                    ch = "+"
                elif c < 36:
                    ch = "*"
                elif c < 58:
                    ch = "#"
                elif c < 59:
                    ch = "*"
                elif c < 63:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 12:
                if c < 29:
                    ch = "-"
                elif c < 32:
                    ch = "+"
                elif c < 38:
                    ch = "*"
                elif c < 48:
                    ch = "#"
                elif c < 56:
                    ch = "%"
                elif c < 59:
                    ch = "#"
                elif c < 63:
                    ch = "+"
                else:
                    ch = "-"
            elif r == 13:
                if c < 29:
                    ch = "-"
                elif c < 32:
                    ch = "+"
                elif c < 36:
                    ch = "*"
                elif c < 49:
                    ch = "#"
                elif c < 56:
                    ch = "%"
                elif c < 60:
                    ch = "#"
                elif c < 61:
                    ch = "="
                elif c < 63:
                    ch = "+"
                else:
                    ch = "-"

            elif r == 14:
                if c < 29:
                    ch = "-"
                elif c < 33:
                    ch = "+"
                elif c < 38:
                    ch = "*"
                elif c < 53:
                    ch = "#"
                elif c < 57:
                    ch = "%"
                elif c < 60:
                    ch = "#"
                elif c < 64:
                    ch = "+"
                elif c < 66:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 15:
                if c < 29:
                    ch = "-"
                elif c < 32:
                    ch = "+"
                elif c < 43:
                    ch = "*"
                elif c < 46:
                    ch = "#"
                elif c < 51:
                    ch = "*"
                elif c < 57:
                    ch = "#"
                elif c < 60:
                    ch = "%"
                elif c < 62:
                    ch = "+"
                elif c < 64:
                    ch = "="
                elif c < 68:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 16:
                if c < 29:
                    ch = "-"
                elif c < 32:
                    ch = "+"
                elif c < 44:
                    ch = "*"
                elif c < 45:
                    ch = "#"
                elif c < 47:
                    ch = "*"
                elif c < 54:
                    ch = "^"
                elif c < 55:
                    ch = "*"
                elif c < 60:
                    ch = "%"
                elif c < 63:
                    ch = "*"
                elif c < 68:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 17:
                if c < 29:
                    ch = "-"
                elif c < 31:
                    ch = "="
                elif c < 33:
                    ch = "^"
                elif c < 35:
                    ch = "="
                elif c < 37:
                    ch = "^"
                elif c < 39:
                    ch = "="
                elif c < 41:
                    ch = "^"
                elif c < 43:
                    ch = "="
                elif c < 44:
                    ch = "*"
                elif c < 45:
                    ch = "#"
                elif c < 46:
                    ch = "*"
                elif c < 51:
                    ch = "="
                elif c < 62:
                    ch = "#"
                elif c < 64:
                    ch = "*"
                elif c < 68:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 18:
                if c < 29:
                    ch = "-"
                elif c < 30:
                    ch = "*"
                elif c < 31:
                    ch = "="
                elif c < 33:
                    ch = "+"
                elif c < 34:
                    ch = "="
                elif c < 35:
                    ch = "+"
                elif c < 38:
                    ch = "="
                elif c < 42:
                    ch = "+"
                elif c < 43:
                    ch = "*"
                elif c < 47:
                    ch = "#"
                elif c < 51:
                    ch = "*"
                elif c < 54:
                    ch = "#"
                elif c < 63:
                    ch = "%"
                elif c < 65:
                    ch = "*"
                elif c < 68:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 19:
                if c < 29:
                    ch = "-"
                elif c < 30:
                    ch = "*"
                elif c < 32:
                    ch = "="
                elif c < 40:
                    ch = "*"
                elif c < 41:
                    ch = "="
                elif c < 42:
                    ch = "*"
                elif c < 53:
                    ch = "#"
                elif c < 62:
                    ch = "%"
                elif c < 63:
                    ch = "*"
                elif c < 66:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 20:
                if c < 29:
                    ch = "-"
                elif c < 30:
                    ch = "#"
                elif c < 32:
                    ch = "="
                elif c < 37:
                    ch = "*"
                elif c < 39:
                    ch = "#"
                elif c < 41:
                    ch = "*"
                elif c < 42:
                    ch = "="
                elif c < 47:
                    ch = "#"
                elif c < 49:
                    ch = "*"
                elif c < 55:
                    ch = "#"
                elif c < 59:
                    ch = "%"
                elif c < 65:
                    ch = "#"
                else:
                    ch = "-"
            elif r == 21:
                if c < 30:
                    ch = "-"
                elif c < 40:
                    ch = "*"
                elif c < 42:
                    ch = "="
                elif c < 43:
                    ch = "*"
                elif c < 46:
                    ch = "#"
                elif c < 47:
                    ch = "%"
                elif c < 49:
                    ch = "#"
                elif c < 52:
                    ch = "*"
                elif c < 65:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 22:
                if c < 30:
                    ch = "-"
                elif c < 41:
                    ch = "*"
                elif c < 44:
                    ch = "="
                elif c < 55:
                    ch = "*"
                elif c < 62:
                    ch = "#"
                elif c < 64:
                    ch = "*"
                else:
                    ch = "-"


            elif r == 23:
                if c < 30:
                    ch = "-"
                elif c < 35:
                    ch = "="
                elif c < 40:
                    ch = "*"
                elif c < 44:
                    ch = "="
                elif c < 48:
                    ch = "*"
                elif c < 51:
                    ch = "#"
                elif c < 55:
                    ch = "*"
                elif c < 62:
                    ch = "#"
                elif c < 64:
                    ch = "*"
                else:
                    ch = "-"


            elif r == 24:
                if c < 31:
                    ch = "-"
                elif c < 36:
                    ch = "="
                elif c < 50:
                    ch = "*"
                elif c < 53:
                    ch = "#"
                elif c < 56:
                    ch = "*"
                elif c < 62:
                    ch = "#"
                else:
                    ch = "-"


            elif r == 25:
                if c < 32:
                    ch = "-"
                elif c < 36:
                    ch = "="
                elif c < 42:
                    ch = "*"
                elif c < 48:
                    ch = "#"
                elif c < 49:
                    ch = "+"
                elif c < 51:
                    ch = "="
                elif c < 53:
                    ch = "#"
                elif c < 58:
                    ch = "*"
                elif c < 61:
                    ch = "#"
                else:
                    ch = "-"


            elif r == 26:
                if c < 34:
                    ch = "-"
                elif c < 37:
                    ch = "="
                elif c < 40:
                    ch = "*"
                elif c < 44:
                    ch = "="
                elif c < 50:
                    ch = "*"
                elif c < 54:
                    ch = "#"
                elif c < 58:
                    ch = "*"
                elif c < 61:
                    ch = "#"
                else:
                    ch = "-"


            elif r == 27:
                if c < 35:
                    ch = "-"
                elif c < 36:
                    ch = "+"
                elif c < 37:
                    ch = "*"
                elif c < 40:
                    ch = "="
                elif c < 48:
                    ch = "*"
                elif c < 54:
                    ch = "#"
                elif c < 58:
                    ch = "*"
                elif c < 61:
                    ch = "#"
                else:
                    ch = "-"


            elif r == 28:
                if c < 36:
                    ch = "-"
                elif c < 42:
                    ch = "="
                elif c < 49:
                    ch = "*"
                elif c < 56:
                    ch = "#"
                elif c < 58:
                    ch = "*"
                elif c < 61:
                    ch = "#"
                else:
                    ch = "-"


            elif r == 29:
                if c < 35:
                    ch = "-"
                elif c < 43:
                    ch = "="
                elif c < 49:
                    ch = "*"
                elif c < 54:
                    ch = "#"
                elif c < 58:
                    ch = "*"
                elif c < 61:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 30:
                if c < 34:
                    ch = "-"
                elif c < 45:
                    ch = "="
                elif c < 57:
                    ch = "*"
                elif c < 62:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 31:
                if c < 33:
                    ch = "-"
                elif c < 37:
                    ch = "#"
                elif c < 52:
                    ch = "="
                elif c < 59:
                    ch = "*"
                elif c < 63:
                    ch = "#"
                else:
                    ch = "-"

            elif r == 32:
                if c < 30:
                    ch = "-"
                elif c < 33:
                    ch = "'"
                elif c < 36:
                    ch = "*"
                elif c < 49:
                    ch = "="
                elif c < 59:
                    ch = "*"
                elif c < 64:
                    ch = "#"
                elif c < 67:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 33:
                if c < 26:
                    ch = "-"
                elif c < 34:
                    ch = "'"
                elif c < 36:
                    ch = "*"
                elif c < 44:
                    ch = "="
                elif c < 54:
                    ch = "*"
                elif c < 64:
                    ch = "#"
                elif c < 74:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 34:
                if c < 25:
                    ch = "-"
                elif c < 35:
                    ch = "'"
                elif c < 48:
                    ch = "="
                elif c < 54:
                    ch = "*"
                elif c < 63:
                    ch = "#"
                elif c < 74:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 35:
                if c < 18:
                    ch = "-"
                elif c < 36:
                    ch = "'"
                elif c < 37:
                    ch = "+"
                elif c < 40:
                    ch = "="
                elif c < 55:
                    ch = "*"
                elif c < 62:
                    ch = "#"
                elif c < 82:
                    ch = "'"
                else:
                    ch = "-"


            elif r == 36:
                if c < 15:
                    ch = "-"
                elif c < 40:
                    ch = "'"
                elif c < 57:
                    ch = "*"
                elif c < 61:
                    ch = "#"
                elif c < 86:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 37:
                if c < 12:
                    ch = "-"
                elif c < 44:
                    ch = "'"
                elif c < 58:
                    ch = "*"
                elif c < 60:
                    ch = "#"
                elif c < 90:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 38:
                if c < 8:
                    ch = "-"
                elif c < 93:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 39:
                if c < 7:
                    ch = "-"
                elif c < 95:
                    ch = "'"
                else:
                    ch = "-"

            elif r == 40:
                if c < 5:
                    ch = "-"
                elif c < 97:
                    ch = "'"
                else:
                    ch = "-"

            else:
                ch = "-"
            line += ch
        f.write(line + "\n")