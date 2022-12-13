creation_file = open('./SQL/Creation.sql', 'r')
CREATE_TABLES = creation_file.read()

deletion_file = open('./SQL/Deletion.sql', 'r')
DROP_TABLES = deletion_file.read()

insertion_file = open('./SQL/Insert.sql', 'r')
INSERT_DATA = insertion_file.read()