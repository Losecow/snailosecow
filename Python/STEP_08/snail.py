a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)	#삼항연산자

#https://stultus.tistory.com/m/entry/Python-백준-2869-달팽이는-올라가고-싶다
