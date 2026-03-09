import sys
import re

def process(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it's the sequence editor file (git-rebase-todo)
    if 'pick ' in content:
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if line.startswith('pick '):
                # Change pick to reword
                new_lines.append(line.replace('pick ', 'reword ', 1))
            else:
                new_lines.append(line)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
    else:
        # If it's the commit message editor (COMMIT_EDITMSG)
        lines = content.split('\n')
        if not lines:
            return
            
        msg = lines[0]
        
        # fix missing colon in feat
        if msg.startswith('feat '):
            msg = 'feat: ' + msg[5:]
            
        # specifically fix the exact one asked
        if msg.strip() == 'feat: add UI order_sucess':
            msg = 'feat: add order success page'
        elif msg.strip() == 'Add base HTML structure in index.html':
            msg = 'feat: add base HTML structure'
            
        lines[0] = msg
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

if __name__ == '__main__':
    process(sys.argv[1])
