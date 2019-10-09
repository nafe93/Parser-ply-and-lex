
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CNF DNF DOUBLE_NEGATION LPAREN NEGATION OR RPAREN VARIABLE impexpression : expression AND term\n                  | expression OR term\n                  | expression imp term\n\n    term          : term DNF factor\n                  | term CNF factor\n\n    factor        : NEGATION factor\n                  | DOUBLE_NEGATION factorexpression : termterm : factorfactor : VARIABLEfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'NEGATION':([0,4,5,7,8,9,10,11,12,],[4,4,4,4,4,4,4,4,4,]),'DOUBLE_NEGATION':([0,4,5,7,8,9,10,11,12,],[5,5,5,5,5,5,5,5,5,]),'VARIABLE':([0,4,5,7,8,9,10,11,12,],[6,6,6,6,6,6,6,6,6,]),'LPAREN':([0,4,5,7,8,9,10,11,12,],[7,7,7,7,7,7,7,7,7,]),'$end':([1,2,3,6,13,14,16,17,18,19,20,21,],[0,-8,-9,-10,-6,-7,-1,-2,-3,-4,-5,-11,]),'AND':([1,2,3,6,13,14,15,16,17,18,19,20,21,],[8,-8,-9,-10,-6,-7,8,-1,-2,-3,-4,-5,-11,]),'OR':([1,2,3,6,13,14,15,16,17,18,19,20,21,],[9,-8,-9,-10,-6,-7,9,-1,-2,-3,-4,-5,-11,]),'imp':([1,2,3,6,13,14,15,16,17,18,19,20,21,],[10,-8,-9,-10,-6,-7,10,-1,-2,-3,-4,-5,-11,]),'RPAREN':([2,3,6,13,14,15,16,17,18,19,20,21,],[-8,-9,-10,-6,-7,21,-1,-2,-3,-4,-5,-11,]),'DNF':([2,3,6,13,14,16,17,18,19,20,21,],[11,-9,-10,-6,-7,11,11,11,-4,-5,-11,]),'CNF':([2,3,6,13,14,16,17,18,19,20,21,],[12,-9,-10,-6,-7,12,12,12,-4,-5,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,7,],[1,15,]),'term':([0,7,8,9,10,],[2,2,16,17,18,]),'factor':([0,4,5,7,8,9,10,11,12,],[3,13,14,3,3,3,3,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression AND term','expression',3,'p_binary_operators','calc_yacc.py',52),
  ('expression -> expression OR term','expression',3,'p_binary_operators','calc_yacc.py',53),
  ('expression -> expression imp term','expression',3,'p_binary_operators','calc_yacc.py',54),
  ('term -> term DNF factor','term',3,'p_binary_operators','calc_yacc.py',56),
  ('term -> term CNF factor','term',3,'p_binary_operators','calc_yacc.py',57),
  ('factor -> NEGATION factor','factor',2,'p_binary_operators','calc_yacc.py',59),
  ('factor -> DOUBLE_NEGATION factor','factor',2,'p_binary_operators','calc_yacc.py',60),
  ('expression -> term','expression',1,'p_expression_term','calc_yacc.py',84),
  ('term -> factor','term',1,'p_term_factor','calc_yacc.py',89),
  ('factor -> VARIABLE','factor',1,'p_factor_variable','calc_yacc.py',94),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','calc_yacc.py',99),
]