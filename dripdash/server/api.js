const { loadSchemaSync } = require("@graphql-tools/load");
const { GraphQLFileLoader } = require("@graphql-tools/graphql-file-loader");
const { addResolversToSchema } = require("@graphql-tools/schema");
const { ApolloServer } = require("apollo-server-express");
const { join } = require('path');
const tokens = require("./tokens");


const typeDefs = loadSchemaSync(
  join(__dirname, "schema.graphql"),
  { loaders: [new GraphQLFileLoader()] }
);

const resolvers = require("./resolvers");

const schema = addResolversToSchema({
  schema: typeDefs,
  resolvers: resolvers
});

const apollo = new ApolloServer({
  schema,
  context: ({ req }) => {
    const token = req.headers.authorization || '';

    const user = tokens.check(token);
    return { user };
  }
});

module.exports = apollo;