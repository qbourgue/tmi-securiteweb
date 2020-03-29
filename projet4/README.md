# Projet Sécurité Web

## Exercice 2

Nous allons suivre l'exemple 4:

Intitulé du sujet:

- Vous pouvez mettre en place une petite application Web dont l'authentification a été mis en oeuvre manuellement avec faiblesse pour la mise en place de règles sur l'authentification.

- contre mesure possible, utilisation d'openid connect, déploiement de [keycloak](https://www.keycloak.org/) pour l'authentification.

## Exploration de solutions existante

### Simple Docker image for basic authentication

https://github.com/beevelop/docker-nginx-basic-auth

### Requirement 

- Docker
- WildFly 10 running
- Java 8.0 (Java SDK 1.8) or later
- Maven 3.1.1 or later

### Keycloak

- Solution on Docker: 

https://www.keycloak.org/getting-started/getting-started-docker

#### Launch the Keycloak docker: 

docker run -p 8070:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:9.0.2

Keycloak available on localhost port 8070.

#### Application exemple

From Github repertory: https://github.com/keycloak/keycloak-quickstarts

##### Launch JAX-RS Service:
https://github.com/keycloak/keycloak-quickstarts/tree/latest/service-jee-jaxrs

In keycloak-quickstarts/service-jee-jaxrs: 

> mvn clean wildfly:deploy

It will open three endpoint for the service:
- public - http://localhost:8080/service/public
- secured - http://localhost:8080/service/secured
- admin - http://localhost:8080/service/admin

#### Launch Html5 Application 



### Requirement Setup

#### Keycload WildFly Adapter

Download: https://www.keycloak.org/downloads.html

##### Docker wildfly
sudo docker run -p 8080:8080 -p 9990:9990 -it jboss/wildfly /opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0

Doc: https://github.com/JBoss-Dockerfiles/wildfly

##### Local Install
https://vitux.com/install-and-configure-wildfly-jboss-on-ubuntu/

sh wildfly-10.1.0.Final/bin/standalone.sh

Disponible on localhost:8080

Admin on localhost:9990/console

#### Wildfly 

### JDK 8
sudo apt install openjdk-8-jdk openjdk-8-jre
