
# add this to ../makefile:
# exercises-[name]:
#     (cd exercises/[name] && make)

run: test0.txt plot0.tex
	$(NOOP)

test0.txt: test0.py
	python test0.py > test0.txt

plot0.tex: plot0.py
	python plot0.py > plot0.tex
