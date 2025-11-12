from flask import Flask 

app = Flask (__name__)

@app.route ('/api', methods = ['GET'])
def index ():
    return{
        'message' : 'Api rodando'

    }
# Se for o modulo principal, roda o projeto em debug
if __name__ == '__main__':
    app.run (debug = True)
    app.run
    @app.route('/api/tarefas/<int:todo_id', methods=['POST'])
    def create_tarefa()
        corpo = request.get_json()
        tarefa_name = corpo.get('name')
        tarefa_descrition = corpo.get('descrition')
        criar_tarefa(tarefa_name, tarefa_descrition)
        return{
            'message' : 'tarefa cadastrada'
        }