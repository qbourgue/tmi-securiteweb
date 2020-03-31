# Projet Sécurité Web: Exercice 2

Nous allons suivre l'exemple 4:

Intitulé du sujet:

- application Web dont l'authentification a été mis en oeuvre manuellement avec faiblesse pour la mise en place de règles sur l'authentification.

- contre mesure possible, utilisation d'openid connect, déploiement de [keycloak](https://www.keycloak.org/) pour l'authentification.

## Keycloak and Wildfly configuration

### Requirement 

- Docker
- Java 8.0 (Java SDK 1.8) or later
- Maven 3.1.1 or later

### Keycloak

To test keycloak solution, please follow the [**Getting started** guide](./gettingStarted.md).

## Authentification sans keycloak

### Simple Docker image for basic authentication

https://github.com/beevelop/docker-nginx-basic-auth
