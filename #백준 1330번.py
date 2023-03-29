#백준 1330번
A,B = map(int,input().split())

print('>') if A > B else print('<') if A < B else print('==')