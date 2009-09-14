#!/usr/bin/python
import sys
import re

nice_thing=r'''\maketitle
\AtBeginSection[]
{
   \begin{frame}
       \frametitle{Outline}
       \tableofcontents[currentsection]
   \end{frame}
}
'''

def line2title(line):
    if line.startswith('\\') and 'section' in line:
        leader , rest = line.split('{', 1)
        if '}' in rest:
            title, rest   = rest.rsplit('}', 1)
        else:
            title = rest
    else:
        title = None
    return title

in_frame = False
def make_frame(line):
    global in_frame
    # were we in a frame to begin with?
    out = ''
    if in_frame:
        out += '\end{frame}\n'
        in_frame = False
    out += line
    out += r'\begin{frame}' + '\n'
    out += r'\frametitle{' + line2title(line) + '}\n'
    in_frame = True
    return out

lines = sys.stdin.read().split('\n')
while len(lines):
    line = lines.pop(0)
    if line.startswith('\\') and 'section' in line:
        while not line.rstrip().endswith('}'):
            # extend line
            line += lines.pop(0)

    # line fixed; now real logic
    if line.startswith(r'\setlength'):
        pass
    # page size? drop that
    elif line.startswith(r'\geometry'):
        pass
    elif line.startswith(r'\begin{document}'):
        line = (r'% shallow toc' + '\n' + 
                r'\setcounter{tocdepth}{1}' + '\n' +
                line)
        print line.rstrip()
    elif line.startswith(r'\usepackage{babel}'):
        pass
    elif line.startswith(r'\documentclass'):
        print r'\documentclass{beamer}'
    elif line.startswith(r'\footnote'):
        pass # eat it
    elif line.startswith('}.)'):
        pass # eat it
    elif line2title(line):
        print make_frame(line)
    elif line.startswith(r'\end{document}'):
        if in_frame:
            line = r'\end{frame}' + '\n' + line
        print line
    elif line.startswith(r'\item'):
        if '<' in line:
            line = line.replace('<', r'$<$')
        #    line = line.replace('<', r'<')
        #if '>' in line:
        #    line = line.replace('>', r'>')
        line = r'\pause' + '\n' + line
        print line.rstrip()
    elif line.startswith(r'\maketitle'):
        line = nice_thing
        print line
    else:
        print line.rstrip()
