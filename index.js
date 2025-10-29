const http = require('http');
const port = process.env.PORT || 3000;
const server = http.createServer((req, res) => {
  res.end('Movies app - hello');
});
server.listen(port, () => console.log(`Listening on ${port}`));
