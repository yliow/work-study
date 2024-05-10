from latextool_basic import table
print(table([('5', '0', '0', '0', '...'),
('1', '4', '1', '5', '...'),
('', '', '', ''),
('', '', '', '')
],
col_headings = ['$0$', '$1$', '$2$', '$3$', r'$\ldots$'],
row_headings = ['$x_0$', '$x_1$', '$x_2$', '$x_3$', r'$\ldots$']))
