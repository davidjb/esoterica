from datetime import datetime
print('%s days til Codeathon!' % (datetime(int(input('Future Year? ')), 6, 25) - datetime.now()).days)
