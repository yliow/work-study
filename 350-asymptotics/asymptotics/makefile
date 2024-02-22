OPEN = xdg-open
PDF = rm -rf solutions; touch solutions.tex; \
	pdflatex --shell-escape -halt-on-error -interaction=nonstopmode -file-line-error $@.tex && \
	pdflatex --shell-escape $@.tex && \
	pdflatex --shell-escape $@.tex && \
	pythontex main.tex && \
        makeindex $@.idx && \
        pdflatex --shell-escape $@.tex && \
        $(OPEN) $@.pdf;
LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out \
        latex.py

main: separating_polynomial_functions_1.tex \
	separating_polynomial_functions_2.tex \
	separating_polynomial_functions_3.tex \
	separating_polynomial_functions_4.tex \
	separating_polynomial_functions_5.tex \
	definition_of_big_O_1.tex \
	definition_of_big_O_2.tex \
	definition_of_big_O_3.tex \
	definition_of_big_O_4.tex \
	definition_of_big_O_5.tex \
	definition_of_big_O_6.tex \
	definition_of_big_O_7.tex \
	definition_of_big_O_8.tex \
	definition_of_big_O_9.tex \
	definition_of_big_O_10.tex \
	definition_of_big_O_11.tex \
	definition_of_big_O_12.tex \
	definition_of_big_O_13.tex \
	definition_of_big_O_14.tex \
	definition_of_big_O_15.tex \
	definition_of_big_O_16.tex \
	definition_of_big_O_17.tex \
	definition_of_big_O_18.tex \
	definition_of_big_O_19.tex \
	definition_of_big_O_20.tex \
	definition_of_big_O_21.tex \
	definition_of_big_O_22.tex \
	definition_of_big_O_23.tex \
	definition_of_big_O_24.tex \
	definition_of_big_O_25.tex \
	definition_of_big_O_26.tex \
	definition_of_big_O_27.tex \
	definition_of_big_O_28.tex \
	definition_of_big_O_29.tex \
	definition_of_big_O_30.tex \
	definition_of_big_O_31.tex \
	definition_of_big_O_33.tex \
	definition_of_big_O_34.tex \
	definition_of_big_O_35.tex \
	definition_of_big_O_36.tex \
	definition_of_big_O_37.tex \
	algorithm_analysis_1.tex \
	algorithm_analysis_2.tex \
	algorithm_analysis_3.tex \
	algorithm_analysis_4.tex \
	algorithm_analysis_5.tex \
	function_call_1.tex \
	function_call_2.tex \
	function_call_3.tex \
	function_call_4.tex \
	function_call_5.tex \
	function_call_6.tex \
	#exercises-doors
	$(PDF)
	#$(LATEXRM)
c:
	$(LATEXRM)
v:
	$(OPEN) main.pdf

separating_polynomial_functions_1.tex: separating_polynomial_functions_1.py
	python separating_polynomial_functions_1.py > separating_polynomial_functions_1.tex

separating_polynomial_functions_2.tex: separating_polynomial_functions_2.py
	python separating_polynomial_functions_2.py > separating_polynomial_functions_2.tex

separating_polynomial_functions_3.tex: separating_polynomial_functions_3.py
	python separating_polynomial_functions_3.py > separating_polynomial_functions_3.tex

separating_polynomial_functions_4.tex: separating_polynomial_functions_4.py
	python separating_polynomial_functions_4.py > separating_polynomial_functions_4.tex

separating_polynomial_functions_5.tex: separating_polynomial_functions_5.py
	python separating_polynomial_functions_5.py > separating_polynomial_functions_5.tex

definition_of_big_O_1.tex:
	python definition_of_big_O_1.py > definition_of_big_O_1.tex

definition_of_big_O_2.tex:
	python definition_of_big_O_2.py > definition_of_big_O_2.tex

definition_of_big_O_3.tex:
	python definition_of_big_O_3.py > definition_of_big_O_3.tex

definition_of_big_O_4.tex:
	python definition_of_big_O_4.py > definition_of_big_O_4.tex

definition_of_big_O_5.tex:
	python definition_of_big_O_5.py > definition_of_big_O_5.tex

definition_of_big_O_6.tex:
	python definition_of_big_O_6.py > definition_of_big_O_6.tex

definition_of_big_O_7.tex:
	python definition_of_big_O_7.py > definition_of_big_O_7.tex

