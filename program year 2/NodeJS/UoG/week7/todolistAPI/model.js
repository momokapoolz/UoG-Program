const mongoose = require('mongoose')

const taskSchema = new mongoose.Schema({
    name: String,
    created_date: {
        type: Date,
        default: Date.now
    },
    status: [{
        type: String,
        enum: ['pending', 'ongoing', 'finish'] //enum: limit option for user to choose
    }],
    default: ['pending']
})

const taskModel = mongoose.model('Tasks', taskSchema)

module.exports = taskModel
