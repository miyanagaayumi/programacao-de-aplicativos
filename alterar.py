import sqlite3

 conexao = sqlite3.connect('escola_demonstracao.db')
 cursor = conexao.cursor()

 cursor.execute('''
      DROP TABLE professores
 ''')

 conexao.commit()


 conexao = sqlite3.connect('escola_demonstracao.db')
 cursor = conexao.cursor()

 cursor.execute('''
      ALTER TABLE professores
      ADD COLUMN endereco_professor TEXT;
 ''')

conexao.commit()



conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
     ALTER TABLE alunos
     ADD COLUMN endereco_aluno TEXT;
''')



conexao.commit()

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
     ALTER TABLE alunos
     ADD COLUMN cidade_aluno TEXT;
''')

conexao.commit()


conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
     ALTER TABLE alunos
     ADD COLUMN estado_aluno TEXT;
''')

conexao.commi