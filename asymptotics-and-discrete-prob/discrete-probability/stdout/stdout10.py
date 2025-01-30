from latextool_basic import *
p = Plot()

data = [
  ['uniform pdf', r'$p_{U(n)}$', r'$X_{U(n)}$', r'$G_{U(n)}$'],
  ['coin toss', r'$p_{\COIN}$', r'$X_{\COIN}$', r'$G_{\COIN}$'],
  ['die roll', r'$p_{\DIE}$', r'$p_{\DIE}$', r'$G_{\DIE}$'],
  ['Bernoulli', r'$p_{\BERNOULLI(p)}$', r'$X_{\BERNOULLI(p)}$', r'$G_{\BERNOULLI(p)}$'],
  ['Binomial', r'$p_{B(n,p)}$', r'$X_{B(n,p)}$', r'$G_{B(n,p)}$'],
  ['Geometric', r'$p_{G(p)}$', r'$X_{G(p)}$', r'$G_{G(p)}$'],
]

rowlabels = [data[i][0] for i in range(len(data))]
collabels = ['pdf', 'r.v.', 'pgf']
data = [data[i][1:] for i in range(len(data))]

m00 = [['']]              
m10 = [[x] for x in rowlabels] 
m01 = [collabels]
m11 = data
M = [[m00, m01],
     [m10, m11]]
N = table3(p, M, width=4, height=0.8)
print(p)
