from latextool_basic import table
print table([('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', '')
],
col_headings = ['$0$', '$1$', '$2$', '$3$', r'$\ldots$'],
row_headings = ['$f_0$', '$f_1$', '$f_2$', '$f_3$', r'$\ldots$'])
