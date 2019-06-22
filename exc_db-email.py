import sqlite3

conn = sqlite3.connect('mailbd.sqlite')  # 新建一个数据库文件
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS orgCounts')
cur.execute('''CREATE TABLE Counts (org TEXT,count INTEGER)''')

count = dict()
handle = '/Users/superallen/Desktop/mbox.txt'
fn = open(handle)
for lines in fn:
    if lines.startswith('From: '):
        pices1 = lines.split()
        orgnz = ((pices1[1]).split('@'))[1]
        cur.execute('SELECT count FROM Counts WHERE org= ? ', (orgnz,))
        row = cur.fetchone()
        if row is None:
            cur.execute(
                '''INSERT INTO Counts (org,count) VALUES (?,1)''', (orgnz,))
        else:
            cur.execute(
                'UPDATE Counts SET count=count+1 WHERE org=?', (orgnz,))
        conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
