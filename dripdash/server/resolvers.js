const Mutation = require("./resolvers/mutation");
const Query = require("./resolvers/query");
const User = require("./resolvers/user");
const Device = require("./resolvers/device");
const Group = require("./resolvers/group");
const DataEntry = require("./resolvers/dataEntry");

const resolvers = {
  Query,
  Mutation,
  User,
  Device,
  Group,
  DataEntry
}


module.exports = resolvers;