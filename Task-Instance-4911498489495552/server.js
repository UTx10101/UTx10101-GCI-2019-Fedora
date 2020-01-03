const express = require('express');
const app = express()

app.use(express.static('public'));
app.set('view engine', 'ejs')

app.get('/', function (req, res) {
  res.render('index');
})
app.listen(2120, function () {
  console.log('News App running at http://localhost:2120 !!')
})
