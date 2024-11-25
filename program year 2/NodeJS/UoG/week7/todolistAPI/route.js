const get_all = require('./controller')


const router = (app) =>{
    app.route('/tasks').get(get_all).post()

    app.route('/tasks/:id').get().put().delete()
}