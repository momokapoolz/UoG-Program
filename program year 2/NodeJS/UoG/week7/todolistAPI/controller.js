const productModel = require('./model')

const get_all = async(req, res)=>{
    const getAll = productModel.find()
    res.json = {
        status: 200,
        message: 'success',
        data: getAll
    }
}

module.exports = get_all