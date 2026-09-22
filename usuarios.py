from mysqlconnection import connectToMySQL
DB_NAME = 'usuarios_cert2'

class Usuario:
    def __init__(self, data):
        id = data['id']
        #si da error, pongale data.get, asi salta al siguient e y no da error
        nombre_completo = data['nombre_completo']
        email = data['email']
        created_at = data['created_at']
        updated_at = data['updated_at']

    @classmethod
    def crear(cls,data):
        query = "INSERT INTO usuarios (nombre_completo, email) VALUES (%(nombre_completo)s,%(email)s);"
        # %(dato)s = sentencia preparada
        return connectToMySQL(DB_NAME).query_db(query, data)

    @classmethod
    def actualizar(cls, data):
      query = """
         UPDATE usuarios
         SET nombre_completo = %(nombre_completo)s,
             email = %(email)s,
         WHERE id = %(id)s;
      """
      resultado = connectToMySQL(DB_NAME).query_db(query, data)

      if resultado is False:
         raise RuntimeError("Failed to update profile")
  
      return resultado

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(DB_NAME).query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def borrar(cls, usuario_id):
      query = "DELETE FROM usuarios WHERE id = %(id)s"
      data = {"id": usuario_id}

      resultado = connectToMySQL(DB_NAME).query_db(query, data)

      if resultado is False:
         raise RuntimeError("Failed to delete user")

      return resultado