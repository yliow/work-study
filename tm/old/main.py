from latextool_basic import table
print(table([('0', '0', '1', '0', '...'),
('1', '0', '1', '1', '...'),
('0', '1', '1', '1', '...'),
('1', '0', '1', '1', '...'),
],
col_headings = ['$w_1$', '$w_2$', '$w_3$', '$w_4$', r'$\ldots$'],
row_headings = ['$M_1$', '$M_2$', '$M_3$', '$M_4$', r'$\ldots$']))

