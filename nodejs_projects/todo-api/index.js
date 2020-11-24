const express = require('express');
const mongoose = require('mongoose');
const Todo = require('./models/todo');


mongoose.connect('mongodb://localhost/todo', {useNewUrlParser: true});
let app = express();


// fetch all the models required for this
const Todos = require('./models/todo');

app.get('/getall', (req, res) => {
  Todos.find().lean().exec((err, results) => {
    if(err){
      console.log(err);
    }
    res.json(results);
  })
})

app.post('/todo', (req, res) => {
  let data = req.body.data;
  data.foreach((val) => {
    let viva = new Todo(val);
    viva.save()
  })

  res.send('done');
})


app.get('/', (req, res) => { res.send('hello world')});

app.listen(8080)
