c:
	g++ *.cpp
r:
	./a.out

# for github ... 
p:
	git pull
git:
	cat ~/mykey.txt ; git add -A ; git commit -m "sync" ; git push
