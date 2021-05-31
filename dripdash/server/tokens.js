const jwt = require("jsonwebtoken");
const privatekey = require("crypto")
  .randomBytes(48)
  .toString("base64")
  .replace(/\//g, "_")
  .replace(/\+/g, "-");

module.exports = {
  create(user) {
    return jwt.sign({ username: user.username, id: user.id }, privatekey, {
      expiresIn: 3600,
      algorithm: "HS256"
    });
  },

  check(token) {
    try {
      var payload = jwt.verify(token, privatekey, {
        algorithms: ["HS256"]
      });
      if (payload) {
        return payload;
      }
    } catch (err) {
      return null;
    }
    return null;
  }
};
