import mysql.connector as sql
import random as rd
conn=sql.connect(host='localhost',user='root',password='a',charset='utf8')
print('Welcome to the MySQL monitor.  Commands end with ;.')
print('Your MySQL connection id is',rd.randint(1,50))
while 1!=0:
    elo="a"
    st=input("mysql> ")
    if st=="exit" or st=='quit' or st=="exit;" or st=='quit;':
        break
    else:
        cr=conn.cursor()
        try:
            cr.execute(st)
            try:
                data=cr.fetchall()
                ct=len(data)
                try:
                    ctr=len(data[0])
                except:
                    print('Empty set (0.0 sec)')
                    continue
                a=[]
                for i in range(0,ctr):
                    l=0
                    for j in range(0,ct+1):
                        if j!=0:
                            d=len(str(data[j-1][i]))
                            if d>l:
                                l=d
                        else:
                            l=len(str(data[j][0]))
                    a=a+[l]
        
                cr.execute
                dr='+'
                for k in a:
                    dr=dr+"-"*(k+2)+"+"
                print(dr)
                for i in range(0,ct):
                    hj=''
                    for j in range(0,ctr):
                        if ctr==1:
                            hj=hj+"| "+str(data[i][j])+" "*((((len(str(data[i][j])))-a[j]))*(-1))+" |"
                        else:
                            if j==0:
                                hj="| "+str(data[i][j])+" "*(((len(str(data[i][j])))-a[j])*(-1))
                            elif j==ctr-1 :
                                hj=hj+" | "+str(data[i][j])+" "*((((len(str(data[i][j])))-a[j]))*(-1))+" |"
                            else:
                                hj=hj+" | "+str(data[i][j])+" "*((((len(str(data[i][j])))-a[j]))*(-1))
                    print(hj)
                print(dr)
                conn.commit()
                print(ct,'rows in set (0.5 sec)')
            except sql.Error as elo:
                if str(elo)!='No result set to fetch from.':
                    print('ERROR',elo)
                else:
                    print('Query OK, (0.5 sec)')
        except sql.Error as e:
            print('ERROR',e)
