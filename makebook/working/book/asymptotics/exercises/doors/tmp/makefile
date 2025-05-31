# add this to ../makefile:
# exercises-[name]:
#     (cd exercises/[name] && make)

plot0.tex: plot0.py cpp-stdout
	python plot0.py > plot0.tex

cpp-stdout:
	cd cpp && make stdout.txt
