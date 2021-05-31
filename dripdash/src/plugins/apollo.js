import {
  ApolloClient,
  ApolloLink,
  HttpLink,
  InMemoryCache
} from "apollo-boost";
import Vue from "vue";
import VueApollo from "vue-apollo";

const httpLink = new HttpLink({ uri: `${window.location.origin}/api` });
const authLink = new ApolloLink((operation, forward) => {
  const token = localStorage.getItem("user-token");

  document.dispatchEvent(
    new CustomEvent("apollo-status", { detail: "fetching" })
  );

  operation.setContext({
    headers: {
      Authorization: token || ""
    }
  });

  return forward(operation);
});

const postLink = new ApolloLink((operation, forward) => {
  return forward(operation).map(response => {
    document.dispatchEvent(
      new CustomEvent("apollo-status", { detail: "fetched" })
    );
    return response;
  });
});

export const apolloClient = new ApolloClient({
  // request -> apply auth -> send http request.
  link: postLink.concat(authLink.concat(httpLink)),
  cache: new InMemoryCache()
});

Vue.use(VueApollo);

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

export default apolloProvider;