definition_of_big_O_8.tex:
	python definition_of_big_O_8.py > definition_of_big_O_8.tex

definition_of_big_O_9.tex:
	python definition_of_big_O_9.py > definition_of_big_O_9.tex

definition_of_big_O_10.tex:
	python definition_of_big_O_10.py > definition_of_big_O_10.tex

definition_of_big_O_11.tex:
	python definition_of_big_O_11.py > definition_of_big_O_11.tex

definition_of_big_O_12.tex:
	python definition_of_big_O_12.py > definition_of_big_O_12.tex

definition_of_big_O_13.tex:
	python definition_of_big_O_13.py > definition_of_big_O_13.tex

definition_of_big_O_14.tex:
	python definition_of_big_O_14.py > definition_of_big_O_14.tex

definition_of_big_O_15.tex:
	python definition_of_big_O_15.py > definition_of_big_O_15.tex

definition_of_big_O_16.tex:
	python definition_of_big_O_16.py > definition_of_big_O_16.tex

definition_of_big_O_17.tex:
	python definition_of_big_O_17.py > definition_of_big_O_17.tex

definition_of_big_O_18.tex:
	python definition_of_big_O_18.py > definition_of_big_O_18.tex

definition_of_big_O_19.tex:
	python definition_of_big_O_19.py > definition_of_big_O_19.tex

definition_of_big_O_20.tex:
	python definition_of_big_O_20.py > definition_of_big_O_20.tex

definition_of_big_O_21.tex:
	python definition_of_big_O_21.py > definition_of_big_O_21.tex

definition_of_big_O_22.tex:
	python definition_of_big_O_22.py > definition_of_big_O_22.tex

definition_of_big_O_23.tex:
	python definition_of_big_O_23.py > definition_of_big_O_23.tex

definition_of_big_O_24.tex:
	python definition_of_big_O_24.py > definition_of_big_O_24.tex

definition_of_big_O_25.tex:
	python definition_of_big_O_25.py > definition_of_big_O_25.tex

definition_of_big_O_26.tex:
	python definition_of_big_O_26.py > definition_of_big_O_26.tex

definition_of_big_O_27.tex:
	python definition_of_big_O_27.py > definition_of_big_O_27.tex

definition_of_big_O_28.tex:
	python definition_of_big_O_28.py > definition_of_big_O_28.tex

definition_of_big_O_29.tex:
	python definition_of_big_O_29.py > definition_of_big_O_29.tex

definition_of_big_O_30.tex:
	python definition_of_big_O_30.py > definition_of_big_O_30.tex

definition_of_big_O_31.tex: definition_of_big_O_31.py
	python definition_of_big_O_31.py > definition_of_big_O_31.tex

definition_of_big_O_33.tex:
	python definition_of_big_O_33.py > definition_of_big_O_33.tex

definition_of_big_O_34.tex:
	python definition_of_big_O_34.py > definition_of_big_O_34.tex

definition_of_big_O_35.tex:
	python definition_of_big_O_35.py > definition_of_big_O_35.tex

definition_of_big_O_36.tex:
	python definition_of_big_O_36.py > definition_of_big_O_36.tex

definition_of_big_O_37.tex:
	python definition_of_big_O_37.py > definition_of_big_O_37.tex

algorithm_analysis_1.tex:
	python algorithm_analysis_1.py > algorithm_analysis_1.tex

algorithm_analysis_2.tex:
	python algorithm_analysis_2.py > algorithm_analysis_2.tex

algorithm_analysis_3.tex:
	python algorithm_analysis_3.py > algorithm_analysis_3.tex

algorithm_analysis_4.tex:
	python algorithm_analysis_4.py > algorithm_analysis_4.tex

algorithm_analysis_5.tex:
	python algorithm_analysis_5.py > algorithm_analysis_5.tex

function_call_1.tex: function_call_1.py 
	python function_call_1.py > function_call_1.tex
function_call_2.tex: function_call_2.py
	python function_call_2.py > function_call_2.tex
function_call_3.tex: function_call_3.py
	python function_call_3.py > function_call_3.tex
function_call_4.tex: function_call_4.py fib_node.py
	python function_call_4.py > function_call_4.tex
function_call_5.tex: function_call_5.py fib_node.py
	python function_call_5.py > function_call_5.tex
function_call_6.tex: function_call_6.py fib_node.py
	python function_call_6.py > function_call_6.tex

#exercises-doors:
#	cd exercises/doors && make
