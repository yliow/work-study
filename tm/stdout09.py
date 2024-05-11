from latextool_basic import table
print(table([('1', '0', '1', '1'),
('0', '0', '0', '1'),
('1', '0', '1', '0'),
('0', '0', '1', '1')
],
col_headings = ['$0$', '$1$', '$2$', '$3$', r'$\ldots$'],
row_headings = ['$f_0$', '$f_1$', '$f_2$', '$f_3$', r'$\ldots$']))
