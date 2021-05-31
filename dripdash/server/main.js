/*
 * DripDash Server
 */

const { resolve } = require("path");
const history = require("connect-history-api-fallback");
const express = require("express");
const bodyParser = require("body-parser");

const api = require("./api");
const collector = require("./collector");

const { PORT = 8000 } = process.env;

const configure = app => {
  app.use(bodyParser.json());
  api.applyMiddleware({ app, path: "/api" });
  app.use("/collect", collector);
}

if (require.main === module) {
  const app = express();

  configure(app);

  // Vue UI History Mode
  const publicPath = resolve(__dirname, "../dist");
  const staticConf = { maxAge: "1y", etag: false };

  app.use(history());
  app.use(express.static(publicPath, staticConf));

  app.listen(PORT, () => console.log(`🚀 DripDash server running at http://localhost:${PORT}`));
}


module.exports = configure;