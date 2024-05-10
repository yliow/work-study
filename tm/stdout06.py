from latextool_basic import table
print(table([('', '', '', ''),
('', '', '', ''),
('', '', '', ''),
('', '', '', '')
],
col_headings = ['$0$', '$1$', '$2$', '$3$', r'$\ldots$'],
row_headings = ['$x_0$', '$x_1$', '$x_2$', '$x_3$', r'$\ldots$']))
